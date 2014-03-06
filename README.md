Word Clouds in Python

Daniel Klein
Computer-Based Honors Program
The University of Alabama
Fall 2013

=========

Project Description:

This project is in under the direction of Dr. Joseph Smith, Associate Professor of Political Science at the University of 
Alabama. We aim to build a piece of software, written in Python, that will perform automated content analysis on a 
collection of legal documents and create a statistical word cloud illustrating the terms that characterize the collection. 

We are approaching the research objective with a highly object-oriented design that will be built incrementally though 
primarily test-driven development. Final delivery of the initial version of the system is scheduled for early December 2013,
but development will continue into the foreseeable future. 
The GitHub repository for the project is viewable at https://github.com/dmarklein/WordCloud.

We presented our work at the 2014 Southern Political Science Association Conference in New Orleans, Louisiana, and we will 
also be presenting our work at the 2014 Undergraduate Research & Creative Activity Conference at the University of Alabama 
in Tuscaloosa, Alabama.

The basic idea for the flow of the project is this:
(I)		Each document has a file to itself. The DocumentConverter parses each file and creates a Document object from each one.
(II)	Given a group of these Document objects, the DocumentSorter creates subsets of them (by sorting on a given metadata 
field).
(III)	Given a collection of one or more subsets of Documents, the AnalysisEngine performs the actual statistical analysis 
on term frequency and whatnot and creates a list of (term, weight) tuples representing the most important terms in each 
subset, which it passes to the WordCloudGenerator.
(IV)	The WordCloudGenerator has the easy part: it takes the list of terms and weights and creates a visualization word cloud. 




