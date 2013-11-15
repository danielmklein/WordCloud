import os, os.path
import re
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata
from Document import Document
from DocumentConverter import DocumentConverter
from DocumentSorter import DocumentSorter
from AnalysisEngine import AnalysisEngine
from WordCloudGenerator import WordCloudGenerator

# directory containing parsed opinions
OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions"
ACCEPTED_CITES = (['1947 U.S. LEXIS 2266','1947 U.S. LEXIS 2860',
                   '1947 U.S. LEXIS 2923','1948 U.S. LEXIS 2086',
                   '1948 U.S. LEXIS 2371','1948 U.S. LEXIS 2450',
                   '1949 U.S. LEXIS 2400','1949 U.S. LEXIS 3003',
                   '1949 U.S. LEXIS 3028','1949 U.S. LEXIS 3034',
                   '1950 U.S. LEXIS 2518','1950 U.S. LEXIS 2530',
                   '1950 U.S. LEXIS 2530','1950 U.S. LEXIS 2532',
                   '1950 U.S. LEXIS 2532','1950 U.S. LEXIS 2534',
                   '1950 U.S. LEXIS 2561','1951 U.S. LEXIS 1729',
                   '1951 U.S. LEXIS 2249','1951 U.S. LEXIS 2407',
                   '1952 U.S. LEXIS 2345','1952 U.S. LEXIS 2345',
                   '1952 U.S. LEXIS 2345','1952 U.S. LEXIS 2387',
                   '1952 U.S. LEXIS 2796','1952 U.S. LEXIS 2799',
                   '1954 U.S. LEXIS 2505','1954 U.S. LEXIS 2505',
                   '1954 U.S. LEXIS 2657','1957 U.S. LEXIS 1252',
                   '1957 U.S. LEXIS 1617','1957 U.S. LEXIS 585',
                   '1957 U.S. LEXIS 587','1957 U.S. LEXIS 587',
                   '1958 U.S. LEXIS 1830','1959 U.S. LEXIS 1744',
                   '1959 U.S. LEXIS 1885','1959 U.S. LEXIS 662',
                   '1960 U.S. LEXIS 1948','1961 U.S. LEXIS 1998',
                   '1961 U.S. LEXIS 2042','1961 U.S. LEXIS 813',
                   '1962 U.S. LEXIS 846','1963 U.S. LEXIS 2050',
                   '1963 U.S. LEXIS 2094','1963 U.S. LEXIS 2398','1964 U.S. LEXIS 150','1964 U.S. LEXIS 1655',
                   '1964 U.S. LEXIS 1655','1964 U.S. LEXIS 822','1964 U.S. LEXIS 823','1965 U.S. LEXIS 1304',
                   '1965 U.S. LEXIS 1351','1965 U.S. LEXIS 1537','1965 U.S. LEXIS 1537','1965 U.S. LEXIS 1732',
                   '1965 U.S. LEXIS 2008','1965 U.S. LEXIS 2286','1965 U.S. LEXIS 2286','1965 U.S. LEXIS 2328',
                   '1966 U.S. LEXIS 1644','1966 U.S. LEXIS 2013','1966 U.S. LEXIS 2014','1966 U.S. LEXIS 238',
                   '1966 U.S. LEXIS 2847','1966 U.S. LEXIS 2906','1966 U.S. LEXIS 75','1967 U.S. LEXIS 1084',
                   '1967 U.S. LEXIS 1084','1967 U.S. LEXIS 132','1967 U.S. LEXIS 1571','1967 U.S. LEXIS 1571','1967 U.S. LEXIS 1571','1967 U.S. LEXIS 2991','1967 U.S. LEXIS 344','1968 U.S. LEXIS 1145','1968 U.S. LEXIS 1471','1968 U.S. LEXIS 1555','1968 U.S. LEXIS 1879','1968 U.S. LEXIS 1880','1968 U.S. LEXIS 2549','1968 U.S. LEXIS 2910','1968 U.S. LEXIS 2910','1968 U.S. LEXIS 2948','1968 U.S. LEXIS 2996','1968 U.S. LEXIS 3004','1968 U.S. LEXIS 3005','1968 U.S. LEXIS 3005','1969 U.S. LEXIS 103','1969 U.S. LEXIS 1367','1969 U.S. LEXIS 1972','1969 U.S. LEXIS 2295','1969 U.S. LEXIS 2296','1969 U.S. LEXIS 2443','1969 U.S. LEXIS 3189','1969 U.S. LEXIS 3267','1969 U.S. LEXIS 3267','1970 U.S. LEXIS 13','1970 U.S. LEXIS 2453','1970 U.S. LEXIS 27','1970 U.S. LEXIS 34','1970 U.S. LEXIS 39','1970 U.S. LEXIS 42','1970 U.S. LEXIS 44','1970 U.S. LEXIS 49','1971 U.S. LEXIS 100','1971 U.S. LEXIS 100','1971 U.S. LEXIS 116','1971 U.S. LEXIS 124','1971 U.S. LEXIS 32','1971 U.S. LEXIS 44','1971 U.S. LEXIS 46','1971 U.S. LEXIS 77','1971 U.S. LEXIS 78','1971 U.S. LEXIS 79','1971 U.S. LEXIS 94','1971 U.S. LEXIS 94','1972 U.S. LEXIS 128','1972 U.S. LEXIS 132','1972 U.S. LEXIS 132','1972 U.S. LEXIS 132','1972 U.S. LEXIS 137','1972 U.S. LEXIS 22','1972 U.S. LEXIS 26','1972 U.S. LEXIS 28','1972 U.S. LEXIS 43','1972 U.S. LEXIS 46','1972 U.S. LEXIS 72','1973 U.S. LEXIS 124','1973 U.S. LEXIS 146','1973 U.S. LEXIS 149','1973 U.S. LEXIS 150','1973 U.S. LEXIS 164','1973 U.S. LEXIS 167','1973 U.S. LEXIS 177','1973 U.S. LEXIS 19','1973 U.S. LEXIS 30','1973 U.S. LEXIS 34','1973 U.S. LEXIS 38','1973 U.S. LEXIS 4','1973 U.S. LEXIS 4','1973 U.S. LEXIS 4','1973 U.S. LEXIS 4','1973 U.S. LEXIS 40','1973 U.S. LEXIS 41','1973 U.S. LEXIS 93','1974 U.S. LEXIS 132','1974 U.S. LEXIS 158','1974 U.S. LEXIS 16','1974 U.S. LEXIS 25','1974 U.S. LEXIS 82','1974 U.S. LEXIS 82','1974 U.S. LEXIS 83','1974 U.S. LEXIS 85','1974 U.S. LEXIS 86','1974 U.S. LEXIS 87','1974 U.S. LEXIS 88','1974 U.S. LEXIS 89','1974 U.S. LEXIS 96','1975 U.S. LEXIS 139','1975 U.S. LEXIS 3','1975 U.S. LEXIS 73','1975 U.S. LEXIS 79','1976 U.S. LEXIS 11','1976 U.S. LEXIS 12','1976 U.S. LEXIS 149','1976 U.S. LEXIS 17','1976 U.S. LEXIS 181','1976 U.S. LEXIS 26','1976 U.S. LEXIS 3','1976 U.S. LEXIS 35','1976 U.S. LEXIS 5','1976 U.S. LEXIS 55','1977 U.S. LEXIS 100','1977 U.S. LEXIS 106','1977 U.S. LEXIS 113','1977 U.S. LEXIS 145','1977 U.S. LEXIS 24','1977 U.S. LEXIS 29','1977 U.S. LEXIS 58','1977 U.S. LEXIS 81','1977 U.S. LEXIS 92','1978 U.S. LEXIS 11','1978 U.S. LEXIS 135','1978 U.S. LEXIS 84','1978 U.S. LEXIS 92','1979 U.S. LEXIS 139','1979 U.S. LEXIS 142','1979 U.S. LEXIS 209','1979 U.S. LEXIS 57','1979 U.S. LEXIS 57','1979 U.S. LEXIS 57','1979 U.S. LEXIS 88','1979 U.S. LEXIS 95','1980 U.S. LEXIS 18','1980 U.S. LEXIS 4','1980 U.S. LEXIS 48','1980 U.S. LEXIS 6','1980 U.S. LEXIS 68','1980 U.S. LEXIS 71','1980 U.S. LEXIS 78','1980 U.S. LEXIS 91','1981 U.S. LEXIS 108','1981 U.S. LEXIS 127','1981 U.S. LEXIS 145','1981 U.S. LEXIS 39','1981 U.S. LEXIS 50','1982 U.S. LEXIS 12','1982 U.S. LEXIS 137','1982 U.S. LEXIS 49','1982 U.S. LEXIS 78','1982 U.S. LEXIS 8','1982 U.S. LEXIS 92','1983 U.S. LEXIS 130','1983 U.S. LEXIS 153','1983 U.S. LEXIS 154','1983 U.S. LEXIS 33','1983 U.S. LEXIS 33','1983 U.S. LEXIS 6','1983 U.S. LEXIS 85','1984 U.S. LEXIS 123','1984 U.S. LEXIS 136','1984 U.S. LEXIS 139','1984 U.S. LEXIS 147','1984 U.S. LEXIS 20','1984 U.S. LEXIS 28','1984 U.S. LEXIS 28','1984 U.S. LEXIS 40','1984 U.S. LEXIS 41','1984 U.S. LEXIS 73','1984 U.S. LEXIS 83','1984 U.S. LEXIS 85','1985 U.S. LEXIS 100','1985 U.S. LEXIS 103','1985 U.S. LEXIS 127','1985 U.S. LEXIS 127','1985 U.S. LEXIS 133','1986 U.S. LEXIS 1','1986 U.S. LEXIS 104','1986 U.S. LEXIS 120','1986 U.S. LEXIS 129','1986 U.S. LEXIS 139','1986 U.S. LEXIS 140','1986 U.S. LEXIS 2','1986 U.S. LEXIS 81','1986 U.S. LEXIS 97','1987 U.S. LEXIS 1815','1987 U.S. LEXIS 1930','1987 U.S. LEXIS 1934','1987 U.S. LEXIS 2362','1987 U.S. LEXIS 2617','1987 U.S. LEXIS 2619','1987 U.S. LEXIS 2875','1987 U.S. LEXIS 2895','1988 U.S. LEXIS 1445','1988 U.S. LEXIS 2489','1988 U.S. LEXIS 2863','1988 U.S. LEXIS 3026','1988 U.S. LEXIS 3031','1988 U.S. LEXIS 310','1988 U.S. LEXIS 941','1989 U.S. LEXIS 1042','1989 U.S. LEXIS 2437','1989 U.S. LEXIS 3115','1989 U.S. LEXIS 3116','1989 U.S. LEXIS 3120','1989 U.S. LEXIS 3129','1989 U.S. LEXIS 3135','1989 U.S. LEXIS 3135','1989 U.S. LEXIS 3289','1989 U.S. LEXIS 648','1989 U.S. LEXIS 648','1990 U.S. LEXIS 1533','1990 U.S. LEXIS 2036','1990 U.S. LEXIS 2862','1990 U.S. LEXIS 3087','1990 U.S. LEXIS 3087','1990 U.S. LEXIS 3296','1990 U.S. LEXIS 3298','1990 U.S. LEXIS 3298','1990 U.S. LEXIS 333','1990 U.S. LEXIS 334','1990 U.S. LEXIS 334','1990 U.S. LEXIS 334','1990 U.S. LEXIS 334','1990 U.S. LEXIS 334','1990 U.S. LEXIS 334','1990 U.S. LEXIS 3460','1990 U.S. LEXIS 638','1990 U.S. LEXIS 638','1991 U.S. LEXIS 2220','1991 U.S. LEXIS 2220','1991 U.S. LEXIS 3630','1991 U.S. LEXIS 3633','1991 U.S. LEXIS 3639','1991 U.S. LEXIS 3820','1991 U.S. LEXIS 7172','1992 U.S. LEXIS 3125','1992 U.S. LEXIS 3692','1992 U.S. LEXIS 3863','1992 U.S. LEXIS 4532','1992 U.S. LEXIS 4535','1993 U.S. LEXIS 2401','1993 U.S. LEXIS 2985','1993 U.S. LEXIS 3191','1993 U.S. LEXIS 4024','1993 U.S. LEXIS 4402','1994 U.S. LEXIS 4104','1994 U.S. LEXIS 4448','1994 U.S. LEXIS 4831','1995 U.S. LEXIS 1624','1995 U.S. LEXIS 2844','1995 U.S. LEXIS 2847','1995 U.S. LEXIS 4050','1995 U.S. LEXIS 909','1996 U.S. LEXIS 3020','1996 U.S. LEXIS 4261','1996 U.S. LEXIS 4261','1996 U.S. LEXIS 4262','1997 U.S. LEXIS 2078','1997 U.S. LEXIS 4036','1997 U.S. LEXIS 4037','1998 U.S. LEXIS 3102','1998 U.S. LEXIS 4211','1999 U.S. LEXIS 4010','1999 U.S. LEXIS 506','1999 U.S. LEXIS 8239','2000 U.S. LEXIS 2196','2000 U.S. LEXIS 2347','2000 U.S. LEXIS 3427','2001 U.S. LEXIS 1954','2001 U.S. LEXIS 1954','2001 U.S. LEXIS 3205','2001 U.S. LEXIS 3815','2001 U.S. LEXIS 3815','2001 U.S. LEXIS 4904','2001 U.S. LEXIS 4911','2001 U.S. LEXIS 4911','2002 U.S. LEXIS 2789','2002 U.S. LEXIS 3035','2002 U.S. LEXIS 3424','2002 U.S. LEXIS 488','2002 U.S. LEXIS 4883','2003 U.S. LEXIS 2715','2003 U.S. LEXIS 3430','2003 U.S. LEXIS 4782','2003 U.S. LEXIS 4799','2004 U.S. LEXIS 4026','2004 U.S. LEXIS 4762','2004 U.S. LEXIS 8165','2005 U.S. LEXIS 4181','2005 U.S. LEXIS 4343','2005 U.S. LEXIS 4343','2005 U.S. LEXIS 4347','2006 U.S. LEXIS 2025','2006 U.S. LEXIS 3450','2006 U.S. LEXIS 4341','2006 U.S. LEXIS 5176','2007 U.S. LEXIS 8271','2007 U.S. LEXIS 8514','2008 U.S. LEXIS 4314','2009 U.S. LEXIS 1632','2009 U.S. LEXIS 1636','2010 U.S. LEXIS 2206','2010 U.S. LEXIS 2206','2010 U.S. LEXIS 3478','2010 U.S. LEXIS 5252','2010 U.S. LEXIS 5252','2011 U.S. LEXIS 1903','2011 U.S. LEXIS 4379','2011 U.S. LEXIS 4794','2011 U.S. LEXIS 4802','2012 U.S. LEXIS 4666','2013 U.S. LEXIS 605'])

class WordCloudMain():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    This class represents the Word Cloud application itself -- it integrates
    all of the components into a functional application.
    '''
    
    def __init__(self):
        pass
        
        
    def main(self):
        print "Here's the main method..."
        '''
        take all the opinions we want to convert,
        convert them,
        sort them into subsets,
        then analyze subsets and create word cloud for each
        '''
        # first we convert the opinion files into Document objects
        opinion_list = self.convert_opinions()
        # now we sort them
        subsets = self.sort_opinions(opinion_list)
        # perform the analysis
        subset_lists = self.run_analysis(subsets)
        # and generate the word cloud
        self.generate_clouds(subset_lists)
                
        
    def convert_opinions(self):
        opinion_list = []
        txtfile_regex = re.compile(r"\.txt$")
        for opinion_file in os.listdir(OPINION_PATH):
            input_path = os.path.join(OPINION_PATH, opinion_file)
            is_text_file = re.search(txtfile_regex, input_path)
            if not is_text_file:
                print ("{0} is not a text file, so we can't convert it!"
                       .format(input_path))
                continue
            pickle_path = input_path + ".Document"
            converter = DocumentConverter(input_path, pickle_path)
            print "converting file {0}...".format(opinion_file)
            opinion_list.append(converter.convert_file())
            del converter
        # test output
        print opinion_list
        print "there are {0} opinions in the list...".format(len(opinion_list))
        # /test output
        return opinion_list
    
    
    def sort_opinions(self, opinion_list):
        '''
        Modify the lines between ### for your specific situation.
        '''
        print "sorting the opinions into subsets..."
        sorter = DocumentSorter(opinion_list)
        ###
        sort_field = "case_lexis_cite"
        free_speech_subset = sorter.create_subset(sort_field, ACCEPTED_CITES)
        subsets = [free_speech_subset]
        ###
        print "the set contains {0} subsets...".format(len(subsets))
        return subsets
    
    
    def run_analysis(self, subsets):
        print "running analysis..."
        analysis_engine = AnalysisEngine(subsets)
        subset_lists = analysis_engine.analyze_docs()
        return subset_lists
    
    
    def generate_clouds(self, subset_lists):
        '''
        This method will be modified for your specific situation.
        NOTE that subset_lists is a list of (output_filename, weighted_list) pairs.
        '''
        '''
        subset_lists = [(output_filename, weighted_list), (filename, list), ... , (filename, list)]
        '''
        free_speech_file = subset_lists[0][0] + "_free_speech.jpg"
        free_speech_terms = subset_lists[0][1]
        # test output
        print "FREE SPEECH TERMS: {0}".format(free_speech_terms)
        print "FREE SPEECH OUTPUT FILE: {0}".format(free_speech_file)
        # /test output
        
        print "generating a word cloud for each subset..."
        free_speech_cloud_gen = WordCloudGenerator(free_speech_terms, free_speech_file)
        free_speech_cloud_gen.generate_word_cloud()
        
        return
    

word_cloud_app = WordCloudMain()
word_cloud_app.main()  