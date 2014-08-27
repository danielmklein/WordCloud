package core.javacore;

import java.io.IOException;

/**
 *   DocumentConverter Class for Word Cloud Project (Java)
 *   
 *   Daniel Klein
 *   Computer-Based Honors Program
 *   The University of Alabama
 *   8.27.2014
 *   
 *  Given a file containing one and only one document (along with
 *  fields/labels/metadata), this class will parse the file and create a 
 *  Document object from the file. This will be extended by the
 *  SupremeCourtOpinionFileConverter class.
 */
public class DocumentConverter 
{

	private Document convertedDoc;
	private String inputPath;
	private String outputPath;
	
	/**
	 * 
	 */
	public DocumentConverter(final String fileToParse, final String serializePath) 
	{
		this.convertedDoc = null;
		this.inputPath = fileToParse;
		this.outputPath = serializePath;
	}
	
	public Document convertFile() throws IOException
	{
		return new Document(null, null, null);
	}
	
	public void saveConvertedDoc() throws IOException
	{
		this.convertedDoc.serialize();
	}
	
	public String getTitledItem(final String line, final String itemRegex)
	{
		String item = "";
		
		// TODO: find out how regexes work in java
		
		return item;
	}

}
