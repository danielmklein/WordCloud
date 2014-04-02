import wx

class WordCloudGenerationDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    3.31.2014    
    
    This implements the dialog box that displays info about the process
    of creating a word cloud from the given subset and corpus. As this
    process currently can take a long time, this dialog box is important
    to display important info, like progress and such.
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        