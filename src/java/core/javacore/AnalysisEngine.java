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
     *  Given corpus and list of terms, we get rid of the terms
     *  that appear in more than x% or less than y% of the opinions.
     *  
     * @param corpus
     * @param termList
     * @return
     */
    private List<String> determineRelevantTerms(List<DocumentStorage> corpus, List<String> termList)
    {

        List<String> relevantTerms = new ArrayList<String>();
        Double upperBound = WordCloudConstants.RELEVANT_TERM_PERCENTAGE_UPPER;
        Double lowerBound = WordCloudConstants.RELEVANT_TERM_PERCENTAGE_LOWER;
        
        // test output
        System.out.println("TOTAL NUM OF DOCS: " + this.numCorpusDocs);
        // end test output
        
        for (String term : termList)
        {
            int docFreq = 0;
            for (DocumentStorage doc : corpus)
            {
                // doc.termList is filtered and stemmed
                if (doc.getTermList().keySet().contains(term))
                {
                    docFreq++;
                }
            }
            
            Double percentageOfDocs = (new Double(docFreq)) 
                                    / (new Double(this.numCorpusDocs));
            boolean withinRange = ((percentageOfDocs > lowerBound)
                                && (percentageOfDocs < upperBound));
            if (withinRange)
            {
                relevantTerms.add(term);
            }
        }
        
        return relevantTerms;
    }
    
    /**
     * The method this class is all about -- kicks off the analysis process.
     * TODO: maybe change this method to just return list of TermMetrics, 
     * pull out terms and weights on front end?
     * 
     * @param numRelevantTerms
     * @return
     */
    public Map<String, Double> analyzeDocs(int numRelevantTerms)
    {
        
        List<String> mostFreqTerms = this.getMostFreqTerms(this.corpus, numRelevantTerms);
        List<String> relevantTerms = this.determineRelevantTerms(this.corpus, mostFreqTerms);
        
        System.out.println("Analyzing subset against corpus...");
        
        List<TermMetrics> rawInfo = this.collectTermInfo(this.subset, relevantTerms,
                                                        WordCloudConstants.NUM_TERMS_IN_CLOUD);
        
        // TODO: maybe just return rawInfo (list of termmetrics) to client side??
        Map<String, Double> weightedTerms = new HashMap<String, Double>();
        for (TermMetrics tm : rawInfo)
        {
            weightedTerms.put(tm.term, tm.weight);
        }
        
        return weightedTerms;
    }
    
    /**
     * Builds collection of info (weight, tf-idf, tf, df) for each term
     * we care about. 
     * 
     * @param subset
     * @param relevantTerms
     * @param numTerms
     * @return
     */
    private List<TermMetrics> collectTermInfo(List<DocumentStorage> subset, List<String> relevantTerms, int numTerms)
    {
        
        List<TermMetrics> rawTermInfo = new ArrayList<TermMetrics>();
        
        Double tfidf;
        Double weight;
        Double docFreq;
        Double termFreq;
        
        for (String term : relevantTerms)
        {
            tfidf = this.calcTfidfForSubset(term, subset);
            weight = tfidf;
            docFreq = this.termList.get(term);
            termFreq = tfidf * docFreq;
            
            TermMetrics newTerm = new TermMetrics();
            newTerm.term = term;
            newTerm.tfidf = tfidf;
            newTerm.weight = weight;
            newTerm.docFrequency = docFreq;
            newTerm.termFrequency = termFreq;
            rawTermInfo.add(newTerm);
        }
        
        // get the index of the term having the highest unscaled weight
        // we're going to scale all weights so they are <= 1.0
        int maxWeightIdx = this.getHighestWeight(rawTermInfo);
        Double scaleFactor = rawTermInfo.get(maxWeightIdx).weight;
        
        for (TermMetrics curTerm : rawTermInfo)
        {
            // destem each term and scale each weight
            curTerm.term = this.destem(curTerm.term, this.corpus);
            curTerm.weight = curTerm.weight / scaleFactor;
        }
        
        return rawTermInfo;
    }
    
    /**
     * Returns index of the TermMetrics having the highest weight.
     * 
     * @return
     */
    private int getHighestWeight(List<TermMetrics> terms)
    {
        int highIdx = 0;
        for (int i = 1; i < terms.size(); ++i)
        {
            if (terms.get(i).weight > terms.get(highIdx).weight)
            {
                highIdx = i;
            }
        }
        
        return highIdx;
    }
    
    /**
     *  Extracts the term weight pairs (that the WordCloudGenerator needs)
     *  from our collection of term info.
     *  
     * @param rawTermInfo
     * @return
     */
    private Map<String, Double> buildWeightedPairs(List<TermMetrics> rawTermInfo)
    {
        // TODO: write me -- this is currently done in analyzeDocs.
        
        return null;     
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
     *  Given a term and a subset, calculates the characteristic tf-idf for
     *  the term in that subset -- ie the median of the tf-idf's for
     *  the term for each document in the subset.
     *  
     * @param term
     * @param subset
     * @return
     */
    private Double calcTfidfForSubset(String term, List<DocumentStorage> subset)
    {
        
        Double docFreq = this.termList.get(term);
        List<Double> tfidfList = new ArrayList<Double>();
        
        Double newTfidf;
        for (DocumentStorage doc : subset)
        {
            newTfidf = doc.calcTfidf(term, docFreq);
            tfidfList.add(newTfidf);
        }
        
        return this.mean(tfidfList);
    }
    
    private Double mean(List<Double> nums)
    {
        Double sum = new Double(0);
        for (Double num : nums)
        {
            sum += num;
        }
        
        return sum / nums.size();
    }
    
    /**
     * Saves a generated weighted_list to file in a readable format.
     * TODO: I can do this after we have a working web app. Maybe.
     * TODO: This probably won't be very useful for the web app until
     * we add functionality to allow user to download file containg term metrics.
     * 
     * @param rawInfo
     * @param outputPath
     */
    private void saveTermInfo(List<TermMetrics> rawInfo, String outputPath)
    {
        //  TODO: write me??
    }
    
    /**
     * Constructs a line of term info to save to file.
     * 
     * @param termMetrics
     */
    private void buildOutputLine(TermMetrics termMetrics)
    {
        // TODO: write me once we need me
    }
    
    /**
     *  Given a stemmed term, we look through the text of every document
     *  in corpus, determine the most common "parent" version of the 
     *  given stemmed term, and return it. 
     *    
     * @param stemmedTerm
     * @param corpus
     * @return
     */
    private String destem(String stemmedTerm, List<DocumentStorage> corpus)
    {
        
        String destemmedTerm = "";
        
        int minNumTerms = WordCloudConstants.DESTEMMER_MIN_NUM_TERMS;
        Double minPercentage = WordCloudConstants.DESTEMMER_MIN_PERCENTAGE;
        
        Map<String, Integer> candidates = new HashMap<String, Integer>();
        Stemmer stemmer;
        
        long numTermsChecked = 0;
        long numDocsChecked = 0;
        long totalMatches = 0;
        
        for (DocumentStorage doc : corpus)
        {
            // matches is the list of all term in the current text that are
            // "ancestor" versions of the stemmed term.
            List<String> matches = new ArrayList<String>();
            for (String term : doc.getSplitText())
            {
                stemmer = new Stemmer();
                stemmer.add(term.toCharArray(), term.length());
                stemmer.stem();
                String curStemmed = stemmer.toString();
                if (curStemmed.equals(stemmedTerm))
                {
                    matches.add(term);
                }
            }
            numTermsChecked += doc.getSplitText().size();
            numDocsChecked++;
            totalMatches += matches.size();
            if (matches.size() == 0)
            {
                continue;
            }
            
            // we keep a tally of the number of times each "ancestor"
            // appears in our text
            for (String match : matches)
            {
                if (candidates.keySet().contains(match))
                {
                    Integer curValue = candidates.get(match);
                    candidates.put(match, curValue + 1);
                } else 
                {
                    candidates.put(match, 1);
                }
            }
            
            // sort potential destemmed versions in descending order
            // by frequency
            List<String> sortedCandidates = new ArrayList<String>(candidates.keySet());
            Collections.sort(sortedCandidates, new DestemCandidateComparator(candidates));
            
            if (numDocsChecked == this.numCorpusDocs)
            {
                // we've run through every doc, so the most frequent 
                // ancestor of the stemmed term is the best destemmed 
                // result.
                destemmedTerm = sortedCandidates.get(0);
                break;
            }
            
            // if we've reviewed enough total words, we can start trying
            // to find a suitable destemmed term from what we have so far
            if (minNumTerms <= numTermsChecked)
            {
                // this is the most frequent ancestor of the stemmed term
                String possibleMatch = sortedCandidates.get(0);
                Double testPercentage = (new Double(candidates.get(possibleMatch)))
                                        / (new Double(totalMatches));
                // if the potential destemmed version accounts for a 
                // sufficient percentage of the total matches, we can
                // decide that it's a suitable destemmed result.
                if (minPercentage <= testPercentage)
                {
                    destemmedTerm = possibleMatch;
                    break;
                }
            }
        }
        
        System.out.println("Destemmed: " + stemmedTerm + " --> " + destemmedTerm);
        
        return destemmedTerm;
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
    
    /**
     * Class for comparing terms by looking at their term frequencies;
     * this sorts in reverse order (most frequent terms first);
     * 
     */
    private class DestemCandidateComparator implements Comparator<String>
    {
        private Map<String, Integer> candidates;
        
        public DestemCandidateComparator(Map<String, Integer> candidates)
        {
            this.candidates = candidates;
        }
        
        public int compare(String term1, String term2)
        {
            Integer freq1 = this.candidates.get(term1);
            Integer freq2 = this.candidates.get(term2);
            
            return freq2.compareTo(freq1); // reverse sorted order
        }
    }
    
    private class TermMetrics 
    {
        private String term;
        private Double tfidf;
        private Double weight;
        private Double docFrequency;
        private Double termFrequency;
    }
          
}
