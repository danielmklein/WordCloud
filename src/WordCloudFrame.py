import wx
from WordCloudSorterDialog import WordCloudSorterDialog
from WordCloudInitDialog import WordCloudInitDialog

class WordCloudFrame(wx.Frame): 
    
    def __init__(self, parent, id, title="Word Cloud Creator"):
        wx.Frame.__init__(self, parent, id, title, size=(550,500))

        panel = wx.Panel(self, -1)

        main_box = wx.BoxSizer(wx.VERTICAL)

        # these go in first box
        label_box = wx.BoxSizer(wx.HORIZONTAL)
        
        subsets_label = wx.StaticText(panel, -1, "Subsets")
        subsets_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        subsets_label.SetSize(subsets_label.GetBestSize())
        label_box.Add(subsets_label, flag = wx.ALIGN_LEFT)
        
        corpus_label = wx.StaticText(panel, -1, "Corpus")
        corpus_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        corpus_label.SetSize(subsets_label.GetBestSize())
        label_box.Add(corpus_label, flag = wx.ALIGN_RIGHT)
        
        main_box.Add(label_box)
        
        # two scroll lists will go in second box
        list_box = wx.BoxSizer(wx.HORIZONTAL) # this variable name sucks.
        
        subset_list = wx.ListBox(panel, choices = ["herp", "derp"])
        list_box.Add(subset_list, flag = wx.ALIGN_LEFT)
        
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
        
        list_box.Add(switch_box, flag = wx.ALIGN_CENTER)
        
        corpus_list = wx.ListBox(panel, choices = ["lerp", "nerp"])
        list_box.Add(corpus_list, flag = wx.ALIGN_RIGHT)
        
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
        dia = WordCloudInitDialog(self, -1, 'Word Cloud Setup')
        dia.ShowModal()
        self.opinions = dia.opinion_list
        for opin in self.opinions:
            print opin.output_filename
                
        
    def OnAddSubset(self, event):
        dia = WordCloudSorterDialog(self, -1, 'Subset Builder')
        dia.ShowModal()
        dia.Destroy()
        
    
    def OnViewSubset(self, event):
        pass
    
    
    def OnCreateWordCloud(self, event):
        pass
    
    
    def OnAddOne(self, event):
        pass
    
    
    def OnRemoveOne(self, event):
        pass
    
    
    def OnAddAll(self, event):
        pass
    
    
    def OnRemoveAll(self, event):
        pass
    
    
        
        
