import os, os.path
import re
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from Document import Document
from DocumentConverter import DocumentConverter
from DocumentSorter import DocumentSorter
from AnalysisEngine import AnalysisEngine
from WordCloudGenerator import WordCloudGenerator

# directory containing parsed opinions
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
#OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"
'''
"War on Terror" cases
 
Rasul v. Bush and Al Odah v. United States 542 U.S. 466 (2004)
 
Hamdi v. Rumsfeld, 542 U.S. 507 (2004)
 
Rumsfeld v. Padilla, 542 U.S. 426 (2004)
 
Hamdan v. Rumsfeld, 548 U.S. 557 (2006)
 
Boumediene v. Bush, 553 U.S. 723 (2008)
 
Munaf v. Geren / Geren v. Omar, 553 U.S. 674 (2008)

Holder v. Humanitarian Law Project, 130 S. Ct. 2705 (2010)
'''
ACCEPTED_CITES = (["542 U.S. 466","542 U.S. 507","542 U.S. 426","548 U.S. 557","553 U.S. 723","553 U.S. 674"])

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
        num_relevant_terms = 1000
        print "Here's the main method..."
        '''
        Take all the opinions we want to convert, convert them,
        sort them into subsets, then analyze subsets and create 
        word cloud for each subset.
        '''
        # first we convert the opinion files into Document objects
        opinion_list = self.convert_opinions()
        # now we sort them
        subsets = self.sort_opinions(opinion_list)
        
        # should I del opinion_list now??
        
        # perform the analysis
        subset_lists = self.run_analysis(subsets, num_relevant_terms)
        # and generate the word cloud
        self.generate_clouds(subset_lists)
                
        
    def convert_opinions(self):
        '''
        Convert each given opinion into a Document object.
        '''
        opinion_list = []
        txtfile_regex = re.compile(r"\.txt$")
        for opinion_file in os.listdir(OPINION_PATH):
            input_path = os.path.join(OPINION_PATH, opinion_file)
            is_text_file = re.search(txtfile_regex, input_path)
            if not is_text_file:
                print ("{0} is not a text file, so we can't convert it!"
                       .format(input_path))
                continue
            pickle_path = os.path.join(OPINION_PATH, "output", 
                                       opinion_file + ".Document")
            converter = DocumentConverter(input_path, pickle_path)
            print "Converting file {0}...".format(opinion_file)
            opinion_list.append(converter.convert_file())
            del converter
        # test output
        #print opinion_list
        print "There are {0} opinions in the list...".format(len(opinion_list))
        # /test output
        return opinion_list
    
    
    def sort_opinions(self, opinion_list):
        '''
        Sort the opinions into subset(s).
        
        Modify the lines between ### for your specific situation.
        '''
        print "Sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
        ###
        sort_field = "case_us_cite"
        terror_cases = sorter.create_subset(sort_field, ACCEPTED_CITES)
        
        sort_field = "opinion_type"
        sorter = DocumentSorter(terror_cases)
        terror_majs = sorter.create_subset(sort_field, 
                                                  ["majority"])
        terror_concurs = sorter.create_subset(sort_field, 
                                                  ["concur"])        
        terror_dissents = sorter.create_subset(sort_field, 
                                                  ["dissent"])        
        subsets = [terror_majs, terror_concurs, terror_dissents]
        ###
        print "The set contains {0} subset(s)...".format(len(subsets))
        return subsets
    
    
    def run_analysis(self, subsets, num_terms):
        print "Running analysis..."
        analysis_engine = AnalysisEngine(subsets)
        subset_lists = analysis_engine.analyze_docs(num_terms)
        return subset_lists
    
    
    def generate_clouds(self, subset_lists):
        '''
        This method will be modified for your specific situation.
        NOTE that subset_lists is a list of (output_filename, weighted_list) 
        pairs.
        
        i.e. subset_lists = [(output_filename, weighted_list), 
                            (filename, list), ... , (filename, list)]
        '''
        terror_maj_file = subset_lists[0][0] + "_terror_majority.jpg"
        terror_maj_terms = subset_lists[0][1]
            
        terror_concur_file = subset_lists[1][0] + "_terror_concurs.jpg"
        terror_concur_terms = subset_lists[1][1]
        
        terror_dissent_file = subset_lists[2][0] + "_terror_dissents.jpg"
        terror_dissent_terms = subset_lists[2][1]
        
        # test output
        print "TERROR MAJORITY TERMS: {0}".format(terror_maj_terms)
        print "TERROR MAJORITY OUTPUT FILE: {0}".format(terror_maj_file)
        
        print "TERROR CONCUR TERMS: {0}".format(terror_concur_terms)
        print "TERROR CONCUR OUTPUT FILE: {0}".format(terror_concur_file)
        
        print "TERROR DISSENT TERMS: {0}".format(terror_dissent_terms)
        print "TERROR DISSENT OUTPUT FILE: {0}".format(terror_dissent_file)
        # /test output
        
        print "Generating a word cloud for each subset..."
        terror_maj_cloud = WordCloudGenerator(terror_maj_terms, terror_maj_file)
        terror_maj_cloud.generate_word_cloud()
        print "Word cloud generated and saved to {0}".format(terror_maj_file)
        
        terror_concur_cloud = WordCloudGenerator(terror_concur_terms, terror_concur_file)
        terror_concur_cloud.generate_word_cloud()
        print "Word cloud generated and saved to {0}".format(terror_concur_file)
        
        terror_dissent_cloud = WordCloudGenerator(terror_dissent_terms, terror_dissent_file)
        terror_dissent_cloud.generate_word_cloud()
        print "Word cloud generated and saved to {0}".format(terror_dissent_file)
        
        return
    

word_cloud_app = WordCloudMain()
word_cloud_app.main()  