import wx
from WordCloudInitDialog import WordCloudInitDialog
from WordCloudMainDialog import WordCloudMainDialog
from WordCloudSorterDialog import WordCloudSorterDialog

class WordCloudApp(wx.App):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.16.2014    
    '''


    def run(self):
        app = wx.App()

        frame = WordCloudFrame(None, -1, 'Word Cloud')
        # so we load all the opinions first, display some
        # info about that process
        
        # then we want to display the main dialog window
        #   from the main dialog window the user can build a new subset,
        #   view the list of opinions in a current subset, add/delete subsets
        #   from the corpus, and select a subset from which to generate a WC
        
        # if the user clicks on "Build New Subset", the sorter dialog box opens,
        # which allows the user to name the new subset, choose the field to sort on,
        # and enter allowed values for that field to build the subset. also present
        # should be a check box to invert the above subset (create the complement)
        
        frame.Show()
        frame.Centre()
        
        app.MainLoop()
       

class WordCloudFrame(wx.Frame): 
    
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(550,500))

        panel = wx.Panel(self, -1)
        self.RunSetupDialog()
        self.RunMainDialog()
        
        #wx.Button(panel, 1, 'Show Custom Dialog', (100,100))
        #self.Bind (wx.EVT_BUTTON, self.OnShowCustomDialog, id=1)
        

    def RunMainDialog(self):
        dia = WordCloudMainDialog(self, -1, 'Word Cloud Creator')
        dia.ShowModal()
        dia.Destroy()
        
        
    def RunSetupDialog(self):
        dia = WordCloudInitDialog(self, -1, 'Word Cloud Setup')
        dia.ShowModal()
        dia.Destroy()
        
        
word_cloud_app = WordCloudApp(0)
word_cloud_app.run()

        