
package core.javacore;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

/**
 * Daniel Klein
 * Computer-Based Honors Program
 * The University of Alabama
 * 9.24.2014
 *
 * This is a demo class that shows that a grails controller can get data
 * from our objects properly.
 */
public class Demo
{
    
    public String runDemo() throws FileNotFoundException, ClassNotFoundException, IOException
    {
        String serializeDirPath = WordCloudConstants.SERIALIZE_DIR_PATH;
        
        File docsDir = new File(serializeDirPath);
        List<File> docsFiles = Arrays.asList(docsDir.listFiles());
        
        Random rand = new Random();
        
        // pick a serialized doc
        File chosenFile = docsFiles.get(rand.nextInt(20000));
        
        
        // Read from disk using FileInputStream
        FileInputStream f_in = new 
            FileInputStream(chosenFile);

        // Read object using ObjectInputStream
        ObjectInputStream obj_in = 
            new ObjectInputStream (f_in);

        // Read an object
        Object obj = obj_in.readObject();
        SupremeCourtOpinion opinion;
        
        if (obj instanceof SupremeCourtOpinion)
        {
            // Cast object to a SCO
            opinion = (SupremeCourtOpinion) obj;

        } else
        {
            return "loading object didn't work";
        }
        
        System.out.println(opinion.toString());
        return opinion.toString();
    }

}
