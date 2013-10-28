import re
from string import punctuation
from Document import Document
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

class DocumentStorage(Document):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    10.27.2013
    
    This guy is basically just a Document object along with a place
    to store the list of terms in the document and each of their 
    frequencies.
    '''
    
    def __init__(self, doc_metadata, doc_text, output_filename):
        Document.__init__(self, doc_metadata, doc_text, output_filename)
        self.identifier = self.doc_metadata.opinion_author + "_" \
                            + self.doc_metadata.case_lexis_cite
        # remove punctuation from doc_text
        self.doc_text = re.sub('[%s]' % re.escape(punctuation), '', self.doc_text)
        self.split_text = self.doc_text.split()
        self.split_text = self.remove_stop_words()
        self.split_text = self.stem_text()
        self.term_list = self.build_term_list()
        
        
    def build_term_list(self):
        '''
        build term list of form 
        {term1: (term_freq, tf_idf), term2:(term_freq, tf_idf), ... , termn:(term_freq, tf_idf)}
        '''
        self.term_list = {}
        
        
        return self.term_list
    
    
    def remove_stop_words(self):
        '''
        removes stop words from the text of the document
        '''
        pass
    
    
    def stem_text(self):
        '''
        stems the appropriate words in the text of the document
        '''
        stemmer = PorterStemmer()
        pass
        