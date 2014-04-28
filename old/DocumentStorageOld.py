class DocumentStorageOld(object):
    def create_split_text(self, text):
        '''
        Turns the text of the document into a list of terms
        with stop words removed.
        '''
        split_text = [word.lower() for word in text.split()]
        split_text = self.remove_stop_words(split_text)
        return split_text
    
    def remove_proper_nouns(self, text):
        '''
        Remove the proper nouns from the text. More accurately, removes
        any word that starts with a capital letter and does not follow
        a period.
        '''
        '''
        TODO: this method is no longer used
        '''
        cap_regex = re.compile("[A-Z]+")
        punc_regex = re.compile("[\.\?!]")
        filtered_text = []
        split_text = text.split()
        if len(split_text) < 1:
            return text
        filtered_text.append(split_text[0])
        for i in range(1, len(split_text)):
            prev_term = split_text[i-1]
            cur_term = split_text[i]
            is_proper_noun = (cap_regex.match(cur_term)
                              and not (punc_regex.search(prev_term)))
            if not is_proper_noun:
                filtered_text.append(cur_term)
        return " ".join(filtered_text)
        
    
    def remove_punctuation(self, text):
        '''
        Delete all punctuation from text -- replaced with space.
        '''
        '''
        TODO: this method is no longer used.
        '''
        return re.sub('[%s]' % re.escape(punctuation), ' ', text)
    
    
    def remove_nums(self, text):
        '''
        Delete all digits from text.
        '''
        '''
        TODO: this method is no longer used.
        '''
        return re.sub('[\d]', '', text)
    
    
    def remove_short_words(self, text):
        '''
        Remove all words shorter than 3 letters long.
        '''
        '''
        TODO: this method is no longer used.
        '''
        #return re.sub(r'\s.\s', ' ', text) 
        filtered_words = []
        for term in text.split():
            if len(term) > 2:
                filtered_words.append(term)
        return ' '.join(filtered_words)
            
    
    def remove_stop_words(self, word_list):
        '''
        Removes stop words from word_list.
        '''
        '''
        TODO: this method is no longer used.
        '''
        extra_stop_words = (["concur", "dissent", "concurring", 
                             "dissenting", "case", "join"])
        filtered_text = ([word for word in word_list if 
                          (not word in stopwords.words('english'))
                          and (not word in extra_stop_words)])
        return filtered_text


    def is_stop_word(self, word):
        '''
        Determines if a given word is considered a stop word.
        '''
        '''
        NOTE: this method is no longer used
        '''
        extra_stop_words = (["concur", "dissent", "concurring", 
                             "dissenting", "case", "join"])        
        is_stop_word = ((word in stopwords.words('english'))
                        or (word in extra_stop_words))
        return is_stop_word
        