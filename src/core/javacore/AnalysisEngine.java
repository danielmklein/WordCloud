package core.javacore;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
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
    private Map<String, Double> termList;
    
    private int numCorpusDocs;
    private int numSubsetDocs;
    
    /**
     * 
     */
    public AnalysisEngine(List<Document> corpus, List<Document> subset) throws Exception
    {

        this.setCorpus(corpus);
        this.setSubset(subset);
    }
    
    /**
     * Basic setup for the corpus list of documents.
     * 
     * @param corpus
     * @throws Exception
     */
    public void setCorpus(List<Document> corpus) throws Exception
    {
        this.numCorpusDocs = this.countDocs(corpus);
        if (this.numCorpusDocs < 1)
        {
            throw new Exception("Corpus must contain at least 1 Document.");
        }
        
        this.corpus = this.convertDocs(corpus);
        this.termList = this.buildFullTermList(this.corpus);
        
    }
    
    /**
     * Basic setup for the subset list of documents.
     * 
     * @param subset
     */
    public void setSubset(List<Document> subset) throws Exception
    {
        this.numSubsetDocs = this.countDocs(subset);
        if (this.numSubsetDocs < 1)
        {
            throw new Exception("Subset must contain at least 1 Document");
        }
        this.subset = this.convertDocs(subset);
    }
    
    /**
     * Calculates the total number of docs in set.
     * 
     * @param set
     * @return
     */
    public int countDocs(List<Document> set)
    {
        return set.size();
    }
    
    /**
     *  Transforms each doc in a set into a DocumentStorage object,
     *  which makes them much easier to deal with as we perform our
     *  calculations.  
     *  
     * @param docSet
     * @return
     */
    public List<DocumentStorage> convertDocs(List<Document> docSet) throws Exception
    {
        
        System.out.println("Converting documents into DocumentStorage objects...");
        
        int numDocs = docSet.size();
        
        List<DocumentStorage> converted = new ArrayList<DocumentStorage>();
        Document curDoc;
        DocumentStorage convertedDoc;
        
        for (int i = 0; i < numDocs; ++i)
        {
            
            try
            {
                System.out.println("Converting document " 
                                    + (i+1) + " of " + numDocs 
                                    + " to Storage object...");
                curDoc = docSet.get(i);
                convertedDoc = new DocumentStorage(curDoc.getMetadata(), curDoc.getText(),
                                                    curDoc.getOutputFilename());
                converted.add(convertedDoc);
                
            } catch (Exception e)
            {
                throw new Exception("AnalysisEngine: failed to instantiate new DocumentStorage object.");
            }
        }
        
        return converted;
    }
    
    /**
     *  Constructs a list of all terms used in the entire corpus along
     *  with each term's doc frequency
     *  
     * @param corpus
     * @return
     */
    private Map<String, Double> buildFullTermList(List<DocumentStorage> corpus)
    {
        System.out.println("Building list of all terms in document corpus...");
        
        Map<String, Double> terms = new HashMap<String, Double>();
        List<String> newTerms;
        
        for (DocumentStorage doc : corpus)
        {
            newTerms = new ArrayList<String>();
            
            // construct list of all terms in this doc that are not
            // already in termList
            for (String term : doc.getTermList().keySet())
            {
                if (!terms.keySet().contains(term))
                {
                    newTerms.add(term);
                }
            }
            
            // put the new terms into termList along with each one's
            // relative document frequency
            for (String newTerm : newTerms)
            {
                terms.put(newTerm, this.calcDocFrequency(newTerm));
            }
        }
        
        return terms;
    }
    
    /**
     * Given num_terms, compile list of all terms in corpus and return
     * the num_terms most frequent terms (num_terms = 1000/5000/15000/etc)
     *  
     * @param corpus
     * @param numTerms
     * @return
     */
    private List<String> getMostFreqTerms(List<DocumentStorage> corpus, int numTerms)
    {
        Map<String, Integer> termsWithFreqs = new HashMap<String, Integer>();
        
        for (DocumentStorage doc : corpus)
        {
            for (String term : doc.getStemmedText())
            {
                if (termsWithFreqs.keySet().contains(term))
                {
                    int freq = termsWithFreqs.get(term);
                    termsWithFreqs.put(term, freq + 1);
                } else
                {
                    termsWithFreqs.put(term, 1);
                }
            }
        }
        
        List<String> termList = new ArrayList<String>(termsWithFreqs.keySet());
        Collections.sort(termList, new TermFreqComparator(termsWithFreqs));
                
        return termList.subList(0, numTerms);
    }
    
    /**
     *  Given a term, calculates its relative doc frequency, ie
     *  (# docs term in which term appears) / (# docs total in corpus)
     *  
     * @param term
     * @return
     */
    private Double calcDocFrequency(String term)
    {
        int docFrequency = 0;
        
        for (DocumentStorage doc : this.corpus)
        {
            if (doc.getTermList().keySet().contains(term))
            {
                docFrequency++;
            }
        }
        
        Double relFrequency = (new Double(docFrequency) 
                            / (new Double(this.numCorpusDocs)));
        
        return relFrequency;
    }
    
    /**
     * Class for comparing terms by looking at their term frequencies;
     * this sorts in reverse order (most frequent terms first);
     * 
     */
    private class TermFreqComparator implements Comparator<String>
    {
        private Map<String, Integer> termsWithFreqs;
        
        public TermFreqComparator(Map<String, Integer> freqs)
        {
            this.termsWithFreqs = freqs;
        }
        
        public int compare(String term1, String term2)
        {
            Integer freq1 = this.termsWithFreqs.get(term1);
            Integer freq2 = this.termsWithFreqs.get(term2);
            
            return freq2.compareTo(freq1); // reverse sorted order
        }
    }
          
}
