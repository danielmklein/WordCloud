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

class WordCloudCore():
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
                    continue
                
        print "Unpacking complete."
        print "{0} Documents unpacked.".format(num_unpacked)
        print "{0} Documents failed to unpack.".format(num_failed)
        self.opinion_labels = ([opin.doc_metadata.case_title  
                               for opin in self.opinion_list])
        return self.opinion_list
    
    
    def create_subset(self, opinion_list, sort_field, accepted_values):
        '''
        Sort the opinions into subset(s).
        '''
        print "Sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
  
        subset = sorter.create_subset(sort_field, accepted_values)
        return subset
    
