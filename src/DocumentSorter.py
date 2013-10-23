class DocumentSorter():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    Given a collection of document objects and a sort key (which is a field of
    the appropriate metadata object), this will yield subsets of document 
    objects, each subset having the same value for the sort field (subsets will
    be returned as a dictionary?).
    '''


    def __init__(self, doc_list = []):
        '''
        Constructor
        '''
        self.doc_list = doc_list
        
        
    def sort_docs(self, sort_field):
        '''
        this method is messy... I think it could be done a lot more elegantly.
        also I need to update the way I check the subsets -- need to check the
        value of the sort_field in each object in each subset, not for 
        object equality.
        '''
        for doc in self.doc_list:
            if not hasattr(doc, "doc_metadata"):
                print "A doc in doc_list doesn't have metadata, "\
                "so we can't sort on a metadata field!".format(sort_field)
                raise Exception
            if not hasattr(doc.doc_metadata, sort_field):
                print "A doc in doc_list doesn't have the metadata field: "\
                "'{0}', so we can't sort on that field!".format(sort_field)
                raise Exception
            
        sorted_doc_list = sorted(self.doc_list, 
                        key = lambda doc:getattr(doc.doc_metadata, sort_field))
        subsets = []
        subset_start = 0
        for i in range(1, len(sorted_doc_list)):
            prev_doc_field = getattr(sorted_doc_list[i-1].doc_metadata, 
                                     sort_field)
            curr_doc_field = getattr(sorted_doc_list[i].doc_metadata, 
                                     sort_field)
            if prev_doc_field != curr_doc_field:
                subsets.append(sorted_doc_list[subset_start : i])
                subset_start = i
            if i == len(sorted_doc_list) - 1:
                subsets.append([sorted_doc_list[i]])
        # test output
        print "here are the subsets: {0}".format(subsets)
        # /test output
        return subsets
    
    def create_subset(self, sort_field, allowed_values):
        pass
    
    
    def print_subsets(self):
        pass
    
    
    def add_doc(self, doc_to_add):
        '''
        Should I assert that doc_to_add has doc_metadata attribute?
        '''
        pass
    
    
    