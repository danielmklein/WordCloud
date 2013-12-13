import os, os.path
import re
import cPickle as pickle
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from Document import Document
from DocumentConverter import DocumentConverter
from DocumentSorter import DocumentSorter
from AnalysisEngine import AnalysisEngine
from WordCloudGenerator import WordCloudGenerator

# directory containing parsed opinions
'''
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_pickled"
'''
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\pickled"

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
        
        
    '''
    write method to 
    '''
   
    def main(self, should_pack_opinions=False):
        num_relevant_terms = 1000
        print "Here's the main method..."
        '''
        Take all the opinions we want to convert, convert them,
        sort them into subsets, then analyze subsets and create 
        word cloud for each subset.
        '''
        if should_pack_opinions:
            '''
            run through files in OPINION_PATH, convert each opinion to a Document,
            and pickle each one to a file in PICKLE_PATH
            '''
            self.pack_opinions()
            return
        # unpickle opinions
        opinion_list = self.unpack_opinions()
        
        # first we convert the opinion files into Document objects
        #opinion_list = self.convert_opinions()
        # now we sort them
        subsets = self.sort_opinions(opinion_list)
        
        # should I del opinion_list now??
        del opinion_list
        
        # perform the analysis
        subset_lists = self.run_analysis(subsets, num_relevant_terms)
        # and generate the word cloud
        self.generate_clouds(subset_lists)
                
        
    def convert_opinions(self):
        '''
        Convert each given opinion into a Document object.
        
        THIS METHOD IS NOT USED NOW.
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
    
    
    def pack_opinions(self):
        '''
        Convert every opinion file residing in OPINION_PATH into a Document
        object and pickle it to file in PICKLE_PATH.
        '''
        print "Converting files in {0} to Document objects".format(OPINION_PATH)
        print "and serializing them to files in {0}...".format(PICKLE_PATH)
        txtfile_regex = re.compile(r"\.txt$")
        num_converted = 0
        num_failed = 0
        file_list = os.listdir(OPINION_PATH)
        for opinion_file in file_list:
            input_path = os.path.join(OPINION_PATH, opinion_file)
            is_text_file = re.search(txtfile_regex, input_path)
            if not is_text_file:
                print ("{0} is not a text file, so we can't convert it!"
                       .format(input_path))
                continue
            pickle_path = os.path.join(PICKLE_PATH, 
                                       opinion_file + ".Document")
            converter = DocumentConverter(input_path, pickle_path)
            try:
                print "Converting file {0} ({1} of {2})...".format(opinion_file,
                                                            num_converted+1, 
                                                            len(file_list))
                converter.convert_file().write_to_file()
                num_converted += 1
            except:
                print "Unable to convert {0} to a Document and "\
                        "save it to file...".format(opinion_file)
                num_failed += 1
                continue
            del converter
        # test output
        #print opinion_list
        # /test output
        print "Opinion conversion and pickling complete."
        print "{0} opinions converted...".format(num_converted)
        print "{0} opinions failed to be converted.".format(num_failed)
        return
    
    
    def unpack_opinions(self):
        '''
        Unpickle all of the Document files from PICKLE_PATH into 
        Document objects.        
        '''
        print "Unpacking Document objects from serialized files..."
        opinion_list = []    
        doc_regex = re.compile(r"\.Document$")
        num_unpacked = 0
        num_failed = 0
        file_list = os.listdir(PICKLE_PATH)
        for pickle_file in os.listdir(PICKLE_PATH):
            print "Unpacking Document object from {0}... "\
                    "({1} of {2})".format(pickle_file, num_unpacked+1, 
                                          len(file_list))
            is_document_file = re.search(doc_regex, pickle_file)
            if not is_document_file:
                print ("{0} is not file containing a pickled Document,"
                       "so we can't unpack it!".format(pickle_file))
                continue
            full_path = os.path.join(PICKLE_PATH, pickle_file)
            with open(full_path, 'r') as doc_file:
                try:
                    unpacked_doc = pickle.load(doc_file)
                    num_unpacked += 1
                    opinion_list.append(unpacked_doc)
                except:
                    print "Unable to unpack Document contained in "\
                        "{0}!".format(pickle_file)
                    num_failed += 1
        print "Unpacking complete."
        print "{0} Documents unpacked.".format(num_unpacked)
        print "{0} Documents failed to unpack.".format(num_failed)
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
        
        #oh_four_cases = sorter.create_subset("case_dates", ["2004"])  
              
        
        subsets = [terror_majs, terror_concurs, terror_dissents]
        ###
        print "The set contains {0} subset(s)...".format(len(subsets))
        # test output
        subset_num = 0
        for subset in subsets:
            print "subset {0} contains {1} docs.".format(subset_num, len(subset))
            subset_num += 1
        # /test output
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
        terror_maj_file = os.path.join(OPINION_PATH, "output", "terror_majority.jpg")
        terror_maj_terms = subset_lists[0]
            
        terror_concur_file = os.path.join(OPINION_PATH, "output", "terror_concurs.jpg")
        terror_concur_terms = subset_lists[1]
        
        terror_dissent_file = os.path.join(OPINION_PATH, "output", "terror_dissents.jpg")
        terror_dissent_terms = subset_lists[2]
        
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
word_cloud_app.main(should_pack_opinions=False)  