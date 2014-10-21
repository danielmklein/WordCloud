Word Clouds in Python

Daniel Klein
Computer-Based Honors Program
The University of Alabama
Fall 2013/2014

=========

Project Description:

This project is in under the direction of Dr. Joseph Smith, Associate Professor of Political Science at the 
University of Alabama. The initial goal of this project was design and build a piece of software, written in 
Python, that would perform automated content analysis on a collection of legal documents and create a statistical
word cloud illustrating the terms that characterize the collection. An initial version of this software was 
completed in December 2013, and later a graphical user interface was added during the Spring of 2014. This piece of
software is now viewed as a prototype, and as of Fall 2014 development has shifted to focus on building a web 
application that performs the same content analysis and cloud generation. 

The GitHub repository for the project is viewable at https://github.com/dmarklein/WordCloud.

We presented our work at the 2014 Southern Political Science Association Conference in New Orleans, Louisiana, and 
at the 2014 Undergraduate Research & Creative Activity Conference at the University of Alabama in Tuscaloosa, 
Alabama.

The basic idea for the flow of the project is this:
(I)		Each document has a file to itself. The DocumentConverter parses each file and creates a Document object 
from each one.
(II)	Given a group of these Document objects, the DocumentSorter creates subsets of them (by sorting on a given
 metadata 
field).
(III)	Given a collection of one or more subsets of Documents, the AnalysisEngine performs the actual statistical
analysis on term frequency and whatnot and creates a list of (term, weight) tuples representing the most important 
terms in each subset, which it passes to the WordCloudGenerator.
(IV)	The WordCloudGenerator has the easy part: it takes the list of terms and weights and creates a word cloud.

NOTE: The Python prototype of this software requires the NumPy, PyYAML, NLTK, and wxPython libraries.




