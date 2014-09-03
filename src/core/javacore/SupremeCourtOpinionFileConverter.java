package core.javacore;

import java.io.IOException;
import java.io.File;

import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

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

	private String inputPath;
	/**
	 * @param fileToParse
	 * @param serializePath
	 */
	public SupremeCourtOpinionFileConverter(String fileToParse,
			String serializePath) 
	{
		super(fileToParse, serializePath);
		this.inputPath = fileToParse;
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public SupremeCourtOpinion convertFile() throws IOException
	{
		SupremeCourtOpinion converted = null;
		
		// Check to see if the input file exists.
		File inputFile = new File(this.inputPath);
		if (!inputFile.isFile())
		{
			throw new IOException("The path " + this.inputPath + " does not exist!");
		}
		
		Pattern txtFileRegex = Pattern.compile("\\.txt$");
		Matcher match = txtFileRegex.matcher(this.inputPath);
		if (!match.find())
		{
			throw new IOException("The file " + this.inputPath + " is not a text file and "
					+ "thus cannot be converted.");
		}
		
		
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
