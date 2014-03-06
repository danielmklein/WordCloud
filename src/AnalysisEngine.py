from DocumentStorage import DocumentStorage
import os, os.path
from nltk.stem.porter import PorterStemmer
from numpy import mean
# from numpy import median

class AnalysisEngine(object):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
        
    Given a set of Documents (divided into subsets) (and perhaps analysis 
    parameters TBD), this class will perform natural language text processing 
    on the collection of documents and return a weighted list of the "most 
    important" terms in the collection. This utilizes term 
    frequency-inverse document frequency analysis as its basis for weighting 
    terms (http://en.wikipedia.org/wiki/Tf%E2%80%93idf).
    '''


    def __init__(self, corpus, subset):
        self.set_corpus(corpus)
        self.set_subset(subset)
        

    def set_corpus(self, corpus):
        '''
        Basic setup for the corpus list of documents.
        '''
        self.corpus = corpus
        self.num_docs = self.count_docs()
        self.corpus = self.convert_docs(self.corpus)
        self.term_list = self.build_full_term_list(self.corpus)
    
    
    def set_subset(self, subset):
        '''
        Basic setup for the subset list of documents.
        '''
        self.subset = subset
        self.subset = self.convert_docs(self.subset)
    

    def count_docs(self):
        '''
        Calculates the total number of docs in corpus.
        '''
        return len(self.corpus)
        
        
    def convert_docs(self, doc_set):
        '''
        Transforms each doc in a set into a DocumentStorage object,
        which makes them much easier to deal with as we perform our
        calculations.  
        '''
        print "Converting documents into DocumentStorage objects..."
        doc_num = 1
        num_docs = len(doc_set)
        converted_set = []
        for doc in doc_set:
            try:
                print ("Converting document {0} of {1} to Storage object..."
                       .format(doc_num, num_docs))
                doc_num += 1
                doc = DocumentStorage(doc.doc_metadata, doc.doc_text, 
                                  doc.output_filename)
                converted_set.append(doc)
            except:
                raise Exception("AnalysisEngine: The input seems to be of "
                                "the wrong type...")
        return converted_set
            
    
    def build_full_term_list(self, corpus):
        '''
        Constructs a list of all terms used in the entire corpus along
        with each term's doc frequency
        '''
        print "Building list of all terms in document corpus..."
        term_list = {}
        for doc in corpus:
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
    
    
    def get_most_freq_terms(self, corpus, num_terms):
        '''
        Given num_terms, compile list of all terms in corpus and return
        the num_terms most frequent terms (num_terms = 1000/5000/15000/etc)
        '''
        terms_with_freqs = {}
        for doc in corpus:
            for term in doc.stemmed_text:
                if term in terms_with_freqs:
                    terms_with_freqs[term] += 1
                else:
                    terms_with_freqs[term] = 1
        # sort terms in decreasing order by frequency
        term_list = sorted(terms_with_freqs.keys(), 
                           key = lambda 
                           term: terms_with_freqs[term], 
                           reverse=True)        
        return term_list[:num_terms]
    
    
    def determine_relevant_terms(self, corpus, term_list):
        '''
        Given corpus and list of terms, we get rid of the terms
        that appear in more than x% or less than y% of the opinions.
        '''
        upper_bound = 0.95
        lower_bound = 0.05
        relevant_terms = []
        # test output
        print "TOTAL NUM OF DOCS: {0}".format(self.num_docs)
        # /test output
        for term in term_list:
            doc_freq = 0
            for doc in corpus:
                # doc.term_list is filtered and stemmed
                if term in doc.term_list:
                    doc_freq += 1
            percentage_of_docs = doc_freq / float(self.num_docs)
            term_within_range = ((percentage_of_docs > lower_bound)
                                 and (percentage_of_docs < upper_bound))
            
            if term_within_range:
                relevant_terms.append(term)
            #print "TERM {0} appears in {1} docs; {2}% of all docs".format(term, doc_freq, percentage_of_docs)
        return relevant_terms
        

    def analyze_docs(self, num_relevant_terms=1000):
        '''
        Main method -- kicks off the analysis process.
        '''
        # determine which terms we care about
        most_freq_terms = self.get_most_freq_terms(self.corpus, 
                                                   num_relevant_terms)
        relevant_terms = self.determine_relevant_terms(self.corpus,
                                                       most_freq_terms)
        
        print "Analyzing subset against corpus..."
        raw_info = self.collect_term_info(self.subset, relevant_terms)
        weighted_terms = self.build_weighted_pairs(raw_info)
        #weighted_terms = self.process_subset(subset, relevant_terms)
        ##
        curdir = os.path.abspath(os.curdir)
        # TODO: if a subset is empty, the next line yields an error
        # there's gotta be a be a better way to choose a filename.
        output_path = os.path.join(curdir, 
                                   self.subset[0].output_filename 
                                   + "_weighted_list.txt")
        ##
        self.save_term_info(raw_info, output_path)
            
        return weighted_terms
            
            
    def collect_term_info(self, subset, relevant_terms, num_terms=50):
        '''
        Builds collection of info (weight, tf-idf, tf, df) for each term
        we care about. 
        '''
        # build initial list of info, set weight = tfidf for now
        raw_term_info = []
        for term in relevant_terms:
            tfidf = self.calc_tfidf_for_subset(term, subset)
            weight = tfidf
            doc_freq = self.term_list[term]
            term_freq = tfidf * doc_freq
            raw_term_info.append((term, weight, tfidf, term_freq, doc_freq))
        raw_term_info.sort(key=lambda info_set: info_set[1], reverse=True)
        
        # now scale the weight for each term so max weight == 1.0
        weighted_raw_terms = []
        scale_factor = raw_term_info[0][1]
        for info_set in raw_term_info[:num_terms]:
            destemmed_term = self.destem(info_set[0], self.corpus)
            #term = info_set[0]
            weight = info_set[1] / scale_factor
            tfidf = info_set[2]
            term_freq = info_set[3]
            doc_freq = info_set[4]
            weighted_raw_terms.append((destemmed_term, weight, tfidf, 
                                       term_freq, doc_freq))
            #weighted_raw_terms.append((term, weight, tfidf, tf,df))
            
        return weighted_raw_terms
    
    
    def build_weighted_pairs(self, raw_term_info):
        '''
        Extracts the term weight pairs (that the WordCloudGenerator needs)
        from our collection of term info.
        '''
        weighted_terms = []
        for info_set in raw_term_info:
            weighted_terms.append((info_set[0], info_set[1]))
        return weighted_terms
    
    
    def calc_doc_frequency(self, term):
        '''
        Given a term, calculates its relative doc frequency, ie
        (# docs term in which term appears) / (# docs total in corpus)
        '''
        doc_frequency = 0
        for doc in self.corpus:
            if term in doc.term_list:
                doc_frequency += 1
        rel_frequency = doc_frequency / float(self.num_docs)
        return rel_frequency
    
    
    def calc_tfidf_for_subset(self, term, subset):
        '''
        Given a term and a subset, calculates the characteristic tf-idf for
        the term in that subset -- ie the median of the tf-idf's for
        the term for each document in the subset.
        
        TODO: possibly switch this from mean to median??
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
    

    def save_term_info(self, raw_info, output_path):
        '''
        Saves a generated weighted_list to file in a readable format.
        '''
        # test output
        print "PATH: {0}".format(output_path)
        # /test output
        
        try:
            with open(output_path, 'w') as output_file:
                for info_set in raw_info:
                    output_string = self.build_output(info_set)
                    output_file.write(output_string + '\n')
        except IOError:
            print "An error occurred while saving the subset "\
                    "to {0}...".format(output_path)
            raise IOError
        
        
    def build_output(self, info_set):
        '''
        Constructs a line of term info to save to file.
        '''
        output_string = ""        
        term = info_set[0]
        weight = "{0:.4f}".format(info_set[1])
        tfidf = "{0:.4f}".format(info_set[2])
        term_freq = "{0:.4f}".format(info_set[3])
        doc_freq = "{0:.4f}".format(info_set[4])
        output_string += "["+ term +"]" 
        if len(term) > 5:
            output_string += "\tweight:" + weight
        else:
            output_string += "\t\tweight:" + weight
        output_string += "\ttfidf:" + tfidf + "\ttf:" + term_freq \
                        + "\tdf:" + doc_freq
        return output_string
    
    
    def destem(self, stemmed_term, corpus):
        '''
        Given a stemmed term, we look through the text of every document
        in corpus, determine the most common "parent" version of the 
        given stemmed term, and return it. 
        '''
        destemmed_term = ""
        min_num_terms = 5000
        min_percentage = 0.20
        candidates = {}
        stemmer = PorterStemmer()
        num_terms_checked = 0
        num_docs_checked = 0
        total_matches = 0
        
        for doc in corpus:
            # matches is the list of all term in the current text that are
            # "ancestor" versions of the stemmed term.
            matches = ([term for term in doc.split_text 
                        if stemmer.stem(term) == stemmed_term])
            num_terms_checked += len(doc.split_text)
            num_docs_checked += 1
            total_matches += len(matches)
            if not matches:
                continue
            # we keep a tally of the number of times each "ancestor"
            # appears in our text
            for match in matches:
                if match in candidates:
                    candidates[match] += 1
                else:
                    candidates[match] = 1
            # sort potential destemmed versions in descending order
            # by frequency
            sorted_candidates = sorted(candidates.keys(), 
                                       key=lambda 
                                       term: candidates[term], 
                                       reverse=True)
            if num_docs_checked == self.num_docs: 
                # we've run through every doc, so the most frequent 
                # ancestor of the stemmed term is the best destemmed 
                # result.
                destemmed_term = sorted_candidates[0]
                break
            # if we've reviewed enough total words, we can start trying
            # to find a suitable destemmed term from what we have so far 
            if min_num_terms <= num_terms_checked:
                # this is the most frequent ancestor of the stemmed term
                possible_match = sorted_candidates[0]
                test_percentage = candidates[possible_match] \
                                    / float(total_matches)
                # if the potential destemmed version accounts for a 
                # sufficient percentage of the total matches, we can
                # decide that it's a suitable destemmed result.
                if min_percentage <= test_percentage:
                    destemmed_term = possible_match
                    break
                
        print "Destemmed: {0} --> {1}".format(stemmed_term, destemmed_term)
        return destemmed_term

