'''
Created 3.5.14
Daniel Klein

Old, now-unused methods from the AnalysisEngine class from the WordCloud project.
'''


def process_subset(self, subset, relevant_terms, num_terms=50):
    '''
    !!!!!!!NOTE: THIS METHOD IS NO LONGER USED!!!!!!

    Constructs the list of weighted terms.
    NOTE: output list must be of form [(term1,weight1),(term2,weight2),
    ...,(termn,weightn)]
    '''
    # build list of terms with their tf_idf weights
    raw_weighted_terms = []
    for term in relevant_terms:
        tfidf = self.calc_tfidf_for_subset(term, subset)
        raw_weighted_terms.append((term, tfidf))
    raw_weighted_terms.sort(key=lambda pair: pair[1], reverse=True)
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
    return (subset[0].output_filename, weighted_terms)


def destem(self, stemmed_term, subsets):
    '''
    !!!!THIS IS THE OLD VERSION OF THIS METHOD!!!!
    
    Given a stemmed term, we look through the text of every document
    involved, determine the most common "parent" version of the 
    given stemmed term, and return it. 
    '''
    candidates = {}
    stemmer = PorterStemmer()
    for subset in subsets:
        for doc in subset:
            for term in doc.split_text:
                if stemmer.stem(term) == stemmed_term:
                    if term in candidates:
                        candidates[term] += 1
                    else:
                        candidates[term] = 1
    sorted_candidates = candidates.keys()
    # sort potential destemmed versions by frequency in decreasing order
    sorted_candidates.sort(key = lambda 
                            term: candidates[term], reverse=True)
    destemmed_term = sorted_candidates[0]
    print "Destemmed: {0} --> {1}".format(stemmed_term, destemmed_term)
    return destemmed_term


