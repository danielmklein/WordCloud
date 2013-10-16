import pickle
from Document import Document
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata

class DocumentConverter():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    Given a file containing one and only one document (along with
    fields/labels/metadata), this class will parse the file and create a 
    Document object from the file.
    '''


    def __init__(self, file_to_parse, pickle_path):
        '''
        Constructor
        '''
        self.input_path = file_to_parse
        self.output_path = pickle_path
    
    
    def convert_file(self):
        '''
        Returns a Document object.
        '''
        # open input file
        # parse out metadata
        # create metadata object 
        # concatenate lines of opinion body
        # create Document object
        # close input file
        pass
        
        
    
    
    def save_converted_doc(self):
        '''
        '''
        # save Document object to file using appropriate Document method
        pass
    
        