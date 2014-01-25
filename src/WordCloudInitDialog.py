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
        panel = wx.Panel(self, -1)
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        info = wx.StaticText(panel, -1, "this is where info about loading opinions goes")
        info.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD))
        info.SetSize(info.GetBestSize())
        main_box.Add(info, flag = wx.ALIGN_CENTER)
        
        done = wx.Button(panel, wx.ID_CLOSE, "Done")
        done.Bind(wx.EVT_BUTTON, self.OnDone)
        main_box.Add(done, flag = wx.ALIGN_CENTER)
        
        panel.SetSizer(main_box)
        panel.Layout()

        
        
    def OnDone(self, event):
        self.Destroy()


        