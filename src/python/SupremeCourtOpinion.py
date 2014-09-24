from src.core.python.Document import Document

class SupremeCourtOpinion(Document):
    '''
    Document Class for Word Cloud Project
    
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    4.27.14
    
    This class represents a single Supreme Court opinion. A typical object 
    will consist of the opinions's text and a 
    metadata object consisting of various fields relevant to the opinion. 
    We will subclass the metadata class for each type of document we will use.
    '''


    def __init__(self, doc_metadata, doc_text, output_filename):
        '''
        Constructor
        '''
        super(SupremeCourtOpinion, self).__init__(doc_metadata, doc_text, output_filename)
    
    
    def build_display_string(self):
        '''
        Build string for displaying opinion in GUI.
        '''
        pass
        