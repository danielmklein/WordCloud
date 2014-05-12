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
package core.javacore;

import java.util.List;
import java.util.Map;
import java.util.HashMap;

/**
 * The Metadata Class
 * @author dmklein
 * This is really an example for how the classes that inherit from this class
 * should act. 
 */
public abstract class Metadata {

	protected Map<String, String> fields;
	protected List<String> fieldNames;
	
	public Metadata() 
	{
		this.fields = new HashMap<String, String>();
	}
	
	/**
	 * 
	 * @param the name of the field to return
	 * @return field for key, if present; null otherwise
	 */
	public String getField(String key) 
	{
		return this.fields.get(key);
	}
	
	/**
	 * 
	 * @param the name of the field to set
	 * @param the value to place in that fields
	 */
	public void setField(String key, String value) 
	{
		this.fields.put(key, value);
	}
	
	/**
	 * Generates a pretty string representing the metadata.
	 * @return metadata as a string
	 */
	public abstract String toString();
	
	/**
	 * Prints out list of metadata fields
	 */
	public abstract void printFields();
	
	/**
	 * Prints out formatted metadata
	 */
	public abstract void print();
}
