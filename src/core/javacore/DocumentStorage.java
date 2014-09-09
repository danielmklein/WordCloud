package core.javacore;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
*   Daniel Klein
*   Computer-Based Honors Program
*   The University of Alabama
*   9.8.2014
*   
*   This class is basically just a Document object along with a place
*   to store the list of terms in the document and each of their 
*   frequencies.
*/
public class DocumentStorage extends Document
{

    /**
     * 
     */
    public DocumentStorage(Metadata docMetadata, String docText, String outputFilename)
    {
        super(docMetadata, docText, outputFilename);
        // TODO Auto-generated constructor stub
    }
    
    private Map<String, Map<String, Double>> buildTermList(List<String> splitText)
    {
        
        Map<String, Map<String, Double>> termList = new HashMap<String, Map<String, Double>>();
        
        for (String term : splitText)
        {
            if (!termList.containsKey(term))
            {
                Map<String, Double> metrics = new HashMap<String, Double>();
                metrics.put("tf", null);
                metrics.put("count", new Double(0));
            } else
            {
                Double oldCount = termList.get(term).get("count");
                termList.get(term).put("count", oldCount + 1);
            }
        }
        
        return termList;
    }
    
    private Map<String, Map<String, Double>> populateTermFreqs(Map<String, Map<String, Double>> termList)
    {
        
        for (String term : termList.keySet())
        {
            Double tf = this.calcTermFreq(term);
            termList.get(term).put("tf", tf);
        }
        
        return termList;
    }
    
    private List<String> filterText(String text, boolean shouldDropPropNouns)
    {
        
    }
    
    private boolean isProperNoun(String curTerm, String prevTerm)
    {
        
    }
    
    private List<String> stemText(List<String> wordList)
    {
        // TODO: use opennlp.tools.stemmer.Stemmer.
        
    }
    
    private Double calcTermFreq(String term)
    {
        
    }
    
    private Double calcTfidf(String term, int docFreq)
    {
        
    }
}
