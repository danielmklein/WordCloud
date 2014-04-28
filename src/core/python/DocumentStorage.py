import re
from string import punctuation
from src.core.python.Document import Document
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

CAP_REGEX = re.compile("[A-Z]+")
PUNC_REGEX = re.compile("[\.\?!]")
EXTRA_STOP_WORDS = (["concur", "dissent", "concurring", 
                     "dissenting", "case", "join"])
ALL_STOP_WORDS = stopwords.words('english') + EXTRA_STOP_WORDS


class DocumentStorage(Document):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    10.27.2013
    
    This class is basically just a Document object along with a place
    to store the list of terms in the document and each of their 
    frequencies.
    '''
    def __init__(self, doc_metadata, doc_text, output_filename):        
        Document.__init__(self, doc_metadata, doc_text, output_filename)
        # TODO: this identifier is useless, currently.
        self.identifier = self.doc_metadata.opinion_author + "_" \
                            + self.doc_metadata.case_lexis_cite
                            
        # doc_text holds the actual string containing the raw text from the doc
        self.doc_text = doc_text

        # split_text contains the full filtered text of the document
        self.split_text = self.filter_text(self.doc_text)
        
        # stemmed_text contains full filtered text with all words stemmed
        self.stemmed_text = self.stem_text(self.split_text)
        
        # term_list is a list of unique terms in the document along with
        # each term's term frequency and tf_idf metric -- only term freq
        # is calculated for each term at this point.
        self.term_list = self.build_term_list(self.stemmed_text)
        self.term_list = self.populate_term_freqs(self.term_list)
        
        
    def build_term_list(self, split_text):
        '''
        Build term list of form 
        {term1: {'tf':0, 'tf_idf':0}, term2:{'tf':0, 'tf_idf':0}, ... , 
        termn:{'tf':0, 'tf_idf':0}}
        This method also counts the instances of each term in the text
        as we go along building the list.
        '''
        term_list = {}
        for term in split_text:
            if not term in term_list:
                term_list[term] = {"tf":None, "count":0}
            else:
                term_list[term]["count"] += 1            
        return term_list
    
    
    def populate_term_freqs(self, term_list):
        '''
        Calculates relative term frequency for each term in term_list.
        '''
        for term in term_list:
            term_list[term]['tf'] = self.calculate_term_frequency(term)
        return term_list
    
    
    def filter_text(self, text, should_drop_prop_nouns=False):
        '''
        Remove certain items from text. Currently we're removing
        punctuation, digits, short words, and stop words. Optionally 
        we can dumbly remove proper nouns. 
        There is a possibility we might want to remove opinion footnotes
        in the future, but we currently leave them in.
        '''
        # first remove numbers
        text = re.sub('[\d]', ' ', text)
        unfiltered_text = text.split()
        filtered_text = []
        for i in range(len(unfiltered_text)):
            cur_term = unfiltered_text[i]   
            
            # we MUST do the proper noun filter before we take out punctuation
            if should_drop_prop_nouns:
                if i != 0:
                    prev_term = unfiltered_text[i - 1]
                else:
                    prev_term = "null"

                # remove proper noun, if needed
                if self.is_proper_noun(cur_term, prev_term):
                    continue
            
            # remove punctuation
            cur_term = re.sub('[%s]' % re.escape(punctuation), '', cur_term)
            # convert term to lowercase and remove any whitespace  
            cur_term = cur_term.lower().strip()
            
            # remove words less than 3 letters long
            if len(cur_term) < 3:
                continue
          
            filtered_text.append(cur_term)
            
        # filter out stopwords
        filtered_text = [word for word in filtered_text 
                         if word not in ALL_STOP_WORDS] 
        return filtered_text
        
        
    def is_proper_noun(self, cur_term, prev_term):
        '''
        Given a term and the preceding term, roughly determines if the 
        given term is a proper noun. Keyword: roughly.
        '''
        is_proper_noun = (CAP_REGEX.match(cur_term)
                          and not (PUNC_REGEX.search(prev_term)))
        return is_proper_noun
        
    
    def remove_footnotes(self, text):
        '''
        Removes footnotes sections from the text of the document.
        Not used in the project currently.
        '''
        pass
    
    
    def stem_text(self, word_list):
        '''
        Stems the appropriate words in the given word_list.
        '''
        stemmed_list = []
        stemmer = PorterStemmer()
        for word in word_list:
            stemmed_list.append(stemmer.stem(word))
        return stemmed_list
    
    
    def calculate_term_frequency(self, term):
        '''
        Given a term and a doc, calculates term's relative frequency
        in that doc, ie
        (# times term appears in doc) / (# total terms in doc)
        '''
        rel_term_freq = self.term_list[term]["count"] \
                        / float(len(self.stemmed_text))
        return rel_term_freq
    
    
    def calc_tfidf(self, term, doc_freq):
        '''
        Given a term and its relative doc frequency, calculates the tf-idf 
        for the term in the document.
        '''
        try:
            term_freq = self.term_list[term]['tf']
        except KeyError:
            term_freq = 0
        tf_idf = term_freq / float(doc_freq)

        return tf_idf

        