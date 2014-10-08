
package core.javacore;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

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
    
    // TODO: change this return type (maybe list of TermMetrics?)
    public static List<AnalysisEngine.TermMetrics> /*Map<String, Double>*/ runDemo() throws FileNotFoundException, ClassNotFoundException, IOException, Exception
    {
        
        List<Document> allOpinions = loadOpinions();
        
        DocumentSorter sorter = new DocumentSorter(allOpinions);
        
        String sortField = WordCloudConstants.META_OPIN_AUTHOR;
        List<String> allowedVals = new ArrayList<String>();
        allowedVals.add("FRANKFURTER");
        boolean shouldInvert = false;
        
        List<Document> warrenOpinions = sorter.createSubset(sortField, allowedVals, shouldInvert);
        
        System.out.println("Corpus has " + allOpinions.size() + " opinions.");
        System.out.println("Subset has " + warrenOpinions.size() + " opinions.");
        
        AnalysisEngine engine = new AnalysisEngine(allOpinions, warrenOpinions);
        int numRelevantTerms = WordCloudConstants.NUM_TERMS_IN_CLOUD;
        //Map<String, Double> terms = engine.analyzeDocs(numRelevantTerms);
        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(numRelevantTerms);
        
        //for (String term : terms.keySet())
        for (AnalysisEngine.TermMetrics term : terms)
        {
            System.out.println("Term '" + term.term + "' has weight " + term.weight);
        }
        
        return terms;
    }
    
    public static List<Document> loadOpinions() throws FileNotFoundException, ClassNotFoundException, IOException
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
            
            Document opinion;
            
            if (obj instanceof SupremeCourtOpinion)
            {
                // Cast object to a SCO
                opinion = (SupremeCourtOpinion) obj;
                System.out.println("Loaded opinion from file " + curFile.getName());
                opinions.add(opinion);
            } else
            {
                System.out.println("Loading opinion didn't work for file " + curFile.getName());
            }
            
            numConverted++;
        }
        
        return opinions;
    }
    
    
    public static void main(String[] args) throws FileNotFoundException, ClassNotFoundException, IOException, Exception
    {
        runDemo();

    }
    

}
