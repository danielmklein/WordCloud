'''
Test Cases for Document Class for Word Cloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.12.2013
'''

import unittest
import Metadata
import Document

class DocumentTest(unittest.TestCase):


    def setUp(self):
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321Yea Alabama Drown 'em Tide!\n")
        self.test_metadata = Metadata.Metadata()
        self.test_document = Document.Document(self.test_metadata, self.test_text)


    def tearDown(self):
        del self.test_metadata
        del self.test_document
                                                                               

    def test_serialization(self):
        self.fail("Document class: You need to write a serialization test.")
        
    
    def test_serialization_output_nonwritable(self):
        self.fail("Document class: You need to write a serialization test "
                  "for when the output file isn't writable.")
    
    
    def test_convert_to_string(self):
        self.fail("Document class: You need to write a __str__ test.")
        
    
    def test_count_words(self):
        self.fail("Document class: You need to write a count_words test.")
        
        
    def test_print_doc(self):
        self.fail("Document class: You need to write a print_doc test.")
        
    
    def test_print_metadata(self):
        self.fail("Document class: You need to write a print_metadata test.")
    
        
        
        
    
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()