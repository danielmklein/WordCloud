package wordcloudweb

import core.javacore.Metadata;
//import core.javacore.Document;

class SCOpinionDomain
{

    static constraints = {
    }

    private Metadata docMetadata;
    protected String docText;
    private String outputFilename;
    private int wordCount;

    public SCOpinionDomain(Metadata docMetadata, String docText, String outputFilename)
    {

        this.docMetadata = docMetadata;
        this.docText = docText;
        this.outputFilename = outputFilename;
        this.wordCount = countWords(docText);
    }

    /*public SCOpinionDomain(Metadata docMetadata, String docText,
                    String outputFilename)
    {

        super(docMetadata, docText, outputFilename);
    }*/

    public int countWords(String text)
    {

        return text.split(" ").length;
    }

    public String getOutputFilename()
    {

        return this.outputFilename;
    }

    public String getText()
    {

        return this.docText;
    }

    public Metadata getMetadata()
    {

        return this.docMetadata;
    }
}
