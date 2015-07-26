package core.javacore;

import static java.util.Arrays.asList;
import java.util.List;

/**
 * SupremeCourtOpinionMetadata Class for Word Cloud Project (Java)
 *
 * Daniel Klein Computer-Based Honors Program The University of Alabama 9.3.2014
 *
 * This class holds constants used by the WordCloud app.
 */
public class WordCloudConstants
{
    // where the opinion text files live
    public static final String OPINION_DIR_PATH_LOCAL = "C:\\Users\\Daniel\\Dropbox\\Class_Files\\CBH_301\\Word_Cloud\\supreme_court_opinions\\test_output\\opinions";
    public static final String OPINION_DIR_PATH_DEPLOY = "/srv/tomcat/opinion_files";
    public static final String SERIALIZE_DIR_PATH = "";

    // names of metadata fields
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

    public static final List<String> META_FIELD_NAMES =
                        asList(META_CASE_TITLE,
                        META_CASE_NUM,
                        META_US_CITE,
                        META_SC_CITE,
                        META_LAWYERS_ED,
                        META_LEXIS_CITE,
                        META_FULL_CITE,
                        META_CASE_DATES,
                        META_DISPOSITION,
                        META_OPIN_AUTHOR,
                        META_OPIN_TYPE);

    public static final List<String> META_DB_FIELDS =
                        asList("caseTitle",
                                "caseNumber",
                                "usCitation",
                                "scCitation",
                                "lawyersEd",
                                "lexisCitation",
                                "fullCitation",
                                "caseDates",
                                "disposition",
                                "opinionAuthor",
                                "opinionType");

    // when filtering out terms used a ton and terms barely used at all,
    // these are the upper and lower percentage bounds
    public static final Double RELEVANT_TERM_PERCENTAGE_UPPER = 0.95;
    public static final Double RELEVANT_TERM_PERCENTAGE_LOWER = 0.05;

    // the minimum number of terms destemmer will check before
    // deciding the "winning" candidate term is the one to choose
    public static final int DESTEMMER_MIN_NUM_TERMS = 5000;

    // the minimum percentage of terms a candidate term must meet
    // in order to be chosen as destemmed term
    public static final Double DESTEMMER_MIN_PERCENTAGE = 0.20;

    // this is the number of terms that will appear in stats/word cloud
    public static final int NUM_TERMS_IN_CLOUD = 50;
}
