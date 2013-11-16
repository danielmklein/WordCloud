from DocumentStorage import DocumentStorage
import os, os.path
import pickle
from nltk.stem.porter import PorterStemmer
from numpy import mean, median

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
        In other words, a list representing the full set of docs, broken
        into sublists, each representing a subset.
        '''
        self.set_subsets(set_of_docs)


    def set_subsets(self, set_of_docs):
        '''
        Updates the list of subsets to be analyzed.
        For every doc in set, create new DocumentStorage object from doc
        build list of all terms in entire set (build_full_term_list)
        '''
        self.subsets = set_of_docs
        self.num_docs = self.count_docs()
        self.subsets = self.convert_docs(self.subsets)
        self.term_list = self.build_full_term_list(self.subsets)
        
        
    def count_docs(self):
        '''
        Calculates the total number of docs in all subsets.
        '''
        num_docs = 0
        for subset in self.subsets:
            num_docs += len(subset)
        return num_docs
        
        
    def convert_docs(self, subsets):
        '''
        Transforms each doc in each subset into a DocumentStorage object,
        which makes them much easier to deal with as we perform our
        calculations.
        '''
        print "converting docs into DocumentStorage objects..."
        doc_num = 1
        converted_subsets = []
        for subset in subsets: 
            new_subset = []
            for doc in subset:
                #try:
                print ("converting doc {0} of {1} to Storage object..."
                       .format(doc_num, self.num_docs))
                doc_num += 1
                doc = DocumentStorage(doc.doc_metadata, doc.doc_text, 
                                  doc.output_filename)
                new_subset.append(doc)
                #except:
                #    raise Exception, "AnalysisEngine: The input seems to be of"\
                #        " the wrong type..."
            converted_subsets.append(new_subset)
        return converted_subsets
            
    
    def build_full_term_list(self, subsets):
        '''
        constructs a list of all terms used in the entire set along
        with each one's doc frequency
        '''
        print "building list of all terms in document set..."
        term_list = {}
        for subset in subsets:
            for doc in subset:
                new_terms = ([term for term in doc.term_list 
                             if term not in term_list])
                for term in new_terms:
                    term_list[term] = self.calc_doc_frequency(term)
        # test output
        #print "TERM LIST"
        #print term_list
        #print "END TERM LIST"
        # /test output
        return term_list
    
    
    def analyze_docs(self):
        '''
        Main method -- kicks off the analysis process.
        NOTE: The return structure of this method is a list of (output_filename, weighted_list) pairs.
        '''
        '''
        for each term:
            calculate_doc_frequency (performed in self.build_full_term_list)
            for each doc in set_of_docs:
                calc_term_frequency(term, doc)
        for each subset in set: (self.process_subset)
            for each term in subset:
                for each doc:
                    calculate tf-idf for term in doc (if term appears, else 0)
                calculate tf-idf for term in subset (median/mean)
            build, save, and return list of terms in subset sorted by tf-idf
        '''
        subset_lists = []
        for subset in self.subsets:
            print "processing subset {0}...".format(self.subsets.index(subset))
            weighted_terms = self.process_subset(subset)
            ##
            curdir = os.path.abspath(os.curdir)
            output_path = os.path.join(curdir, 
                                       weighted_terms[0] 
                                       + "_weighted_list.txt")
            ##
            subset_lists.append(weighted_terms)
            self.save_weighted_list(weighted_terms[1], output_path)
            
        return subset_lists
            
    
    def process_subset(self, subset, num_terms=50):
        '''
        Constructs the list of weighted terms.
        
        NOTE: output list must be of form [(term1,weight1),(term2,weight2),
        ...,(termn,weightn)]
        '''
        # build list of terms with their tf_idf weights
        raw_weighted_terms = []
        for term in self.term_list:
            tfidf = self.calc_tfidf_for_subset(term, subset)
            raw_weighted_terms.append((term, tfidf))
        raw_weighted_terms.sort(key=lambda pair: pair[1], reverse=True)
        # test output
        #print "INITIAL WEIGHTED TERMS: {0}".format(raw_weighted_terms)
        # /test output
        
        # scale the weights so that they are <= 1.0 (max weight == 1.0)
        weighted_terms = []
        # since list is reverse sorted, first element has highest weight
        scale_factor = raw_weighted_terms[0][1] 
        for pair in raw_weighted_terms[:num_terms+1]:
            weighted_terms.append((pair[0], pair[1] / scale_factor))
        # destem the terms in the weighted list  
        for i in range(0, len(weighted_terms)):
            cur_pair = weighted_terms[i]
            weighted_terms[i] = (self.destem(cur_pair[0]), cur_pair[1])
        # test output
        #print "SCALED WEIGHTED TERMS: {0}".format(weighted_terms)
        # /test output
        return (subset[0].output_filename, weighted_terms)
    
    
    def calc_doc_frequency(self, term):
        '''
        Given a term, calculates its relative doc frequency, ie
        (# docs term in which term appears) / (# docs total in set)
        '''
        doc_frequency = 0
        for subset in self.subsets:
            for doc in subset:
                if term in doc.term_list:
                    doc_frequency += 1
        rel_frequency = doc_frequency / float(self.num_docs)
        return rel_frequency
    
    
    def calc_tfidf_for_subset(self, term, subset):
        '''
        Given a term and a subset, calculates the characteristic tf-idf for
        the term in that subset -- ie the median of the tf-idf's for
        the term for each document in the subset.
        
        TODO: possibly switch this from mean to median
        '''
        doc_freq = self.term_list[term]
        tfidf_list = []
        for doc in subset:
            new_tfidf = doc.calc_tfidf(term, doc_freq)
            tfidf_list.append(new_tfidf)
        tfidf = mean(tfidf_list)
        #tfidf = median(tfidf_list)
        
        # test output
        #print "TFIDF LIST FOR TERM {0} : {1}".format(term, tfidf_list)
        #print "MEAN TFIDF FOR TERM {0} : {1}".format(term, tfidf)
        # /test output
        return tfidf
    

    def save_weighted_list(self, weighted_list, output_path):
        '''
        Saves a generated weighted_list to file in a readable format.
        '''
        # test output
        print "PATH: {0}".format(output_path)
        # /test output
        try:
            with open(output_path, 'w') as output_file:
                for pair in weighted_list:
                    output_file.write(str(pair) + '\n')
        except IOError:
            print "An error occurred while saving the subset "\
                    "to {0}...".format(output_path)
            raise IOError
        
        
    def destem(self, stemmed_term):
        '''
        Given a stemmed term, we look through the text of every document
        involved, determine the most common "parent" version of the 
        given stemmed term, and return it. 
        This process is very time-consuming with large document sets.
        '''
        print "Destemming term {0}".format(stemmed_term)
        candidates = {}
        stemmer = PorterStemmer()
        for subset in self.subsets:
            for doc in subset:
                for term in doc.split_text:
                    if stemmer.stem(term) == stemmed_term:
                        if term in candidates:
                            candidates[term] += 1
                        else:
                            candidates[term] = 1
        # test output
        #print candidates
        # /test output
        sorted_candidates = candidates.keys()
        sorted_candidates.sort(key=lambda 
                                term: candidates[term], reverse=True)
        destemmed_term = sorted_candidates[0]
        print "Term {0} destemmed to {1}".format(stemmed_term, destemmed_term)
        return destemmed_term

        