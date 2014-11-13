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

        List<Document> allOpinions = new ArrayList<Document>();

        for (SCOpinionDomain opin : allDomainOpinions)
        {
        	allOpinions.add(new SupremeCourtOpinion(opin.getMetadata(),
        											opin.getText(),
        											opin.getOutputFilename()));
        }
        
        //render demo.runDemo();
        //Map<String, Double> terms = demo.runDemo();
        //List<AnalysisEngine.TermMetrics> terms = demo.runDemo();
        List<AnalysisEngine.TermMetrics> terms = demo.runDemo(allOpinions);
        [terms:terms]
    }
}
