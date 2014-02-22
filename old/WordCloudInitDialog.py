import wx
import re
import os, os.path
import cPickle as pickle

# directory containing parsed opinions

OPINION_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_opinions"
PICKLE_PATH = r"C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\test_pickled"

class WordCloudInitDialog(wx.MessageDialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.20.2014    
    '''

    def __init__(self, parent, message, 
                               caption, style=wx.OK):
        self.opinion_list = []
        # TODO: add functionality for packing opinions the first time
        
        wx.MessageDialog.__init__(self, parent, message, caption, style=wx.OK)
        # show info about loading of opinion files, then
        # display a button to click when user wants to continue
        '''self.panel = wx.Panel(self, -1)
        
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        
        self.info = wx.StaticText(self.panel, -1, "Loading opinions?")
        self.info.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.info.SetSize(self.info.GetBestSize())
        self.main_box.Add(self.info, flag = wx.ALIGN_CENTER)
        
        # TODO: make "load" button unclickable after loading first time
        load_opinions = wx.Button(self.panel, wx.ID_CLOSE, "Load")
        load_opinions.Bind(wx.EVT_BUTTON, self.unpack_opinions)
        self.main_box.Add(load_opinions, flag = wx.ALIGN_CENTER)
        
        self.panel.SetSizer(self.main_box)
        self.panel.Layout()'''
        
        
    def unpack_opinions(self, event):
        '''
        Unpickle all of the Document files from PICKLE_PATH into 
        Document objects.      
        '''
        print "Unpacking Document objects from serialized files..."
        
            
        doc_regex = re.compile(r"\.Document$")
        num_unpacked = 0
        num_failed = 0
        
        file_list = os.listdir(PICKLE_PATH)
        for pickle_file in os.listdir(PICKLE_PATH):
            '''
            print "Unpacking Document object from {0}... "\
                    "({1} of {2})".format(pickle_file, num_unpacked+1, 
                                          len(file_list))
            '''
            self.info.SetLabel("Unpacking Document object from {0}... "\
                    "({1} of {2})".format(pickle_file, num_unpacked+1, 
                                          len(file_list)))
            # if a file doesn't have a .Document extension, we ignore it
            is_document_file = re.search(doc_regex, pickle_file)
            if not is_document_file:
                print ("{0} is not file containing a pickled Document,"
                       "so we can't unpack it!".format(pickle_file))
                num_failed += 1
                continue
            # we attempt to un-pickle the file into a Document object
            full_path = os.path.join(PICKLE_PATH, pickle_file)
            with open(full_path, 'r') as doc_file:
                try:
                    unpacked_doc = pickle.load(doc_file)
                    num_unpacked += 1
                    self.opinion_list.append(unpacked_doc)
                except:
                    print "Unable to unpack Document contained in "\
                        "{0}!".format(pickle_file)
                    num_failed += 1
                    continue
        done_string = "Unpacking complete.\n"\
                        "{0} Documents unpacked.\n"\
                        "{1} Documents failed to unpack.\n".format(num_unpacked,num_failed)
        '''
        print "Unpacking complete."
        print "{0} Documents unpacked.".format(num_unpacked)
        print "{0} Documents failed to unpack.".format(num_failed)
        '''
        self.info.SetLabel(done_string)
        
        self.done = wx.Button(self.panel, wx.ID_OK, "Done")
        self.done.Bind(wx.EVT_BUTTON, self.OnDone)
        self.main_box.Add(self.done, flag = wx.ALIGN_CENTER)
        
        return
    
        

        
        
    def OnDone(self, event):
        self.Destroy()


        