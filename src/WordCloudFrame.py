import wx
from src.WordCloudSorterDialog import WordCloudSorterDialog
from src.WordCloudCore import WordCloudCore

class WordCloudFrame(wx.Frame): 
    '''
    This is the primary frame for the WordCloud GUI app. It contains a list of
    subsets and the corpus, along with various buttons for manipulating them.
    It also has buttons for viewing a subset and creating a word cloud. 
    '''
    
    def __init__(self, parent, dialog_id, title="Word Cloud Creator"):
        wx.Frame.__init__(self, parent, dialog_id, title, size=(750, 675))
        
        self.wc_core = WordCloudCore()

        panel = wx.Panel(self, -1, size=(750, 675))

        self.main_box = wx.BoxSizer(wx.VERTICAL)

        #######################################################################
        # "Subsets" and "Corpus" labels
        #######################################################################
        subsets_label = wx.StaticText(panel, -1, "Subsets")
        subsets_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        subsets_label.SetSize(subsets_label.GetBestSize())
        
        spacer = wx.StaticText(panel, -1, "              ")
        spacer.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        spacer.SetSize(spacer.GetBestSize())
        
        corpus_label = wx.StaticText(panel, -1, "Corpus")
        corpus_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        corpus_label.SetSize(subsets_label.GetBestSize())
        
        label_box = wx.BoxSizer(wx.HORIZONTAL)
        label_box.Add(subsets_label, flag=wx.CENTER)
        label_box.Add(spacer, flag=wx.CENTER)
        label_box.Add(corpus_label, flag=wx.CENTER)
        
        self.main_box.Add(label_box, flag=wx.CENTER)
        
        #######################################################################
        # scroll list for subsets
        #######################################################################
        subsets_and_corpus = wx.BoxSizer(wx.HORIZONTAL) 
        
        self.subset_list = wx.ListBox(panel, size=(300, 500), 
                                      choices=self.wc_core.subset_names)
        subsets_and_corpus.Add(self.subset_list, flag=wx.CENTER)
        
        #######################################################################
        # buttons for adding/removing subsets from corpus list 
        #######################################################################
        add_one = wx.Button(panel, wx.ID_CLOSE, " > ", size=(50, 50), 
                            style=wx.BU_EXACTFIT)
        add_one.Bind(wx.EVT_BUTTON, self.OnAddOne)
        
        remove_one = wx.Button(panel, wx.ID_CLOSE, " < ", size=(50, 50), 
                               style=wx.BU_EXACTFIT)
        remove_one.Bind(wx.EVT_BUTTON, self.OnRemoveOne)
        
        add_all = wx.Button(panel, wx.ID_CLOSE, " >>", size=(50, 50), 
                            style=wx.BU_EXACTFIT)
        add_all.Bind(wx.EVT_BUTTON, self.OnAddAll)
        
        remove_all = wx.Button(panel, wx.ID_CLOSE, "<< ", size=(50, 50), 
                               style=wx.BU_EXACTFIT)
        remove_all.Bind(wx.EVT_BUTTON, self.OnRemoveAll)
        
        switch_box = wx.BoxSizer(wx.VERTICAL)
        switch_box.Add(add_one, flag=wx.ALL, border=15)
        switch_box.Add(remove_one, flag=wx.ALL, border=15)
        switch_box.Add(add_all, flag=wx.ALL, border=15)
        switch_box.Add(remove_all, flag=wx.ALL, border=15)
        
        subsets_and_corpus.Add(switch_box, flag=wx.CENTER)
        
        #######################################################################
        # scroll list for corpus
        #######################################################################
        self.corpus_list = wx.ListBox(panel, size=(300, 500), 
                                      choices=self.wc_core.corpus_subset_names)
        subsets_and_corpus.Add(self.corpus_list, flag=wx.CENTER)
        
        self.main_box.Add(subsets_and_corpus, flag=wx.CENTER)
        
        #######################################################################
        # add subset, view subset, and create wordcloud buttons
        #######################################################################
        add_subset = wx.Button(panel, wx.ID_CLOSE, "Add Subset", 
                               size=(150, 100))
        add_subset.Bind(wx.EVT_BUTTON, self.OnAddSubset)
        
        view_subset = wx.Button(panel, wx.ID_CLOSE, "View Subset", 
                                size=(150, 100))
        view_subset.Bind(wx.EVT_BUTTON, self.OnViewSubset)
        
        create_wc = wx.Button(panel, wx.ID_CLOSE, "Create Word Cloud", 
                              size=(150, 100))
        create_wc.Bind(wx.EVT_BUTTON, self.OnCreateWordCloud)
        
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        button_box.Add(add_subset, flag=wx.ALL, border=25)
        button_box.Add(view_subset, flag=wx.ALL, border=25)
        button_box.Add(create_wc, flag=wx.ALL, border=25)
        
        self.main_box.Add(button_box, flag=wx.CENTER)

        panel.SetSizer(self.main_box)
        panel.Layout()
        
        self.OnStart()
        
        
    def OnStart(self):
        self.Hide()
        wait = wx.BusyInfo("Loading opinions...", parent=self)
        self.wc_core.unpack_opinions()
        wait = None
        self.Show()
        return
                
        
    def OnAddSubset(self, event):
        dia = WordCloudSorterDialog(self, -1, 'Subset Builder')
        dia.ShowModal()
        dia.Destroy()
        self.subset_list.Set(self.wc_core.subset_names)
        
    
    def OnViewSubset(self, event):
        '''
        TODO: This is terrible. Make it better. It's also really really slow.
        '''
        indexes = self.subset_list.GetSelections()
        for i in indexes:
            subset_name = self.wc_core.subset_names[i]
            subset = self.wc_core.subsets[subset_name]
            info_string = self.build_info_string(subset)
            wx.MessageDialog(None, info_string, subset_name, wx.OK).ShowModal()
        
    
    def OnCreateWordCloud(self, event):
        '''
        Create a word cloud using the selected subset and the current corpus.
        '''
        subset_index = self.subset_list.GetSelection()
        subset_name = self.wc_core.subset_names[subset_index]
        subset = self.wc_core.subsets[subset_name]
        # flatten the corpus list of lists into one list
        corpus = [opinion for subset in self.wc_core.corpus_subsets.values() 
                            for opinion in subset]
        weighted_terms = self.wc_core.run_analysis(corpus, subset)
        self.wc_core.generate_cloud(weighted_terms)
        return
        
    
    def OnAddOne(self, event):
        '''
        Add selected subset(s) to corpus.
        '''
        # TODO: make sure you can't add duplicate
        indexes = self.subset_list.GetSelections()
        for i in indexes:
            subset_name = self.wc_core.subset_names[i]
            subset = self.wc_core.subsets[subset_name]
            self.wc_core.corpus_subsets[subset_name] = subset
            self.wc_core.corpus_subset_names.append(subset_name)
            self.corpus_list.Set(self.wc_core.corpus_subset_names)
    
    
    def OnRemoveOne(self, event):
        '''
        Remove selected corpus subset(s) from corpus.
        '''
        indexes = self.corpus_list.GetSelections()
        for i in indexes:
            subset_name = self.wc_core.corpus_subset_names[i]
            self.wc_core.corpus_subsets.pop(subset_name)
            self.wc_core.corpus_subset_names.pop(i)
        self.corpus_list.Set(self.wc_core.corpus_subset_names)
            
    
    def OnAddAll(self, event):
        '''
        Add all subsets to corpus.
        NOTE: this could also be done by setting the corpus name list equal
        to the subset name list, and the corpus dict equal to the subset dict.
        '''
        '''
        for subset_name in self.wc_core.subset_names:
            if subset_name not in self.wc_core.corpus_subset_names:
                subset = self.wc_core.subsets[subset_name]
                self.wc_core.corpus_subsets[subset_name] = subset
                self.wc_core.corpus_subset_names.append(subset_name)
        '''
        self.wc_core.corpus_subsets = self.wc_core.subsets
        self.wc_core.corpus_subset_names = self.wc_core.subset_names
        self.corpus_list.Set(self.wc_core.corpus_subset_names)
    
    
    def OnRemoveAll(self, event):
        '''
        Remove all corpus subsets from corpus.
        '''
        self.wc_core.corpus_subset_names = []
        self.wc_core.corpus_subsets = {}
        self.corpus_list.Set(self.wc_core.corpus_subset_names)
            
            
    def build_info_string(self, subset):
        '''
        TODO: This is terrible. Make it better. It's also really really slow.
        '''
        info_string = "CASE TITLE                 OPINION AUTHOR  OPINION TYPE\n"
        for opinion in subset:
            info_string += opinion.doc_metadata.case_title + "\t"
            info_string += opinion.doc_metadata.opinion_author + "\t"
            info_string += opinion.doc_metadata.opinion_type +"\n"
        return info_string
            
            
    
    
        
        
