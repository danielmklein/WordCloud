'''
Supreme Court Opinion parser for Word Cloud project.

Daniel Klein
The University of Alabama
Computer-Based Honors Program
10.06.2013


What stuff do I want to explicitly save (like a record) in each opinion file?

case title
lexis citation
date/year
disposition
opinion type
opinion author

'''
import re
import glob
import os, os.path


class SupremeCourtOpinionParser():

	def __init__(self, output_dir):
		self.output_dir = output_dir
		self.majority_dir = os.path.join(output_dir, "majority")
		self.dissent_dir = os.path.join(output_dir, "dissenting")
		self.concur_dir = os.path.join(output_dir, "concurring")
		self.concur_dissent_dir = os.path.join(output_dir, "concur-dissent")


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
		'''
		file_names = ["foo.txt", "bar.txt", "lol.txt", "test.txt", "boom.txt"]
		for i in range(0, len(file_names)):
			with open(os.path.join(self.output_dir, file_names[i]), 'w') as output:
				output.write('\n'.join(cases[i]))
		'''
		# /test output
		for case in self.cases[:5]:
			self.parse_case(case)
		
	
	def parse_case(self, case):
		'''
		This parses a string containing all opinions for one case and
		splits each opinion into its own string. 
		'''
		blank_line_regex = re.compile("\n{2,10}")
		alt_opinion_regex = re.compile(r"CONCUR BY|DISSENT")

		cite_found = False
		maj_start_found = False
		alt_opinions_found = False

		case = "\n".join(case)
		case_paragraphs = blank_line_regex.split(case)
		num_paragraphs = len(case_paragraphs)
		# find the lexis citation
		lexis_regex = re.compile("U.S.\n?\s*LEXIS")
		for index in range(0, len(case_paragraphs)):
			current_paragraph = case_paragraphs[index]
			if lexis_regex.search(current_paragraph):
				lexis_citation = self.get_citation(current_paragraph)
				
			if re.match("OPINION$", current_paragraph) and not maj_start_found:
				case_header = case_paragraphs[: index - 1]
				# test output
				#print "\n".join(case_header)
				# /test output
				maj_start_index = index
				maj_end_index = len(case_paragraphs) - 1
				maj_start_found = True

			if re.match("OPINION BY:", current_paragraph):
				maj_author = " ".join(current_paragraph.split()[2:])
				# test output
				#print "majority author is: {0}".format(maj_author)
				# /test output

			if re.match(alt_opinion_regex, current_paragraph):
				maj_end_index = index - 1
				alt_start_index = index
				alt_opinions_found = True
				break
		if alt_opinions_found:
			self.parse_alt_opinions(case_paragraphs[index:], case_header, lexis_citation)

		maj_opinion = case_paragraphs[maj_start_index:maj_end_index]
	
		output_filename = maj_author + "_" + lexis_citation + ".txt"
		with open(os.path.join(self.majority_dir, output_filename), 'w') as opinion_file:
			# test output
			print case_header[:4]
			# /test output
			opinion_file.write("\n".join(case_header))
			opinion_file.write("\n* * * * * * * *\n")
			opinion_file.write("\n".join(maj_opinion))


	def parse_alt_opinions(self, alt_opinions, case_header, lexis_citation):
		'''
		This parses the concurring and dissenting opinions for a case.
		'''

		alt_opinion_regex = re.compile(r"CONCUR BY|DISSENT")
		alt_start_indices = []
		for index in range(0, len(alt_opinions)):
			current_paragraph = alt_opinions[index]
			
			if re.match(alt_opinion_regex, current_paragraph):
				alt_start_indices.append(index)
		
		start_end_pairs = []

		if len(alt_start_indices) == 1:
			start_end_pairs = [(0, len(alt_opinions) - 1)]
		else:
			for i in range(0, len(alt_start_indices)):
				if i == len(alt_start_indices) - 1:
					start_end_pairs.append(
						(alt_start_indices[i], len(alt_opinions) - 1))
				else:
					start_end_pairs.append(
						(alt_start_indices[i], alt_start_indices[i+1] - 1))
		
		split_alt_opinions = []
		for index in range(0, len(start_end_pairs)):
			current_pair = start_end_pairs[index]
			if current_pair[0] == current_pair[1]:
				start_end_pairs[index + 1] = (current_pair[0], start_end_pairs[index + 1][1])
				continue
			else:
				opinion_string = "\n".join(alt_opinions[current_pair[0]:current_pair[1]])
				split_alt_opinions.append(opinion_string)

		categorized_opinions = self.categorize_opinions(split_alt_opinions)
		
		# test output
		#print categorized_opinions
		#for opinion in categorized_opinions:
		#	print opinion[0]
		#	print opinion[1][:200]
		#	print "***************************************"
		# /test output
		
		for opinion in categorized_opinions:
			#opinion_authors = []
			# test output
			#print opinion[1][:200]
			print opinion[1].split('\n')[:5]
			# /test output

			opinion_author = self.get_author(opinion)
			self.write_opinion(opinion, opinion_author, lexis_citation, case_header)


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
		'''
		This method parses the US LEXIS citation out of a paragraph.
		'''	
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


	def categorize_opinions(self, split_alt_opinions):
		'''
		Given a list of non-majority opinions, this determines whether
		each on is concurring, dissenting, or both.
		This returns a list of tuples of the form (<opinion-type>,<opinion-text>)
		'''
		categorized_opinions = []

		for index in range(0, len(split_alt_opinions)):
			is_concur = False
			is_dissent = False
			sample = split_alt_opinions[index][:200]
			# test output
			#print sample
			# /test output
			if re.search("CONCUR BY:", sample):
				is_concur = True
			if re.search("DISSENT", sample):
				is_dissent = True
			# test output
			#print "*************"
			# /test output
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
		for paragraph in opinion[1].split("\n")[:5]:
			paragraph_words = paragraph.split()
			author_sample = ([word.strip('\xa0') for word in paragraph_words[0:4]
								if word is not ' '])
			# test output
			#print author_sample
			print "***********************"
			#print author_sample[0]
			#print " ".join(author_sample)
			#print "***********************"
			# /test output

			if (len(paragraph_words) > 2) \
			and (re.search("JUSTICE", author_sample[0]) \
			or re.search("CHIEF JUSTICE", " ".join(author_sample))):
				print "MATCHED"
				if re.search("CHIEF JUSTICE", " ".join(author_sample)):
					opinion_author = "CHIEF"
				else:
					opinion_author = author_sample[1].strip(',')
				#opinion_authors.append(opinion_author)
		return opinion_author


	def write_opinion(self, opinion, opinion_author, lexis_citation, case_header):
		'''
		Given the key info about an opinion, this writes it to file.
		'''
		# test output
		print "author of this opinion is: {0}".format(opinion_author)
		# /test output
		opinion_filename = opinion_author + "_" + lexis_citation + ".txt"
		if opinion[0] == "concur-dissent":
			output_dir = self.concur_dissent_dir
		elif opinion[0] == "concur":
			output_dir = self.concur_dir
		else: 
			output_dir = self.dissent_dir

		output_path = os.path.join(output_dir, opinion_filename)
		# test output
		print "filename is: {0}".format(opinion_filename)
		print "output path is: {0}".format(output_path)
		# /test output
		'''
		TODO: i need to work on formatting the header and adding other
		information to this write. but it's working now, and that's a start.
		'''

		with open(output_path, 'w') as output_file:
			output_file.write("\n".join(case_header))
			output_file.write("\n* * * * * * * *\n")
			output_file.write(opinion[1])



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




