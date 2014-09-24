'''
Daniel Klein
Computer-Based Honors Program
The University of Alabama
5.8.2014

This file contains some key constants that are used throughout the 
WordCloud system.
'''
# set these variables to match local paths where everything is/you want it to go

# path where case files from LEXIS live (for parser)
LEXIS_FILE_PATH = r"C:\Users\Daniel\Dropbox\Class_files\CBH_301\Word_Cloud\supreme_court_opinions\test"
# path where parser should save parsed opinions
OPINION_OUTPUT_PATH = r"C:\Users\Daniel\Dropbox\Class_files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"

# path where parsed opinions live (for Converter)
OPINION_PATH = r"/home/dmklein/Code/test_opinions"
# path where Converter should save serialized SupremeCourtOpinion objects
PICKLE_PATH = r"/home/dmklein/Code/test_pickled"
#OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
#PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_pickled"

# path of font to use for word cloud
FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
#FONT_PATH = "C:/Windows/Fonts/FRABK.ttf"
