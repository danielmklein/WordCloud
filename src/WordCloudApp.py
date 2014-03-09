import wx
from src.WordCloudFrame import WordCloudFrame

# so we load all the opinions first, display some
# info about that process

# then we want to display the main dialog window
#   from the main dialog window the user can build a new subset,
#   view the8 list of opinions in a current subset, add/delete subsets
#   from the corpus, and select a subset from which to generate a WC

# if the user clicks on "Build New Subset", the sorter dialog box opens,
# which allows the user to name the new subset, choose the field to sort on,
# and enter allowed values for that field to build the subset. also present
# should be a check box to invert the above subset (create the complement)
       
word_cloud_app = wx.App()
frame = WordCloudFrame(None, -1, 'Word Cloud Creator')
frame.Show()

word_cloud_app.MainLoop()



        