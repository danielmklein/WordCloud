package core.javacore;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Daniel Klein
 * Computer-Based Honors Program
 * The University of Alabama
 * 9.24.2014
 *
 * This program is responsible for taking plain-text opinion files,
 * converting the opinions into SupremeCourtOpinion objects, and 
 * serializing those objects to file.
 */
public class OpinionSerializer
{

    private static final String OPINION_PATH = "C:\\Users\\Daniel\\Dropbox\\Class_Files\\CBH_301\\Word_Cloud\\supreme_court_opinions\\test_output\\opinions";
    private static final String SERIALIZE_PATH = "C:\\Users\\Daniel\\Dropbox\\Class_Files\\CBH_301\\Word_Cloud\\supreme_court_opinions\\test_output\\serialized";
    
    public static void main(String[] args) throws IOException
    {
        packOpinions();

    }
    
    /**
     *  Convert every opinion file residing in OPINION_PATH into a Document
     *  object and pickle it to file in SERIALIZE_PATH.
     */
    private static void packOpinions() throws IOException
    {
        
        System.out.println("Converting files in " + OPINION_PATH + " to Document objects");
        System.out.println("and serializing them to files in " + SERIALIZE_PATH + "...");
        
        File opinionDir = new File(OPINION_PATH);
        List<File> opinionFiles = Arrays.asList(opinionDir.listFiles());
        
        long numOpinions = opinionFiles.size();
        long numConverted = 0;
        long numFailed = 0;
        Pattern txtFileRegex = Pattern.compile("\\.txt$");
        
        System.out.println(numOpinions + " opinion files found.");
        
        String inputPath;
        String serializePath;
        boolean isTextFile;
        SupremeCourtOpinionFileConverter converter;
        
        for (File opinionFile : opinionFiles)
        {
            inputPath = opinionFile.getCanonicalPath();
            // if a file doesn't have a .txt extension, we ignore it 
            isTextFile = txtFileRegex.matcher(inputPath).find();
            if (!isTextFile)
            {
                System.out.println(inputPath + " is not a text file, so we can't convert it!");
                numFailed++;
                continue;
            }
            
            // serializePath = SERIALIZE_PATH + filename + ".Document"
            serializePath = (new File(SERIALIZE_PATH, opinionFile.getName() + ".Document")).getCanonicalPath();
            
            converter = new SupremeCourtOpinionFileConverter(inputPath, serializePath);
            converter.convertFile().serialize();
        }
    }

}
