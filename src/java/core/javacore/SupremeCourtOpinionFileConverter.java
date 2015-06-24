package core.javacore;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * SupremeCourtOpinionFileConverter Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama
 * 8.27.2014
 * 
 * Given a file containing one and only one opinion (along with
 * fields/labels/metadata), this class will parse the file and create a
 * SupremeCourtOpinion object from the file.
 */
public class SupremeCourtOpinionFileConverter extends DocumentConverter
{
    private SupremeCourtOpinion converted;

    /**
     * @param fileToParse
     * @param serializePath
     */
    public SupremeCourtOpinionFileConverter(String fileToParse,
                    String serializePath)
    {

        super(fileToParse, serializePath);
        this.converted = new SupremeCourtOpinion(null, null, null);
    }

    public void setFileToParse(String inputPath)
    {
        this.inputPath = inputPath;
    }

    private boolean isTextFile(String path)
    {
        Pattern txtFileRegex = Pattern.compile("\\.txt$");
        Matcher match = txtFileRegex.matcher(path);

        return match.find();
    }

    private boolean isExistingFile(String path)
    {
        File inputFile = new File(path);
        return inputFile.isFile();
    }

    public SupremeCourtOpinion convertFromInputStream(InputStream stream, String path) throws IOException
    {
        if (!this.isTextFile(path))
        {
            throw new IOException("The file " + path
                            + " is not a text file and "
                            + "thus cannot be converted.");
        }

        SupremeCourtOpinion converted = null;
        try 
        {
            BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
            converted = this.convertFromBufferedReader(reader, path);
        } catch (Exception e)
        {
            throw new IOException(e);
        }

        return converted;
    }

    public SupremeCourtOpinion convertFromPath(String path) throws IOException
    {

        // Check to see if the input file exists.
        if (!this.isExistingFile(path))
        {
            System.out.println("couldn't find the file!");
            throw new IOException("The path " + path
                            + " does not exist!");
        }


        if (!this.isTextFile(path))
        {
            throw new IOException("The file " + path
                            + " is not a text file and "
                            + "thus cannot be converted.");
        }


        File file = new File(path);
        BufferedReader reader = null;
        SupremeCourtOpinion converted = null;

        try
        {
            reader = new BufferedReader(new FileReader(file));
            converted = this.convertFromBufferedReader(reader, path);
        } catch (FileNotFoundException e)
        {
            // TODO: handle these more gracefully?
            e.printStackTrace();
        } catch (IOException e)
        {
            e.printStackTrace();
        } finally
        {
            try
            {
                if (reader != null)
                {
                    reader.close();
                }
            } catch (IOException e)
            {
                // so what?
            }
        }
        
        return converted;

    }

    private SupremeCourtOpinion convertFromBufferedReader(BufferedReader reader, String path) throws IOException
    {
        String title = "";
        String caseNum = "";
        String usCite = "";
        String scCite = "";
        String lawyersEd = "";
        String lexisCite = "";
        String fullCite = "";
        String dates = "";
        String disposition = "";
        String author = "";
        String opinType = "";
        String bodyText = "";

        String titleMatch;
        String caseNumMatch;
        String usCiteMatch;
        String scCiteMatch;
        String lawyersEdMatch;
        String lexisCiteMatch;
        String fullCiteMatch;
        String dateMatch;
        String dispositionMatch;
        String opinTypeMatch;

        Pattern titleRegex = Pattern.compile("TITLE: (.*)");
        Pattern caseNumRegex = Pattern.compile("CASE NUMBER: (.*)");
        Pattern usCiteRegex = Pattern.compile("US CITATION: (.*)");
        Pattern scCiteRegex = Pattern.compile("SUPREME COURT CITATION: (.*)");
        Pattern lawyersEdRegex = Pattern.compile("LAWYERS ED CITATION: (.*)");
        Pattern lexisCiteRegex = Pattern.compile("LEXIS CITATION: (.*)");
        Pattern fullCiteRegex = Pattern.compile("FULL CITATION: (.*)");
        Pattern datelineRegex = Pattern.compile("DATES: (.*)");
        Pattern dispositionRegex = Pattern.compile("DISPOSITION: (.*)");
        Pattern opinTypeRegex = Pattern.compile("OPINION TYPE: (.*)");

        Pattern breakRegex = Pattern.compile("\\* \\* \\* \\* \\* \\* \\* \\*");
        boolean foundBreak = false;
        List<String> opinionLines = new ArrayList<String>();

        String line = null;
        // Parse out necessary fields
        try
        {
            while ((line = reader.readLine()) != null)
            {
                //System.out.println("next line is: " + line);
                // regex stuff goes here

                if (foundBreak) // we have reached the opinion body
                {
                    opinionLines.add(line.trim());
                    continue;
                }

                titleMatch = this.getTitledItem(line, titleRegex);
                if (!titleMatch.equals(""))
                {
                    title = titleMatch;
                }

                caseNumMatch = this.getTitledItem(line, caseNumRegex);
                if (!caseNumMatch.equals(""))
                {
                    caseNum = caseNumMatch;
                }

                usCiteMatch = this.getTitledItem(line, usCiteRegex);
                if (!usCiteMatch.equals(""))
                {
                    usCite = usCiteMatch;
                }

                scCiteMatch = this.getTitledItem(line, scCiteRegex);
                if (!scCiteMatch.equals(""))
                {
                    scCite = scCiteMatch;
                }

                lawyersEdMatch = this.getTitledItem(line, lawyersEdRegex);
                if (!lawyersEdMatch.equals(""))
                {
                    lawyersEd = lawyersEdMatch;
                }

                lexisCiteMatch = this.getTitledItem(line, lexisCiteRegex);
                if (!lexisCiteMatch.equals(""))
                {
                    lexisCite = lexisCiteMatch;
                }

                fullCiteMatch = this.getTitledItem(line, fullCiteRegex);
                if (!fullCiteMatch.equals(""))
                {
                    fullCite = fullCiteMatch;
                }

                dateMatch = this.getTitledItem(line, datelineRegex);
                if (!dateMatch.equals(""))
                {
                    dates = this.splitDates(dateMatch);
                }

                dispositionMatch = this.getTitledItem(line, dispositionRegex);
                if (!dispositionMatch.equals(""))
                {
                    disposition = dispositionMatch;
                }

                opinTypeMatch = this.getTitledItem(line, opinTypeRegex);
                if (!opinTypeMatch.equals(""))
                {
                    opinType = opinTypeMatch;
                }

                if (breakRegex.matcher(line).find())
                {
                    foundBreak = true;
                }

            }
        } catch (IOException e)
        {
            throw e;
        }

        SupremeCourtOpinion converted = new SupremeCourtOpinion(null, null, null);
        author = this.getAuthor(path);
        //bodyText = String.join("\n", opinionLines);
        bodyText = this.joinStrings(opinionLines, "\n"); // changed for java 7 compatibility.

        // Create new metadata object to go in the new opinion
        Metadata newMeta = new SupremeCourtOpinionMetadata();
        newMeta.setField(WordCloudConstants.META_CASE_TITLE, title);
        newMeta.setField(WordCloudConstants.META_CASE_NUM, caseNum);
        newMeta.setField(WordCloudConstants.META_US_CITE, usCite);
        newMeta.setField(WordCloudConstants.META_SC_CITE, scCite);
        newMeta.setField(WordCloudConstants.META_LAWYERS_ED, lawyersEd);
        newMeta.setField(WordCloudConstants.META_LEXIS_CITE, lexisCite);
        newMeta.setField(WordCloudConstants.META_FULL_CITE, fullCite);
        newMeta.setField(WordCloudConstants.META_CASE_DATES, dates);
        newMeta.setField(WordCloudConstants.META_DISPOSITION, disposition);
        newMeta.setField(WordCloudConstants.META_OPIN_AUTHOR, author);
        newMeta.setField(WordCloudConstants.META_OPIN_TYPE, opinType);

        //converted = new SupremeCourtOpinion(newMeta, bodyText, this.outputPath);
        converted.setText(bodyText);
        converted.setMetadata(newMeta);
        converted.setOutputFilename(this.outputPath);

        return converted;

    }

    private String joinStrings(List<String> strings, String separator)
    {
        StringBuilder sb = new StringBuilder();
        String sep = "";
        for (String s: strings) {
            sb.append(sep).append(s);
            sep = separator;
        }

        return sb.toString();   
    }

    public String getAuthor(String filePath)
    {

        String author = "";
        Pattern authorRegex = Pattern
                        .compile("([\\w'\\- ]+)_\\d{4} U\\.S\\. LEXIS");
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
        Pattern dateStringRegex = Pattern
                        .compile("\\w+\\s\\d{1,2}-?\\d?\\d?,\\s\\d{4},\\s\\w+;");
        Matcher rawDatesMatch = dateStringRegex.matcher(dateString);
        List<String> rawDates = new ArrayList<String>();

        while (rawDatesMatch.find())
        {
            rawDates.add(rawDatesMatch.group());
        }

        Pattern groupedDateRegex = Pattern
                        .compile("(\\w+\\s\\d{1,2}-?\\d?\\d?,\\s\\d{4}),\\s(\\w+);");
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
