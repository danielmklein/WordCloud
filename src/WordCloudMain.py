import os, os.path
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from Document import Document
from DocumentConverter import DocumentConverter
from DocumentSorter import DocumentSorter
from AnalysisEngine import AnalysisEngine
from WordCloudGenerator import WordCloudGenerator

OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"

class WordCloudMain():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    This class represents the Word Cloud application itself -- it integrates
    all of the components into a functional application.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
        
    def main(self):
        print "Here's the main method..."
        '''
        take all the opinions we want to convert,
        convert them,
        sort them into subsets,
        then analyze subsets and create word cloud for each
        '''
        # first we convert the opinion files into Document objects
        opinion_list = []
        for opinion_file in os.listdir(OPINION_PATH):
            input_path = os.path.join(OPINION_PATH, opinion_file)
            pickle_path = input_path + ".Document"
            converter = DocumentConverter(input_path, pickle_path)
            print "converting file {0}...".format(opinion_file)
            opinion_list.append(converter.convert_file())
            del converter
        # test output
        print opinion_list
        print "there are {0} opinions in the list...".format(len(opinion_list))
        '''
        for doc in opinion_list:
            print "DOC AUTHOR: {0}".format(doc.doc_metadata.opinion_author)
            print "US CITE: {0}".format(doc.doc_metadata.case_us_cite)
        '''
        # /test output
        
        # now we sort them
        print "sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
        sort_field = "opinion_type"
        concur_subset = sorter.create_subset(sort_field, ["concur"])
        dissent_subset = sorter.create_subset(sort_field, ["dissent"])
        subsets = [concur_subset, dissent_subset]
        print "the set contains {0} subsets...".format(len(subsets))
        # test output
        #print subsets
        
        #for subset in subsets:
            #print "SUBSET {0}".format(subsets.index(subset))
            #for doc in subset:
                #print "DOC AUTHOR: {0}".format(doc.doc_metadata.opinion_author)
        # /test output
        print "running analysis..."
        analysis_engine = AnalysisEngine(subsets)
        subset_lists = analysis_engine.analyze_docs()
        ###
        # right now I'm just generating a word cloud for the first
        # subset in the set.
        concur_terms = subset_lists[0][1]
        concur_file = subset_lists[0][0] + "_scalia_concurs.jpg"
        dissent_terms = subset_lists[1][1]
        dissent_file = subset_lists[1][0] + "_scalia_dissents.jpg"
        # test output
        print "CONCUR TERMS: {0}".format(concur_terms)
        print "CONCUR OUTPUT FILE: {0}".format(concur_file)
        print "DISSENT TERMS: {0}".format(dissent_terms)
        print "DISSENT OUTPUT FILE: {0}".format(dissent_file)
        # /test output
        print "generating a word cloud for each subset..."
        cloud_generator = WordCloudGenerator(concur_terms, concur_file)
        cloud_generator.generate_word_cloud()
        
        cloud_generator = WordCloudGenerator(dissent_terms, dissent_file)
        cloud_generator.generate_word_cloud()
        
        


word_cloud_app = WordCloudMain()
word_cloud_app.main()  