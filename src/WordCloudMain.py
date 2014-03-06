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

OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_pickled"
'''
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\pickled"
'''
# these are the cases dealing with the War on Terror
ACCEPTED_CITES = (["542 U.S. 466","542 U.S. 507","542 U.S. 426","548 U.S. 557","553 U.S. 723","553 U.S. 674"])

class WordCloudMain(object):
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

   
    def main(self, should_pack_opinions=False):
        '''
        Take all the opinions we want to convert, convert them,
        sort them into subsets, then analyze subsets and create 
        word cloud for each subset.
        '''
        num_relevant_terms = 1000
        print "Initializing analysis..."
        
        # if this is the first time running, we should convert all
        # opinions and save the Document objects for future use.
        if should_pack_opinions:
            self.pack_opinions()
            return
        
        # unpickle opinions
        opinion_list = self.unpack_opinions()
        
        # now we sort them
        subsets = self.sort_opinions(opinion_list)
        
        # delete the list to save memory (it isn't used anymore)
        del opinion_list
        
        # perform the analysis
        weighted_terms = self.run_analysis(subsets, num_relevant_terms)
        # and generate the word cloud
        self.generate_clouds(weighted_terms)
        print "Analysis and word cloud generation complete."
    
    
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
            # if a file doesn't have a .txt extension, we ignore it
            is_text_file = re.search(txtfile_regex, input_path)
            if not is_text_file:
                print ("{0} is not a text file, so we can't convert it!"
                       .format(input_path))
                num_failed += 1
                continue
            pickle_path = os.path.join(PICKLE_PATH, 
                                       opinion_file + ".Document")
            converter = DocumentConverter(input_path, pickle_path)
            # we attempt to convert, to a Document object and pickle it
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
            # if a file doesn't have a .Document extension, we ignore it
            is_document_file = re.search(doc_regex, pickle_file)
            if not is_document_file:
                print ("{0} is not file containing a pickled Document,"
                       "so we can't unpack it!".format(pickle_file))
                num_failed += 1
                continue
            # we attempt to un-pickle the file into a Document object
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
                    continue
                
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
        
        sort_field = "case_dates"
        oh_three_cases = sorter.create_subset(sort_field, ["2003"])  
        oh_four_cases = sorter.create_subset(sort_field, ["2004"])  
        oh_five_cases = sorter.create_subset(sort_field, ["2005"])       

        print "length of 2003 subset is {0}".format(len(oh_three_cases))
        print "length of 2004 subset is {0}".format(len(oh_four_cases))
        print "length of 2005 subset is {0}".format(len(oh_five_cases))
        
        subsets = [oh_three_cases, oh_four_cases, oh_five_cases]
        ###
        print "The set contains {0} subset(s)...".format(len(subsets))
        return subsets
    
    
    def run_analysis(self, subsets, num_terms):
        '''
        Performs term analysis on the given subsets.
        '''
        print "Running analysis..."
        oh_three_cases = subsets[0]
        corpus = subsets[0] + subsets[1] + subsets[2]
        analysis_engine = AnalysisEngine(corpus, oh_three_cases)
        weighted_terms = analysis_engine.analyze_docs(num_terms)
        return weighted_terms
    
    
    def generate_clouds(self, weighted_terms):
        '''
        This method will be modified for your specific situation.
        NOTE that subset_lists is a list of (output_filename, weighted_list) 
        pairs.
        
        i.e. subset_lists = [weighted_list, weighted_list, ... , weighted_list]
        '''
        # define the image output file paths and name each weighted list.
        oh_three_file = os.path.join(OPINION_PATH, "output", "2003_opinions.jpg")
        oh_three_terms = weighted_terms
        
        # test output
        print "2003 TERMS: {0}".format(oh_three_terms)
        print "2003 OUTPUT FILE: {0}".format(oh_three_file)

        # /test output
        
        print "Generating a word cloud for subset..."

        oh_three_cloud = WordCloudGenerator(oh_three_terms, oh_three_file)
        oh_three_cloud.generate_word_cloud()
        print "Word cloud generated and saved to {0}".format(oh_three_file)
        
        return
    

'''
NOTE: If should_pack_opinions=True, main() will take all the opinions living in 
OPINION_PATH, convert them to Document objects, and pickle them to PICKLE_PATH.
This process need only be done once to pack all the pickled Documents.

If should_pack_opinions=False, main() runs as normal, creating subsets, 
performing analysis, and creating word clouds and weighted list output.
'''
word_cloud_app = WordCloudMain()
word_cloud_app.main(should_pack_opinions=False)  