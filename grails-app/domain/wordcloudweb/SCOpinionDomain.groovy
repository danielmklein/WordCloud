package wordcloudweb

//import core.javacore.Metadata;
//import core.javacore.Document;

class SCOpinionDomain
{

    private Map docMetadata;
    protected String docText;
    private String outputFilename;
    //private int wordCount;


    static mapping = {
        docText column: "docText", sqlType: "text"
        docMetadata column: "docMetadata"
        outputFilename column: "outputFilename", sqlType: "varchar(255)"
    }

    static constraints = {
    }

    public SCOpinionDomain(Map docMetadata, String docText, String outputFilename)
    {

        this.docMetadata = docMetadata;
        this.docText = docText;
        this.outputFilename = outputFilename;
        //this.wordCount = countWords(docText);
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

    public Map getMetadata()
    {

        return this.docMetadata;
    }

    public void setOutputFilename(String filename)
    {

        this.outputFilename = filename;
    }

    public void setText(String text)
    {

        this.docText = text;
    }

    public void setMetadata(Map meta)
    {

        this.docMetadata = meta;
    }
}
