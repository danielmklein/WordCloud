'''
Test Cases for Metadata Class for Word Cloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.12.2013
'''

import unittest
from Metadata import Metadata

class MetadataTest(unittest.TestCase):


    def setUp(self):
        self.test_metadata = Metadata()


    def tearDown(self):
        del self.test_metadata


    def test_convert_to_string(self):
        print "MetadataTest: testing Metadata.convert_to_string()..."
        metadata_string = self.test_metadata.__str__()
        expected_string = "field1: test1\n" \
                        + "field2: test2\n" \
                        + "field3: test3\n" \
                        + "field4: test4\n"
        self.assertEqual(metadata_string, expected_string)
        
    def test_print_fields(self):
        print "MetadataTest: testing Metadata.print_fields()..."
        self.test_metadata.print_fields()
        
        
    def test_print_metadata(self):
        print "MetadataTest: testing Metadata.print_metadata()..."
        self.test_metadata.print_metadata()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()