package core.javacore;

import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
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

	/**
	 * @param fileToParse
	 * @param serializePath
	 */
	public SupremeCourtOpinionFileConverter(String fileToParse,
			String serializePath) 
	{
		super(fileToParse, serializePath);
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
	
	public String getAuthor(String filePath)
	{
	    
	    String author = "";
	    Pattern authorRegex = Pattern.compile("([\\w'\\- ]+)_\\d{4} U\\.S\\. LEXIS");
	    Matcher authorMatch = authorRegex.matcher(filePath);
	    if (authorMatch.find())
	    {
	        author = authorMatch.group(1);
	    }
	    
	    return author;
	}
	
	public String splitDates(String dateString)
	{
	    
	    String dates = "";
	    Pattern dateStringRegex = Pattern.compile("\\w+\\s\\d{1,2}-?\\d?\\d?,\\s\\d{4},\\s\\w+;");
	    Matcher rawDatesMatch = dateStringRegex.matcher(dateString);
	    List<String> rawDates = new ArrayList<String>();
	    
	    while (rawDatesMatch.find())
	    {
	        rawDates.add(rawDatesMatch.group());
	    }
	    
	    Pattern groupedDateRegex = Pattern.compile("(\\w+\\s\\d{1,2}-?\\d?\\d?,\\s\\d{4}),\\s(\\w+);");
	    Matcher groupedDateMatch;
	    String date;
	    String action;
	    
	    for (String rawDate : rawDates)
	    {
	        groupedDateMatch = groupedDateRegex.matcher(rawDate);
	        
	        if (groupedDateMatch.find())
	        {
	            date = groupedDateMatch.group(1);
	            action = groupedDateMatch.group(2);
	            dateString = date + " (" + action + ") ";
	            dates += dateString;
	        }
	    }
	    
	    return dates;
	    
	}

}
