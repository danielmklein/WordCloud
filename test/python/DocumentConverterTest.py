'''
Test Cases for DocumentConverter Class for WordCloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.27.2013
'''

import unittest
import os, os.path
from DocumentConverter import DocumentConverter

##### Here are all the global variables used in these tests.
VALID_OPINION_FILE_LINES = ([
"""\
TITLE: UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES\
DENTAL CO., ET AL.\
""",
"""CASE NUMBER: No. 43""",
"""US CITATION: 323 U.S. 273""",
"""SUPREME COURT CITATION: 65 S. Ct. 249""",
"""LAWYERS ED CITATION: 89 L. Ed. 236""",
"""LEXIS CITATION: 1944 U.S. LEXIS 1230""",
"""\
FULL CITATION: 323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230\
""",
"""DATES: November 8, 1944, Argued;December 18, 1944, Decided;""",
"""DISPOSITION: 53 F.Supp. 596, affirmed.""",
"""OPINION TYPE: concur""",
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

CASE_TITLE = """\
UNITED STATES v. JOHNSON ET AL., DOING BUSINESS AS UNITED STATES\
DENTAL CO., ET AL.\
"""
CASE_NUM = "No. 43"
CASE_US_CITE = "323 U.S. 273"
CASE_SUPREME_COURT_CITE = "65 S. Ct. 249"
CASE_LAWYERS_ED_CITE = "89 L. Ed. 236"
CASE_LEXIS_CITE = "1944 U.S. LEXIS 1230"
CASE_FULL_CITE = "323 U.S. 273; 65 S. Ct. 249; 89 L. Ed. 236; 1944 U.S. LEXIS 1230"
CASE_DATES = "November 8, 1944 (Argued) December 18, 1944 (Decided) " # THIS MIGHT CHANGE!!
CASE_DISPOSITION = "53 F.Supp. 596, affirmed."

OPINION_AUTHOR = "MURPHY"
OPINION_TYPE = "concur"
OPINION_TEXT = "\n".join(VALID_OPINION_FILE_LINES[11:])

TEST_FILE_PATH = os.path.join(os.path.abspath(os.curdir), "MURPHY_1944 U.S. LEXIS 1230.txt")
TEST_PICKLE_PATH = os.path.join(os.path.abspath(os.curdir), "pickled_test_doc")
#####

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
        self.test_path = TEST_FILE_PATH
        self.test_converter = DocumentConverter(self.test_path, TEST_PICKLE_PATH)
        

    def tearDown(self):
        if os.path.exists(self.test_path): 
            os.remove(self.test_path)
        if os.path.exists(TEST_PICKLE_PATH):
            os.chmod(TEST_PICKLE_PATH, 0777)
            os.remove(TEST_PICKLE_PATH)
        del self.test_converter
        

    def testNormalCase(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() normal case..."
        # create a normal test file
        create_test_file(VALID_OPINION_FILE_LINES)
        converted_doc = self.test_converter.convert_file()
        print "word count: {0}".format(converted_doc.word_count)
        # here assert a bunch of things about the resulting converted_doc
        self.assertTrue(hasattr(converted_doc, 'output_filename'))
        self.assertEqual(converted_doc.output_filename, TEST_PICKLE_PATH)
        
        self.assertTrue(hasattr(converted_doc, 'doc_text'))
        self.assertEqual(converted_doc.doc_text, OPINION_TEXT)
        
        self.assertTrue(hasattr(converted_doc, 'doc_metadata'))
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_title'))
        self.assertEqual(converted_doc.doc_metadata.case_title, CASE_TITLE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_author'))
        self.assertEqual(converted_doc.doc_metadata.opinion_author, OPINION_AUTHOR)
                
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_type'))
        self.assertEqual(converted_doc.doc_metadata.opinion_type, OPINION_TYPE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_num'))
        self.assertEqual(converted_doc.doc_metadata.case_num, CASE_NUM)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_us_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_us_cite, CASE_US_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_supreme_court_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_supreme_court_cite, CASE_SUPREME_COURT_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lawyers_ed_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lawyers_ed_cite, CASE_LAWYERS_ED_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lexis_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lexis_cite, CASE_LEXIS_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_full_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_full_cite, CASE_FULL_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_dates'))
        self.assertEqual(converted_doc.doc_metadata.case_dates, CASE_DATES)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_disposition'))
        self.assertEqual(converted_doc.doc_metadata.case_disposition, CASE_DISPOSITION)

    
    def testNoMetadataInFile(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() "\
        "with no Metadata in the input file..."
        # create a test file without any metadata fields in it
        create_test_file(VALID_OPINION_FILE_LINES[10:])
        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.assertTrue(hasattr(converted_doc, 'output_filename'))
        self.assertEqual(converted_doc.output_filename, TEST_PICKLE_PATH)
        
        self.assertTrue(hasattr(converted_doc, 'doc_text'))
        self.assertEqual(converted_doc.doc_text, OPINION_TEXT)
        
        self.assertTrue(hasattr(converted_doc, 'doc_metadata'))
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_title'))
        self.assertEqual(converted_doc.doc_metadata.case_title, "")
    
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_author'))
        self.assertEqual(converted_doc.doc_metadata.opinion_author, OPINION_AUTHOR)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_type'))
        self.assertEqual(converted_doc.doc_metadata.opinion_type, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_num'))
        self.assertEqual(converted_doc.doc_metadata.case_num, "")

        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_us_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_us_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_supreme_court_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_supreme_court_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lawyers_ed_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lawyers_ed_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lexis_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lexis_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_full_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_full_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_dates'))
        self.assertEqual(converted_doc.doc_metadata.case_dates, [])
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_disposition'))
        self.assertEqual(converted_doc.doc_metadata.case_disposition, "")
        #self.fail("DocumentConverterTest: I haven't written testNoMetadataInFile yet.")
    
    
    def testNoBodyTextInFile(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() "\
        "with no body text in the input file..."
        # create a test file with valid metadata but without any body text in it
        create_test_file(VALID_OPINION_FILE_LINES[:11])
        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.assertTrue(hasattr(converted_doc, 'output_filename'))
        self.assertEqual(converted_doc.output_filename, TEST_PICKLE_PATH)
        
        self.assertTrue(hasattr(converted_doc, 'doc_text'))
        self.assertEqual(converted_doc.doc_text, "")
        
        self.assertTrue(hasattr(converted_doc, 'doc_metadata'))
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_title'))
        self.assertEqual(converted_doc.doc_metadata.case_title, CASE_TITLE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_author'))
        self.assertEqual(converted_doc.doc_metadata.opinion_author, OPINION_AUTHOR)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_type'))
        self.assertEqual(converted_doc.doc_metadata.opinion_type, OPINION_TYPE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_num'))
        self.assertEqual(converted_doc.doc_metadata.case_num, CASE_NUM)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_us_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_us_cite, CASE_US_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_supreme_court_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_supreme_court_cite, CASE_SUPREME_COURT_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lawyers_ed_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lawyers_ed_cite, CASE_LAWYERS_ED_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lexis_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lexis_cite, CASE_LEXIS_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_full_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_full_cite, CASE_FULL_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_dates'))
        self.assertEqual(converted_doc.doc_metadata.case_dates, CASE_DATES)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_disposition'))
        self.assertEqual(converted_doc.doc_metadata.case_disposition, CASE_DISPOSITION)
        #self.fail("DocumentConverterTest: I haven't written testNoBodyTextInFile yet.")
    
    
    def testOutputFileNotWritable(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() "\
        "and save_converted_doc() with an unwritable output file..."
        create_test_file(VALID_OPINION_FILE_LINES)
        converted_doc = self.test_converter.convert_file()
        # assert stuff about the created converted_doc
        self.assertTrue(hasattr(converted_doc, 'output_filename'))
        self.assertEqual(converted_doc.output_filename, TEST_PICKLE_PATH)
        
        self.assertTrue(hasattr(converted_doc, 'doc_text'))
        self.assertEqual(converted_doc.doc_text, OPINION_TEXT)
        
        self.assertTrue(hasattr(converted_doc, 'doc_metadata'))
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_title'))
        self.assertEqual(converted_doc.doc_metadata.case_title, CASE_TITLE)

        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_author'))
        self.assertEqual(converted_doc.doc_metadata.opinion_author, OPINION_AUTHOR)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_type'))
        self.assertEqual(converted_doc.doc_metadata.opinion_type, OPINION_TYPE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_num'))
        self.assertEqual(converted_doc.doc_metadata.case_num, CASE_NUM)
    
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_us_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_us_cite, CASE_US_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_supreme_court_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_supreme_court_cite, CASE_SUPREME_COURT_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lawyers_ed_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lawyers_ed_cite, CASE_LAWYERS_ED_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lexis_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lexis_cite, CASE_LEXIS_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_full_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_full_cite, CASE_FULL_CITE)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_dates'))
        self.assertEqual(converted_doc.doc_metadata.case_dates, CASE_DATES)
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_disposition'))
        self.assertEqual(converted_doc.doc_metadata.case_disposition, CASE_DISPOSITION)
        # I need to change the permisssions of the pickle_path (chmod 0444)
        with open(converted_doc.output_filename, 'w') as dummy:
            pass
        os.chmod(converted_doc.output_filename, 0444)
        self.assertRaises(IOError, self.test_converter.save_converted_doc)
        #self.fail("DocumentConverterTest: I haven't written testOutputFileNotWritable yet.")
        
    
    def testInputFileNonexistent(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() "\
        "with nonexistent input file..."
        # skip the create_test_file call and just try to convert.
        self.assertRaises(IOError, self.test_converter.convert_file)
        #self.fail("DocumentConverterTest: I haven't written testInputFileNonexistent yet.")

    
    def testEmptyInputFile(self):
        print "DocumentConverterTest: testing DocumentConverter.convert_file() "\
        "with completely empty input file..."
        # create a test file with nothing in it
        create_test_file([])

        converted_doc = self.test_converter.convert_file()
        # here assert a bunch of things about the resulting converted_doc
        self.assertTrue(hasattr(converted_doc, 'output_filename'))
        self.assertEqual(converted_doc.output_filename, TEST_PICKLE_PATH)
        
        self.assertTrue(hasattr(converted_doc, 'doc_text'))
        self.assertEqual(converted_doc.doc_text, "")
        
        self.assertTrue(hasattr(converted_doc, 'doc_metadata'))
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_title'))
        self.assertEqual(converted_doc.doc_metadata.case_title, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_author'))
        self.assertEqual(converted_doc.doc_metadata.opinion_author, OPINION_AUTHOR)

        self.assertTrue(hasattr(converted_doc.doc_metadata, 'opinion_type'))
        self.assertEqual(converted_doc.doc_metadata.opinion_type, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_num'))
        self.assertEqual(converted_doc.doc_metadata.case_num, "")

        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_us_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_us_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_supreme_court_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_supreme_court_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lawyers_ed_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lawyers_ed_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_lexis_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_lexis_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_full_cite'))
        self.assertEqual(converted_doc.doc_metadata.case_full_cite, "")
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_dates'))
        self.assertEqual(converted_doc.doc_metadata.case_dates, [])
        
        self.assertTrue(hasattr(converted_doc.doc_metadata, 'case_disposition'))
        self.assertEqual(converted_doc.doc_metadata.case_disposition, "")
        #self.fail("DocumentConverterTest: I haven't written testEmptyInputFile yet.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()