/**
 *     Metadata Class for Word Cloud Project (Java)
 *   
 *   Daniel Klein
 *   Computer-Based Honors Program
 *   The University of Alabama
 *   5.9.2014
 *       
 *   A metadata object will be a collection of fields (pieces of metadata) that 
 *   accompany a piece of data (in our case, the text of a document). We will 
 *   subclass this class for each type of document we use.
 */
package core.java;

import java.util.ArrayList;
import java.util.List;
import static java.util.Arrays.asList;

/**
 * The Metadata Class
 * @author dmklein
 *
 */
public class Metadata {

	private List<String> fieldNames;
	private String field1;
	private String field2;
	private String field3;
	private String field4;
	
	public Metadata() 
	{
		this.fieldNames = new ArrayList<String>(asList("field1", "field2", "field3", "field4"));
        this.field1 = "test1";
        this.field2 = "test2";
        this.field3 = "test3";
        this.field4 = "test4";
	}
	
	/**
	 * Generates a pretty string representing the metadata.
	 * @return metadata as a string
	 */
	public String toString()
	{
		return "";
	}
	
	/**
	 * Prints out list of metadata fields
	 */
	public void printFields() 
	{
		System.out.println("test");
	}
	
	/**
	 * Prints out formatted metadata
	 */
	public void print()
	{
		System.out.println("test");
	}
}
