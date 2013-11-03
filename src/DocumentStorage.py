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
        # remove footnotes?
        # remove punctuation from doc_text
        self.doc_text = re.sub('[%s]' % re.escape(punctuation), ' ', self.doc_text)
        self.split_text = self.create_split_text()
        self.term_list = self.build_term_list()
        
        
    def create_split_text(self):
        split_text = [word.lower() for word in self.doc_text.split()]
        split_text = self.remove_stop_words(split_text)
        split_text = self.stem_text(split_text)
        return split_text
        
        
    def build_term_list(self):
        '''
        build term list of form 
        {term1: (term_freq, tf_idf), term2:(term_freq, tf_idf), ... , termn:(term_freq, tf_idf)}
        '''
        self.term_list = {}
        for term in self.split_text:
            if not term in self.term_list:
                self.term_list[term] = [0,0]
        # test output
        print self.term_list
        # /test output
        return self.term_list
    
    
    def remove_footnotes(self):
        '''
        removes footnotes sections from the text of the document.
        '''
        pass
    
    
    def remove_stop_words(self, word_list):
        '''
        removes stop words from the text of the document
        '''
        filtered_text = ([word for word in word_list if not word in
                         stopwords.words('english')])
        # test output
        print word_list
        print filtered_text
        # \ test output
        return filtered_text
    
    
    def stem_text(self, word_list):
        '''
        stems the appropriate words in the text of the document
        '''
        stemmed_list = []
        stemmer = PorterStemmer()
        for word in word_list:
            stemmed_list.append(stemmer.stem(word))
        # test output
        print stemmed_list
        # /test output
        return stemmed_list

        