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
        opinion_list = self.convert_opinions()
        # now we sort them
        subsets = self.sort_opinions(opinion_list)
        # perform the analysis
        subset_lists = self.run_analysis(subsets)
        # and generate the word cloud
        self.generate_clouds(subset_lists)
                
        
    def convert_opinions(self):
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
        # /test output
        return opinion_list
    
    
    def sort_opinions(self, opinion_list):
        '''
        Modify the lines between ### for your specific situation.
        '''
        print "sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
        ###
        sort_field = "opinion_type"
        concur_subset = sorter.create_subset(sort_field, ["concur"])
        dissent_subset = sorter.create_subset(sort_field, ["dissent"])
        subsets = [concur_subset, dissent_subset]
        ###
        print "the set contains {0} subsets...".format(len(subsets))
        return subsets
    
    
    def run_analysis(self, subsets):
        print "running analysis..."
        analysis_engine = AnalysisEngine(subsets)
        subset_lists = analysis_engine.analyze_docs()
        return subset_lists
    
    
    def generate_clouds(self, subset_lists):
        '''
        This method will be modified for your specific situation.
        NOTE that subset_lists is a list of (output_filename, weighted_list) pairs.
        '''
        concur_file = subset_lists[0][0] + "_scalia_concurs.jpg"
        concur_terms = subset_lists[0][1]
        dissent_file = subset_lists[1][0] + "_scalia_dissents.jpg"
        dissent_terms = subset_lists[1][1]
        # test output
        print "CONCUR TERMS: {0}".format(concur_terms)
        print "CONCUR OUTPUT FILE: {0}".format(concur_file)
        print "DISSENT TERMS: {0}".format(dissent_terms)
        print "DISSENT OUTPUT FILE: {0}".format(dissent_file)
        # /test output
        
        print "generating a word cloud for each subset..."
        concur_cloud_gen = WordCloudGenerator(concur_terms, concur_file)
        concur_cloud_gen.generate_word_cloud()
        
        dissent_cloud_gen = WordCloudGenerator(dissent_terms, dissent_file)
        dissent_cloud_gen.generate_word_cloud()
        return
    

word_cloud_app = WordCloudMain()
word_cloud_app.main()  