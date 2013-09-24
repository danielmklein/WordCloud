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
                          + "1234567890987654321 Yea Alabama Drown 'em Tide!\n")
        self.test_filename = "test_document.txt"
        self.test_document = Document.Document(self.test_metadata, 
                                               self.test_text,
                                               self.test_filename)
        self.test_metadata_list = ([self.test_metadata, 
                                    self.test_metadata, self.test_metadata])
        self.test_superdoc_text = self.test_text * 3
        #print self.test_superdoc_text
        self.test_superdoc = SuperDocument.SuperDocument(
                            self.test_metadata_list, self.test_superdoc_text)
        

    def tearDown(self):
        del self.test_metadata
        del self.test_text
        del self.test_document


    def test_serialization(self):
        print "Testing SuperDocument.write_to_file()..."
        self.fail("SuperDocument class: You need to write a serialization test.")
        
    
    def test_serialization_output_nonwritable(self):
        print "Testing SuperDocument.write_to_file() with read-only output file..."
        self.fail("SuperDocument class: You need to write a serialization test "
                  "for when the output file isn't writable.")
    
    
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
        print "Testing SuperDocument.print_superdoc()..."
        self.fail("SuperDocument class: You need to write a print_doc test.")
        
    
    def test_print_metadata(self):
        print "Testing SuperDocument.print_component_metadata()..."
        self.fail("SuperDocument class: You need to write a print_metadata test.")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()