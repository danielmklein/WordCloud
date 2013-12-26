'''
Created on Sep 12, 2013

@author: Daniel
'''
import unittest
from Metadata import Metadata
from Document import Document
from SuperDocument import SuperDocument
import pickle
import os, os.path


class SuperDocumentTest(unittest.TestCase):


    def setUp(self):
        self.test_metadata = Metadata()
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321 Yea Alabama Drown 'em Tide!\n")
        self.test_filename = "test_superdoc.txt"
        self.test_document = Document(self.test_metadata, 
                                      self.test_text,
                                      self.test_filename)
        self.test_metadata_list = ([self.test_metadata, 
                                    self.test_metadata, self.test_metadata])
        self.test_superdoc_text = self.test_text * 3
        #print self.test_superdoc_text
        self.test_superdoc = SuperDocument(self.test_metadata_list, 
                                           self.test_superdoc_text, 
                                           self.test_filename)
        self.assertEqual(len(self.test_superdoc.component_metadata), 3)
        

    def tearDown(self):
        del self.test_metadata
        del self.test_text
        del self.test_document


    def test_serialization(self):
        print "Testing SuperDocument.write_to_file()..."
        #self.fail("SuperDocument class: You need to write a serialization test.")
        test_output_path = self.test_superdoc.output_filename
        if not self.test_superdoc.write_to_file():
            self.fail("Document class: You need to write a serialization test.")
            
        with open(test_output_path, 'r') as pickled_superdoc_file:
            unpickled_superdoc = pickle.load(pickled_superdoc_file)
        self.assertEqual(unpickled_superdoc.superdoc_text, self.test_superdoc.superdoc_text)
        self.assertEqual(unpickled_superdoc.word_count, self.test_superdoc.word_count)
        self.assertEqual(unpickled_superdoc.output_filename, self.test_superdoc.output_filename)
        # clean-up
        os.remove(test_output_path)
        
    
    def test_serialization_output_nonwritable(self):
        print "Testing SuperDocument.write_to_file() with read-only output file..."
        #self.fail("SuperDocument class: You need to write a serialization test "
        #          "for when the output file isn't writable.")
        test_output_path = self.test_superdoc.output_filename
        with open(test_output_path, 'w') as touch:
            pass
        os.chmod(test_output_path, 0444)
        self.assertRaises(IOError, self.test_superdoc.write_to_file)
        # clean-up
        os.chmod(test_output_path, 0777)
        os.remove(test_output_path)
        
    
    def test_convert_to_string(self):
        print "Testing SuperDocument.__str__()..."
        #print self.test_superdoc
        expected_string= ""
        for metadata in self.test_metadata_list:
            expected_string += str(metadata)
        expected_string += self.test_superdoc_text
        self.assertEqual(str(self.test_superdoc), expected_string)
        #self.fail("SuperDocument class: You need to write a __str__ test.")

        
    def test_count_words(self):
        print "Testing SuperDocument.count_words()..."
        #self.fail("SuperDocument class: You need to write a count_words test.")
        expected_word_count = 45
        self.assertEqual(self.test_superdoc.word_count, expected_word_count)
        
        
    def test_print_doc(self):
        print "***Testing SuperDocument.print_superdoc()...***"
        #self.fail("SuperDocument class: You need to write a print_doc test.")
        self.test_superdoc.print_superdoc()
        print "SuperDocument.print_superdoc() testing finished.***"
        
    
    def test_print_metadata(self):
        print "Testing SuperDocument.print_component_metadata()..."
        #self.fail("SuperDocument class: You need to write a print_metadata test.")
        self.test_superdoc.print_component_metadata()
        print "SuperDocument.print_component_metadata() testing finished.***"
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()