import pickle
import re
import os, os.path
from Document import Document
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata


class DocumentConverter():
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
    
    
    def convert_file(self):
        '''
        Returns a Document object created from file.
        '''
        # check to make sure the input file exists
        if not os.path.exists(self.input_path):
            raise IOError, "The path {0} does not exist!".format(self.input_path)
        # and check to be sure it's a txt file
        txtfile_regex = re.compile(r"\.txt$")
        if not re.search(txtfile_regex, self.input_path):
            raise IOError, ("The file {0} is not a text file and thus cannot "
                            "be converted.".format(self.input_path)) 
        
        title = ""
        case_num = ""
        us_cite = ""
        supreme_court_cite = ""
        lawyers_ed_cite = ""
        lexis_cite = ""
        full_cite = ""
        dates = []
        disposition = ""
        author = ""
        opinion_type = ""
        body_text = ""
        
        break_regex = re.compile(r"\* \* \* \* \* \* \* \*")
        found_break = False
        opinion_lines = []
        
        title_regex = re.compile(r"TITLE: (.*)")
        case_num_regex = re.compile(r"CASE NUMBER: (.*)")
        us_cite_regex = re.compile(r"US CITATION: (.*)")
        supreme_court_regex = re.compile(r"SUPREME COURT CITATION: (.*)")
        lawyers_ed_regex = re.compile(r"LAWYERS ED CITATION: (.*)")
        lexis_cite_regex = re.compile(r"LEXIS CITATION: (.*)")
        full_cite_regex = re.compile(r"FULL CITATION: (.*)")
        dateline_regex = re.compile(r"DATES: (.*)")
        disposition_regex = re.compile(r"DISPOSITION: (.*)")
        opinion_type_regex = re.compile(r"OPINION TYPE: (.*)")
        
        # parse out all of the necessary fields
        with open(self.input_path, 'r') as opinion:
            for line in opinion:
                # this means we are in the body of the text and we should
                # stop parsing fields 
                if found_break:
                    opinion_lines.append(line.strip('\n'))
                
                title_match = self.get_titled_item(line, title_regex)
                if title_match:
                    title = title_match
                    
                case_num_match = self.get_titled_item(line, case_num_regex)
                if case_num_match:
                    case_num = case_num_match
                    
                us_cite_match = self.get_titled_item(line, us_cite_regex)
                if us_cite_match:
                    us_cite = us_cite_match
                    
                supr_court_cite_match = self.get_titled_item(line, 
                                                        supreme_court_regex)
                if supr_court_cite_match:
                    supreme_court_cite = supr_court_cite_match
                    
                lawyers_ed_cite_match = self.get_titled_item(line, 
                                                             lawyers_ed_regex)
                if lawyers_ed_cite_match:
                    lawyers_ed_cite = lawyers_ed_cite_match
                    
                lexis_cite_match = self.get_titled_item(line, lexis_cite_regex)
                if lexis_cite_match:
                    lexis_cite = lexis_cite_match
                    
                full_cite_match = self.get_titled_item(line, full_cite_regex)
                if full_cite_match:
                    full_cite = full_cite_match
                    
                date_match = self.get_titled_item(line, dateline_regex)
                if date_match:
                    dates = self.split_dates(date_match)
                    
                disposition_match = self.get_titled_item(line, 
                                                         disposition_regex)
                if disposition_match:
                    disposition = disposition_match
                    
                opin_type_match = self.get_titled_item(line, 
                                                       opinion_type_regex)
                if opin_type_match:
                    opinion_type = opin_type_match
                
                if break_regex.match(line):
                    found_break = True
                    
        author = self.get_author(self.input_path)
        body_text = "\n".join(opinion_lines)
        # create metadata object 
        new_metadata = SupremeCourtOpinionMetadata()
        new_metadata.case_title = title
        new_metadata.case_num = case_num
        new_metadata.case_us_cite = us_cite
        new_metadata.case_supreme_court_cite = supreme_court_cite
        new_metadata.case_lawyers_ed_cite = lawyers_ed_cite
        new_metadata.case_lexis_cite = lexis_cite
        new_metadata.case_full_cite = full_cite
        new_metadata.case_dates = dates
        new_metadata.case_disposition = disposition
        new_metadata.opinion_author = author
        new_metadata.opinion_type = opinion_type
        # tie the entire new Document together and return it
        self.converted_doc = Document(new_metadata, body_text, 
                                      self.output_path)
        return self.converted_doc
        
        
    def save_converted_doc(self):
        '''
        Save Document object to file using appropriate Document method
        '''
        self.converted_doc.write_to_file()
    
    
    def get_author(self, file_path):
        '''
        Parses the author out of the filename.
        '''
        author = ""
        author_regex = re.compile(r"([\w'\- ]+)_\d{4} U.S. LEXIS")
        author_match = author_regex.search(file_path)
        if author_match:
            author = author_match.group(1)
        return author
    
    
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
    

    def split_dates(self, date_string):
        '''
        Pulls the individual dates out of the dates line.
        '''
        # TODO: convert datestrings into datetime objects
        dates = []
        datestring_regex = re.compile(r"\w+\s\d{1,2}-?\d?\d?,\s\d{4},\s\w+;")
        raw_dates = datestring_regex.findall(date_string)
        
        grouped_date_regex = re.compile(
                            r"(\w+\s\d{1,2}-?\d?\d?,\s\d{4}),\s(\w+);")
        for raw_date in raw_dates:
            group_match = grouped_date_regex.search(raw_date)
            date = group_match.group(1)
            action = group_match.group(2)
            date_string = date + ' (' + action + ')'
            #dates.append((date, action))
            dates.append(date_string)           
        return dates
        
        