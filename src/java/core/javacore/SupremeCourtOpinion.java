package core.javacore;

import java.io.Serializable;

/**
 * SupremeCourtOpinion Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama 8.27.14
 * 
 * This specializes the generic Document class to apply to Supreme Court
 * opinions.
 */
public class SupremeCourtOpinion extends Document implements Serializable
{

    /**
     * @param docMetadata
     * @param docText
     * @param outputFilename
     */
    public SupremeCourtOpinion(Metadata docMetadata, String docText,
                    String outputFilename)
    {

        super(docMetadata, docText, outputFilename);
    }
    
    @Override
    public String toString()
    {
        String caseTitle = this.getMetadata().getField(WordCloudConstants.META_CASE_TITLE);
        String caseNum = this.getMetadata().getField(WordCloudConstants.META_CASE_NUM);
        String usCite = this.getMetadata().getField(WordCloudConstants.META_US_CITE);
        String scCite = this.getMetadata().getField(WordCloudConstants.META_SC_CITE);
        String lawyersEd = this.getMetadata().getField(WordCloudConstants.META_LAWYERS_ED);
        String lexisCite = this.getMetadata().getField(WordCloudConstants.META_LEXIS_CITE);
        String fullCite = this.getMetadata().getField(WordCloudConstants.META_FULL_CITE);
        String caseDates = this.getMetadata().getField(WordCloudConstants.META_CASE_DATES);
        String caseDisposition = this.getMetadata().getField(WordCloudConstants.META_DISPOSITION);
        String opinAuthor = this.getMetadata().getField(WordCloudConstants.META_OPIN_AUTHOR);
        String opinType = this.getMetadata().getField(WordCloudConstants.META_OPIN_TYPE);

        String retString = "";
        
        retString = "CASE TITLE: " + caseTitle 
                    + "\nCASE NUMBER: " + caseNum
                    + "\nCASE DATES: " + caseDates
                    + "\nUS CITATION: " + usCite
                    + "\nSUPREME COURT CITATION: " + scCite
                    + "\nLAWYERS ED CITATION: " + lawyersEd
                    + "\nLEXIS CITATION: " + lexisCite
                    + "\nFULL CITATION: " + fullCite
                    + "\nOPINION AUTHOR: " + opinAuthor
                    + "\nOPINION TYPE: " + opinType
                    + "\n\nOPINION TEXT:\n\n"
                    + this.docText;
        
        return retString;
    }

}
