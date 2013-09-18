Word Clouds in Python

Daniel Klein
Computer-Based Honors Program
The University of Alabama
Fall 2013

=========

Project Description:
This project is in under the direction of Dr. Joseph Smith, Associate Professor of Political Science at the University of Alabama. 
We aim to build a piece of software, written in Python, that will perform automated content analysis on a collection of legal documents 
and create a statistical word cloud illustrating the terms that characterize the collection. 
We are approaching the research objective with a highly object-oriented design that can be built incrementally. 

Final delivery of the software is scheduled for early December 2013. 
The GitHub repository for the project is viewable at https://github.com/dmarklein/WordCloud.

The basic idea for the flow of the project is this:
(I)		Each document has a file to itself. The DocumentConverter parses each file and creates a Document object from each one.
(II)	Given a group of these Document objects, the DocumentSorter creates subsets of them (by sorting on a given metadata field) and passes each subset to the SuperDocGenerator.
(III)	Given a subset of Document objects, the SuperDocGenerator creates a SuperDocument object.
(IV)	Given a set of SuperDocumentObjects, the AnalysisEngine performs the actual statistical analysis on term frequency and whatnot and creates a weighted dictionary of the most important terms in the set of SuperDocuments, which it passes to the WordCloudGenerator.
(V)		The WordCloudGenerator has the easy part: it takes the weighted dict of terms and creates a visualization word cloud. 


