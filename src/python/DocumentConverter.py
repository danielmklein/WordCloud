class DocumentConverter(object):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    Given a file containing one and only one document (along with
    fields/labels/metadata), this class will parse the file and create a 
    Document object from the file.
    '''

    def __init__(self, file_to_parse, pickle_path):
        '''
        Constructor
        '''
        self.input_path = file_to_parse
        self.output_path = pickle_path
        self.converted_doc = None
    
    
    def convert_file(self):
        '''
        This needs to be overriden in a descendant class.
        '''
        pass
        
        
    def save_converted_doc(self):
        '''
        Save Document object to file using appropriate Document method
        '''
        self.converted_doc.write_to_file()
    
    
    def get_titled_item(self, line, item_regex):
        '''
        This generic helping method parses info out of any line that starts 
        with <TITLE>:.
        '''
        item = ""
        item_match = item_regex.search(line)
        if item_match:
            item = item_match.group(1)
        return item
    



