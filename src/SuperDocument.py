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
import pickle 

class SuperDocument():
    '''
    classdocs
    '''


    def __init__(self, component_metadata, superdoc_text):
        '''
        component_metadata should be a list of Metadata objects.
        superdoc_text should be a string.
        '''
        self.component_metadata = component_metadata
        self.superdoc_text = superdoc_text
        self.word_count = self.count_words(self.superdoc_text)
    
    
    def count_words(self, text):
        '''
        Utility method to perform simple wordcount.
        '''
        num_words = 0
        num_words = len(text.split())
        # test output
        #print "WORD COUNT:{0}".format(num_words)
        # \test output
        return num_words
        
    
    def write_to_file(self):
        '''
        Uses pickle to serialize and save the SuperDocument to file.
        '''
        pass
    
    
    def print_superdoc(self):
        '''
        Displays the entire SuperDocument, formatted.
        '''
        pass
        
    
    def print_component_metadata(self):
        '''
        Displays the metadata for each document making up the SuperDoc.
        '''
        pass
    
    
    def __str__(self):
        '''
        Converts the SuperDocument to a formatted string.
        '''
        super_doc_string = ""
        for metadata in self.component_metadata:
            super_doc_string += str(metadata)
        super_doc_string += self.superdoc_text
        #print super_doc_string
        return super_doc_string
    
    