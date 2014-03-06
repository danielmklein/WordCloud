'''
Created on 3.5.14
Daniel Klein

Old, unused methods from the WordCloudMain class of the WordCloud project.
'''


def convert_opinions(self):
    '''
    !!!!!!THIS METHOD IS NO LONGER USED!!!!!
    
    Convert each given opinion into a Document object.
    '''
    opinion_list = []
    txtfile_regex = re.compile(r"\.txt$")
    for opinion_file in os.listdir(OPINION_PATH):
        input_path = os.path.join(OPINION_PATH, opinion_file)
        is_text_file = re.search(txtfile_regex, input_path)
        if not is_text_file:
            print ("{0} is not a text file, so we can't convert it!"
                   .format(input_path))
            continue
        pickle_path = os.path.join(OPINION_PATH, "output", 
                                   opinion_file + ".Document")
        converter = DocumentConverter(input_path, pickle_path)
        print "Converting file {0}...".format(opinion_file)
        opinion_list.append(converter.convert_file())
        del converter
    print "There are {0} opinions in the list...".format(len(opinion_list))
    return opinion_list
