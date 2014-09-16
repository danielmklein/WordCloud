package core.javacore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


// an implementation of the Porter stemmer from http://tartarus.org/~martin/PorterStemmer/
import core.javacore.Stemmer;

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
    private static final Pattern CAP_REGEX = Pattern.compile("[A-Z]+");
    private static final Pattern PUNC_REGEX = Pattern.compile("[\\.\\?!]");
    
    private String identifier;
    private List<String> splitText;
    private List<String> stemmedText;
    private Map<String, Map<String, Double>> termList;
    
    public DocumentStorage(Metadata docMetadata, String docText, String outputFilename)
    {
        // TODO: create identifier?
        
        super(docMetadata, docText, outputFilename);
        // this.docText holds the actual string containing the raw, unmodified text from the doc
                
        // this.splitText contains the full filtered text of the document
        this.splitText = this.filterText(this.docText, false);
                
        // this.stemmedText contains full filtered text with all words stemmed
        this.stemmedText = this.stemText(this.splitText);
        
        /*
        * this.termList is a list of unique terms in the document along with
        * each term's term frequency and tfidf metric -- only term freq
        * is calculated for each term at this point.
        */
        this.termList = this.buildTermList(this.stemmedText);
        this.populateTermFreqs();
    }
    
    /**
    *  Build term list of form 
    *  {term1: {'tf':0, 'count':0}, term2:{'tf':0, 'count':0}, ... , 
    *  termn:{'tf':0, 'count':0}}
    *  This method counts the instances of each term in the text
    *  as we go along building the list.
    */
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
    
    /**
     * Calculates relative term frequency for each term in term_list.
     */
    private void populateTermFreqs()
    {
        
        for (String term : this.termList.keySet())
        {
            Double tf = this.calcTermFreq(term);
            this.termList.get(term).put("tf", tf);
        }
        
    }
    
    /**
     *  Remove certain items from text. Currently we're removing
     *  punctuation, digits, short words, and stop words. Optionally 
     *  we can dumbly remove proper nouns. 
     *  There is a possibility we might want to remove opinion footnotes
     *  in the future, but we currently leave them in.
     *  
     * @param text
     * @param shouldDropPropNouns
     * @return
     */
    public List<String> filterText(String text, boolean shouldDropPropNouns)
    {
        // first remove numbers
        String unfilteredText = text.replaceAll("\\d", " ");
        String [] rawTerms = unfilteredText.split("\\s+"); 
        
        List<String> filteredText = new ArrayList<String>();
        
        for (int i = 0; i < rawTerms.length; ++i)
        {
            String curTerm = rawTerms[i];
            String prevTerm;
            
            // we MUST do the proper noun filter before we take out punctuation
            if (shouldDropPropNouns)
            {
                if (i > 0)
                {
                    prevTerm = rawTerms[i - 1];
                } else
                {
                    prevTerm = "null";
                }
                
                if (this.isProperNoun(curTerm, prevTerm))
                {
                    // don't add the term to the filteredText list.
                    continue;
                }
            }
            
            // now remove punctuation
            curTerm = curTerm.replaceAll("[^a-zA-Z]+", "");
            // convert term to lowercase and remove any whitespace  
            curTerm = curTerm.toLowerCase().replaceAll("\\s*", "");
            
            // remove words less than 3 letters long
            if (curTerm.length() < 3)
            {
                //System.out.println("term '" + curTerm + "'is too short!");
                continue;
            }
            
            // remove stop words
            if (StopWords.isStopWord(curTerm))
            {
                //System.out.println("term '" + curTerm + "'is a stop word!");
                continue;
            }
            
            // congratulations, you passed the test!
            filteredText.add(curTerm);
        }
                
        return filteredText;
    }
    
    private boolean isProperNoun(String curTerm, String prevTerm)
    {
        
        Matcher prevPunc = PUNC_REGEX.matcher(prevTerm);
        Matcher curCaps = CAP_REGEX.matcher(curTerm);
        
        return (curCaps.find() && !prevPunc.find());
    }
    
    /**
     * Stems the appropriate words in the given wordList.
     * @param wordList
     * @return
     */
    public List<String> stemText(List<String> wordList)
    {

        List<String> stemmed = new ArrayList<String>();
        Stemmer stemmer;
        
        for (String word : wordList)
        {
            stemmer = new Stemmer();
            stemmer.add(word.toCharArray(), word.length());
            stemmer.stem();
            stemmed.add(stemmer.toString());
        }
        
        return stemmed;
    }
    
    /**
     * Given a term and a doc, calculates term's relative frequency
     * in that doc, ie
     * (# times term appears in doc) / (# total terms in doc)
     * 
     * @param term
     * @return
     */
    private Double calcTermFreq(String term)
    {
        
        return this.termList.get(term).get("count") 
                        / new Double(this.stemmedText.size());
    }
    
    /**
     *  Given a term and its relative doc frequency, calculates the tf-idf 
     *  for the term in the document.
     *  
     * @param term
     * @param docFreq
     * @return
     */
    private Double calcTfidf(String term, int docFreq)
    {
        
        Double termFreq;
        
        try
        {
            termFreq = this.termList.get(term).get("tf");
        } catch (Exception e) // term is not in the term list.
        {
            termFreq = new Double(0);
        }
        
        return termFreq / new Double(docFreq);
        
    }
}
