class AnalysisEngine():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    Given a set of Documents (divided into subsets) (and perhaps analysis 
    parameters TBD), this class will perform natural language text processing 
    on the collection of documents and return a weighted list of the "most 
    important" terms in the collection. This will likely utilize term 
    frequency-inverse document frequency analysis as its basis for weighting 
    terms (http://en.wikipedia.org/wiki/Tf%E2%80%93idf).
    '''


    def __init__(self, set_of_docs):
        '''
        set_of_docs should be of the form 
        [[doc1, doc2, doc3], [doc4, doc5] , ... , [docx, docy, docz]]
        in other words, a list representing the full set of docs, broken
        into sublists, each representing a subset.
        '''
        '''
        for every doc in set, create new DocumentStorage object from doc???
        '''
        pass
    
    
    def build_full_term_list(self):
        '''
        constructs a list of all terms used in the entire set.
        '''
        pass
    
    
    def build_doc_term_list(self, doc):
        ''' 
        constructs list of all terms used in a doc.
        '''
        pass
    
    
    def analyze_docs(self):
        '''
        '''
        pass
    
    
    def process_subset(self, subset):
        '''
        '''
        pass
    
    
    def calc_doc_frequency(self, term):
        '''
        given a term, calculates its relative doc frequency, ie
        (# docs term in which term appears) / (# docs total in set)
        '''
        pass
    
    
    def calc_term_frequency(self, term, doc):
        '''
        given a term and a doc, calculates term's relative frequency
        in that doc, ie
        (# times term appears in doc) / (# total terms in doc)
        '''
        pass
    
    
    def calc_tfidf(self, term, subset):
        '''
        given a term and a subset, calculates the median tf-idf for
        the term in that subset -- ie the median of the tf-idf's for
        the term for each document in the subset.
        '''
        pass
    
    
    def save_output(self, output_path):
        pass
    
    
        