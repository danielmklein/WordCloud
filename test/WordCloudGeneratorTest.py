'''
Test Cases for WordCloudGenerator Class for WordCloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.27.2013
'''

import unittest
import WordCloudGenerator

class WordCloudGeneratorTest(unittest.TestCase):


    def setUp(self):
        self.test_output_filename = "test_word_cloud.jpg"
        self.test_weighted_terms = []
        self.test_generator = \
            WordCloudGenerator.WordCloudGenerator(self.test_weighted_terms, 
                                                self.test_output_filename)


    def tearDown(self):
        del self.test_generator


    def testGenerateWordCloud(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with normal weighted list of terms."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("test", 0.25),("America",0.24),
                                              ("Roll",0.99), ("Tide",0.98),
                                              ("Yea",0.75),("Alabama",0.74),
                                              ("Rammer",0.5), ("Jammer",0.51)]
        self.test_generator.generate_word_cloud()


    def testGenerateWordCloudReducedTermList(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with normal weighted list of terms."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("test", 0.25),("America",0.24),
                                              ("Roll",0.99), ("Tide",0.98),
                                              ("Yea",0.75),("Alabama",0.74),
                                              ("Rammer",0.5), ("Jammer",0.51)]
        self.test_generator.generate_word_cloud(6)
        
    
    def testGenerateWordCloudEmptyList(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with empty weighted list of terms."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("America",0.5),("test", 1.56)]
        self.test_generator.generate_word_cloud()        
        
        
    def testGenerateWordCloudSingleTerm(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with weighted list of terms containing a single term."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("test", 0.56)]
        self.test_generator.generate_word_cloud()
        
        
    def testGenerateWordCloudTooBigParameter(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with the num_terms_to_visualize parameter greater than "\
        "the length of the input list."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("America",0.5),("test", 1.56)]
        self.test_generator.generate_word_cloud()


    def testGenerateWordCloudWrongInputFormat(self):
        print "Testing WordCloudGenerator.generate_word_cloud() "\
        "with wrong type of input data."
        # reset test_weighted_list before generating
        self.test_generator.weighted_terms = [("America",0.5),("test", 1.56)]
        self.test_generator.generate_word_cloud()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()