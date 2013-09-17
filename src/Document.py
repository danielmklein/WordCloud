'''
Document Class for Word Cloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.12.2013

This class represents a document object (such as a single Supreme Court opinion).
A typical object will consist of the document's text and a metadata object
consisting of various fields relevant to the document. We will subclass this
class for each type of document we will use.
'''

class Document():
    '''
    classdocs
    '''
    
    def __init__(self, doc_metadata, doc_text):
        '''
        doc_metadata should be a Metadata object or ancestor.
        doc_text should be a string.
        '''
        self.doc_metadata = doc_metadata
        self.doc_text = doc_text
        self.word_count = self.count_words(self.doc_text)
    
    
    def count_words(self, text):
        '''
        Utility method to perform simple wordcount.
        '''
        num_words = 0
        for line in text:
            num_words += len(line.split())
        # test output
        print "WORD COUNT:{0}".format(num_words)
        # \test output
        return num_words
    
    
    def write_to_file(self):
        '''
        Uses pickle to serialize and save the Document to file.
        '''
        pass
     
    
    def print_doc(self):
        '''
        Display document with its metadata.
        '''
        pass
    
    
    def print_metadata(self):
        '''
        Display metadata data fields and values from doc.
        '''
        pass
    
        
    def __str__(self):
        '''
        Converts Document object to formatted string.
        '''
        pass
    