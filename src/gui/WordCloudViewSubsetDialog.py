import wx

class WordCloudViewSubsetDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    4.22.2014  
    
    This dialog box displays a list of the documents in a subset and allows
    the user to view more info about a given document in the subset.
    '''
    

    def __init__(self, parent, wc_core, subset_name, title="View Subset"):
        super(WordCloudViewSubsetDialog, self).__init__(self, parent, -1, title, size=(500, 1000))
        self.parent = parent
        self.wc_core = wc_core
        self.subset_name = subset_name
        
        self.panel = wx.Panel(self, -1)
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        
        self.name_label = wx.StaticText(self.panel, -1, 
                                   "Subset Name:  {0}".format(self.subset_name))
        
        self.subset = self.wc_core.subsets[self.subset_name]
        self.titles = [doc.doc_metadata.case_title for doc in self.subset]
        self.doc_list = wx.ListBox(self.panel, size=(500, 500), 
                                      choices=self.titles)
        
        self.view_details = wx.Button(self.panel, wx.ID_CLOSE, "View Document Details")
        self.view_details.Bind(wx.EVT_BUTTON, self.OnViewDetails)
        
        self.main_box.Add(self.name_label)
        self.main_box.Add(self.doc_list)
        self.main_box.Add(self.view_details)
        
        self.panel.SetSizer(self.main_box)
        self.panel.Layout()
        self.panel.Fit()
        self.Fit()
        
        
    def OnViewDetails(self, event):
        title = self.titles[self.doc_list.GetSelection()]
        for item in self.subset:
            if title == item.doc_metadata.case_title:
                document = item
                break
        else:
            raise Exception("Should have been able to find document in list, but couldn't.")
        dia = WordCloudViewDocDetailsDialog(self, document, "View Details")
        dia.ShowModal()
        dia.Destroy()
        
    
    

class WordCloudViewDocDetailsDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    4.26.2014  
    
    This dialog box displays the details about a document in a subset.
    '''
    
    '''
    TODO: This should really call the Document's build_display_string method instead 
    of building the display here piece by piece.
    '''
    
    def __init__(self, parent, document, title="View Details"):
        wx.Dialog.__init__(self, parent, -1, title, size=(1000, 1000))
        self.panel = wx.Panel(self, -1)
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        '''
        TODO: fit text to width (especially opinion_text)
        '''
        case_title = wx.StaticText(self.panel, -1, 
                                   "Case Title:  {0}".format(document.doc_metadata.case_title))
        case_cite = wx.StaticText(self.panel, -1,
                                  "Case Citation: {0}".format(document.doc_metadata.case_full_cite))
        case_dates = wx.StaticText(self.panel, -1,
                                   "Case Dates: {0}".format(document.doc_metadata.case_dates))
        case_disposition = wx.StaticText(self.panel, -1,
                                         "Case Disposition: {0}".format(document.doc_metadata.case_disposition))
        opinion_author = wx.StaticText(self.panel, -1,
                                       "Opinion Author: {0}".format(document.doc_metadata.opinion_author))
        opinion_text_label = wx.StaticText(self.panel, -1, "Opinion Text:")
        opinion_text = wx.StaticText(self.panel, -1, document.doc_text)
        
        self.main_box.Add(case_title)
        self.main_box.Add(case_cite)
        self.main_box.Add(case_dates)
        self.main_box.Add(case_disposition)
        self.main_box.Add(opinion_author)
        self.main_box.Add(opinion_text_label)
        self.main_box.Add(opinion_text)
        self.panel.SetSizer(self.main_box)
        self.panel.Layout()
        self.panel.Fit()
        self.Fit()
    
    
        