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
import os, os.path

class DocumentTest(unittest.TestCase):


    def setUp(self):
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321 Yea Alabama Drown 'em Tide!\n")
        self.test_metadata = Metadata.Metadata()
        self.test_filename = "test_document.txt"
        self.test_document = Document.Document(self.test_metadata, 
                                               self.test_text,
                                               self.test_filename)


    def tearDown(self):
        del self.test_metadata
        del self.test_document
                                                                      

    def test_serialization(self):
        print "Testing Document.write_to_file()..."
        test_output_path = self.test_document.output_filename
        if not self.test_document.write_to_file():
            self.fail("Document class: You need to write a serialization test.")
            
        with open(test_output_path, 'r') as pickled_doc_file:
            unpickled_doc = pickle.load(pickled_doc_file)
        self.assertEqual(unpickled_doc.doc_text, self.test_document.doc_text)
        self.assertEqual(unpickled_doc.word_count, self.test_document.word_count)
        self.assertEqual(unpickled_doc.output_filename, self.test_document.output_filename)
        # clean-up
        os.remove(test_output_path)
        
    
    def test_serialization_output_nonwritable(self):
        print "Testing Document.write_to_file() with read-only output file..."
        test_output_path = self.test_document.output_filename
        with open(test_output_path, 'w') as touch:
            pass
        os.chmod(test_output_path, 0444)
        self.assertRaises(IOError, self.test_document.write_to_file)
        # clean-up
        os.chmod(test_output_path, 0777)
        os.remove(test_output_path)
    
    
    def test_convert_to_string(self):
        print "Testing Document.__str__()..."
        expected_string = ""
        expected_string += str(self.test_metadata)
        expected_string += self.test_text
        self.assertEqual(str(self.test_document), expected_string)
        
    
    def test_count_words(self):
        print "Testing Document.count_words()..."
        expected_word_count = 15
        self.assertEqual(self.test_document.word_count, expected_word_count)
        
        
    def test_print_doc(self):
        print "Testing Document.print_doc()..."
        self.test_document.print_doc()
        print "Document.print_doc() testing finished.***"
        
    
    def test_print_metadata(self):
        print "Testing Document.print_metadata()..."
        self.test_document.print_metadata()
        print "Document.print_metadata() testing finished.***"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()