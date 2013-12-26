from Document import Document
from SuperDocument import SuperDocument

class SuperDocGenerator():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    Given a list of Document objects, this class will combine the text of the
    documents into one text and the respective Metadata objects into a list of
    Metadata objects.
    '''


    def __init__(self, output_path, doc_list = []):
        '''
        Constructor
        '''
        self.doc_list = doc_list
        self.output_path = output_path
        
    
    def create_superdoc(self):
        '''
        Takes all the Documents in the doc_list and creates from them
        a SuperDocument object containing all of their text and all of
        their respective Metadata objects.
        '''
        for doc in self.doc_list:
            if not (hasattr(doc, "doc_metadata") and hasattr(doc, "doc_text")):
                print "Found an object in doc_list that isn't a Document!"
                raise Exception
        if len(self.doc_list) < 1:
            print "doc_list must contain at least 1 Document in order to "\
                    "create a SuperDocument!"
            raise Exception
        
        new_metadata = [doc.doc_metadata for doc in self.doc_list]
        new_text = "".join([doc.doc_text for doc in self.doc_list])
        self.new_superdoc = SuperDocument(new_metadata, new_text, self.output_path)
        return self.new_superdoc
    
    
    def add_doc(self, doc_to_add):
        '''
        Adds a Document object to the list of Documents to go into the
        created SuperDocument
        '''
        if not (hasattr(doc_to_add, "doc_metadata") 
                and hasattr(doc_to_add, "doc_text")):
            print "The object to add is not a Document object!"
            raise Exception
        self.doc_list.append(doc_to_add)
    
    
    def save_generated_superdoc(self):
        '''
        Uses the created SuperDocument's method to save it to file.
        '''
        self.new_superdoc.write_to_file()
    
    
        