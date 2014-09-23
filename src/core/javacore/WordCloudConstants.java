/**
 * 
 */
package core.javacore;

/**
 * SupremeCourtOpinionMetadata Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama 9.3.2014
 * 
 * This class holds constants used by the WordCloud app.
 */
public class WordCloudConstants
{

    public static final String META_CASE_TITLE = "Case Title";
    public static final String META_CASE_NUM = "Case Number";
    public static final String META_US_CITE = "US Citation";
    public static final String META_SC_CITE = "Supreme Court Citation";
    public static final String META_LAWYERS_ED = "Case Lawyers Ed Citation";
    public static final String META_LEXIS_CITE = "Lexis Citation";
    public static final String META_FULL_CITE = "Full Citation";
    public static final String META_CASE_DATES = "Case Dates";
    public static final String META_DISPOSITION = "Case Disposition";
    public static final String META_OPIN_AUTHOR = "Opinion Author";
    public static final String META_OPIN_TYPE = "Opinion Type";
    
    public static final Double RELEVANT_TERM_PERCENTAGE_UPPER = 0.95;
    public static final Double RELEVANT_TERM_PERCENTAGE_LOWER = 0.05;
    
    public static final int DESTEMMER_MIN_NUM_TERMS = 5000;
    public static final Double DESTEMMER_MIN_PERCENTAGE = 0.20;
}
