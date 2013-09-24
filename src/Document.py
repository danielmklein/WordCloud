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
import pickle 

class Document():
    '''
    classdocs
    '''
    
    def __init__(self, doc_metadata, doc_text, output_filename):
        '''
        doc_metadata should be a Metadata object or ancestor.
        doc_text should be a string.
        '''
        self.doc_metadata = doc_metadata
        self.doc_text = doc_text
        self.output_filename = output_filename
        self.word_count = self.count_words(self.doc_text)
    
    
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
        Uses pickle to serialize and save the Document to file.
        '''
        #print "I haven't written the Document.write_to_file() method yet!"
        try:
            with open(self.output_filename, 'wb') as output_file:
                pickle.dump(self, output_file)
        except IOError: 
            print "An error occurred while pickling the document -- the output file may not be writable."
            raise IOError
        return True
    
    
    def print_doc(self):
        '''
        Display document with its metadata.
        '''
        #print "I haven't written the Document.print_doc() method yet!"
        print self
        return True
    
    
    def print_metadata(self):
        '''
        Display metadata data fields and values from doc.
        '''
        self.doc_metadata.print_metadata()
        return True
    
        
    def __str__(self):
        '''
        Converts Document object to formatted string.
        '''
        #print "I haven't written the Document.__str__() method yet!"
        #return "haven't written it yet"
        document_string = ""
        document_string += str(self.doc_metadata)
        document_string += self.doc_text
        return document_string
    
    
    
    