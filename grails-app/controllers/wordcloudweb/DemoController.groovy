package wordcloudweb

import core.javacore.*;

class DemoController 
{

    def index() 
    { 
        Demo demo = new Demo();
        
        //render demo.runDemo();
        //Map<String, Double> terms = demo.runDemo();
        List<AnalysisEngine.TermMetrics> terms = demo.runDemo();
        [terms:terms]
    }
}
