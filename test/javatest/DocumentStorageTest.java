package javatest;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import core.javacore.Document;
import core.javacore.DocumentStorage;
import core.javacore.Metadata;
import core.javacore.SupremeCourtOpinionMetadata;

/**
 * @author Daniel
 *
 */
public class DocumentStorageTest
{
    
    private static String TEST_TEXT =
                    "The reader is probably asking: Why would anyone go to Camp Green Lake? "
                    + "Most campers weren't given a choice. Camp Green Lake is a camp for bad boys. "
                    + "If you take a bad boy and make him dig a hole every day in the hot sun, it "
                    + "will turn him into a good boy. That was what some people thought. "
                    + "Stanley Yelnats was given a choice. The judge said, 'You may go to jail, or "
                    + "you may go to Camp Green Lake.' "
                    + "Stanley was from a poor family. He had never been to camp before.";

    private static String NO_PROPER_NOUNS =
                    "The reader is probably asking: would anyone go to "
                    + "Most campers weren't given a choice. Camp is a camp for bad boys. "
                    + "If you take a bad boy and make him dig a hole every day in the hot sun, it "
                    + "will turn him into a good boy. That was what some people thought. "
                    + "Stanley was given a choice. The judge said, 'You may go to jail, or "
                    + "you may go to "
                    + "Stanley was from a poor family. He had never been to camp before.";
                    

    private static String NO_PUNCTUATION =
                    "The reader is probably asking  Why would anyone go to Camp Green Lake  Most "
                    + "campers werent given a choice  Camp Green Lake is a camp for bad boys  If "
                    + "you take a bad boy and make him dig a hole every day in the hot sun  it will "
                    + "turn him into a good boy  That was what some people thought  Stanley Yelnats "
                    + "was given a choice  The judge said   You may go to jail  or you may go to Camp "
                    + "Green Lake   Stanley was from a poor family  He had never been to camp before ";
                   

    private static String NO_SHORT_WORDS =
                    "The reader probably asking Why would anyone Camp Green Lake Most campers weren "
                    + "given choice Camp Green Lake camp for bad boys you take bad boy and make him "
                    + "dig hole every day the hot sun will turn him into good boy That was what some "
                    + "people thought Stanley Yelnats was given choice The judge said You may jail "
                    + "you may Camp Green Lake Stanley was from poor family had never been camp before";
            
    private static List<String> SPLIT_TEXT = Arrays.asList("reader", "probably", "asking", "anyone", 
                   "camp", "green", "lake", "campers", "werent", "given", 
                   "choice", "camp", "green", "lake", "camp", "bad", 
                   "boys", "take", "bad", "boy", "make", "dig", "hole", 
                   "every", "day", "hot", "sun", "turn", "good", "boy", 
                   "people", "thought", "stanley", "yelnats", "given", 
                   "choice", "judge", "said", "may", "jail", "may", 
                   "camp", "green", "lake", "stanley", "poor", "family", 
                   "never", "camp");

    private static List<String> STEMMED_TEXT = Arrays.asList("reader", "probabl", "ask", "anyon", 
                     "camp", "green", "lake", "camper", "werent", 
                     "given", "choic", "camp", "green", "lake", "camp", 
                     "bad", "boi", "take", "bad", "boi", "make", "dig", 
                     "hole", "everi", "dai", "hot", "sun", "turn", 
                     "good", "boi", "peopl", "thought", "stanlei", 
                     "yelnat", "given", "choic", "judg", "said", "mai", 
                     "jail", "mai", "camp", "green", "lake", "stanlei", 
                     "poor", "famili", "never", "camp");

    private String testText;
    private Metadata testMeta;
    private String testFilename;
    private DocumentStorage testDoc;
    
    /**
     * @throws java.lang.Exception
     */
    @Before
    public void setUp() throws Exception
    {
        this.testText = TEST_TEXT;
        this.testMeta = new SupremeCourtOpinionMetadata();
        this.testFilename = "test_document.txt";
        this.testDoc = new DocumentStorage(this.testMeta, this.testText, this.testFilename);
    }

    /**
     * @throws java.lang.Exception
     */
    @After
    public void tearDown() throws Exception
    {

    }
    
    @Test
    public void testStemText()
    {
        System.out.println("Testing DocumentStorage.stemText()...");
        
        List<String> expected = STEMMED_TEXT;
        List<String> actual = this.testDoc.stemText(SPLIT_TEXT);
        
        System.out.println("expected: " + expected);
        System.out.println("actual  : " + actual);
        assertEquals(expected, actual);
        
        System.out.println("DocumentStorage.stemText() testing finished.***");
    }
    
    @Test
    public void testFilterText()
    {
        System.out.println("Testing DocumentStorage.filterText()...");
        List<String> expected = SPLIT_TEXT;//FILTERED_TEXT;
        List<String> actual = this.testDoc.filterText(TEST_TEXT, false);
                        System.out.println("expected: " + expected);
        System.out.println("actual  : " + actual);
        assertEquals(expected, actual);
        System.out.println("DocumentStorage.filter_text() testing finished.***");
    }
        

}
