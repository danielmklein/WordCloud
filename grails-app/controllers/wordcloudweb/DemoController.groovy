package wordcloudweb

import java.util.List;
import java.util.ArrayList;

import core.javacore.*;

class DemoController 
{

    def index() 
    { 
        Demo demo = new Demo();
        List<SCOpinionDomain> allDomainOpinions = SCOpinionDomain.getAll();
        System.out.println("we found " + allDomainOpinions.size() + " domain opinions.");
        
        List<Document> allOpinions = new ArrayList<Document>();
        SupremeCourtOpinionMetadata meta;

        for (SCOpinionDomain opin : allDomainOpinions)
        {
            meta = new SupremeCourtOpinionMetadata();
            meta.setField(WordCloudConstants.META_CASE_TITLE, opin.caseTitle);
            meta.setField(WordCloudConstants.META_CASE_NUM, opin.caseNumber);
            meta.setField(WordCloudConstants.META_US_CITE, opin.usCitation);
            meta.setField(WordCloudConstants.META_SC_CITE, opin.scCitation);
            meta.setField(WordCloudConstants.META_LAWYERS_ED, opin.lawyersEd);
            meta.setField(WordCloudConstants.META_LEXIS_CITE, opin.lexisCitation);
            meta.setField(WordCloudConstants.META_FULL_CITE, opin.fullCitation);
            meta.setField(WordCloudConstants.META_CASE_DATES, opin.caseDates);
            meta.setField(WordCloudConstants.META_DISPOSITION, opin.disposition);
            meta.setField(WordCloudConstants.META_OPIN_AUTHOR, opin.opinionAuthor);
            meta.setField(WordCloudConstants.META_OPIN_TYPE, opin.opinionType);

            SupremeCourtOpinion newOpin = new SupremeCourtOpinion(meta, 
                                                                opin.docText,
                                                                opin.outputFilename);
        	allOpinions.add(newOpin);
        }
        
        //render demo.runDemo();
        //Map<String, Double> terms = demo.runDemo();
        //List<AnalysisEngine.TermMetrics> terms = demo.runDemo();
        List<AnalysisEngine.TermMetrics> terms = demo.runDemo(allOpinions);
        [terms:terms]
    }
}
