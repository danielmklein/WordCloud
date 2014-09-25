package wordcloudweb

import core.javacore.Demo;

class DemoController 
{

    def index() 
    { 
        Demo demo = new Demo();
        
        render demo.runDemo();
    }
}
