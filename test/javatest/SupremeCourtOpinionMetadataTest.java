/**
 * 
 */
package javatest;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static java.util.Arrays.asList;
import java.util.List;

import core.javacore.SupremeCourtOpinionMetadata;

/**
 * @author dmklein
 *
 */
public class SupremeCourtOpinionMetadataTest {
	private SupremeCourtOpinionMetadata testMetadata;
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		this.testMetadata = new SupremeCourtOpinionMetadata();
	}

	
	/**
	 * @throws java.lang.Exception
	 */
	@After
	public void tearDown() throws Exception {
	}

	
	/**
	 * Test method for {@link core.javacore.SupremeCourtOpinionMetadata#toString()}.
	 */
	@Test
	public void testToString() {
		List<String> expectedFields = asList("Case Title", "Case Number", "US Citation",
									"Supreme Court Citation", "Case Lawyers Ed Citation",
									"Lexis Citation", "Full Citation", "Case Dates", 
									"Case Disposition", "Opinion Author", 
									"Opinion Type")	;
		
		// first let's test the string conversion with all blank fields
		String expected = "";
		for (String curField: expectedFields)
		{
			expected += curField + " : " + this.testMetadata.getField(curField) + "\n";
		}
		String actual = this.testMetadata.toString();
		
		assertEquals("String representation of SupremeCourtOpinionMetadata different than expected.",
						expected, actual);
		
		// set some fields and make sure they show up properly in the string 
		this.testMetadata.setField("Case Title", "This is a test title.");
		this.testMetadata.setField("Opinion Author", "JUSTICE SCALIA");
		
		expected = "";
		for (String curField: expectedFields)
		{
			expected += curField + " : " + this.testMetadata.getField(curField) + "\n";
		}
		actual = this.testMetadata.toString();
		
		assertEquals("String representation of SupremeCourtOpinionMetadata different than expected.",
						expected, actual);
	}

	
	/**
	 * Test method for {@link core.javacore.SupremeCourtOpinionMetadata#printFields()}.
	 */
	@Test
	public void testPrintFields() {
		
		fail("Not yet implemented");
	}

	
	/**
	 * Test method for {@link core.javacore.SupremeCourtOpinionMetadata#print()}.
	 */
	@Test
	public void testPrint() {
		fail("Not yet implemented");
	}

	
	/**
	 * Test method for {@link core.javacore.Metadata#getField(java.lang.String)}.
	 */
	@Test
	public void testGetField() {
		fail("Not yet implemented");
	}
	
	
	/**
	 * Test method for {@link core.javacore.Metadata#setField(java.lang.String, java.lang.String)}.
	 */
	@Test
	public void testSetField() {
		fail("Not yet implemented");
	}
}
