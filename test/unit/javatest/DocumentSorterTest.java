package unit.javatest;

import static org.junit.Assert.*;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import core.javacore.Document;
import core.javacore.DocumentSorter;
import core.javacore.Metadata;
import core.javacore.SupremeCourtOpinion;
import core.javacore.SupremeCourtOpinionMetadata;
import core.javacore.WordCloudConstants;

public class DocumentSorterTest
{
    private static final List<String> VALID_OPINION_LINES = Arrays
                    .asList("TITLE: UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES DENTAL CO., ET AL.",
                                    "CASE NUMBER: No. 43",
                                    "US CITATION: 323 U.S. 273",
                                    "SUPREME COURT CITATION: 65 S. Ct. 249",
                                    "LAWYERS ED CITATION: 89 L. Ed. 236",
                                    "LEXIS CITATION: 1944 U.S. LEXIS 1230",
                                    "FULL CITATION: 323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230",
                                    "DATES: November 8, 1944, Argued;December 18, 1944, Decided;",
                                    "DISPOSITION: 53 F.Supp. 596, affirmed.",
                                    "OPINION TYPE: concur",
                                    "* * * * * * * *",
                                    "MR. JUSTICE MURPHY, concurring.",

                                    "I join in the opinion of the Court and believe that the judgment should be affirmed.",
                                    "Congress has the constitutional power to fix venue at any place where a "
                                                    + "crime occurs. Our problem here is to determine, in the absence of a specific "
                                                    + "venue provision, where the crime outlawed by the Federal Denture Act occurred "
                                                    + "for purposes of venue.",

                                    "The Act prohibits the use of the mails for the purpose of sending or "
                                                    + "bringing into any state certain prohibited articles. It is undisputed that "
                                                    + "when a defendant places a prohibited article in the mails in Illinois for "
                                                    + "the purpose of sending it into Delaware he has completed a statutory offense. "
                                                    + "Hence he is triable in Illinois. But to hold that the statutory crime also "
                                                    + "encompasses the receipt of the prohibited article in Delaware, justifying a "
                                                    + "trial at that point, requires an implication that I am unwilling to make in "
                                                    + "the absence of more explicit Congressional language.",

                                    "Very often the difference between liberty and imprisonment in cases where "
                                                    + "the direct evidence offered by the government and the defendant is evenly "
                                                    + "balanced depends upon the presence of character witnesses. The defendant is "
                                                    + "more likely to obtain their presence in the district of his residence, which "
                                                    + "in this instance is usually the place where the prohibited article is mailed. "
                                                    + "The inconvenience, expense and loss of time involved in transplanting these "
                                                    + "witnesses to testify in trials far removed from their homes are often too "
                                                    + "great to warrant their use. Moreover, they are likely to lose much of their "
                                                    + "effectiveness before a distant jury that knows nothing of their reputations. "
                                                    + "Such factors make it difficult for me to conclude, where Congress has not "
                                                    + "said so specifically, that we should construe the Federal Denture Act as "
                                                    + "covering more than the first sufficient and punishable use of the mails "
                                                    + "insofar as the sender of a prohibited article is concerned. The principle of "
                                                    + "narrow construction of criminal statutes does not warrant interpreting the "
                                                    + "\"use\" of the mails to cover all possible uses in light of the foregoing "
                                                    + "considerations.");

    public static final String CASE_TITLE = "UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES DENTAL CO., ET AL.";
    public static final String CASE_NUM = "No. 43";
    public static final String CASE_US_CITE = "323 U.S. 273";
    public static final String CASE_SUPREME_COURT_CITE = "65 S. Ct. 249";
    public static final String CASE_LAWYERS_ED_CITE = "89 L. Ed. 236";
    public static final String CASE_LEXIS_CITE = "1944 U.S. LEXIS 1230";
    public static final String CASE_FULL_CITE = "323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230";
    public static final String CASE_DATES = "November 8, 1944 (Argued) December 18, 1944 (Decided) "; // THIS
                                                                                                      // MIGHT
                                                                                                      // CHANGE!!
    public static final String CASE_DISPOSITION = "53 F.Supp. 596, affirmed.";

    public static final String OPINION_AUTHOR = "MURPHY";
    public static final String OPINION_TYPE = "concur";

    public static final String OPINION_TEXT = String
                    .join("\n", VALID_OPINION_LINES.subList(11,
                                    VALID_OPINION_LINES.size()));

    public static String TEST_FILE_PATH;
    public static String TEST_SERIALIZED_PATH;

    private List<Document> testDocs;
    private DocumentSorter testSorter;

    public List<Document> createTestDocs() throws Exception
    {

        Metadata testMeta1 = new SupremeCourtOpinionMetadata();
        testMeta1.setField(WordCloudConstants.META_CASE_TITLE, CASE_TITLE);
        testMeta1.setField(WordCloudConstants.META_CASE_NUM, CASE_NUM);
        testMeta1.setField(WordCloudConstants.META_US_CITE, CASE_US_CITE);
        testMeta1.setField(WordCloudConstants.META_SC_CITE,
                        CASE_SUPREME_COURT_CITE);
        testMeta1.setField(WordCloudConstants.META_LAWYERS_ED,
                        CASE_LAWYERS_ED_CITE);
        testMeta1.setField(WordCloudConstants.META_LEXIS_CITE, CASE_LEXIS_CITE);
        testMeta1.setField(WordCloudConstants.META_FULL_CITE, CASE_FULL_CITE);
        testMeta1.setField(WordCloudConstants.META_CASE_DATES, CASE_DATES);
        testMeta1.setField(WordCloudConstants.META_DISPOSITION,
                        CASE_DISPOSITION);
        testMeta1.setField(WordCloudConstants.META_OPIN_AUTHOR, OPINION_AUTHOR);
        Document testDoc1 = new SupremeCourtOpinion(testMeta1, OPINION_TEXT,
                        TEST_SERIALIZED_PATH);

        Metadata testMeta2 = new SupremeCourtOpinionMetadata();
        testMeta2.setField(WordCloudConstants.META_CASE_NUM, "No. 43");
        Document testDoc2 = new SupremeCourtOpinion(testMeta2, OPINION_TEXT,
                        TEST_SERIALIZED_PATH);

        Metadata testMeta3 = new SupremeCourtOpinionMetadata();
        testMeta3.setField(WordCloudConstants.META_CASE_NUM, "No. 67");
        testMeta3.setField(WordCloudConstants.META_OPIN_AUTHOR, "JOHNSON");
        Document testDoc3 = new SupremeCourtOpinion(testMeta3, OPINION_TEXT,
                        TEST_SERIALIZED_PATH);

        Metadata testMeta4 = new SupremeCourtOpinionMetadata();
        testMeta4.setField(WordCloudConstants.META_CASE_NUM, "No. 46");
        testMeta4.setField(WordCloudConstants.META_OPIN_AUTHOR, "MURPHY");
        Document testDoc4 = new SupremeCourtOpinion(testMeta4, OPINION_TEXT,
                        TEST_SERIALIZED_PATH);

        Metadata testMeta5 = new SupremeCourtOpinionMetadata();
        testMeta5.setField(WordCloudConstants.META_CASE_NUM, "No. 43");
        Document testDoc5 = new SupremeCourtOpinion(testMeta5, OPINION_TEXT,
                        TEST_SERIALIZED_PATH);

        return Arrays.asList(testDoc1, testDoc2, testDoc3, testDoc4, testDoc5);
    }

    @Before
    public void setUp() throws Exception
    {

        this.testDocs = this.createTestDocs();
        this.testSorter = new DocumentSorter(this.testDocs);
    }

    @After
    public void tearDown() throws Exception
    {

    }

    /*@Test
    public void testSortDocsNormalCase() throws IOException
    {

        // If I sort on case num, I should get one subset of 3 for "No. 43",
        // a subset of 1 for "No. 46", and a subset of 1 for "No. 67"
        System.out.println("DocumentSorterTest: testing DocumentSorter.sortDocs normal case.");
        
        List<List<Document>> sortedSubsets = this.testSorter.sortDocs(WordCloudConstants.META_CASE_NUM);
        List<List<Document>> expectedSubsets = Arrays.asList(Arrays.asList(this.testDocs.get(0), this.testDocs.get(1), this.testDocs.get(4)),
                                                Arrays.asList(this.testDocs.get(3), this.testDocs.get(2)));
        assertEquals(expectedSubsets.size(), sortedSubsets.size());
        
        List<Document> expectedSubset;
        List<Document> sortedSubset;
        Document expectedDoc;
        Document sortedDoc;
        
        for (int i = 0; i < expectedSubsets.size(); ++i)
        {
            expectedSubset = expectedSubsets.get(i);
            sortedSubset = sortedSubsets.get(i);
            assertEquals(expectedSubset.size(), sortedSubset.size());
            
            for (int j = 0; j < expectedSubset.size(); ++j)
            {
                expectedDoc = expectedSubset.get(j);
                sortedDoc = sortedSubset.get(j);
                assertEquals(expectedDoc.getMetadata().getField(WordCloudConstants.META_CASE_NUM),
                             sortedDoc.getMetadata().getField(WordCloudConstants.META_CASE_NUM));
            }
        }
    }

    @Test
    public void testSortDocsEmptyInputList() throws IOException
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.sortDocs with empty input list of docs.");

        this.testSorter.setDocList(new ArrayList<Document>());
        List<List<Document>> sortedSubsets = this.testSorter.sortDocs(WordCloudConstants.META_CASE_NUM);
        
        assertEquals(0, sortedSubsets.size());
    }

    @Test
    public void testSortDocsInvalidSortField()
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.sortDocs with invalid sort field...");

        try
        {
            this.testSorter.sortDocs("this_isnt_a_field");
        } catch (Exception e)
        {
            // the exception is expected behavior
        }
        fail("sortDocs should have thrown an exception when it encountered an invalid sort field.");
    }*/

    @Test
    public void testCreateSubsetNormalCase() throws IOException
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.createSubset normal case...");

        List<String> testAllowedVals = Arrays.asList("MURPHY", "JOHNSON");
        List<Document> expectedSubset = Arrays.asList(this.testDocs.get(0), this.testDocs.get(2), this.testDocs.get(3));
        List<Document> createdSubset = this.testSorter.createSubset(WordCloudConstants.META_OPIN_AUTHOR, testAllowedVals, false);
        System.out.println(expectedSubset);
        System.out.println(createdSubset);
        
        assertEquals(expectedSubset, createdSubset);
    }
    
    @Test
    public void testCreateSubsetNormalCaseInverted() throws IOException
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.createSubset normal case, inverting the subset...");

        List<String> testAllowedVals = Arrays.asList("MURPHY", "JOHNSON");
        List<Document> expectedSubset = Arrays.asList(this.testDocs.get(1), this.testDocs.get(4));
        List<Document> createdSubset = this.testSorter.createSubset(WordCloudConstants.META_OPIN_AUTHOR, testAllowedVals, true);
        System.out.println(expectedSubset);
        System.out.println(createdSubset);
        
        assertEquals(expectedSubset, createdSubset);
    }

    @Test
    public void testCreateSubsetNoAllowedValues() throws IOException
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.createSubset with no "
                        + "list of allowed values...");
        List<String> testAllowedVals = new ArrayList<String>();
        List<Document> expectedSubset = new ArrayList<Document>();
        List<Document> createdSubset = this.testSorter.createSubset(WordCloudConstants.META_OPIN_AUTHOR, testAllowedVals, false);
        
        assertEquals(expectedSubset, createdSubset);
    }

    @Test
    public void testCreateSubsetNoAllowedValueMatches() throws IOException
    {

        System.out.println("DocumentSorterTest: testing DocumentSorter.createSubset with no "
                        + "matches on the allowed values...");
        
        List<String> testAllowedVals = Arrays.asList("JACKSON", "THOMPSON");
        List<Document> expectedSubset = new ArrayList<Document>();
        List<Document> createdSubset = this.testSorter.createSubset(WordCloudConstants.META_OPIN_AUTHOR, testAllowedVals, false);
        
        assertEquals(expectedSubset, createdSubset);

    }
}
