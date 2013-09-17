'''
Created on Sep 12, 2013

@author: Daniel
'''
import unittest
import Metadata
import Document
import SuperDocument


class SuperDocumentTest(unittest.TestCase):


    def setUp(self):
        self.test_metadata = Metadata.Metadata()
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321Yea Alabama Drown 'em Tide!\n")
        self.test_document = Document.Document(self.test_metadata, self.test_text)
        self.test_metadata_list = ([self.test_metadata, 
                                    self.test_metadata, self.test_metadata])
        self.test_superdoc_text = self.test_text * 3
        print self.test_superdoc_text
        self.test_superdoc = SuperDocument.SuperDocument(
                            self.test_metadata_list, self.test_superdoc_text)
        

    def tearDown(self):
        del self.test_metadata
        del self.test_text
        del self.test_document


    def test_serialization(self):
        self.fail("SuperDocument class: You need to write a serialization test.")
        
    
    def test_serialization_output_nonwritable(self):
        self.fail("SuperDocument class: You need to write a serialization test "
                  "for when the output file isn't writable.")
    
    
    def test_convert_to_string(self):
        self.fail("SuperDocument class: You need to write a __str__ test.")
        
    
    def test_count_words(self):
        self.fail("SuperDocument class: You need to write a count_words test.")
        
        
    def test_print_doc(self):
        self.fail("SuperDocument class: You need to write a print_doc test.")
        
    
    def test_print_metadata(self):
        self.fail("SuperDocument class: You need to write a print_metadata test.")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()