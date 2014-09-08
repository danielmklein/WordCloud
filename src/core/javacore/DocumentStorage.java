package core.javacore;

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
public class DocumentStorage
{

    /**
     * 
     */
    public DocumentStorage(Metadata docMetadata, String docText, String outputFilename)
    {

        // TODO Auto-generated constructor stub
    }
    
    private Map<String, Map<String, Double>> buildTermList(List<String> splitText)
    {
        
    }
    
    private Map<String, Map<String, Double>> populateTermFreqs(Map<String, Map<String, Double>> termList)
    {
        
    }
    
    private List<String> filterText(String text, boolean shouldDropPropNouns)
    {
        
    }
    
    private boolean isProperNoun(String curTerm, String prevTerm)
    {
        
    }
    
    private List<String> stemText(List<String> wordList)
    {
        
    }
    
    private Double calcTermFreq(String term)
    {
        
    }
    
    private Double calcTfidf(String term, int docFreq)
    {
        
    }
}
