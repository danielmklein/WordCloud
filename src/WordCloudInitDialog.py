import wx

class WordCloudInitDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.20.2014    
    '''

    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(350,300))
        # show info about loading of opinion files, then
        # display a button to click when user wants to continue


        