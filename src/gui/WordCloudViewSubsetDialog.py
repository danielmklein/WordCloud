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
        wx.Dialog.__init__(self, parent, -1, title, size=(500, 1000))
        self.parent = parent
        self.wc_core = wc_core
        self.subset_name = subset_name
        
        self.panel = wx.Panel(self, -1)
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        
        self.name_label = wx.StaticText(self.panel, -1, 
                                   "Subset Name:  {0}".format(self.subset_name))
        
        subset = self.wc_core.subsets[self.subset_name]
        titles = [doc.doc_metadata.case_title for doc in subset]
        self.doc_list = wx.ListBox(self.panel, size=(500, 500), 
                                      choices=titles)
        
        
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
        '''
        TODO: populate the text for this dialog box. Maybe this shouldn't 
        be a MessageDialog, but rather something else.
        '''
        info_string = "This is where I will plop all the document info."
        wx.MessageDialog(None, info_string, "placeholder", wx.OK).ShowModal()
        
        
    def build_info_string(self, subset):
        '''
        TODO: This is terrible. Make it better. It's also really really slow.
        This was taken from WordCloudFrame. I don't think I want to do it this way.
        It's probably better to just create a new type of dialog box to display document info.
        '''
        info_string = "CASE TITLE                 OPINION AUTHOR  OPINION TYPE\n"
        for opinion in subset:
            info_string += opinion.doc_metadata.case_title + "\t"
            info_string += opinion.doc_metadata.opinion_author + "\t"
            info_string += opinion.doc_metadata.opinion_type +"\n"
        return info_string
        
        
        