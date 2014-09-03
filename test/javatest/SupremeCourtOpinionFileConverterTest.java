package javatest;

import static org.junit.Assert.*;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import core.javacore.SupremeCourtOpinion;
import core.javacore.SupremeCourtOpinionFileConverter;

public class SupremeCourtOpinionFileConverterTest {

	private static final List<String> VALID_OPINION_LINES = Arrays.asList(
		"TITLE: UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES DENTAL CO., ET AL.",
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
		+ "considerations."		
	);
	
	public static final String CASE_TITLE = "UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES DENTAL CO., ET AL.";
	public static final String CASE_NUM = "No. 43";
	public static final String CASE_US_CITE = "323 U.S. 273";
	public static final String CASE_SUPREME_COURT_CITE = "65 S. Ct. 249";
	public static final String CASE_LAWYERS_ED_CITE = "89 L. Ed. 236";
	public static final String CASE_LEXIS_CITE = "1944 U.S. LEXIS 1230";
	public static final String CASE_FULL_CITE = "323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230";
	public static final String CASE_DATES = "November 8, 1944 (Argued) December 18, 1944 (Decided) "; // THIS MIGHT CHANGE!!
	public static final String CASE_DISPOSITION = "53 F.Supp. 596, affirmed.";

	public static final String OPINION_AUTHOR = "MURPHY";
	public static final String OPINION_TYPE = "concur";
			
	public static final String OPINION_TEXT = String.join("\n", VALID_OPINION_LINES.subList(11, VALID_OPINION_LINES.size()));		
	
	public static String TEST_FILE_PATH;
	public static String TEST_SERIALIZED_PATH;
	
	private SupremeCourtOpinionFileConverter testConverter;
	
	private void createTestFile(List<String> fileLines) throws IOException
	{
		PrintWriter pw = null; 
		try 
		{
			pw = new PrintWriter(TEST_FILE_PATH);
			for (String line : fileLines)
			{
				pw.println(line);
			}
		} catch (IOException e)
		{
			throw new IOException("Something went wrong while creating the test file " + TEST_FILE_PATH);
		} finally 
		{
			if (pw != null)
			{
				pw.close();
			}
		}	
	}
	
	@Before
	public void setUp() throws Exception {
		// create the TEST_FILE_PATH 
		try
		{
			TEST_FILE_PATH = (new File(".")).getCanonicalPath()
					+ File.separator + "MURPHY_1944 U.S. LEXIS 1230.txt";
			TEST_SERIALIZED_PATH = (new File(".")).getCanonicalPath()
					+ File.separator + "serialized_test_doc";
		} catch (IOException e)
		{
			throw new IOException("Something went wrong while building the TEST_FILE_PATH or TEST_SERIALIZED_PATH.");
		}
		
		this.testConverter = new SupremeCourtOpinionFileConverter(TEST_FILE_PATH, TEST_SERIALIZED_PATH);
		this.createTestFile(VALID_OPINION_LINES);
	}

	@After
	public void tearDown() throws Exception {
		File testFile = new File(TEST_FILE_PATH);
		if (testFile.isFile()) 
		{
			try 
			{
				testFile.delete();
			} catch (Exception e)
			{
				throw new Exception("Something went wrong while deleting the file at " + TEST_FILE_PATH);
			}
		}
	}

	@Test
	public void testNormalCase() throws IOException {
        System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() normal case...");

		this.createTestFile(VALID_OPINION_LINES);
		SupremeCourtOpinion convertedOpinion = this.testConverter.convertFile();
		
		fail("Not yet implemented");
	}
	
	@Test
	public void testNoNoMetadataInFile() throws IOException {
        System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() "
                + "with no Metadata in the input file...");
        
        this.createTestFile(VALID_OPINION_LINES.subList(10, VALID_OPINION_LINES.size()));
        SupremeCourtOpinion convertedOpinion = this.testConverter.convertFile();
        
		fail("Not yet implemented");
	}
	@Test
	public void testNoBodyTextInFile() throws IOException {
        System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() "
	              + "with no body text in the input file...");
        
        this.createTestFile(VALID_OPINION_LINES.subList(0, 11));
        SupremeCourtOpinion convertedOpinion = this.testConverter.convertFile();
        
		System.out.println(TEST_FILE_PATH);
		fail("Not yet implemented");
	}
	
	@Test
	public void testOutputFileNotWritable() throws IOException {
        System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() "
                + "and save_converted_doc() with an unwritable output file...");
		System.out.println(TEST_FILE_PATH);
		
        this.createTestFile(VALID_OPINION_LINES);
        SupremeCourtOpinion convertedOpinion = this.testConverter.convertFile();
        
		fail("Not yet implemented");
	}
	
	@Test
	public void testInputFileNonexistent() throws IOException {
		System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() "
              + "with nonexistent input file...");
		
		try 
		{
			this.testConverter.convertFile();
		} catch (IOException e) 
		{
			// this exception is expected behavior.
			return;
		}
        
		fail("convertFile should have thrown an exception because of the nonexistent file.");
	}
	
	@Test
	public void testEmptyInputFile() throws IOException {
        System.out.println("DocumentConverterTest: testing DocumentConverter.convert_file() "
                + "with completely empty input file...");

        this.createTestFile(new ArrayList<String>());

        SupremeCourtOpinion convertedOpinion = this.testConverter.convertFile();
        
        fail("Not yet implemented");
	}
	

}
