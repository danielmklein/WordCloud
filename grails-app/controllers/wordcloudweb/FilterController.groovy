package wordcloudweb

class FilterController {

	List subsets; // these two are lists of Filter objects
	List corpusSubset;

    def index() 
    {
    	def subsets = [];
    	def corpusSubsets = [];

    	// all filter fields will be blank in form
    	def filter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );

        render(view:"filters", action:"filters", model: [filter:filter, subsets:subsets]);
    }

    def filters()
    {
        def subsets = params.subsets;
        def curFilter = params.filter;

        [filter:curFilter, subsets:subsets];
    }

    def createSubset()
    {
        def subsets = params.subsets;
        def newFilter = new Filter(params);
    	subsets = subsets + newFilter.name;
        System.out.println(newFilter.name);
        System.out.println(newFilter.sortField);
        System.out.println(subsets);

    	def emptyFilter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );
    	render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:subsets]);
    }
}
