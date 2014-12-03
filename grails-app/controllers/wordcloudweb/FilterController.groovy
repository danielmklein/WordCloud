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
        def newFilter = new Filter();
        newFilter.setName(params.name);
        newFilter.setSortField(params.sortField);
        newFilter.setAllowedValues(params.allowedValues);
        // TODO: perform error checking on allowedValues list?
        newFilter.setAllowedValuesList(this.parseAllowedVals(params.allowedValues));
        // TODO: ALL OF THE ERROR CHECKING

        session.subsets.add(newFilter);

        System.out.println(newFilter.name);
        System.out.println(newFilter.sortField);
        System.out.println("allowed vals in new filter are: ");
        for (val in newFilter.getAllowedValuesList())
        {
            System.out.println(val);
        }
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

    private def parseAllowedVals(String allowedVals)
    {
        return Arrays.asList(allowedVals.split("\\s*,\\s*"));
    }

    def addSubsetToCorpus()
    {
        def nameOfSubset = params.subset; // TODO this var name sucks
        System.out.println("Name of subset: " + nameOfSubset);
        
        for (filter in session.subsets)
        {
            if (filter.name.equals(nameOfSubset))
            {
                def alreadyInCorpus = false;
                for (corpusFilter in session.corpusSubsets)
                {
                    if (corpusFilter.name.equals(nameOfSubset))
                    {
                        System.out.println("Tried to add " + nameOfSubset 
                                           + " to corpus, but it's already in there!");
                        alreadyInCorpus = true;
                        break;
                    }
                }

                if (!alreadyInCorpus)
                {
                    System.out.println("Adding subset " + nameOfSubset + " to corpus.");
                    session.corpusSubsets.add(filter);
                    break;
                }
            }
        }

        def emptyFilter = new Filter(name:'', allowedValues:'', 
                                    sortField:'' );
        render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }

    def removeSubsetFromCorpus()
    {
        def nameOfSubset = params.corpusSubset; // TODO this var name sucks
        System.out.println("We're gonna remove subset "  + nameOfSubset
                            + " from the corpus!");

        def idxToRemove = -1;

        for (int i = 0; i < session.corpusSubsets.size(); ++i)
        {
            def curSubset = session.corpusSubsets[i];
            if (curSubset.name.equals(nameOfSubset))
            {
                idxToRemove = i;
                break;
            }
        }

        if (idxToRemove != -1)
        {
            session.corpusSubsets.remove(idxToRemove);
        } else
        {
            System.out.println("Didn't find subset " + nameOfSubset + " in the corpus!");
        } 


        def emptyFilter = new Filter(name:'', allowedValues:'', 
                                    sortField:'' );
        render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }

    def addAllSubsetsToCorpus()
    {
        System.out.println("We're gonna add all subsets to the corpus.");

        session.corpusSubsets.clear();
        for (filter in session.subsets)
        {
            session.corpusSubsets.add(filter);
        }

        def emptyFilter = new Filter(name:'', allowedValues:'', 
                                    sortField:'' );
        render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }

    def removeAllSubsetsFromCorpus()
    {
        System.out.println("We're gonna remove all subsets from the corpus.");

        session.corpusSubsets.clear();

        def emptyFilter = new Filter(name:'', allowedValues:'', 
                                    sortField:'' );
        render(view: "filters", action:"filters", model: [filter:emptyFilter, subsets:session.subsets, 
                                                            corpusSubsets:session.corpusSubsets]);
    }

    def createWordCloud()
    {
        def nameOfSubset = params.subset;
        def nameOfCorpusSubset = params.corpusSubset;

        System.out.println("name of subset to use for word cloud: " + nameOfSubset);
        System.out.println("name of corpus subset to use for word cloud: " + nameOfCorpusSubset);

        // get subset filter and corpus filter objects to pass
        def subsetFilter;
        for (filter in session.subsets)
        {
            if (filter.name.equals(nameOfSubset))
            {
                subsetFilter = filter;
                break;
            }
        }

        System.out.println("subset filter has: ");
        System.out.println("name: " + subsetFilter.getName());
        System.out.println("sort field: " + subsetFilter.getSortField());

        def corpusFilter;
        for (filter in session.corpusSubsets)
        {
            if (filter.name.equals(nameOfCorpusSubset))
            {
                corpusFilter = filter;
                break;
            }
        }


        /*chain(controller: "Demo", 
                action: "createCloud", 
                model: [subsetFilter: subsetFilter, corpusFilter: corpusFilter]);
        */
        flash.subsetFilter = subsetFilter;
        flash.corpusFilter = corpusFilter;
        redirect(controller: "Demo",
                action: "createCloud");
    }
}
