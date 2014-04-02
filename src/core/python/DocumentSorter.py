class DocumentSorter(object):
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
    
    def __init__(self, doc_list=[]):
        self.doc_list = doc_list
        
        
    def sort_docs(self, sort_field):
        '''
        Given a sort_field on which to sort, this will return a list
        of lists of Document objects, grouped by sort_field value.
        '''
        for doc in self.doc_list:
            if not hasattr(doc, "doc_metadata"):
                print "A doc in doc_list doesn't have metadata, "\
                "so we can't sort on a metadata field!"
                raise Exception
            if not hasattr(doc.doc_metadata, sort_field):
                print "A doc in doc_list doesn't have the metadata field: "\
                "'{0}', so we can't sort on that field!".format(sort_field)
                raise Exception
        sorted_doc_list = sorted(self.doc_list, 
                        key=lambda doc: getattr(doc.doc_metadata, sort_field))
        
        # this splits the list into subsets -- all items in a subset have the
        # same value for the given sort_field
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
                subsets.append(sorted_doc_list[subset_start:])
        return subsets
    
    
    def create_subset(self, sort_field, allowed_values, should_invert=False):
        '''
        Given a sort field and a list of values to accept for that field,
        this will return a list of Document objects, each of whose value
        for the sort field is in the list of allowed_values.
        If shouldInvert=True, this will return the set of documents whose
        value for sort_field != anything in allowed_values.
        '''
        subset = []
        for doc in self.doc_list:
            if not hasattr(doc, "doc_metadata"):
                print "A doc in doc_list doesn't have metadata, "\
                "so we can't sort on a metadata field!"
                raise Exception
            if not hasattr(doc.doc_metadata, sort_field):
                print "A doc in doc_list doesn't have the metadata field: "\
                "'{0}', so we can't sort on that field!".format(sort_field)
                raise Exception
            
            # the handling of dates here is super duper messy right now...
            # TODO: this is going to need work in the future -- convert  
            # datestrings to datetime objects in DocumentConverter??
            
            # pick the items in the list whose value for the sort_field
            # matches something in allowed_values
            # exact match not necessary
            if not "dates" in sort_field:
                for value in allowed_values:
                    field_value = getattr(doc.doc_metadata, sort_field).upper()
                    if value.upper() in field_value:
                        subset.append(doc)
                        # if we hit a match, we break to avoid adding a doc
                        # to the subset multiple times.
                        break
            else: # the attribute is a string containing dates (this is dirty)
                # this code is redundant, but I want to remember that it might
                # change in the future, and keep it separate
                for value in allowed_values:
                    field_value = getattr(doc.doc_metadata, sort_field).upper()
                    if value.upper() in field_value:
                        subset.append(doc)
                        # if we hit a match, we break to avoid adding a doc
                        # to the subset multiple times.
                        break
        # TODO: potentially work this into the code above, though this way
        # of inverting is super simple and straightforward (but sometimes slow)
        if should_invert:
            return [doc for doc in self.doc_list if doc not in subset]
        else:
            return subset
    
    
    def add_doc(self, doc_to_add):
        '''
        Add a Document object to self.doc_list.
        '''
        if not hasattr(doc_to_add, "doc_metadata"):
            print "It appears that the object to add isn't a "\
            "Document object!"
            raise Exception
        self.doc_list.append(doc_to_add)
    
    
    