'''
Test Cases for DocumentSorter Class for WordCloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.27.2013
'''

import unittest
import os, os.path
from Document import Document
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from DocumentSorter import DocumentSorter

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
CASE_DATES = [("November 8, 1944", "Argued"),("December 18, 1944", "Decided")]
CASE_DISPOSITION = "53 F.Supp. 596, affirmed."

OPINION_AUTHOR = "MURPHY"
OPINION_TEXT = "\n".join(VALID_OPINION_FILE_LINES[10:])

TEST_PICKLE_PATH = os.path.join(os.path.abspath(os.curdir), "pickled_test_doc")
#######


def create_test_docs():
    test_meta1 = SupremeCourtOpinionMetadata()
    test_meta1.case_title = CASE_TITLE
    test_meta1.case_num = CASE_NUM
    test_meta1.case_us_cite = CASE_US_CITE
    test_meta1.case_supreme_court_cite = CASE_SUPREME_COURT_CITE
    test_meta1.case_lawyers_ed_cite = CASE_LAWYERS_ED_CITE
    test_meta1.case_lexis_cite = CASE_LEXIS_CITE
    test_meta1.case_full_cite = CASE_FULL_CITE
    test_meta1.case_dates = CASE_DATES
    test_meta1.case_disposition = CASE_DISPOSITION
    test_meta1.opinion_author = OPINION_AUTHOR
    test_doc1 = Document(test_meta1, OPINION_TEXT, TEST_PICKLE_PATH)
    
    test_meta2 = SupremeCourtOpinionMetadata()
    test_meta2.case_num = "No. 43"
    test_doc2 = Document(test_meta2, OPINION_TEXT, TEST_PICKLE_PATH)

    test_meta3 = SupremeCourtOpinionMetadata()
    test_meta3.case_num = "No. 67"
    test_meta3.opinion_author = "JOHNSON"
    test_doc3 = Document(test_meta3, OPINION_TEXT, TEST_PICKLE_PATH)
    
    test_meta4 = SupremeCourtOpinionMetadata()
    test_meta4.case_num = "No. 46"
    test_meta4.opinion_author = "MURPHY"
    test_doc4 = Document(test_meta4, OPINION_TEXT, TEST_PICKLE_PATH)
    
    test_meta5 = SupremeCourtOpinionMetadata()
    test_meta5.case_num = "No. 43"
    test_doc5 = Document(test_meta5, OPINION_TEXT, TEST_PICKLE_PATH)
    
    test_docs = [test_doc1, test_doc2, test_doc3, test_doc4, test_doc5]
    return test_docs


class DocumentSorterTest(unittest.TestCase):


    def setUp(self):
        self.test_docs = create_test_docs()
        self.test_sorter = DocumentSorter(self.test_docs)


    def tearDown(self):
        del self.test_sorter
        del self.test_docs


    def testSortDocsNormalCase(self):
        # If I sort on case num, I should get one subset of 3 for "No. 43",
        # a subset of 1 for "No. 46", and a subset of 1 for "No. 67"
        sorted_subsets = self.test_sorter.sort_docs("case_num")
        expected_subsets = [self.test_docs[0:3], [self.test_docs[3]], [self.test_docs[4]]]
        self.assertEqual(expected_subsets, sorted_subsets)
        #self.fail("DocumentSorterTest: I haven't written a test for testSortDocsNormalCase yet!")
    
    
    def testSortDocsEmptyInputList(self):
        # should this just return an empty list?
        self.test_docs = []
        sorted_subsets = self.test_sorter.sort_docs("case_num")
        expected_subsets = []
        self.assertEqual(expected_subsets, sorted_subsets)
        #self.fail("DocumentSorterTest: I haven't written a test for testSortDocsEmptyInputList yet!")
    
    
    def testSortDocsNonDocObject(self):
        # throw exception
        self.test_docs.append("THIS IS A STRING")
        self.assertRaises(Exception, self.test_sorter.sort_docs, "case_num")
        #self.fail("DocumentSorterTest: I haven't written a test for testSortDocsNonDocObject yet!")
    
    
    def testSortDocsInvalidSortField(self):
        # throw exception
        self.assertRaises(Exception, self.test_sorter.sort_docs, "this_isnt_a_field")
        #self.fail("DocumentSorterTest: I haven't written a test for testSortDocsInvalidSortField yet!")
    
    
    def testCreateSubsetNormalCase(self):
        # If I create a subset where author is in ["JOHNSON", "MURPHY"], I 
        # should get a subset of 2 -- 2 MUPRHY, 1 JOHNSON
        test_allowed_values = ["MURPHY", "JOHNSON"]
        expected_subset = [self.test_docs[0], self.test_docs[2], self.test_docs[3]]
        created_subset = self.test_sorter.create_subset("opinion_author", test_allowed_values)
        self.assertEqual(expected_subset, created_subset)
        #self.fail("DocumentSorterTest: I haven't written a test for testCreateSubsetNormalCase yet!")


    def testCreateSubsetNoAllowedValues(self):
        # return empty subset list?
        test_allowed_values = []
        expected_subset = []
        created_subset = self.test_sorter.create_subset("opinion_author", test_allowed_values)
        self.assertEqual(expected_subset, created_subset)
        #self.fail("DocumentSorterTest: I haven't written a test for testCreateSubsetNoAllowedValues yet!")


    def testCreateSubsetNoAllowedValueMatches(self):
        # return empty subset list?
        test_allowed_values = ["JACKSON", "THOMPSON"]
        expected_subset = []
        created_subset = self.test_sorter.create_subset("opinion_author", test_allowed_values)
        self.assertEqual(expected_subset, created_subset)
        #self.fail("DocumentSorterTest: I haven't written a test for testCreateSubsetNoAllowedValueMatches yet!")


    def testAddDocNormalCase(self):
        test_meta = SupremeCourtOpinionMetadata()
        test_meta.case_num = "No. 99"
        test_doc = Document(test_meta, OPINION_TEXT, TEST_PICKLE_PATH)
        
        self.assertEqual(len(self.test_sorter.doc_list), 5)
        self.test_sorter.add_doc(test_doc)
        self.assertEqual(len(self.test_sorter.doc_list), 6)
        self.assertEqual(self.test_sorter.doc_list[5], test_doc)
        #self.fail("DocumentSorterTest: I haven't written a test for testAddDocNormalCase yet!")
        
        
    def testAddDocWithNonDocument(self):
        # throw exception, or let it happen??
        # what if I simply assert that it has to have at least doc_metadata?
        self.assertRaises(Exception, self.test_sorter.add_doc, "THIS IS NOT A DOC")
        #self.fail("DocumentSorterTest: I haven't written a test for testAddDocWithNonDocument yet!")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()