package wordcloudweb

import java.util.List;
import java.util.ArrayList;
import grails.gorm.*;
import core.javacore.*;

class DemoController
{
    int ALL_RECORDS = -1;

    def index() // this is a hardcoded demo we used to demonstrate it worked.
    {
        System.out.println("we found " + SCOpinionDomain.count() + " domain opinions.");

        // construct database query to get the subset/corpus we want
        def subsetOpins = SCOpinionDomain.findAllByFullCitationLike("%111%");
        System.out.println("Found " + subsetOpins.size() + " opinions by Frankfurter");
        System.out.println("Found " + SCOpinionDomain.count() + " opinions in entire corpus.");

        // then call analyzeDocs directly with subset and corpus
        // maybe write version of analyzeDocs that takes lists of SCOPinionDomain objects??
        AnalysisEngine engine = new AnalysisEngine();
        engine.setDomainCorpus(subsetOpins);
        engine.setDomainSubset(subsetOpins);

        int numRelevantTerms = WordCloudConstants.NUM_TERMS_IN_CLOUD;
        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(numRelevantTerms);

        [terms:terms]
    }

    def createCloud()
    {
        // turn subset filter into db query, create subset
        def subsetFilter = session.subsetFilter;

        System.out.println("in demo controller");
        System.out.println("subset filter has: ");
        System.out.println("name: " + subsetFilter.getName());

        def subsetFilterList = [];
        subsetFilterList.add(subsetFilter);
        def subset = this.buildDatabaseQuery(subsetFilterList, ALL_RECORDS, 0);
        System.out.println("subset size is: " + subset.size());

        // turn corpus filter into db query, create corpus
        def corpusFilters = session.corpusFilters;
        System.out.println("num of filters in corpus: " + corpusFilters.size());
        for (filter in corpusFilters)
        {
            System.out.println("corpus filter name: " + filter.getName());
        }

        def corpus = this.buildDatabaseQuery(corpusFilters, ALL_RECORDS, 0);
        System.out.println("corpus size is: " + corpus.size());

        // pass subset and corpus to analysis engine to get terms
        AnalysisEngine engine = new AnalysisEngine();
        engine.setDomainCorpus(corpus);
        engine.setDomainSubset(subset);

        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(WordCloudConstants.NUM_TERMS_IN_CLOUD);

        // pass terms to view
        [terms:terms]
    }

    def populateTermContexts()
    {
        def termForInfo = params.term;
        System.out.println("populating context for term: " + termForInfo);
        def subsetFilter = session.subsetFilter;

        int numRecs = 10;
        int offset = 0;

        def subsetFilterList = [];
        subsetFilterList.add(subsetFilter);

        def subset = this.buildDatabaseQuery(subsetFilterList, numRecs, offset);

        // here build the stuff we want to stick in the div
        // iterate through opinions, looking for instances of term.
        // for each instance,
        // get 5? or so words before and 5 or so words after and save that string
        // to build string, let's say we print case title, then all the instances in context of term from that opinion
        // and repeat

        def htmlString = "";

        for (opinion in subset)
        {
            def curDocTextList = Arrays.asList(opinion.getText().split("\\s+"));

            htmlString += "<h3>From '" + opinion.caseTitle + "'...</h3>\n";

            for (int i = 0; i < curDocTextList.size(); i++)
            {
                def curTerm = curDocTextList.get(i);
                System.out.println("cur term is: " + curTerm);

                def spacePadCurTerm = " " + curTerm; // wow this is hacky... we can do this with regex i think
                def spacePadInfoTerm = " " + termForInfo;

                if (spacePadCurTerm.contains(spacePadInfoTerm.toLowerCase()))
                {
                    System.out.println("opinion term " + curTerm + " contains term we want");
                    def startIdx = (i - 5 >= 0) ? (i - 5) : 0;
                    def endIdx = (i + 5 < curDocTextList.size()) ? (i + 5) : (curDocTextList.size() - 1);

                    def contextString = "<p>...'";
                    for (int j = startIdx; j <= endIdx; j++)
                    {
                        if (i == j)
                        {
                            contextString += "<strong>" + curDocTextList.get(j) + "</strong> ";
                        } else
                        {
                            contextString += curDocTextList.get(j) + " ";
                        }

                    }

                    htmlString += contextString + "...</p>\n"
                }
            }
        }

        System.out.println("htmlString is " + htmlString);

        render htmlString;
    }

    private def buildDatabaseQuery(List<Filter> filters, int numRecs, int recOffset)
    {
        // TODO: figure out how to do this without building string??

        def query = "from SCOpinionDomain as o where ";
        def firstTerm = true;
        def curSortField;
        def curAllowedVals;
        def curFilter;

        for (int i = 0; i < filters.size(); i++)
        {
            curFilter = filters.get(i);
            query += "(";

            for (int j = 0; j < curFilter.getSortFields().size(); j++)
            {
                curSortField = curFilter.getSortFields().get(j);
                curAllowedVals = curFilter.getAllowedValueLists().get(j);
                query += "(";

                for (value in curAllowedVals)
                {
                    if (firstTerm)
                    {
                        query += "upper(o." + curSortField + ") like upper('%" + value + "%') ";
                        firstTerm = false;
                    } else
                    {
                        query += "or upper(o." + curSortField + ") like upper('%" + value + "%') ";
                    }
                }

                query += ")";

                if (j != curFilter.getSortFields().size() - 1)
                {
                    query += " and ";
                }
                firstTerm = true;
            }

            query += ")";

            if (i != filters.size() - 1)
            {
                query += " or ";
            }
        }

        /*
        select * from table where
        ( here's a filter
        (sortfield like blah or sortfield like blah...) (filter level)
        and (sortfield like blah or sortfield like blah...) (another filter level)
        )
        or
        (here's another filter

        )
        */

        System.out.println("Executing query: ");
        System.out.println(query);
        System.out.println("with max num records " + numRecs);
        System.out.println("and offset of " + recOffset);

        if (numRecs == ALL_RECORDS)
        {
            return SCOpinionDomain.findAll(query, [offset: recOffset]);
        } else
        {
            return SCOpinionDomain.findAll(query, [max: numRecs, offset: recOffset]);
        }
    }
}
