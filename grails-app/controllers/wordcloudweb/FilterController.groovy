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

        render(view:"filters", action:"filters", model: [filter:filter, subsets:session.subsets, 
                                                        corpusSubsets:session.corpusSubsets]);
    }

    def filters()
    {
        def curFilter = params.filter;

        [filter:curFilter, subsets:session.subsets, corpusSubsets:session.corpusSubsets];
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
        System.out.println("size of subsets:" + session.subsets.size());
        System.out.println("size of corpus subsets:" + session.corpusSubsets.size());

    	def emptyFilter = new Filter(name:'', allowedValues:'', 
    								sortField:'' );
    	render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }

    def addSubsetToCorpus()
    {
        def nameOfSubset = params.subset;
        System.out.println("Name of subset: " + nameOfSubset);
        //session.corpusSubsets.add(subsetToAdd);
        def emptyFilter = new Filter(name:'', allowedValues:'', 
                                    sortField:'' );
        render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }
}
