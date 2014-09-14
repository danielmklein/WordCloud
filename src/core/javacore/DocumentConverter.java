package core.javacore;

import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * DocumentConverter Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama
 * 8.27.2014
 * 
 * Given a file containing one and only one document (along with
 * fields/labels/metadata), this class will parse the file and create a Document
 * object from the file. This will be extended by the
 * SupremeCourtOpinionFileConverter class.
 */
public class DocumentConverter
{

    protected Document convertedDoc;
    protected String inputPath;
    protected String outputPath;

    /**
	 * 
	 */
    public DocumentConverter(final String fileToParse,
                    final String serializePath)
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

    public String getTitledItem(final String line, final Pattern itemRegex)
    {

        String item = "";
        Matcher match = itemRegex.matcher(line);

        if (match.find())
        {
            item = match.group(1);
        }

        return item;
    }

}
