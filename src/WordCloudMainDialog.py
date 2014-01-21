import wx

class WordCloudMainDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.16.2014

    '''


    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(350,300))
        # build main display here -- buttons, scroll fields, etc.