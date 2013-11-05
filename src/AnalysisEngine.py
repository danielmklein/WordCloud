from DocumentStorage import DocumentStorage
import os, os.path
import pickle
from numpy import mean

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
        self.set_subsets(set_of_docs)


    def set_subsets(self, set_of_docs):
        '''
        for every doc in set, create new DocumentStorage object from doc
        build list of all terms in entire set (build_full_term_list)
        '''
        self.subsets = set_of_docs
        self.subsets = self.convert_docs(self.subsets)
        self.num_docs = self.count_docs()
        self.term_list = self.build_full_term_list(self.subsets)
        
        
    def count_docs(self):
        '''
        calculates the total number of docs in all subsets
        '''
        num_docs = 0
        for subset in self.subsets:
            num_docs += len(subset)
        # test output
        print "NUM DOCS IS: {0}".format(num_docs)
        # /test output
        return num_docs
        
        
    def convert_docs(self, subsets):
        converted_subsets = []
        for subset in subsets:
            new_subset = []
            for doc in subset:
                try:
                    doc = DocumentStorage(doc.doc_metadata, doc.doc_text, 
                                      doc.output_filename)
                    new_subset.append(doc)
                except:
                    raise Exception, "AnalysisEngine: The input seems to be of the wrong type..."
            converted_subsets.append(new_subset)
        return converted_subsets
            
    
    def build_full_term_list(self, subsets):
        '''
        constructs a list of all terms used in the entire set along
        with each one's doc frequency
        '''
        term_list = {}
        for subset in subsets:
            for doc in subset:
                new_terms = ([term for term in doc.term_list.keys() 
                             if term not in term_list])
                for term in new_terms:
                    term_list[term] = self.calc_doc_frequency(term)
        # test output
        print "TERM LIST"
        print term_list
        print "END TERM LIST"
        # /test output
        return term_list
    
    
    def build_doc_term_list(self, doc):
        ''' 
        constructs list of all terms used in a doc.
    
        !!!!this is implemented in the DocumentStorage class!!!!
        '''
        pass
    
    
    def analyze_docs(self):
        '''
        the main method -- kicks off the analysis process
        '''
        '''
        for each term:
            calculate_doc_frequency
            for each doc in set_of_docs:
                calc_term_frequency(term, doc)
        for each subset in set: (self.process_subset)
            for each term in subset:
                for each doc:
                    calculate tf-idf for term in doc (if term appears, else 0)
                calculate tf-idf for term in subset (median)
            build, save, and return list of terms in subset sorted by tf-idf
        '''
        for subset in self.subsets:
            weighted_terms = self.process_subset(subset)
            curdir = os.path.abspath(os.curdir)
            output_path = os.path.join(curdir, 
                                       subset[0].output_filename 
                                       + "_weighted_list")
            self.save_weighted_list(weighted_terms, output_path)
        pass
    
    
    def process_subset(self, subset):
        '''
        this method is going to actually construct the weighted list
        for each subset
        
        NOTE: output list must be of form [(term1,weight1),(term2,weight2),...,(termn,weightn)]
        '''
        raw_weighted_terms = []
        for term in self.term_list:
            tfidf = self.calc_tfidf_for_subset(term, subset)
            raw_weighted_terms.append((term, tfidf))
        # test output
        print "INITIAL WEIGHTED TERMS: {0}".format(raw_weighted_terms)
        # /test output
        
        weighted_terms = []
        scale_factor = max([item[1] for item in raw_weighted_terms])
        for pair in raw_weighted_terms:
            weighted_terms.append((pair[0], pair[1] / scale_factor))
        # test output
        print "SCALED WEIGHTED TERMS: {0}".format(weighted_terms)
        # /test output
        return weighted_terms
    
    
    def calc_doc_frequency(self, term):
        '''
        given a term, calculates its relative doc frequency, ie
        (# docs term in which term appears) / (# docs total in set)
        '''
        doc_frequency = 0
        for subset in self.subsets:
            for doc in subset:
                if term in doc.term_list:
                    doc_frequency += 1
        rel_frequency = doc_frequency / float(self.num_docs)
        return rel_frequency
    
    
    def calc_term_frequency(self, term, doc):
        '''
        given a term and a doc, calculates term's relative frequency
        in that doc, ie
        (# times term appears in doc) / (# total terms in doc)
        '''
        '''
        IMPLEMENTED IN DOCUMENT STORAGE CLASS
        '''
        pass
    
    
    def calc_tfidf_for_doc(self, term, doc):
        '''
        given a term and a doc, caluclates the tf-idf for the 
        term in that document.
        '''
        '''
        IMPLEMENTED IN DOCUMENT STORAGE CLASS
        '''
        pass
    
    
    def calc_tfidf_for_subset(self, term, subset):
        '''
        given a term and a subset, calculates the median tf-idf for
        the term in that subset -- ie the median of the tf-idf's for
        the term for each document in the subset.
        '''
        doc_freq = self.term_list[term]
        tfidf_list = []
        for doc in subset:
            new_tfidf = doc.calc_tfidf(term, doc_freq)
            tfidf_list.append(new_tfidf)
        mean_tfidf = mean(tfidf_list)
        # test output
        print "TFIDF LIST FOR TERM {0} : {1}".format(term, tfidf_list)
        print "MEAN TFIDF FOR TERM {0} : {1}".format(term, mean_tfidf)
        # /test output
        
        return mean_tfidf
    

    def save_weighted_list(self, weighted_list, output_path):
        # test output
        print "PATH: {0}".format(output_path)
        # /test output
        with open(output_path, 'w') as output_file:
            for pair in weighted_list:
                output_file.write(str(pair) + '\n')
        
        '''
        try:
            with open(self.output_filename, 'wb') as output_file:
                pickle.dump(self, output_file)
        except IOError: 
            print "An error occurred while pickling the document -- the output file may not be writable."
            raise IOError
        return True
        '''
    
    
        