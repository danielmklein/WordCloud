
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
    public static List<AnalysisEngine.TermMetrics> runDemo(List<Document> allOpinions) throws FileNotFoundException, ClassNotFoundException, IOException, Exception
    {
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
        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(numRelevantTerms);

        for (AnalysisEngine.TermMetrics term : terms)
        {
            System.out.println("Term '" + term.term + "' has weight " + term.weight);
        }

        return terms;
    }
}
