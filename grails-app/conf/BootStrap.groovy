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

import wordcloudweb.SCOpinionDomain;

import core.javacore.*;

class BootStrap 
{

    def init = 
    { servletContext ->
    	this.loadOpinions();
    }

    def destroy =
    {
    }

    public static /*List<Document>*/ void loadOpinions() throws FileNotFoundException, ClassNotFoundException, IOException
    {
        String opinionDirPath = WordCloudConstants.OPINION_DIR_PATH;
        String serializeDirPath = WordCloudConstants.SERIALIZE_DIR_PATH;
        
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
        SupremeCourtOpinionFileConverter converter;
        SupremeCourtOpinion newOpin;
        SCOpinionDomain domainOpin;
        
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
            serializeFullPath = (new File(serializeDirPath, opinionFile.getName() + ".Document")).getCanonicalPath();
            
            converter = new SupremeCourtOpinionFileConverter(inputFullPath, serializeFullPath);
            
            try
            {
                newOpin = converter.convertFile();
                domainOpin = new SCOpinionDomain(newOpin.getMetadata(),
                                                      newOpin.getText(),
                                                      newOpin.getOutputFilename());
                domainOpin.save(failOnError:true);

                numConverted++;
            } catch (Exception e)
            {
                System.out.println("Unable to convert " + opinionFile.getName()
                                + " to Document object and save it to file...");
                numFailed++;
                continue;
            }
            
            if (numConverted % 1000 == 0)
            {
                System.out.println(numConverted + " opinions converted.");
            }
            
        }
        
        System.out.println("Opinion conversion and serialization complete.");
        System.out.println(numConverted + " opinions converted.");
        System.out.println(numFailed + " opinions failed conversion.");
    }


}
