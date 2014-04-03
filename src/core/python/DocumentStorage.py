import re
from string import punctuation
from src.core.python.Document import Document
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
        # TODO: this identifier is useless, currently.
        self.identifier = self.doc_metadata.opinion_author + "_" \
                            + self.doc_metadata.case_lexis_cite
                            
        # TODO: filter_text() and create_split_text() can be rolled together.
        # I don't think there's a reason for doc_text to be a filtered list...
        # it could just be the raw doc_text passed into the constructor.
        self.doc_text = doc_text
        #self.split_text = self.filter_text(self.doc_text,
        #                                 should_drop_prop_nouns=True)
        # split_text contains the full filtered text of the document
        self.split_text = self.filter_text(self.doc_text)
        # stemmed_text contains full filtered text with all words stemmed
        self.stemmed_text = self.stem_text(self.split_text)
        # term_list is a list of unique terms in the document along with
        # each term's term frequency and tf_idf metric -- only term freq
        # is calculated for each term at this point.
        self.term_list = self.build_term_list(self.stemmed_text)
        self.term_list = self.populate_term_freqs(self.term_list)
        
        
    def create_split_text(self, text):
        '''
        Turns the text of the document into a list of terms
        with stop words removed.
        '''
        split_text = [word.lower() for word in text.split()]
        split_text = self.remove_stop_words(split_text)
        return split_text
        
        
    def build_term_list(self, split_text):
        '''
        Build term list of form 
        {term1: {'tf':0, 'tf_idf':0}, term2:{'tf':0, 'tf_idf':0}, ... , 
        termn:{'tf':0, 'tf_idf':0}}
        '''
        term_list = {}
        for term in split_text:
            if not term in term_list:
                term_list[term] = {"tf":None}            
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
        '''
        TODO: we could speed this up by doing it all in one pass over the 
        text, instead of a pass per filter type.
        '''
        '''
        filtered_text = text
        # remove footnotes?
        #text = self.remove_footnotes(text)
        if should_drop_prop_nouns:
            filtered_text = self.remove_proper_nouns(filtered_text)
        # remove punctuation from doc_text
        filtered_text = self.remove_punctuation(filtered_text)
        # remove numbers
        filtered_text = self.remove_nums(filtered_text)
        # remove single-letter words
        filtered_text = self.remove_short_words(filtered_text)
        return filtered_text
        '''
        unfiltered_text = text.split()
        filtered_text = []
        for i in range(len(unfiltered_text)):
            if i != 0:
                prev_term = unfiltered_text[i - 1]
            else:
                prev_term = "null"
            cur_term = unfiltered_text[i]
            should_remove = False
            # remove proper noun, if needed
            if (should_drop_prop_nouns 
                and self.is_proper_noun(cur_term, prev_term)):
                    should_remove = True
            # remove punctuation
            cur_term = re.sub('[%s]' % re.escape(punctuation), ' ', cur_term)
            # remove numbers
            cur_term = re.sub('[\d]', '', cur_term)
            # remove words less than 3 letters long
            if len(cur_term) < 3:
                should_remove = True
            # convert term to lowercase
            cur_term = cur_term.lower()
            # check if term is a stopword -- remove if so.
            if self.is_stop_word(cur_term):
                should_remove = True
                
            if not should_remove:
                filtered_text.append(cur_term.strip())
                
        return filtered_text
        
        
    def is_proper_noun(self, cur_term, prev_term):
        '''
        Given a term and the preceding term, roughly determines if the 
        given term is a proper noun. Keyword: roughly.
        '''
        cap_regex = re.compile("[A-Z]+")
        punc_regex = re.compile("[\.\?!]")
        is_proper_noun = (cap_regex.match(cur_term)
                          and not (punc_regex.search(prev_term)))
        return is_proper_noun
        
        
    def remove_proper_nouns(self, text):
        '''
        Remove the proper nouns from the text. More accurately, removes
        any word that starts with a capital letter and does not follow
        a period.
        '''
        '''
        TODO: this method is no longer used
        '''
        cap_regex = re.compile("[A-Z]+")
        punc_regex = re.compile("[\.\?!]")
        filtered_text = []
        split_text = text.split()
        if len(split_text) < 1:
            return text
        filtered_text.append(split_text[0])
        for i in range(1, len(split_text)):
            prev_term = split_text[i-1]
            cur_term = split_text[i]
            is_proper_noun = (cap_regex.match(cur_term)
                              and not (punc_regex.search(prev_term)))
            if not is_proper_noun:
                filtered_text.append(cur_term)
        return " ".join(filtered_text)
        
    
    def remove_punctuation(self, text):
        '''
        Delete all punctuation from text -- replaced with space.
        '''
        '''
        TODO: this method is no longer used.
        '''
        return re.sub('[%s]' % re.escape(punctuation), ' ', text)
    
    
    def remove_nums(self, text):
        '''
        Delete all digits from text.
        '''
        '''
        TODO: this method is no longer used.
        '''
        return re.sub('[\d]', '', text)
    
    
    def remove_short_words(self, text):
        '''
        Remove all words shorter than 3 letters long.
        '''
        '''
        TODO: this method is no longer used.
        '''
        #return re.sub(r'\s.\s', ' ', text) 
        filtered_words = []
        for term in text.split():
            if len(term) > 2:
                filtered_words.append(term)
        return ' '.join(filtered_words)
            
    
    
    def remove_footnotes(self, text):
        '''
        Removes footnotes sections from the text of the document.
        Not used in the project currently.
        '''
        pass
    
    
    def is_stop_word(self, word):
        '''
        Determines if a given word is considered a stop word.
        '''
        extra_stop_words = (["concur", "dissent", "concurring", 
                             "dissenting", "case", "join"])
        is_stop_word = ((word in stopwords.words('english'))
                        or (word in extra_stop_words))
        return is_stop_word
    
    
    def remove_stop_words(self, word_list):
        '''
        Removes stop words from word_list.
        '''
        '''
        TODO: this method is no longer used.
        '''
        extra_stop_words = (["concur", "dissent", "concurring", 
                             "dissenting", "case", "join"])
        filtered_text = ([word for word in word_list if 
                          (not word in stopwords.words('english'))
                          and (not word in extra_stop_words)])
        return filtered_text
    
    
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
        '''
        TODO: I also think I can speed up conversion by flattening stemmed_text into
        a term:count dict in __init__ and then just referencing that dict here,
        instead of having to use count every time this method is called.
        '''
        rel_term_freq = self.stemmed_text.count(term) \
                        / float(len(self.stemmed_text))
        return rel_term_freq
    
    
    def calc_tfidf(self, term, doc_freq):
        '''
        Given a term and its relative doc frequency, calculates the tf-idf 
        for the term in the document.
        '''
        # I changed this to try...except for speed purposes.
        #if term in self.term_list:
        try:
            term_freq = self.term_list[term]['tf']
        #else:
        except KeyError:
            term_freq = 0
        tf_idf = term_freq / float(doc_freq)
        ### saves the tf_idf in the term_list... is this really necessary?
        #if term in self.term_list:
        #    self.term_list[term]['tf_idf'] = tf_idf
        ###
        return tf_idf

        