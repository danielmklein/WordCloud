package wordcloudweb

class FilterController {

	List subsets; // these two are lists of Filter objects
	List corpusSubset;

    def index() 
    {
    	def subsets = [];
    	def corpusSubsets = [];

    	// all filter fields will be blank in form
    	Filter filter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );
    	[filter:filter];
    	[subsets:subsets];
    }

    def createSubset()
    {
    	subsets << params.filter;

    	filter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );
    	[filter:filter];
    	[subsets:subsets];
    }
}
