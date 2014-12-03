package wordcloudweb

import java.util.List;
import java.util.ArrayList;

import grails.gorm.*;
import org.hibernate.criterion.Restrictions;

import core.javacore.*;

class DemoController 
{

    def index() 
    { 
        //Demo demo = new Demo();
        //List<SCOpinionDomain> allDomainOpinions = SCOpinionDomain.getAll();
        System.out.println("we found " + SCOpinionDomain.count() + " domain opinions.");
        
        //List<Document> allOpinions = new ArrayList<Document>();
        //SupremeCourtOpinionMetadata meta;
        //SCOpinionDomain curDomOpin;

        // TODO: construct database query to get the subset/corpus we want, instead of 
        // loading all opinions and then using DocumentSorter -- this takes too much memory
        def subsetOpins = SCOpinionDomain.findAllByFullCitationLike("%111%");
        System.out.println("Found " + subsetOpins.size() + " opinions by Frankfurter");

        //def allOpinions = SCOpinionDomain.list();
        System.out.println("Found " + SCOpinionDomain.count() + " opinions in entire corpus.");

        // then call analyzeDocs directly with subset and corpus
        // maybe write version of analyzeDocs that takes lists of SCOPinionDomain objects??
        AnalysisEngine engine = new AnalysisEngine();
        //engine.setDomainCorpus(SCOpinionDomain.list());
        engine.setDomainCorpus(subsetOpins);
        engine.setDomainSubset(subsetOpins);
    
        int numRelevantTerms = WordCloudConstants.NUM_TERMS_IN_CLOUD;
        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(numRelevantTerms);

        //for (SCOpinionDomain opin : allDomainOpinions)
        /*for (int i = 1; i <= SCOpinionDomain.count(); i++)
        {
            curDomOpin = SCOpinionDomain.get(i);

            //meta = new SupremeCourtOpinionMetadata();
            meta.setField(WordCloudConstants.META_CASE_TITLE, curDomOpin.caseTitle);
            meta.setField(WordCloudConstants.META_CASE_NUM, curDomOpin.caseNumber);
            meta.setField(WordCloudConstants.META_US_CITE, curDomOpin.usCitation);
            meta.setField(WordCloudConstants.META_SC_CITE, curDomOpin.scCitation);
            meta.setField(WordCloudConstants.META_LAWYERS_ED, curDomOpin.lawyersEd);
            meta.setField(WordCloudConstants.META_LEXIS_CITE, curDomOpin.lexisCitation);
            meta.setField(WordCloudConstants.META_FULL_CITE, curDomOpin.fullCitation);
            meta.setField(WordCloudConstants.META_CASE_DATES, curDomOpin.caseDates);
            meta.setField(WordCloudConstants.META_DISPOSITION, curDomOpin.disposition);
            meta.setField(WordCloudConstants.META_OPIN_AUTHOR, curDomOpin.opinionAuthor);
            meta.setField(WordCloudConstants.META_OPIN_TYPE, curDomOpin.opinionType);

            SupremeCourtOpinion newOpin = new SupremeCourtOpinion(meta, 
                                                                curDomOpin.docText,
                                                                curDomOpin.outputFilename);
        	allOpinions.add(newOpin);
        }*/
        
        //render demo.runDemo();
        //Map<String, Double> terms = demo.runDemo();
        //List<AnalysisEngine.TermMetrics> terms = demo.runDemo();
        //List<AnalysisEngine.TermMetrics> terms = demo.runDemo(allOpinions);
        [terms:terms]
    }

    def createCloud()
    {
        // turn subset filter into db query, create subset
        //def subsetFilter = params.subsetFilter;
        def subsetFilter = flash.subsetFilter;

        System.out.println("in demo controller");
        System.out.println("subset filter has: ");
        System.out.println("name: " + subsetFilter.getName());
        System.out.println("sort field: " + subsetFilter.getSortField());

        def subset = this.buildDatabaseQuery(subsetFilter);
        System.out.println("subset size is: " + subset.size());


        // turn corpus filter into db query, create corpus
        //def corpusFilter = params.corpusFilter;
        def corpusFilter = flash.corpusFilter;

        def corpus = this.buildDatabaseQuery(corpusFilter);
        System.out.println("corpus size is: " + corpus.size());

        // pass subset and corpus to analysis engine to get terms
        AnalysisEngine engine = new AnalysisEngine();
        engine.setDomainCorpus(corpus);
        engine.setDomainSubset(subset);

        List<AnalysisEngine.TermMetrics> terms = engine.analyzeDocs(WordCloudConstants.NUM_TERMS_IN_CLOUD);

        // pass terms to view
        [terms:terms]
    }

    private def buildDatabaseQuery(Filter filter)
    {
        // TODO: check sort field, build query like
        // select opinions from table where [sortField] like "%blah%" or [sortField] like "%foo%" or ....

        // TODO: figure out how to do this without building string??

        def query = "from SCOpinionDomain as o where ";
        def firstTerm = true;

        for (value in filter.getAllowedValuesList())
        {
            if (firstTerm)
            {
                query += "o." + filter.getSortField() + " like '%" + value + "%' ";
                firstTerm = false;
            } else
            {
                query += "or o." + filter.getSortField() + " like '%" + value + "%' ";
            }
        }

        System.out.println("Executing query: ");
        System.out.println(query);

        return SCOpinionDomain.findAll(query);


    }
}
