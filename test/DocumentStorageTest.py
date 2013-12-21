'''
Test Cases for DocumentStorage Class for Word Cloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
11.18.2013
'''

import unittest
import pickle
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from DocumentStorage import DocumentStorage
import os, os.path

TEST_TEXT =\
"""\
The reader is probably asking: Why would anyone go to Camp Green Lake? \
Most campers weren't given a choice. Camp Green Lake is a camp for bad boys. \
If you take a bad boy and make him dig a hole every day in the hot sun, it \
will turn him into a good boy. That was what some people thought. \
Stanley Yelnats was given a choice. The judge said, "You may go to jail, or \
you may go to Camp Green Lake." \
Stanley was from a poor family. He had never been to camp before.\
"""

NO_PROPER_NOUNS =\
"""\
The reader is probably asking: would anyone go to \
Most campers weren't given a choice. Camp is a camp for bad boys. \
If you take a bad boy and make him dig a hole every day in the hot sun, it \
will turn him into a good boy. That was what some people thought. \
Stanley was given a choice. The judge said, "You may go to jail, or \
you may go to \
Stanley was from a poor family. He had never been to camp before.\
"""

EXPECTED_SPLIT_TEXT = (['reader', 'probably', 'asking:', 'would', 'anyone', 'go',
                        'camp', 'green', 'lake?', 'campers', "weren't", 'given', 
                        'choice.', 'camp', 'green', 'lake', 'camp', 'bad', 'boys.', 
                        'take', 'bad', 'boy', 'make', 'dig', 'hole', 'every', 'day', 
                        'hot', 'sun,', 'turn', 'good', 'boy.', 'people', 'thought.', 
                        'stanley', 'yelnats', 'given', 'choice.', 'judge', 'said,', 
                        '"you', 'may', 'go', 'jail,', 'may', 'go', 'camp', 'green', 
                        'lake."', 'stanley', 'poor', 'family.', 'never', 'camp', 
                        'before.'])

EXPECTED_TERM_LIST = ({'lake?': {'tf': None}, 'camp': {'tf': None}, 'people': {'tf': None}, 
                       'boy.': {'tf': None}, 'thought.': {'tf': None}, 'boys.': {'tf': None},
                       'yelnats': {'tf': None}, 'go': {'tf': None}, 'stanley': {'tf': None}, 
                       'said,': {'tf': None}, 'given': {'tf': None}, 'would': {'tf': None}, 
                       '"you': {'tf': None}, 'family.': {'tf': None}, 'campers': {'tf': None}, 
                       'lake': {'tf': None}, 'anyone': {'tf': None}, 'choice.': {'tf': None}, 
                       'take': {'tf': None}, 'reader': {'tf': None}, 'probably': {'tf': None}, 
                       'poor': {'tf': None}, 'good': {'tf': None}, 'may': {'tf': None}, 
                       'never': {'tf': None}, 'before.': {'tf': None}, 'every': {'tf': None}, 
                       'sun,': {'tf': None}, 'judge': {'tf': None}, 'hole': {'tf': None}, 
                       'lake."': {'tf': None}, 'day': {'tf': None}, 'boy': {'tf': None}, 
                       'asking:': {'tf': None}, 'dig': {'tf': None}, 'hot': {'tf': None}, 
                       'turn': {'tf': None}, 'bad': {'tf': None}, 'green': {'tf': None}, 
                       "weren't": {'tf': None}, 'jail,': {'tf': None}, 'make': {'tf': None}})


class DocumentStorageTest(unittest.TestCase):


    def setUp(self):
        self.test_text = ("Here is some test text. Blah blah blah blah \n"
                          + "1234567890987654321 Yea Alabama Drown 'em Tide!\n")
        self.test_metadata = SupremeCourtOpinionMetadata()
        self.test_filename = "test_document.txt"
        self.test_document = DocumentStorage(self.test_metadata, 
                                      self.test_text,
                                      self.test_filename)


    def tearDown(self):
        del self.test_metadata
        del self.test_document
                                                                      

    def test_serialization(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.write_to_file()..."
        test_output_path = self.test_document.output_filename
        if not self.test_document.write_to_file():
            self.fail("DocumentStorage class: You need to write a serialization test.")
            
        with open(test_output_path, 'r') as pickled_doc_file:
            unpickled_doc = pickle.load(pickled_doc_file)
        self.assertEqual(unpickled_doc.doc_text, self.test_document.doc_text)
        self.assertEqual(unpickled_doc.word_count, self.test_document.word_count)
        self.assertEqual(unpickled_doc.output_filename, self.test_document.output_filename)
        # clean-up
        os.remove(test_output_path)
        
    
    def test_serialization_output_nonwritable(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.write_to_file() with read-only output file..."
        test_output_path = self.test_document.output_filename
        with open(test_output_path, 'w') as touch:
            pass
        os.chmod(test_output_path, 0444)
        self.assertRaises(IOError, self.test_document.write_to_file)
        # clean-up
        os.chmod(test_output_path, 0777)
        os.remove(test_output_path)
    
    
    def test_convert_to_string(self):
        print "Testing DocumentStorage.__str__()..."
        expected_string = ""
        expected_string += str(self.test_metadata)
        expected_string += "Here is some test text  Blah blah blah blah em"
        self.assertEqual(str(self.test_document), expected_string)
        
    
    def test_count_words(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.count_words()..."
        expected_word_count = 15
        self.assertEqual(self.test_document.word_count, expected_word_count)
        
        
    def test_print_doc(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.print_doc()..."
        self.test_document.print_doc()
        print "DocumentStorage.print_doc() testing finished.***"
        
    
    def test_print_metadata(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.print_metadata()..."
        self.test_document.print_metadata()
        print "DocumentStorage.print_metadata() testing finished.***"

    
    def test_create_split_text(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.create_split_text()..."
        split_text = self.test_document.create_split_text(TEST_TEXT)
        self.assertEqual(EXPECTED_SPLIT_TEXT, split_text)
        print "DocumentStorage.create_split_text() testing finished.***"


    def test_build_term_list(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.build_term_list()..."
        term_list = self.test_document.build_term_list(EXPECTED_SPLIT_TEXT)
        self.assertEqual(EXPECTED_TERM_LIST, term_list)
        print "DocumentStorage.build_term_list() testing finished.***"        


    def test_populate_term_freqs(self):
        print "Testing DocumentStorage.populate_term_freqs()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.populate_term_freqs() testing finished.***"


    def test_filter_text(self):
        print "Testing DocumentStorage.filter_text()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.filter_text() testing finished.***"


    def test_remove_proper_nouns(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_proper_nouns()..."
        expected = NO_PROPER_NOUNS
        actual = self.test_document.remove_proper_nouns(TEST_TEXT)
        print "Expected text: {0}".format(expected)
        print "Actual text  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_proper_nouns() testing finished.***"


    def test_remove_punctuation(self):
        print "Testing DocumentStorage.remove_punctuation()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_punctuation() testing finished.***"
        
        
    def test_remove_nums(self):
        print "Testing DocumentStorage.remove_nums()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_nums() testing finished.***"
        
        
    def test_remove_single_chars(self):
        print "Testing DocumentStorage.remove_single_chars()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_single_chars() testing finished.***"
        
        
    def test_remove_stop_words(self):
        print "Testing DocumentStorage.remove_stop_words()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"
        
        
    def test_stem_text(self):
        print "Testing DocumentStorage.stem_text()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.stem_text() testing finished.***"
        

    def test_calculate_term_frequency(self):
        print "Testing DocumentStorage.remove_stop_words()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"
    
    
    def test_calc_tfidf(self):
        print "Testing DocumentStorage.remove_stop_words()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()