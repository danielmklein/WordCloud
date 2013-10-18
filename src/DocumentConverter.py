import pickle
import re
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
        Returns a Document object.
        '''

        title = ""
        case_num = ""
        lexis_cite = ""
        full_cite = ""
        dates = []
        disposition = ""
        author = ""
        body_text = ""
        
        break_regex = re.compile(r"\* \* \* \* \* \* \* \*")
        found_break = False
        opinion_lines = []
        try:
            with(open(self.input_path, 'r')) as file_check:
                pass
        except:
            raise IOError
        with open(self.input_path, 'r') as opinion:
            for line in opinion:
                if found_break:
                    opinion_lines.append(line.strip('\n'))
                
                title_match = self.get_title(line)
                if title_match:
                    title = title_match
                    
                case_num_match = self.get_case_num(line)
                if case_num_match:
                    case_num = case_num_match
                    
                lexis_cite_match = self.get_lexis_cite(line)
                if lexis_cite_match:
                    lexis_cite = lexis_cite_match
                    
                full_cite_match = self.get_full_cite(line)
                if full_cite_match:
                    full_cite = full_cite_match
                    
                date_match = self.get_dates(line)
                if date_match:
                    dates = date_match
                    
                disposition_match = self.get_disposition(line)
                if disposition_match:
                    disposition = disposition_match
                
                if break_regex.match(line):
                    found_break = True
                    
        author = self.get_author(self.input_path)
        body_text = "\n".join(opinion_lines)
        # create metadata object 
        new_metadata = SupremeCourtOpinionMetadata()
        new_metadata.case_title = title
        new_metadata.case_num = case_num
        new_metadata.case_lexis_cite = lexis_cite
        new_metadata.case_full_cite = full_cite
        new_metadata.case_dates = dates
        new_metadata.case_disposition = disposition
        new_metadata.opinion_author = author
        
        self.converted_doc = Document(new_metadata, body_text, self.output_path)
        return self.converted_doc
        
        
    def save_converted_doc(self):
        '''
        '''
        # save Document object to file using appropriate Document method
        self.converted_doc.write_to_file()
    
    
    def get_author(self, file_path):
        author = ""
        author_regex = re.compile(r"([\w'\-]+)_\d{4} U.S. LEXIS")
        author_match = author_regex.search(file_path)
        if author_match:
            author = author_match.group(1)
        return author
    
    
    def get_title(self, line):
        title = ""
        title_regex = re.compile(r"TITLE: (.*)")
        title_match = title_regex.search(line)
        if title_match:
            title = title_match.group(1)
        return title
    
    
    def get_case_num(self, line):
        case_num = ""
        case_num_regex = re.compile(r"CASE NUMBER: (.*)")
        case_num_match = case_num_regex.search(line)
        if case_num_match:
            case_num = case_num_match.group(1)
        return case_num
    
    
    def get_lexis_cite(self, line):
        lexis_cite = ""
        lexis_cite_regex = re.compile(r"LEXIS CITATION: (.*)")
        lexis_cite_match = lexis_cite_regex.search(line)
        if lexis_cite_match:
            lexis_cite = lexis_cite_match.group(1)
        return lexis_cite
    
    
    def get_full_cite(self, line):
        full_cite = ""
        full_cite_regex = re.compile(r"FULL CITATION: (.*)")
        full_cite_match = full_cite_regex.search(line)
        if full_cite_match:
            full_cite = full_cite_match.group(1)
        return full_cite
    
    
    def get_dates(self, line):
        '''
        This method is kinda messy... I think it could definitely be simpler.
        '''
        dates = []
        datestring_regex = re.compile(r"\w+ \d{1,2}-?\d{1,2}?, \d{4}, \w+;")
        dateline_regex = re.compile(r"DATES: ")
        dateline_match = dateline_regex.search(line)
        
        raw_dates = []
        if dateline_match:
            raw_dates = datestring_regex.findall(line)
        
        grouped_date_regex = re.compile(r"(\w+ \d{1,2}-?\d{1,2}?, \d{4}), (\w+);")
        for raw_date in raw_dates:
            group_match = grouped_date_regex.search(raw_date)
            date = group_match.group(1)
            action = group_match.group(2)
            dates.append((date, action))           
        return dates
    
    
    def get_disposition(self, line):
        disposition = ""
        disposition_regex = re.compile(r"DISPOSITION: (.*)")
        disposition_match = disposition_regex.search(line)
        if disposition_match:
            disposition = disposition_match.group(1)
        return disposition
    
    
    
    
        