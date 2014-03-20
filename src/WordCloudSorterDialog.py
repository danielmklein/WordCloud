import wx
# TODO REMOVE ME:
from src.WordCloudCore import WordCloudCore

class WordCloudSorterDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.16.2014    
    '''
    
    def __init__(self, parent, dialog_id, title="Subset Builder"):
        wx.Dialog.__init__(self, parent, dialog_id, title, size=(500, 400))
        self.parent = parent
        panel = wx.Panel(self, -1)
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        #######################################################################
        # boxsizer for name input
        #######################################################################
        name_box = wx.BoxSizer(wx.HORIZONTAL)
        name_label = wx.StaticText(panel, -1, "Subset Name:  ")
        name_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        name_box.Add(name_label, flag=wx.ALL)
        self.name_input = wx.TextCtrl(panel, -1, 'Enter Subset Name', 
                                      size=(300, 30))
        name_box.Add(self.name_input, flag=wx.ALL)
        main_box.Add(name_box, flag=wx.ALL, border=10)

        #######################################################################
        # box sizer for "phase" -- field selector with allowed values input
        #######################################################################
        phase_box = wx.BoxSizer(wx.VERTICAL)
        
        phase_label = wx.StaticText(panel, -1, "PHASE 1")
        phase_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        phase_box.Add(phase_label, flag=wx.CENTER|wx.ALL)
        field_box = wx.BoxSizer(wx.HORIZONTAL)
        field_label = wx.StaticText(panel, -1, "Field to Sort:")
        field_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.field_selector = wx.ComboBox(panel, 
                                    choices=self.parent.wc_core.field_names)
        field_box.Add(field_label, flag=wx.ALIGN_LEFT, border=10)
        field_box.Add(self.field_selector, flag=wx.ALL, border=10)
        phase_box.Add(field_box, flag=wx.ALL, border=10)
        
        allowed_box = wx.BoxSizer(wx.HORIZONTAL)  
        allowed_label = wx.StaticText(panel, -1, "Allowed Values:")
        allowed_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))        
        self.allowed_input = wx.TextCtrl(panel, -1, 
                                         "Enter comma-separated values", 
                                         size=(400,30))
        allowed_box.Add(allowed_label, flag=wx.ALIGN_LEFT, border=10)
        allowed_box.Add(self.allowed_input, flag=wx.ALL, border=10)
        phase_box.Add(allowed_box, flag=wx.ALL, border=10)
        main_box.Add(phase_box, flag=wx.ALL, border=10)
        
        #######################################################################
        # boxsizer for the button to add a phase
        #######################################################################
        add_phase_box = wx.BoxSizer(wx.HORIZONTAL)
        add_phase = wx.Button(panel, wx.ID_CLOSE, " + Add New Phase ", 
                              style=wx.BU_EXACTFIT, size=(200,40))
        add_phase.Bind(wx.EVT_BUTTON, self.OnAddPhase)
        add_phase_box.Add(add_phase, flag=wx.ALL, border=10)
        main_box.Add(add_phase_box, flag=wx.ALIGN_CENTER)
        
        #######################################################################
        # boxsizer for the invert checkbox
        #######################################################################
        invert_box = wx.BoxSizer(wx.HORIZONTAL)
        self.checkbox = wx.CheckBox(panel, label="Invert Subset")
        invert_box.Add(self.checkbox, flag=wx.ALIGN_LEFT)
        main_box.Add(invert_box)
        
        #######################################################################
        # sizer for create and cancel buttons
        #######################################################################
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        create = wx.Button(panel, wx.ID_CLOSE, "Create Subset")
        create.Bind(wx.EVT_BUTTON, self.OnCreateSubset)
        button_box.Add(create, 0, wx.ALL, 10)
        
        cancel = wx.Button(panel, wx.ID_CLOSE, "Cancel")
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        button_box.Add(cancel, 0, wx.ALL, 10)
        main_box.Add(button_box, flag=wx.ALIGN_CENTER)
        
        panel.SetSizer(main_box)
        panel.Layout()
        
        
    def OnAddPhase(self, event):
        pass
    
    
    def OnCreateSubset(self, event):
        '''
        Collect the data we need -- the name, the sort field, the list of 
        accepted values, and whether or not we should invert the subset,
        create a new subset from that info, and add it to the list.
        '''
        subset_name = self.name_input.GetValue()
        sort_field_index = self.field_selector.GetCurrentSelection()
        sort_field = self.parent.wc_core.field_names[sort_field_index]
        accepted_values = self.parse_accepted_values( 
                                self.allowed_input.GetValue())
        should_invert = self.checkbox.GetValue()
        new_subset = self.parent.wc_core.create_subset(
                                        self.parent.wc_core.opinion_list,
                                        sort_field, accepted_values,
                                        should_invert)
        test_list = [subset_name, sort_field, accepted_values, new_subset]
        
        self.parent.wc_core.add_subset(subset_name, new_subset)
        # test output
        print str(test_list)
        # /test output
        self.Destroy()
        
    
    def OnCancel(self, event):
        self.Destroy()
        
    
    def parse_accepted_values(self, value_string):
        '''
        This method should take a string of the entered accepted values
        and return a python list of accepted values.
        '''
        # TODO: it may be wise to refine this in the future.
        raw_values = value_string.split(",")
        return [value.strip() for value in raw_values]

'''
# TODO DELETE ME, I'M JUST FOR TESTING
app = wx.App()
frame = wx.Frame(None, -1, "testing")
frame.wc_core = WordCloudCore()


dia = WordCloudSorterDialog(frame, -1, 'Subset Builder')
dia.ShowModal()
dia.Destroy()
'''