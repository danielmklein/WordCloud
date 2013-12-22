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

###############################################################################
# here's all the test data
###############################################################################
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

NO_PUNCTUATION =\
"""\
The reader is probably asking  Why would anyone go to Camp Green Lake  Most \
campers weren t given a choice  Camp Green Lake is a camp for bad boys  If \
you take a bad boy and make him dig a hole every day in the hot sun  it will \
turn him into a good boy  That was what some people thought  Stanley Yelnats \
was given a choice  The judge said   You may go to jail  or you may go to Camp \
Green Lake   Stanley was from a poor family  He had never been to camp before \
"""

NO_SHORT_WORDS =\
"""\
The reader probably asking Why would anyone Camp Green Lake Most campers weren \
given choice Camp Green Lake camp for bad boys you take bad boy and make him \
dig hole every day the hot sun will turn him into good boy That was what some \
people thought Stanley Yelnats was given choice The judge said You may jail \
you may Camp Green Lake Stanley was from poor family had never been camp before\
"""

FILTERED_TEXT = """\
The reader probably asking Why would anyone Camp Green Lake Most campers weren \
given choice Camp Green Lake camp for bad boys you take bad boy and make him \
dig hole every day the hot sun will turn him into good boy That was what some \
people thought Stanley Yelnats was given choice The judge said You may jail \
you may Camp Green Lake Stanley was from poor family had never been camp \
before\
"""

NO_STOP_WORDS = ()

SPLIT_TEXT = (['reader', 'probably', 'asking', 'would', 'anyone', 
                        'camp', 'green', 'lake', 'campers', 'weren', 'given', 
                        'choice', 'camp', 'green', 'lake', 'camp', 'bad', 
                        'boys', 'take', 'bad', 'boy', 'make', 'dig', 'hole', 
                        'every', 'day', 'hot', 'sun', 'turn', 'good', 'boy', 
                        'people', 'thought', 'stanley', 'yelnats', 'given', 
                        'choice', 'judge', 'said', 'may', 'jail', 'may', 
                        'camp', 'green', 'lake', 'stanley', 'poor', 'family', 
                        'never', 'camp'])

STEMMED_TEXT = (['reader', 'probabl', 'ask', 'would', 'anyon', 
                          'camp', 'green', 'lake', 'camper', 'weren', 
                          'given', 'choic', 'camp', 'green', 'lake', 'camp', 
                          'bad', 'boy', 'take', 'bad', 'boy', 'make', 'dig', 
                          'hole', 'everi', 'day', 'hot', 'sun', 'turn', 
                          'good', 'boy', 'peopl', 'thought', 'stanley', 
                          'yelnat', 'given', 'choic', 'judg', 'said', 'may', 
                          'jail', 'may', 'camp', 'green', 'lake', 'stanley', 
                          'poor', 'famili', 'never', 'camp'])

TERM_LIST = ({'lake?': {'tf': None}, 'camp': {'tf': None}, 'people': {'tf': None}, 
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

###############################################################################
###############################################################################

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
        '''
        passing
        '''
        print "Testing DocumentStorage.__str__()..."
        expected = str(self.test_metadata) \
                    + "Here some test text Blah blah blah blah "\
                    "Yea Alabama Drown Tide"
        actual = str(self.test_document)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        
    
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
        expected = SPLIT_TEXT
        actual = self.test_document.create_split_text(FILTERED_TEXT)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        print "DocumentStorage.create_split_text() testing finished.***"


    def test_build_term_list(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.build_term_list()..."
        term_list = self.test_document.build_term_list(SPLIT_TEXT)
        self.assertEqual(TERM_LIST, term_list)
        print "DocumentStorage.build_term_list() testing finished.***"        


    def test_populate_term_freqs(self):
        print "Testing DocumentStorage.populate_term_freqs()..."
        self.fail("haven't written this test yet")
        print "DocumentStorage.populate_term_freqs() testing finished.***"


    def test_filter_text(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.filter_text()..."
        expected = FILTERED_TEXT
        actual = self.test_document.filter_text(TEST_TEXT)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        print "DocumentStorage.filter_text() testing finished.***"


    def test_remove_proper_nouns(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_proper_nouns()..."
        expected = NO_PROPER_NOUNS
        actual = self.test_document.remove_proper_nouns(TEST_TEXT)
        print "Expected: {0}".format(expected)
        print "Actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_proper_nouns() testing finished.***"


    def test_remove_punctuation(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_punctuation()..."
        expected = NO_PUNCTUATION
        actual = self.test_document.remove_punctuation(TEST_TEXT)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_punctuation() testing finished.***"
        
        
    def test_remove_nums(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_nums()..."
        text = "Here is some test text. Blah blah blah blah "\
                "1234567890987654321 Yea Alabama Drown 'em Tide!"
        expected = "Here is some test text. Blah blah blah blah "\
                " Yea Alabama Drown 'em Tide!"
        actual = self.test_document.remove_nums(text)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_nums() testing finished.***"
        
        
    def test_remove_short_words(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_single_chars()..."
        expected = NO_SHORT_WORDS
        actual = self.test_document.remove_short_words(NO_PUNCTUATION)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_single_chars() testing finished.***"
        
        
    def test_remove_stop_words(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_stop_words()..."
        text = [word.lower() for word in FILTERED_TEXT.split()]
        expected = SPLIT_TEXT
        actual = self.test_document.remove_stop_words(text)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"
        
        
    def test_stem_text(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.stem_text()..."
        expected = STEMMED_TEXT
        actual = self.test_document.stem_text(SPLIT_TEXT)
        print "expected: {0}".format(expected)
        print "actual  : {0}".format(actual)
        self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.stem_text() testing finished.***"
        

    def test_calculate_term_frequency(self):
        '''
        passing
        '''
        print "Testing DocumentStorage.remove_stop_words()..."
        for term in self.test_document.term_list:
            print "Checking term frequency of term: {0}".format(term)
            expected = self.test_document.stemmed_text.count(term) \
                        / float(len(self.test_document.stemmed_text))
            actual = self.test_document.calculate_term_frequency(term)
            self.assertEqual(expected, actual)
        #self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"
    
    
    def test_calc_tfidf(self):
        
        print "Testing DocumentStorage.remove_stop_words()..."

        self.fail("haven't written this test yet")
        print "DocumentStorage.remove_stop_words() testing finished.***"



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()