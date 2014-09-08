package core.javacore;

/**
 * SupremeCourtOpinion Class for Word Cloud Project (Java)
 * 
 * Daniel Klein Computer-Based Honors Program The University of Alabama 8.27.14
 * 
 * This specializes the generic Document class to apply to Supreme Court
 * opinions.
 */
public class SupremeCourtOpinion extends Document
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
        // TODO Auto-generated constructor stub
    }
    
    @Override
    public String toString()
    {
        // TODO: fix me... it's just a temporary thing.
        return this.getMetadata().getField(WordCloudConstants.META_OPIN_AUTHOR);
    }

}
