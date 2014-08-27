package core.javacore;

import java.io.IOException;
import java.util.List;

/**
 *   SupremeCourtOpinionFileConverter Class for Word Cloud Project (Java)
 *   
 *   Daniel Klein
 *   Computer-Based Honors Program
 *   The University of Alabama
 *   8.27.2014
 *   
 *  Given a file containing one and only one opinion (along with
 *  fields/labels/metadata), this class will parse the file and create a 
 *  SupremeCourtOpinion object from the file.
 */
public class SupremeCourtOpinionFileConverter extends DocumentConverter 
{

	/**
	 * @param fileToParse
	 * @param serializePath
	 */
	public SupremeCourtOpinionFileConverter(String fileToParse,
			String serializePath) 
	{
		super(fileToParse, serializePath);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public SupremeCourtOpinion convertFile() throws IOException
	{
		SupremeCourtOpinion converted = null;
		
		// TODO: write me!
		if (true) 
		{
			throw new IOException("SupremeCourtOpinion.convertFile() hasn't been written yet.");
		}
		return converted;
	}
	
	private String getAuthor(String filePath)
	{
		// TODO: write me!
		return "";
	}
	
	private List<String> splitDates(String dateString)
	{
		// TODO: write me!
		return null;
	}

}
