import wx
from src.gui.WordCloudFrame import WordCloudFrame

'''
First, load opinions from pickle files.
Then display the main dialog window; from the main dialog window the user 
can build a new subset, view the list of opinions in a selected subset, 
add/delete subsets from the corpus, and select a subset for which to generate
a word cloud.
If the user clicks on "Build New Subset", the sorter dialog box opens,
which allows the user to name the new subset, choose the field on which to 
sort, and enter allowed values for that field to build the subset. 
'''
 
def main():
    word_cloud_app = wx.App()
    frame = WordCloudFrame(None, -1, 'Word Cloud Creator')
    frame.Show()
    word_cloud_app.MainLoop()
    

main()



        