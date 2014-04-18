import wx
# TODO REMOVE ME:
from src.core.python.WordCloudCore import WordCloudCore

class Phase(object):
    def __init__(self, sort_field, allowed_values):
        self.sort_field = sort_field
        self.allowed_values = allowed_values
        

class WordCloudSorterDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.16.2014    
    
    This implements the dialog box through which the user can create a new
    opinion subset, giving it a name and define how the body of opinions should
    be filtered to define the subset.
    '''
    
    def __init__(self, parent, dialog_id, title="Subset Builder"):
        wx.Dialog.__init__(self, parent, dialog_id, title, size=(500, 1000))
        self.parent = parent
        self.phases = [Phase("", "")]
        
        self.create_panel()
        

    def create_panel(self):
        self.panel = wx.Panel(self, -1)
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        
        #######################################################################
        # boxsizer for name input
        #######################################################################
        name_box = wx.BoxSizer(wx.HORIZONTAL)
        name_label = wx.StaticText(self.panel, -1, "Subset Name:  ")
        name_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        name_box.Add(name_label, flag=wx.ALL)
        self.name_input = wx.TextCtrl(self.panel, -1, 'Enter Subset Name', 
                                      size=(300, 30))
        name_box.Add(self.name_input, flag=wx.ALL)
        self.main_box.Add(name_box, flag=wx.ALL, border=10)

        #######################################################################
        # box sizer for "phase" -- field selector with allowed values input
        #######################################################################
        self.phase_box = wx.BoxSizer(wx.VERTICAL)
        
        self.build_phases()

        self.main_box.Add(self.phase_box, flag=wx.ALL, border=10)
        
        #######################################################################
        # boxsizer for the button to add a phase
        #######################################################################
        self.add_phase_box = wx.BoxSizer(wx.HORIZONTAL)
        add_phase = wx.Button(self.panel, wx.ID_CLOSE, " + Add New Phase ", 
                              style=wx.BU_EXACTFIT, size=(200,40))
        add_phase.Bind(wx.EVT_BUTTON, self.OnAddPhase)
        self.add_phase_box.Add(add_phase, flag=wx.ALL, border=10)
        self.main_box.Add(self.add_phase_box, flag=wx.ALIGN_CENTER)
        
        #######################################################################
        # boxsizer for the invert checkbox
        #######################################################################
        self.invert_box = wx.BoxSizer(wx.HORIZONTAL)
        self.checkbox = wx.CheckBox(self.panel, label="Invert Subset")
        self.invert_box.Add(self.checkbox, flag=wx.ALIGN_LEFT)
        self.main_box.Add(self.invert_box)
        
        #######################################################################
        # sizer for create and cancel buttons
        #######################################################################
        self.button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        create = wx.Button(self.panel, wx.ID_CLOSE, "Create Subset")
        create.Bind(wx.EVT_BUTTON, self.OnCreateSubset)
        self.button_box.Add(create, 0, wx.ALL, 10)
        
        cancel = wx.Button(self.panel, wx.ID_CLOSE, "Cancel")
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        self.button_box.Add(cancel, 0, wx.ALL, 10)
        
        self.main_box.Add(self.button_box, flag=wx.ALIGN_CENTER)
        self.panel.SetSizer(self.main_box)
        self.panel.Layout()
        self.panel.Fit()
        self.Fit()
        
        
    def build_phases(self):
        
        self.phase_box = wx.BoxSizer(wx.VERTICAL)
        
        for index in range(len(self.phases)):  
            single_phase = wx.BoxSizer(wx.VERTICAL)
            
            phase_label = wx.StaticText(self.panel, -1, "PHASE {0}".format(index+1))
            phase_label.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
            single_phase.Add(phase_label, flag=wx.CENTER|wx.ALL)
            field_box = wx.BoxSizer(wx.HORIZONTAL)
            field_label = wx.StaticText(self.panel, -1, "Field to Sort:")
            field_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
            self.field_selector = wx.ComboBox(self.panel, 
                                        choices=self.parent.wc_core.field_names)
            field_box.Add(field_label, flag=wx.ALIGN_LEFT, border=10)
            field_box.Add(self.field_selector, flag=wx.ALL, border=10)
            single_phase.Add(field_box, flag=wx.ALL, border=10)
            
            allowed_box = wx.BoxSizer(wx.HORIZONTAL)  
            allowed_label = wx.StaticText(self.panel, -1, "Allowed Values:")
            allowed_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))        
            self.allowed_input = wx.TextCtrl(self.panel, -1, 
                                             "Enter comma-separated values", 
                                             size=(400,30))
            allowed_box.Add(allowed_label, flag=wx.ALIGN_LEFT, border=10)
            allowed_box.Add(self.allowed_input, flag=wx.ALL, border=10)
            single_phase.Add(allowed_box, flag=wx.ALL, border=10)
            self.phase_box.Add(single_phase, flag=wx.ALL, border=10)
        
        
    def OnAddPhase(self, event):
        self.phases.append(Phase("", ""))
        # test output
        print self.phases
        # /test output
        #self.phase_box.Destroy()
        # TODO: what the heck do I do here?
        self.panel.Destroy()
        self.create_panel()
        
        self.Fit()
    
    
    def OnCreateSubset(self, event):
        '''
        Collect the data we need -- the name, the sort field, the list of 
        accepted values, and whether or not we should invert the subset,
        create a new subset from that info, and add it to the list.
        '''
        '''
        TODO: figure out what to do when we have multiple phases of filtering
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


# TODO DELETE ME, I'M JUST FOR TESTING
app = wx.App()
frame = wx.Frame(None, -1, "testing")
frame.wc_core = WordCloudCore()


dia = WordCloudSorterDialog(frame, -1, 'Subset Builder')
dia.ShowModal()
dia.Destroy()
