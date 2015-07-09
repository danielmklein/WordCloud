package wordcloudweb

class SCOpinionDomain
{
    String docText;

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
        docText column: 'doc_text', sqlType: 'longtext'
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

    public SCOpinionDomain(String docText)
    {

        this.docText = docText;
    }

    public String getText()
    {
        return this.docText;
    }

    public Map getMetadata()
    {
        return null; // TODO : maybe fix me later?
    }

}
