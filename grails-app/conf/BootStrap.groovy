import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

import com.amazonaws.services.s3.model.*

import wordcloudweb.SCOpinionDomain;

import core.javacore.*;

class BootStrap
{

    def amazonWebService

    def init =
    { servletContext ->
        this.loadOpinions();
    }

    def destroy =
    {
    }

    private SCOpinionDomain processObject(S3Object object)
    {
        if (!(object.getKey().contains("txt")))
        {
            System.out.println(object.getKey() + " is not a text file, so we can't convert it!");
            return null;
        }

        SCOpinionDomain domainOpin;
        try {
            SupremeCourtOpinion newOpin = (new SupremeCourtOpinionFileConverter(null, "BOGUS_SERIALIZE_PATH.txt")) \
                                            .convertFromInputStream(object.getObjectContent(), object.getKey());
            domainOpin = new SCOpinionDomain(newOpin.getText(), newOpin.getOutputFilename());

            domainOpin.docText = newOpin.getText();

            // using toUpperCase to ensure all these fields are all caps in db
            domainOpin.caseTitle = newOpin.getMetadata().getField(WordCloudConstants.META_CASE_TITLE).toUpperCase();
            domainOpin.caseNumber = newOpin.getMetadata().getField(WordCloudConstants.META_CASE_NUM).toUpperCase();
            domainOpin.usCitation = newOpin.getMetadata().getField(WordCloudConstants.META_US_CITE).toUpperCase();
            domainOpin.scCitation = newOpin.getMetadata().getField(WordCloudConstants.META_SC_CITE).toUpperCase();
            domainOpin.lawyersEd = newOpin.getMetadata().getField(WordCloudConstants.META_LAWYERS_ED).toUpperCase();
            domainOpin.lexisCitation = newOpin.getMetadata().getField(WordCloudConstants.META_LEXIS_CITE).toUpperCase();
            domainOpin.fullCitation = newOpin.getMetadata().getField(WordCloudConstants.META_FULL_CITE).toUpperCase();
            domainOpin.caseDates =  newOpin.getMetadata().getField(WordCloudConstants.META_CASE_DATES).toUpperCase();
            domainOpin.disposition = newOpin.getMetadata().getField(WordCloudConstants.META_DISPOSITION).toUpperCase();
            domainOpin.opinionAuthor = newOpin.getMetadata().getField(WordCloudConstants.META_OPIN_AUTHOR).toUpperCase();
            domainOpin.opinionType = newOpin.getMetadata().getField(WordCloudConstants.META_OPIN_TYPE).toUpperCase();

            // test output
            /*System.out.println("new opinion has title: " + domainOpin.caseTitle);
            System.out.println("new opinion has author: " + domainOpin.opinionAuthor);
            System.out.println("new opinion has full citation: " + domainOpin.fullCitation);
            System.out.println("new opinion has case num: " + domainOpin.caseNumber);
            System.out.println("new opinion has type: " + domainOpin.opinionType);*/

        } catch (Exception e)
        {
            throw new Exception(e);
        }

        return domainOpin;
    }

    private void checkNumConverted(long numConverted)
    {
        if (numConverted % 250 == 0)
        {
            System.out.println(numConverted + " opinions converted.");
            System.out.println("Database currently contains " + SCOpinionDomain.count() + " opinions.");
        }

        return;
    }

    private void loadOpinions() throws Exception, FileNotFoundException, ClassNotFoundException, IOException
    {
        String bucketName = "scotus-opinions";

        System.out.println("Converting files in " + bucketName + " bucket to Document objects");
        System.out.println("And saving them to the database.");

        long numConverted = 0;
        long numFailed = 0;

        ListObjectsRequest listObjectsRequest = new ListObjectsRequest() \
                                                .withBucketName(bucketName);

        S3Object curObject;
        SCOpinionDomain domainOpin;

        ObjectListing objectListing = amazonWebService.s3.listObjects(listObjectsRequest);
        for (S3ObjectSummary objectSummary : objectListing.getObjectSummaries())
        {
            if (objectSummary.getKey().contains(".txt"))
            {
                System.out.println("Converting object " + objectSummary.getKey() + "...");

                curObject = amazonWebService.s3.getObject(
                                                new GetObjectRequest(bucketName, objectSummary.getKey()));
                try {
                    domainOpin = processObject(curObject);
                } catch (Exception e)
                {
                    System.out.println("Unable to convert " + curObject.getKey() +
                                        " to Document object and save it to database...");
                    numFailed++;
                    throw new Exception(e);
                }

                if (domainOpin)
                {
                    numConverted++;
                    System.out.println("saving domain opin: " + domainOpin.caseTitle + " to database.");
                    System.out.println("Number of opinions in databse is: " + SCOpinionDomain.count());
                    domainOpin.save(flush:true);
                } else
                {
                    numFailed++;
                }
                // TODO: REMOVE ME WHEN WE WANT TO DO ALL OPINIONS
                if (numConverted > 2000)
                {
                    break;
                }
            }
        }
        listObjectsRequest.setMarker(objectListing.getNextMarker());

        while (objectListing.isTruncated())
        {
            objectListing = amazonWebService.s3.listObjects(listObjectsRequest);
            for (S3ObjectSummary objectSummary : objectListing.getObjectSummaries())
            {
                if (objectSummary.getKey().contains(".txt"))
                {
                    System.out.println("Converting object " + objectSummary.getKey() + "...");
                    curObject = amazonWebService.s3.getObject(
                                                    new GetObjectRequest(bucketName, objectSummary.getKey()));
                    try {
                        domainOpin = processObject(curObject);
                    } catch (Exception e)
                    {
                        System.out.println("Unable to convert " + curObject.getKey() +
                                            " to Document object and save it to database...");
                        numFailed++;
                        throw new Exception(e);
                    }

                    if (domainOpin)
                    {
                        numConverted++;
                        domainOpin.save(flush:true);
                    } else
                    {
                        numFailed++;
                    }
                    // TODO: REMOVE ME WHEN WE WANT TO DO ALL OPINIONS
                    if (numConverted > 2000)
                    {
                        break;
                    }
                }
            }
            listObjectsRequest.setMarker(objectListing.getNextMarker());
        }

        System.out.println();

        System.out.println("Opinion conversion and serialization complete.");
        System.out.println(numConverted + " opinions converted.");
        System.out.println(numFailed + " opinions failed conversion.");
    } 
}
