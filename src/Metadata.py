class Metadata():
    '''
    Metadata Class for Word Cloud Project
    
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.12.2013
    
    A metadata object will be a collection of fields (pieces of metadata) that 
    accompany of piece of data (in our case, the text of a document). We will 
    subclass this class for each type of document we use.
    '''


    def __init__(self):
        '''
        When I subclass this guy, I have to make sure the fields in the
        field_names list match the member variables.
        
        I need to think on the simplest/best way to do this whole thing.
        '''
        self.field_names = ["field1", "field2", "field3", "field4"]
        self.field1 = "test1"
        self.field2 = "test2"
        self.field3 = "test3"
        self.field4 = "test4"
    
    
    def print_fields(self):
        '''
        Display the list of fields in the metadata.
        '''
        print self.field_names
    
    
    def print_metadata(self):
        '''
        Display the fields and their values.
        '''
        print self
    
    
    def __str__(self):
        '''
        Convert the Metadata object to formatted string.
        Note that vars(self)[field_name] creates a member name out of
        "self." and a field_name, such as "self.field2".
        '''
        output_string = ""
        for field_name in self.field_names:
            output_string += field_name + ": "
            output_string += str(vars(self)[field_name]) 
            output_string += '\n'
        return output_string
        
        