import os, os.path
import re
import cPickle as pickle
from src.core.python.SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from src.core.python.DocumentSorter import DocumentSorter
from src.core.python.AnalysisEngine import AnalysisEngine
from src.core.python.WordCloudGenerator import WordCloudGenerator

# directory containing parsed opinions

OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_pickled"
'''
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\pickled"
'''

class WordCloudCore(object):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    2.22.2014
    
    This class contains the core functionality with which the GUI components
    interact when running the app.
    '''


    def __init__(self):
        self.opinion_list = []
        self.opinion_labels = []
        
        self.subsets = {}
        self.subset_names = []
        
        self.corpus_subsets = {}
        self.corpus_subset_names = []
        
        self.field_names = SupremeCourtOpinionMetadata().field_names
        
        
    def pack_opinions(self):
        '''
        Convert every opinion file residing in OPINION_PATH into a Document
        object and pickle it to file in PICKLE_PATH.
        '''
        '''
        TODO: this is not currently used here... it might be worth it in the future to
        add functionality for packing and unpacking through the GUI.
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
            converter = SupremeCourtOpinionFileConverter(input_path, pickle_path)
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
        
        self.opinion_list = []    
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
                    self.opinion_list.append(unpacked_doc)
                except:
                    print "Unable to unpack Document contained in "\
                        "{0}!".format(pickle_file)
                    num_failed += 1
                    raise
                    #continue
                
        print "Unpacking complete."
        print "{0} Documents unpacked.".format(num_unpacked)
        print "{0} Documents failed to unpack.".format(num_failed)
        self.opinion_labels = ([opin.doc_metadata.case_title  
                               for opin in self.opinion_list])
        return self.opinion_list
    
    
    def create_subset(self, opinion_list, sort_field, 
                      accepted_values, should_invert=False):
        '''
        Sort the opinions into subset(s).
        '''
        print "Sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
  
        subset = sorter.create_subset(sort_field, accepted_values, 
                                      should_invert)
        return subset
    
    
    def add_subset(self, subset_name, subset_opinions):
        self.subsets[subset_name] = subset_opinions
        self.subset_names.append(subset_name)
        
        
    def run_analysis(self, corpus, subset, num_terms=1000):
        '''
        Performs term analysis on the given subsets.
        '''
        print "Running analysis..."
        analysis_engine = AnalysisEngine(corpus, subset)
        weighted_terms = analysis_engine.analyze_docs(num_terms)
        return weighted_terms
    
    
    def generate_cloud(self, weighted_terms):
        '''
        Draws word cloud from given weighted term list.
        '''
        output_file = os.path.join(os.curdir, "wordcloud.jpg")
        cloud_gen = WordCloudGenerator(weighted_terms, output_file)
        cloud_gen.generate_word_cloud()
        return
        
        
    
