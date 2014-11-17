import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

import org.hibernate.SessionFactory;
import org.hibernate.StatelessSession;
import org.hibernate.Transaction;

import wordcloudweb.SCOpinionDomain;

import core.javacore.*;

class BootStrap 
{

    def sessionFactory;

    def init = 
    { servletContext ->
    	this.loadOpinions();
    }

    def destroy =
    {
    }

    private /*List<Document>*/ void loadOpinions() throws Exception, FileNotFoundException, ClassNotFoundException, IOException
    {
        String opinionDirPath = WordCloudConstants.OPINION_DIR_PATH;
        //String serializeDirPath = WordCloudConstants.SERIALIZE_DIR_PATH;
        
        System.out.println("Converting files in " + opinionDirPath + " to Document objects");
        System.out.println("And saving them to the database.");

        File opinionDir = new File(opinionDirPath);
        List<File> opinionFiles = Arrays.asList(opinionDir.listFiles());
        
        long numOpinions = opinionFiles.size();
        long numConverted = 0;
        long numFailed = 0;
        Pattern txtFileRegex = Pattern.compile("\\.txt\$");
        
        System.out.println(numOpinions + " opinion files found.");
        
        String inputFullPath;
        String serializeFullPath;
        boolean isTextFile;
        SupremeCourtOpinionFileConverter converter = new SupremeCourtOpinionFileConverter(null, "BOGUS_SERIALIZE_PATH.txt");
        SupremeCourtOpinion newOpin;
        SCOpinionDomain domainOpin;// = new SCOpinionDomain(null, null);
        
        StatelessSession session = sessionFactory.openStatelessSession();
        Transaction tx = session.beginTransaction();

        for (File opinionFile : opinionFiles)
        {
            inputFullPath = opinionFile.getCanonicalPath();
            // if a file doesn't have a .txt extension, we ignore it 
            isTextFile = txtFileRegex.matcher(inputFullPath).find();
            if (!isTextFile)
            {
                System.out.println(inputFullPath + " is not a text file, so we can't convert it!");
                numFailed++;
                continue;
            }
            
            // serializePath = SERIALIZE_PATH + filename + ".Document"
            //serializeFullPath = (new File(serializeDirPath, opinionFile.getName() + ".Document")).getCanonicalPath();
            
            //converter = new SupremeCourtOpinionFileConverter(inputFullPath, serializeFullPath);
            converter.setFileToParse(inputFullPath);

            try
            {
                newOpin = converter.convertFile();
                //domainOpin = new SCOpinionDomain(newOpin.getMetadata(),
                //                                      newOpin.getText(),
                //                                      newOpin.getOutputFilename());
                // TODO: possible performance improvement -- use domain opin setters 
                // instead of creating new object
                //domainOpin.setMetadata(newOpin.getMetadata().getAllFields());

                /*SCOpinionDomain*/ domainOpin = new SCOpinionDomain(newOpin.getText(), newOpin.getOutputFilename());
                
                domainOpin.docText = newOpin.getText();
                domainOpin.outputFilename = newOpin.getOutputFilename();
                
                domainOpin.caseTitle = newOpin.getMetadata().getField(WordCloudConstants.META_CASE_TITLE);
                domainOpin.caseNumber = newOpin.getMetadata().getField(WordCloudConstants.META_CASE_NUM);
                domainOpin.usCitation = newOpin.getMetadata().getField(WordCloudConstants.META_US_CITE);
                domainOpin.scCitation = newOpin.getMetadata().getField(WordCloudConstants.META_SC_CITE);
                domainOpin.lawyersEd = newOpin.getMetadata().getField(WordCloudConstants.META_LAWYERS_ED);
                domainOpin.lexisCitation = newOpin.getMetadata().getField(WordCloudConstants.META_LEXIS_CITE);
                domainOpin.fullCitation = newOpin.getMetadata().getField(WordCloudConstants.META_FULL_CITE);
                domainOpin.caseDates =  newOpin.getMetadata().getField(WordCloudConstants.META_CASE_DATES);
                domainOpin.disposition = newOpin.getMetadata().getField(WordCloudConstants.META_DISPOSITION);
                domainOpin.opinionAuthor = newOpin.getMetadata().getField(WordCloudConstants.META_OPIN_AUTHOR);
                domainOpin.opinionType = newOpin.getMetadata().getField(WordCloudConstants.META_OPIN_TYPE);

                //domainOpin.save(failOnError:true, flush:true);
                session.insert(domainOpin);

                newOpin = null;

                numConverted++;
            } catch (Exception e)
            {
                System.out.println("Unable to convert " + opinionFile.getName()
                                + " to Document object and save it to file...");
                numFailed++;
                tx.commit();
                session.close();

                throw new Exception(e);
                continue;
            }
            
            if (numConverted % 1000 == 0)
            {
                tx.commit();
                System.out.println(numConverted + " opinions converted.");
                System.out.println("Database currently contains " + SCOpinionDomain.count() + " opinions.");
                tx = session.beginTransaction();
            }
            
        }

        tx.commit();
        session.close();
        
        System.out.println("Opinion conversion and serialization complete.");
        System.out.println(numConverted + " opinions converted.");
        System.out.println(numFailed + " opinions failed conversion.");
    }


}
