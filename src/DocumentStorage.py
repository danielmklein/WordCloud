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
        {term1: {tf:0, tf_idf:0}, term2:{tf:0, tf_idf:0}, ... , termn:{tf:0, tf_idf:0}}
        '''
        self.term_list = {}
        for term in self.split_text:
            if not term in self.term_list:
                self.term_list[term] = {"tf":None, "tf_idf":None}
        for term in self.term_list:
            self.term_list[term]['tf'] = self.calculate_term_frequency(term)
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
    
    
    def calculate_term_frequency(self, term):
        '''
        given a term and a doc, calculates term's relative frequency
        in that doc, ie
        (# times term appears in doc) / (# total terms in doc)
        '''
        term_freq = self.split_text.count(term)
        return term_freq
    
    
    def calc_tfidf(self, term, doc_freq):
        '''
        given a term and its relative doc frequency, calculates the tf-idf 
        for the term in the document.
        '''
        if term in self.term_list:
            term_freq = self.term_list[term]['tf']
        else:
            term_freq = 0
        tf_idf = term_freq / float(doc_freq)
        
        if term in self.term_list:
            self.term_list[term]['tf_idf'] = tf_idf
            
        return tf_idf

        