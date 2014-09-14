package core.javacore;

import java.util.Arrays;
import java.util.List;

/**
 * Daniel Klein Computer-Based Honors Program The University of Alabama
 * 9.14.2014
 * 
 * This is a utility class used in the WordCloud project for checking to see if
 * a given term is deemed a stop word. This holds the list of stop words and can
 * tell a client class whether or not a term is a stop word.
 */
public class StopWords
{

    private static List<String> stopWords = Arrays.asList("a", "about",
                    "above", "after", "again", "against", "all", "am", "an",
                    "and", "any", "are", "aren't", "as", "at", "be", "because",
                    "been", "before", "being", "below", "between", "both",
                    "but", "by", "can't", "cannot", "could", "couldn't", "did",
                    "didn't", "do", "does", "doesn't", "doing", "don't",
                    "down", "during", "each", "few", "for", "from", "further",
                    "had", "hadn't", "has", "hasn't", "have", "haven't",
                    "having", "he", "he'd", "he'll", "he's", "her", "here",
                    "here's", "hers", "herself", "him", "himself", "his",
                    "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if",
                    "in", "into", "is", "isn't", "it", "it's", "its", "itself",
                    "let's", "me", "more", "most", "mustn't", "my", "myself",
                    "no", "nor", "not", "of", "off", "on", "once", "only",
                    "or", "other", "ought", "our", "ours", "ourselves", "out",
                    "over", "own", "same", "shan't", "she", "she'd", "she'll",
                    "she's", "should", "shouldn't", "so", "some", "such",
                    "than", "that", "that's", "the", "their", "theirs", "them",
                    "themselves", "then", "there", "there's", "these", "they",
                    "they'd", "they'll", "they're", "they've", "this", "those",
                    "through", "to", "too", "under", "until", "up", "very",
                    "was", "wasn't", "we", "we'd", "we'll", "we're", "we've",
                    "were", "weren't", "what", "what's", "when", "when's",
                    "where", "where's", "which", "while", "who", "who's",
                    "whom", "why", "why's", "with", "won't", "would",
                    "wouldn't", "you", "you'd", "you'll", "you're", "you've",
                    "your", "yours", "yourself", "yourselves", 
                    /* following words are added, SC opinion-specific */
                    "concur", "dissent", "concurring", "dissenting", "case", "join");
    
    // TODO: figure out cleaner way to do this / add or remove terms

    public StopWords()
    {
    }
    
    public static boolean isStopWord(final String term)
    {
        
        return stopWords.contains(term.toLowerCase());
    }

}
