'''
Test Cases for DocumentConverter Class for WordCloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.27.2013
'''

import unittest
import os, os.path
import DocumentConverter

VALID_OPINION_FILE_LINES = ([
"""\
TITLE: UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES\
DENTAL CO., ET AL.\
""",
"""CASE NUMBER: No. 43""",
"""LEXIS CITATION: 1944 U.S. LEXIS 1230""",
"""\
FULL CITATION: 323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230\
""",
"""DATES: December 18, 1944, Decided;""",
"""DISPOSITION: 53 F.Supp. 596, affirmed.""",
"""* * * * * * * *""",
"""MR. JUSTICE MURPHY, concurring.""",
"""I join in the opinion of the Court and believe that the judgment should be \
affirmed.""",
"""Congress has the constitutional power to fix venue at any place where a \
crime occurs. Our problem here is to determine, in the absence of a specific \
venue provision, where the crime outlawed by the Federal Denture Act occurred \
for purposes of venue.""",
"""The Act prohibits the use of the mails for the purpose of sending or \
bringing into any state certain prohibited articles. It is undisputed that \
when a defendant places a prohibited article in the mails in Illinois for \
the purpose of sending it into Delaware he has completed a statutory offense. \
Hence he is triable in Illinois. But to hold that the statutory crime also \
encompasses the receipt of the prohibited article in Delaware, justifying a \
trial at that point, requires an implication that I am unwilling to make in \
the absence of more explicit Congressional language.""",
"""Very often the difference between liberty and imprisonment in cases where \
the direct evidence offered by the government and the defendant is evenly \
balanced depends upon the presence of character witnesses. The defendant is \
more likely to obtain their presence in the district of his residence, which \
in this instance is usually the place where the prohibited article is mailed. \
The inconvenience, expense and loss of time involved in transplanting these \
witnesses to testify in trials far removed from their homes are often too \
great to warrant their use. Moreover, they are likely to lose much of their \
effectiveness before a distant jury that knows nothing of their reputations. \
Such factors make it difficult for me to conclude, where Congress has not \
said so specifically, that we should construe the Federal Denture Act as \
covering more than the first sufficient and punishable use of the mails \
insofar as the sender of a prohibited article is concerned. The principle of \
narrow construction of criminal statutes does not warrant interpreting the \
"use" of the mails to cover all possible uses in light of the foregoing \
considerations."""])

TEST_FILE_PATH = os.path.join(os.path.abspath(os.curdir), "test_opinion.txt")
TEST_PICKLE_PATH = os.path.join(os.path.abspath(os.curdir), "pickled_test_doc")

def create_test_file(file_lines):
    with open(TEST_FILE_PATH, 'w') as test_file:
        for line in file_lines:
            test_file.write(line + "\n")


class DocumentConverterTest(unittest.TestCase):


    def setUp(self):
        '''
        what do i need to run tests? 
       - a test file.
        '''
        # test output
        print TEST_FILE_PATH
        # /test output
        self.test_path = TEST_FILE_PATH
        self.test_converter = DocumentConverter.DocumentConverter(self.test_path, TEST_PICKLE_PATH)
        


    def tearDown(self):
        if os.path.exists(self.test_path): 
            os.remove(self.test_path)
        del self.test_converter
        

    def testNormalCase(self):
        # create a normal test file
        create_test_file(VALID_OPINION_FILE_LINES)
        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.fail("DocumentConverterTest: I haven't written testNormalCase yet.")


    def testImproperFileFormat(self):
        # this test case might not be necessary... we'll see.
        self.fail("DocumentConverterTest: I haven't written testImproperFileFormat yet.")
    
    
    def testNoMetadataInFile(self):
        # create a test file without any metadata fields in it
        create_test_file(VALID_OPINION_FILE_LINES[7:])
        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.fail("DocumentConverterTest: I haven't written testNoMetadataInFile yet.")
    
    
    def testNoBodyTextInFile(self):
        # create a test file with valid metadata but without any body text in it
        create_test_file(VALID_OPINION_FILE_LINES[:7])
        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.fail("DocumentConverterTest: I haven't written testNoBodyTextInFile yet.")
    
    
    def testOutputFileNotWritable(self):
        # I need to change the permisssions of the pickle_path (chmod 0444)
        self.fail("DocumentConverterTest: I haven't written testOutputFileNotWritable yet.")
        
    
    def testInputFileNonexistent(self):
        # skip the create_test_file call and just try to convert.
        converted_doc = self.test_converter.convert_file()
        # this might actually be a "assertThrows" situation on convert_file
        self.fail("DocumentConverterTest: I haven't written testInputFileNonexistent yet.")

    
    def testEmptyInputFile(self):
        # create a test file with nothing in it
        create_test_file([])
        converted_doc = self.test_converter.convert_file()
        self.fail("DocumentConverterTest: I haven't written testEmptyInputFile yet.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()