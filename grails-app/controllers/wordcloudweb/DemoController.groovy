package wordcloudweb

import core.javacore.*;

class DemoController 
{

    def index() 
    { 
        Demo demo = new Demo();
        
        //render demo.runDemo();
        SupremeCourtOpinion opinion = demo.runDemo();
        [opinion:opinion]
    }
}
