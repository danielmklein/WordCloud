
package core.javacore;

import java.util.List;
import java.util.Map;

/**
*   Daniel Klein
*   Computer-Based Honors Program
*   The University of Alabama
*   9.8.2014
*       
*   Given a set of Documents (divided into subsets) (and perhaps analysis 
*   parameters TBD), this class will perform natural language text processing 
*   on the collection of documents and return a weighted list of the "most 
*   important" terms in the collection. This utilizes term 
*   frequency-inverse document frequency analysis as its basis for weighting 
*   terms (http://en.wikipedia.org/wiki/Tf%E2%80%93idf).
*/
public class AnalysisEngine
{

    private List<DocumentStorage> corpus;
    private List<DocumentStorage> subset;
    /**
     * 
     */
    public AnalysisEngine(List<Document> corpus, List<Document> subset)
    {

        // TODO Auto-generated constructor stub
        this.setCorpus(corpus);
        this.setSubset(subset);
    }
    
    public void setCorpus(List<Document> corpus)
    {
        
    }
    
    public void setSubset(List<Document> subset)
    {
        
    }
    
    public int countDocs(List<Document> set)
    {
        return set.size();
    }
    
    public List<DocumentStorage> convertDocs(List<Document> docSet)
    {
        
    }
    
    private Map<String, Double> buildFullTermList(List<DocumentStorage> corpus)
    {
        
    }

    
}
