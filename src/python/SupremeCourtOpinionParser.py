'''
Supreme Court Opinion parser for Word Cloud project.

Daniel Klein
The University of Alabama
Computer-Based Honors Program
10.06.2013

This script, given a directory containing text files of Supreme Court
cases from Lexis, will parse each file in the directory to extract the
cases, then parse each case to extract the opinions therein. The script
will then write each opinion to file, along with key information about
the corresponding case.

This code is adapted from a piece of code written by my research
advisor, Dr. Joseph Smith. The basic ideas and algorithms are his --
I merely translated them into a more modularized, object-oriented form.
'''
import re
import os, os.path
from src.core.python.WordCloudConstants import *


class SupremeCourtOpinionParser(object):

    def __init__(self, output_dir):
        self.output_dir = output_dir


    def parse_file(self, source_file_path):
        '''
        This parses a file containing cases and splits each
        case into its own string.
        Returns a list of strings, each string containing the opinions
        for one case.
        '''
        print "Parsing file {0}".format(source_file_path)
        
        self.file_text = []
        with open(source_file_path, 'r') as opinion_file:
            self.all_opinions = opinion_file.readlines()
        delimiter = self.get_delimiter()
        # TODO: DO SOMETHING IF DELIMITER IS STILL NONE
        # test output
        print "Delimiter is: {0}".format(delimiter)
        # /test output
        completion_message_line = self.remove_bracket_nums()
        del self.file_text[completion_message_line + 1:]

        self.cases = self.split_into_cases(delimiter)
        for case in self.cases:
            self.parse_case(case)
        
    
    def parse_case(self, case):
        '''
        This parses a string containing all opinions for one case and
        splits each opinion into its own string. 
        '''
        blank_line_regex = re.compile("\n{2,10}")
        alt_opinion_regex = re.compile(r"CONCUR BY|DISSENT")

        #cite_found = False
        maj_start_found = False
        alt_opinions_found = False
        maj_author = ""

        case = "\n".join(case)
        case_paragraphs = blank_line_regex.split(case)
        case_paragraphs = [re.sub('\xa0', '', paragraph) \
						  for paragraph in case_paragraphs]
        case_paragraphs = [re.sub('\n', ' ', paragraph) \
						  for paragraph in case_paragraphs]
        #num_paragraphs = len(case_paragraphs)
        # find the lexis citation
        #lexis_regex = re.compile("U.S.\n?\s*LEXIS")
        for index in range(0, len(case_paragraphs)):
            current_paragraph = case_paragraphs[index]
            if re.match("OPINION$", current_paragraph) and not maj_start_found:
                case_header = ([re.sub(r'[\n]', ' ', line) 
                            for line in case_paragraphs[: index - 1]])
                # test output
                #print "RAW: {0}".format(case_header)
                # /test output
                # this filters out this fishy character
                case_header = [re.sub(r'[\xa0]', '', line) for line in case_header]
                maj_start_index = index
                maj_end_index = len(case_paragraphs) - 1
                maj_start_found = True
                
            if re.match("OPINION BY:", current_paragraph):
                maj_author = " ".join([word 
                                for word in current_paragraph.split()[2:]
                                if "JUSTICE" not in word and "Justice" not in word])

            if re.search(alt_opinion_regex, current_paragraph) and maj_start_found:
                maj_end_index = index - 1
                #alt_start_index = index
                alt_opinions_found = True
                break
            
        if alt_opinions_found:
            self.parse_alt_opinions(case_paragraphs[index:], case_header)

        maj_opinion = case_paragraphs[maj_start_index:maj_end_index]
        if maj_author == "":
            maj_author = "PER CURIAM"

        opinion_with_type = ("majority", "\n".join(maj_opinion))
        self.write_opinion(opinion_with_type, maj_author, case_header)


    def parse_alt_opinions(self, alt_opinions, case_header):
        '''
        This parses the concurring and dissenting opinions for a case.
        '''
        # test output
        #print alt_opinions[:5]
        # /test output
        concur_start_regex = re.compile(r"(JUSTICE|Justice)\s[\w'-]+,[^\.]*\sconcurring")
        dissent_start_regex = re.compile(r"(JUSTICE|Justice)\s[\w'-]+,[^\.]*\sdissenting")
        alt_opinion_regex = re.compile(r"CONCUR BY|DISSENT")
        justice_regex = re.compile(r"(JUSTICE|Justice|MR. JUSTICE|Mr. Justice)\s[\w'-]*\.")
        alt_start_indices = []

        for index in range(0, len(alt_opinions)):
            current_paragraph = alt_opinions[index]
            if ((re.search(concur_start_regex, current_paragraph) 
                or re.search(dissent_start_regex, current_paragraph)
                or re.search(alt_opinion_regex, current_paragraph)
                or re.match(justice_regex, current_paragraph)) 
                and not "Footnotes" in current_paragraph):
                if (len(alt_start_indices) == 0) or (index > alt_start_indices[-1] + 2):
                    alt_start_indices.append(index)
        
        start_end_pairs = []
        if len(alt_start_indices) == 1:
            start_end_pairs = [(0, len(alt_opinions) - 1)]
        else:
            for i in range(0, len(alt_start_indices)):
                if i == len(alt_start_indices) - 1:
                    start_end_pairs.append(
                        (alt_start_indices[i], len(alt_opinions) - 1))
                    break
                else:
                    start_end_pairs.append(
                        (alt_start_indices[i], alt_start_indices[i+1] - 1))
        
        split_alt_opinions = []
        for index in range(0, len(start_end_pairs)):
            current_pair = start_end_pairs[index]
            if current_pair[0] == current_pair[1]:
                start_end_pairs[index + 1] = (current_pair[0], 
											start_end_pairs[index + 1][1])
                continue
            else:
                opinion_string = "\n".join(alt_opinions[current_pair[0]:current_pair[1]])
                split_alt_opinions.append(opinion_string)
    
        categorized_opinions = self.categorize_opinions(split_alt_opinions)
        
        for opinion in categorized_opinions:
            opinion_author = self.get_author(opinion)
            self.write_opinion(opinion, opinion_author, case_header)


    def get_delimiter(self):
        '''
        This method figures out the delimiter that separates opinions.
        This delimiter is typically of the form "of XXX DOCUMENTS"
        '''
        delimiter_regex = re.compile(r"of \d+ DOCUMENTS")
        delimiter = None
        for line in self.all_opinions:
            delimiter_match = delimiter_regex.search(line)
            if delimiter_match is not None:
                break
        delimiter = delimiter_match.group()
        return delimiter


    def remove_bracket_nums(self):
        '''
        This method removes all instances of bracketed numbers from the
        opinion file, as they are unnecessary for our purposes.
        '''
        bracket_regex = re.compile("\[\*+\w*\d*\]")
        completion_regex = re.compile("\*+\sPrint\sCompleted\s\*+")
        for index in range(0, len(self.all_opinions)):
            current_line = self.all_opinions[index]
            split_line = current_line.split()
            list_copy = split_line[:]
            for word in list_copy:
                if re.match(bracket_regex, word):
                    split_line.remove(word)
            current_line = " ".join(split_line)
            if re.search(completion_regex, current_line):
                completion_message_line = index
            self.file_text.append(current_line)
        return completion_message_line


    def split_into_cases(self, delimiter):
        '''
        This method divides the file into individual cases by splitting on 
        the delimiter.
        '''
        cases = []
        delimiter_regex = re.compile(delimiter)
        del self.file_text[:2] # get rid of the initial delimiter line

        start_index = 0
        for index in range(2, len(self.file_text)):
            if delimiter_regex.search(self.file_text[index]):
                matched_case = self.file_text[start_index : index]
                cases.append(matched_case)
                start_index = index + 1
            else:
                index += 1
            if index == len(self.file_text) - 1:
                matched_case = self.file_text[start_index : index]
                cases.append(matched_case)
        return cases


    def categorize_opinions(self, split_alt_opinions):
        '''
        Given a list of non-majority opinions, this determines whether
        each on is concurring, dissenting, or both.
        This returns a list of tuples of the form (<opinion-type>,<opinion-text>)
        '''
        categorized_opinions = []
        #concur_regex = re.compile(r"((JUSTICE|Justice)\s[\w'-]+,.*\sconcurring)|concur")
        #dissent_regex = re.compile(r"((JUSTICE|Justice)\s[\w'-]+,.*\sdissenting)|dissent")
        concur_regex = re.compile(r"concur|CONCUR")
        dissent_regex = re.compile(r"dissent|DISSENT")

        for index in range(0, len(split_alt_opinions)):
            is_concur = False
            is_dissent = False
            #opinion_lines = split_alt_opinions[index][:50].split("\n")
            opinion_sample = " ".join(split_alt_opinions[index].split("\n")[:2])
            # test output
            print " * * * * * * ** "
            #print opinion_lines[:10]
            print "HERE IS OPINION SAMPLE"
            print opinion_sample
            print " * * * * * * ** "
            # /test output
            if re.search(concur_regex, opinion_sample):
                is_concur = True
            if re.search(dissent_regex, opinion_sample):
                is_dissent = True
                
            if is_concur and is_dissent:
                opinion_type = "concur-dissent"
            elif is_concur:
                opinion_type = "concur"
            else:
                opinion_type = "dissent"

            categorized_opinions.append((opinion_type, 
                                    split_alt_opinions[index]))
        return categorized_opinions


    def get_author(self, opinion):
        '''
        Given a non-majority opinion, this method returns its author.
        '''
        opinion_author = "NONE"
        author_found = False
        for paragraph in opinion[1].split("\n")[:10]:
            paragraph_words = paragraph.split()
            author_sample = [re.sub(r'\xa0', '', word) for word in paragraph_words]
            author_sample = [word for word in author_sample if word is not '']

            if (len(paragraph_words) >= 2) \
            and (re.search(re.compile(r"(JUSTICE|Justice)"), " ".join(author_sample))) \
            or (re.search(re.compile(r"CONCUR BY"), " ".join(author_sample))) \
            or (re.search(re.compile(r"DISSENT BY"), " ".join(author_sample))):
                # test output
                #print "***********************"
                #print "HERE IS AUTHOR_SAMPLE"
                #print author_sample
                #print "***********************"
                # /test output
                if re.match("THE CHIEF JUSTICE", " ".join(author_sample).strip()) \
                or re.match("MR. CHIEF JUSTICE", " ".join(author_sample).strip()) \
                or re.match("CHIEF JUSTICE", " ".join(author_sample).strip()):
                    opinion_author = "CHIEF"
                    author_found = True
                    break
                elif re.match("CONCUR BY", " ".join(author_sample).strip()) \
                or re.match("DISSENT BY", " ".join(author_sample).strip()):
                    for i in range(len(author_sample)):
                        if re.search(r"BY", author_sample[i]):
                            opinion_author = author_sample[i + 1].strip(",.;")
                            author_found = True
                            break
                else:
                    for i in range(len(author_sample)):
                        if re.search(re.compile(r"(JUSTICE|Justice)"), 
									author_sample[i]) \
                        or re.search(re.compile(r"(MR. JUSTICE|Mr. Justice)"), 
									author_sample[i]):
                            opinion_author = author_sample[i + 1].strip(",.;")
                            author_found = True
                            break
            if author_found:
                break

        return opinion_author


    def write_opinion(self, opinion_with_type, opinion_author, case_header):
        '''
        Given the key info about an opinion, this writes it to file.
        '''
        (title, case_num, full_citation, us_citation, 
        supr_court_citation, lawyers_ed_citation, lexis_citation,
        dates, disposition) = self.get_info(case_header)

        opinion_filename = opinion_author + "_" + lexis_citation + ".txt"
        output_dir = self.output_dir
        output_path = os.path.join(output_dir, opinion_filename)
        # test output
        print "filename is: {0}".format(opinion_filename)
        print "output path is: {0}".format(output_path)
        # /test output
        
        with open(output_path, 'w') as output_file:
            output_file.write("TITLE: {0}\n".format(title))
            output_file.write("CASE NUMBER: {0}\n".format(case_num))
            output_file.write("US CITATION: {0}\n".format(us_citation))
            output_file.write("SUPREME COURT CITATION: {0}\n".format(
                                                        supr_court_citation))
            output_file.write("LAWYERS ED CITATION: {0}\n".format(
                                                        lawyers_ed_citation))
            output_file.write("LEXIS CITATION: {0}\n".format(lexis_citation))
            output_file.write("FULL CITATION: {0}\n".format(full_citation))
            date_string = "DATES: "
            for date in dates:
                date_string += date + ";"
            output_file.write(date_string + "\n")
            output_file.write("DISPOSITION: {0}\n".format(disposition))
            output_file.write("OPINION TYPE: {0}".format(opinion_with_type[0]))
            output_file.write("\n* * * * * * * *\n")
            output_file.write(opinion_with_type[1])
            
        
    def get_info(self, case_header):
        '''
        Given the header of a case, this parses out the important
        information and returns a tuple containing that information.
        '''
        # test output
        print case_header
        # /test output
        joined_header = " ".join(case_header)
        # these might not be exactly right... check them!!
        title = case_header[0].strip() 
        case_num = case_header[1].strip()
        full_citation = case_header[3].strip()
        lexis_citation = self.get_lexis_cite(joined_header)
        us_citation = self.get_us_cite(full_citation)
        lawyers_ed_citation = self.get_lawyers_ed_cite(full_citation)
        supr_court_citation = self.get_supr_court_cite(full_citation)
        
        dates = []
        date_regex = re.compile(r"\w+\s\d{1,2}-?\d?\d?,\s\d{4},\s\w+")
        for line in case_header:
            dates = dates + date_regex.findall(line)

        disposition_regex = re.compile(r"DISPOSITION:(.*)")
        disposition_match = disposition_regex.search(joined_header)
        if disposition_match:
            disposition = disposition_match.group(1).strip()
        else:
            disposition = "NONE"
        return (title, case_num, full_citation, us_citation, 
                supr_court_citation, lawyers_ed_citation, lexis_citation,
                 dates, disposition)
        
        
    def get_lexis_cite(self, paragraph):
        '''
        This method parses the US LEXIS citation out of a paragraph.
        '''    
        cite_paragraph = paragraph.split()
        for index in range(0, len(cite_paragraph)):
            if re.match("LEXIS", cite_paragraph[index]):
                lexis_cite = cite_paragraph[index - 2:index + 2]
                lexis_cite = " ".join(lexis_cite).strip(";")
                return lexis_cite
        return "NONE"
    
    
    def get_us_cite(self, citation_string):
        us_cite_regex = re.compile(r"\d+\sU\.S\.\s\d+;")
        us_cite_match = us_cite_regex.search(citation_string)
        if us_cite_match:
            return us_cite_match.group().strip(";")
        else:
            return "NONE"
        
    def get_lawyers_ed_cite(self, citation_string):
        led_regex = re.compile(r"\d+\sL\.\sEd\.\s2?d?\s?\d+;")
        led_match = led_regex.search(citation_string)
        if led_match:
            return led_match.group().strip(";")
        else:
            return "NONE"

    
    def get_supr_court_cite(self, citation_string):
        sct_regex = re.compile(r"\d+\sS\.\sCt\.\s\d+;")
        sct_match = sct_regex.search(citation_string)
        if sct_match:
            return sct_match.group().strip(";")
        else:
            return "NONE"


def main():
    source_dir = LEXIS_FILE_PATH
    output_dir = OPINION_OUTPUT_PATH

    parser = SupremeCourtOpinionParser(output_dir)
    print "Beginning to parse files in {0}".format(source_dir)
    for opinion_file in os.listdir(source_dir):
        full_path = os.path.join(source_dir, opinion_file)
        if os.path.isfile(full_path):
            parser.parse_file(full_path)
        

main()
