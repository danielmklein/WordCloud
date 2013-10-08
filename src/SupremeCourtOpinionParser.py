'''
Supreme Court Opinion parser for Word Cloud project.

Daniel Klein
The University of Alabama
Computer-Based Honors Program
10.06.2013

'''
import re
import glob
import os, os.path


class SupremeCourtOpinionParser():

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
		# test output
		print source_file_path
		# /test output
		with open(source_file_path, 'r') as opinion_file:
			self.all_opinions = opinion_file.readlines()

		delimiter = self.get_delimiter()
		# TODO: DO SOMETHING IF DELIMITER IS STILL NONE
		# test output
		print "Delimiter is: {0}".format(delimiter)
		# /test output
		completion_message_line = self.remove_bracket_nums()
		del self.file_text[completion_message_line :]

		self.cases = self.split_into_cases(delimiter)
		# test output
		print "there are perhaps {0} cases in this file?".format(len(self.cases))
		# /test output
		'''
		file_names = ["foo.txt", "bar.txt", "lol.txt", "test.txt", "boom.txt"]
		for i in range(0, len(file_names)):
			with open(os.path.join(self.output_dir, file_names[i]), 'w') as output:
				output.write('\n'.join(cases[i]))
		'''
		for case in self.cases:
			self.parse_case(case)
		
	

	def parse_case(self, case):
		'''
		This parses a string containing all opinions for one case and
		splits each opinion into its own string. 
		'''
		blank_line_regex = re.compile("\n{2,10}")

		cite_found = False
		case = "\n".join(case)
		case_paragraphs = blank_line_regex.split(case)
		num_paragraphs = len(case_paragraphs)
		# find the lexis citation
		lexis_regex = re.compile("U.S.\n?\s*LEXIS")
		for paragraph in case_paragraphs:
			if lexis_regex.search(paragraph):
				lexis_citation = self.get_citation(paragraph)
				break






	def parse_opinion(self):
		'''
		This parses a string containing an opinion and writes the opinion
		to a file with all the necessary metadata.
		'''
		pass


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


	def get_citation(self, paragraph):			
		cite_paragraph = paragraph.split()
		for index in range(0, len(cite_paragraph)):
			if re.match("LEXIS", cite_paragraph[index]):
				lexis_cite = cite_paragraph[index - 2:index + 2]
				lexis_cite = " ".join(lexis_cite).strip(";")
				# test output
				#print lexis_cite
				# /test output
				return lexis_cite


	def remove_bracket_nums(self):
		'''
		This method removes all instances of bracketed numbers from the
		opinion file, as they are unnecessary for our purposes.
		'''
		# take out all the bracketed numbers in the file
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
		del self.file_text[:2] # get rid of the inital delimiter line

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




def main():
	
	source_dir = r"C:\Users\Daniel\Dropbox\Class_files\CBH_301\Word_Cloud\supreme_court_opinions\test"
	output_dir = r"C:\Users\Daniel\Dropbox\Class_files\CBH_301\Word_Cloud\supreme_court_opinions\test_output"
	parser = SupremeCourtOpinionParser(output_dir)
	print "Beginning to parse files in {0}".format(source_dir)
	for opinion_file in os.listdir(source_dir):
		# test output
		print opinion_file
		# /test output

		full_path = os.path.join(source_dir, opinion_file)

		# test output
		print "Parsing {0}".format(full_path)
		# /test output
		parser.parse_file(full_path)
		


main()




