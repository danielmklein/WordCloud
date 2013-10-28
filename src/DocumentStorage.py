from Document import Document

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
        self.term_list = self.build_term_list()
        
        
    def build_term_list(self):
        '''
        build term list of form 
        [(term1, 0), (term2, 0), ... , (termn, 0)]
        '''
        self.term_list = []
        return self.term_list
        
        