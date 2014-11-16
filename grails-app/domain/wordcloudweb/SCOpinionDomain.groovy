package wordcloudweb

class SCOpinionDomain
{

    //Map docMetadata;
    String docText;
    String outputFilename;
    //private int wordCount;

    // TODO: this is hacky, but so what?
    String caseTitle;
    String caseNumber;
    String usCitation;
    String scCitation;
    String lawyersEd;
    String lexisCitation;
    String fullCitation;
    String caseDates;
    String disposition;
    String opinionAuthor;
    String opinionType;

    static mapping = {
        version false
        table 'opinions'
        docText column: 'doc_text', sqlType: 'text'
        outputFilename column: 'output_filename'
        caseTitle sqlType: 'text'
        caseNumber sqlType: 'text'
        usCitation sqlType: 'text'
        scCitation sqlType: 'text'
        lawyersEd sqlType: 'text'
        lexisCitation sqlType: 'text'
        fullCitation sqlType: 'text'
        caseDates sqlType: 'text'
        disposition sqlType: 'text'
        opinionAuthor sqlType: 'text'
        opinionType sqlType: 'text'
    }

    static constraints = {
    }

    public SCOpinionDomain(String docText, String outputFilename)
    {

        this.docText = docText;
        this.outputFilename = outputFilename;
    }

}
