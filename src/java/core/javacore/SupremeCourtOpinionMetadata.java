package core.javacore;

import static java.util.Arrays.asList;

import java.io.Serializable;

/**
 * SupremeCourtOpinionMetadata Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama
 * 5.10.2014
 * 
 * This specializes the generic Metadata class to apply to Supreme Court
 * opinions.
 */
public class SupremeCourtOpinionMetadata extends Metadata implements Serializable
{

    /**
     * Constructor -- initializes every metadata field to empty string
     */
    public SupremeCourtOpinionMetadata()
    {

        this.fieldNames = asList(WordCloudConstants.META_CASE_TITLE,
                        WordCloudConstants.META_CASE_NUM,
                        WordCloudConstants.META_US_CITE,
                        WordCloudConstants.META_SC_CITE,
                        WordCloudConstants.META_LAWYERS_ED,
                        WordCloudConstants.META_LEXIS_CITE,
                        WordCloudConstants.META_FULL_CITE,
                        WordCloudConstants.META_CASE_DATES,
                        WordCloudConstants.META_DISPOSITION,
                        WordCloudConstants.META_OPIN_AUTHOR,
                        WordCloudConstants.META_OPIN_TYPE);

        for (String fieldName : this.fieldNames)
        {
            this.fields.put(fieldName, "");
        }
    }

    public String toString()
    {

        String returnString = "";
        for (String fieldName : this.fieldNames)
        {
            returnString += fieldName + " : " + this.fields.get(fieldName)
                            + "\n";
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
        for (String fieldName : this.fieldNames)
        {
            printString += fieldName + "\n";
        }
        System.out.println(printString);
    }
}
