import pickle 

class SuperDocument():
    '''
    Created on Sep 12, 2013
    
    SuperDocument Class for Word Cloud Project
    
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.12.2013
    
    A SuperDoc object will consist of a piece of text that represents the
    concatenation of the text fields from 1+ documents, along with a list of
    Metadata objects -- each item in this list will be the metadata from one of
    the documents that make up the SuperDoc.
    '''


    def __init__(self, component_metadata, superdoc_text, output_filename):
        '''
        component_metadata should be a list of Metadata objects.
        superdoc_text should be a string.
        '''
        self.component_metadata = component_metadata
        self.superdoc_text = superdoc_text
        self.output_filename = output_filename
        self.word_count = self.count_words(self.superdoc_text)
    
    
    def count_words(self, text):
        '''
        Utility method to perform simple wordcount.
        '''
        return len(text.split())
        
    
    def write_to_file(self):
        '''
        Uses pickle to serialize and save the SuperDocument to file.
        '''
        try:
            with open(self.output_filename, 'wb') as output_file:
                pickle.dump(self, output_file)
        except IOError: 
            print "An error occurred while pickling the SuperDocument -- the output file may not be writable."
            raise IOError
        return True
    
    
    def print_superdoc(self):
        '''
        Displays the entire SuperDocument, formatted.
        '''
        print self
        
    
    def print_component_metadata(self):
        '''
        Displays the metadata for each document making up the SuperDoc.
        '''
        for metadata in self.component_metadata:
            print metadata
    
    
    def __str__(self):
        '''
        Converts the SuperDocument to a formatted string.
        '''
        super_doc_string = ""
        for metadata in self.component_metadata:
            super_doc_string += str(metadata)
        super_doc_string += self.superdoc_text
        return super_doc_string
    
    