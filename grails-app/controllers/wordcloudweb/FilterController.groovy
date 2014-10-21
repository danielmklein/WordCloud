package wordcloudweb

class FilterController {

	//List subsets; // these two are lists of Filter objects
	//List corpusSubsets;

    def index() 
    {
        session.subsets = [];
        session.corpusSubsets = [];

    	// all filter fields will be blank in form
    	def filter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );

        render(view:"filters", action:"filters", model: [filter:filter, subsets:session.subsets]);
    }

    def filters()
    {
        def curFilter = params.filter;

        [filter:curFilter, subsets:session.subsets];
    }

    def createSubset()
    {
        def newFilter = new Filter(params);
        session.subsets.add(newFilter);

        System.out.println(newFilter.name);
        System.out.println(newFilter.sortField);
        System.out.println(session.subsets);

        // test print statements
        for (filter in session.subsets)
        {
            System.out.println(filter.name);
        }
        System.out.println(session.subsets.size());

    	def emptyFilter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );
    	render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets]);
    }
}
