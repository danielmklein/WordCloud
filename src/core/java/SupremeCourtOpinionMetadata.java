/**
 * 
 */
package core.java;

import static java.util.Arrays.asList;

/**
 *   SupremeCourtOpinionMetadata Class for Word Cloud Project (Java)
 *   
 *   Daniel Klein
 *   Computer-Based Honors Program
 *   The University of Alabama
 *   5.10.2014
 *   
 *   This specializes the generic Metadata class to apply to Supreme Court 
 *   opinions. 
 */
public class SupremeCourtOpinionMetadata extends Metadata {
	
	
	/**
	 * Constructor -- initializes every metadata field to empty string
	 */
	public SupremeCourtOpinionMetadata()
	{
		this.fieldNames = asList("Case Title", "Case Number", "US Citation",
		                         "Supreme Court Citation", "Case Lawyers Ed Citation",
		                         "Lexis Citation", "Full Citation", "Case Dates", 
		                         "Case Disposition", "Opinion Author", 
		                         "Opinion Type");
		for (String fieldName: this.fieldNames)
		{
			this.fields.put(fieldName, "");
		}
	}
	
	
	public String toString()
	{
		String returnString = "";
		for (String fieldName: this.fieldNames)
		{
			returnString += fieldName + " : " + this.fields.get(fieldName) + "\n";
		}
		return returnString;
	}

	
	public void print()
	{
		System.out.println(this.toString());
	}
	
	
	public void printFields()
	{
		String printString = "";
		for (String fieldName: this.fieldNames)
		{
			printString += fieldName + "\n";
		}
		System.out.println(printString);
	}
}
