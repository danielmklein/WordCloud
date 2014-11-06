import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

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
        String serializeDirPath = WordCloudConstants.SERIALIZE_DIR_PATH;
        
        File docsDir = new File(serializeDirPath);
        List<File> docsFiles = Arrays.asList(docsDir.listFiles());
        List<Document> opinions = new ArrayList<Document>();
        
        System.out.println(docsFiles.size() + " opinions to load...");
        
        int numConverted = 0;
        int limit = 1000;
        
        // load each serialized doc
        for (File curFile : docsFiles)
        {
            if (numConverted >= limit) // TODO: remove me when we can do alllll the opinions
            {
                break;
            }
            // Read from disk using FileInputStream
            FileInputStream f_in = new 
                FileInputStream(curFile);

            // Read object using ObjectInputStream
            ObjectInputStream obj_in = 
                new ObjectInputStream (f_in);

            // Read an object
            Object obj = obj_in.readObject();
            obj_in.close();
            
            core.javacore.Document opinion;
            
            if (obj instanceof core.javacore.SupremeCourtOpinion)
            {
                // Cast object to a SCO
                opinion = (core.javacore.SupremeCourtOpinion) obj;
                System.out.println("Loaded opinion from file " + curFile.getName());

                // TODO: might need to create opinion Domain class, convert pure java 
                // opinion into domain object, then save domain object

                opinion.save(failOnError:true);

                //opinions.add(opinion);
            } else
            {
                System.out.println("Loading opinion didn't work for file " + curFile.getName());
            }
            
            numConverted++;
        }
        
        //return opinions;
    }
}
