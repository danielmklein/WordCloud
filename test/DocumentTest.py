'''
Test Cases for Document Class for Word Cloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.12.2013
'''

import unittest
import pickle
import Metadata
import Document

class DocumentTest(unittest.TestCase):


    def setUp(self):
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321Yea Alabama Drown 'em Tide!\n")
        self.test_metadata = Metadata.Metadata()
        self.test_filename = "test_document.txt"
        self.test_document = Document.Document(self.test_metadata, 
                                               self.test_text,
                                               self.test_filename)


    def tearDown(self):
        del self.test_metadata
        del self.test_document
                                                                               

    def test_serialization(self):
        if not self.test_document.write_to_file():
            self.fail("Document class: You need to write a serialization test.")
        
    
    def test_serialization_output_nonwritable(self):
        if not self.test_document.write_to_file():
            self.fail("Document class: You need to write a serialization test "
                      "for when the output file isn't writable.")
    
    
    def test_convert_to_string(self):
        expected_string = ""
        expected_string += str(self.test_metadata)
        expected_string += self.test_text
        self.assertEqual(str(self.test_document), expected_string)
        
    
    def test_count_words(self):
        expected_word_count = 14
        self.assertEqual(self.test_document.word_count, expected_word_count)
        
        
    def test_print_doc(self):
        print "Testing Document.print_doc()..."
        if not self.test_document.print_doc():
            self.fail("Document class: You need to write a print_doc test.")
        
    
    def test_print_metadata(self):
        print "Testing Document.print_metadata()..."
        if not self.test_document.print_metadata():
            self.fail("Document class: You need to write a print_metadata test.") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()