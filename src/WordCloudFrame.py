import wx
from src.WordCloudSorterDialog import WordCloudSorterDialog
from src.WordCloudCore import WordCloudCore

class WordCloudFrame(wx.Frame): 
    
    def __init__(self, parent, dialog_id, title="Word Cloud Creator"):
        wx.Frame.__init__(self, parent, dialog_id, title, size=(1500, 1500))
        
        self.wc_core = WordCloudCore()

        panel = wx.Panel(self, -1, size=(1500, 1500))

        main_box = wx.BoxSizer(wx.VERTICAL)

        # these go in first box
        label_box = wx.BoxSizer(wx.HORIZONTAL)
        
        subsets_label = wx.StaticText(panel, -1, "Subsets")
        subsets_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        subsets_label.SetSize(subsets_label.GetBestSize())
        label_box.Add(subsets_label, flag=wx.ALIGN_LEFT)
        
        corpus_label = wx.StaticText(panel, -1, "Corpus")
        corpus_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        corpus_label.SetSize(subsets_label.GetBestSize())
        label_box.Add(corpus_label, flag=wx.ALIGN_RIGHT)
        
        main_box.Add(label_box)
        
        # two scroll lists will go in second box
        list_box = wx.BoxSizer(wx.HORIZONTAL) # this variable name sucks.
        
        self.subset_list = wx.ListBox(panel, size=(500, 500), 
                                      choices=self.wc_core.subset_names)
        list_box.Add(self.subset_list, flag=wx.ALIGN_LEFT)
        
        # buttons for adding/removing subsets from corpus list go in here
        switch_box = wx.BoxSizer(wx.VERTICAL)
        
        add_one = wx.Button(panel, wx.ID_CLOSE, " > ", style=wx.BU_EXACTFIT)
        add_one.Bind(wx.EVT_BUTTON, self.OnAddOne)
        switch_box.Add(add_one, 0, wx.ALL, 10)
        
        remove_one = wx.Button(panel, wx.ID_CLOSE, " < ", style=wx.BU_EXACTFIT)
        remove_one.Bind(wx.EVT_BUTTON, self.OnRemoveOne)
        switch_box.Add(remove_one, 0, wx.ALL, 10)
        
        add_all = wx.Button(panel, wx.ID_CLOSE, " >>", style=wx.BU_EXACTFIT)
        add_all.Bind(wx.EVT_BUTTON, self.OnAddAll)
        switch_box.Add(add_all, 0, wx.ALL, 10)
        
        remove_all = wx.Button(panel, wx.ID_CLOSE, "<< ", style=wx.BU_EXACTFIT)
        remove_all.Bind(wx.EVT_BUTTON, self.OnRemoveAll)
        switch_box.Add(remove_all, 0, wx.ALL, 10)
        
        list_box.Add(switch_box, flag=wx.ALIGN_CENTER)
        
        self.corpus_list = wx.ListBox(panel, size=(500, 500), 
                                      choices=self.wc_core.corpus_subset_names)
        list_box.Add(self.corpus_list, flag=wx.ALIGN_RIGHT)
        
        main_box.Add(list_box)
        
        # buttons go in third box
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        add_subset = wx.Button(panel, wx.ID_CLOSE, "Add Subset")
        add_subset.Bind(wx.EVT_BUTTON, self.OnAddSubset)
        button_box.Add(add_subset, 0, wx.ALL, 10)
        
        view_subset = wx.Button(panel, wx.ID_CLOSE, "View Subset")
        view_subset.Bind(wx.EVT_BUTTON, self.OnViewSubset)
        button_box.Add(view_subset, 0, wx.ALL, 10)
        
        create_wc = wx.Button(panel, wx.ID_CLOSE, "Create Word Cloud")
        create_wc.Bind(wx.EVT_BUTTON, self.OnCreateWordCloud)
        button_box.Add(create_wc, 0, wx.ALL, 10)
        
        main_box.Add(button_box)

        panel.SetSizer(main_box)
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
        '''
        get selected subset
        get corpus and join into one list
        pass them to core.run_analysis
        pass the returned list to core.generate_cloud
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
        for subset_name in self.wc_core.subset_names:
            if subset_name not in self.wc_core.corpus_subset_names:
                subset = self.wc_core.subsets[subset_name]
                self.wc_core.corpus_subsets[subset_name] = subset
                self.wc_core.corpus_subset_names.append(subset_name)
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
            
            
    
    
        
        
