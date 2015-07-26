package core.javacore;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
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

 /**
  * NOTE: this code is not used any more, since we save the opinions to the
  * database and access them from there, not to/from disk.
 **/
public class OpinionSerializer
{
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
        String opinionDirPath = WordCloudConstants.OPINION_DIR_PATH_DEPLOY;
        String serializeDirPath = WordCloudConstants.SERIALIZE_DIR_PATH;

        System.out.println("Converting files in " + opinionDirPath + " to Document objects");
        System.out.println("and serializing them to files in " + serializeDirPath + "...");

        File opinionDir = new File(opinionDirPath);
        List<File> opinionFiles = Arrays.asList(opinionDir.listFiles());

        long numOpinions = opinionFiles.size();
        long numConverted = 0;
        long numFailed = 0;
        Pattern txtFileRegex = Pattern.compile("\\.txt$");

        System.out.println(numOpinions + " opinion files found.");

        String inputFullPath;
        String serializeFullPath;
        boolean isTextFile;
        SupremeCourtOpinionFileConverter converter;

        for (File opinionFile : opinionFiles)
        {
            inputFullPath = opinionFile.getCanonicalPath();
            // if a file doesn't have a .txt extension, we ignore it
            isTextFile = txtFileRegex.matcher(inputFullPath).find();
            if (!isTextFile)
            {
                System.out.println(inputFullPath + " is not a text file, so we can't convert it!");
                numFailed++;
                continue;
            }

            converter = new SupremeCourtOpinionFileConverter(inputFullPath);

            try
            {
                converter.convertFile().serialize();
                numConverted++;
            } catch (Exception e)
            {
                System.out.println("Unable to convert " + opinionFile.getName()
                                + " to Document object and save it to file...");
                numFailed++;
                continue;
            }

            if (numConverted % 1000 == 0)
            {
                System.out.println(numConverted + " opinions converted.");
            }
        }

        System.out.println("Opinion conversion and serialization complete.");
        System.out.println(numConverted + " opinions converted.");
        System.out.println(numFailed + " opinions failed conversion.");
    }

}
