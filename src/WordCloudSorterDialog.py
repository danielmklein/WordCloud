import wx

class WordCloudSorterDialog(wx.Dialog):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    1.16.2014    
    '''

    def __init__(self, parent, id, title="Subset Builder"):
        wx.Dialog.__init__(self, parent, id, title, size=(350,300))
        # build sorter builder dialog here... dropdown, text boxes, button, etc
        self.parent = parent
        
        panel = wx.Panel(self, -1)
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        name_box = wx.BoxSizer(wx.HORIZONTAL)
        
        name_label = wx.StaticText(panel, -1, "Subset Name:  ")
        name_box.Add(name_label, flag = wx.ALIGN_LEFT)
        
        self.name_input = wx.TextCtrl(panel, -1, 'name goes here')
        name_box.Add(self.name_input, flag = wx.ALIGN_RIGHT)

        main_box.Add(name_box)

        phase_box = wx.BoxSizer(wx.VERTICAL)
        
        phase_label = wx.StaticText(panel, -1, "PHASE 1")
        phase_box.Add(phase_label, flag = wx.ALIGN_LEFT)
        
        field_label = wx.StaticText(panel, -1, "Field to Sort:")
        phase_box.Add(field_label, flag = wx.ALIGN_RIGHT)
        
        self.field_selector = wx.ComboBox(panel, choices = self.parent.wc_core.field_names)
        
        
        phase_box.Add(self.field_selector, flag = wx.ALIGN_RIGHT)
        
        allowed_label = wx.StaticText(panel, -1, "Allowed Values:")
        phase_box.Add(allowed_label, flag = wx.ALIGN_RIGHT)
        
        self.allowed_input = wx.TextCtrl(panel, -1, "allowed values go here")
        phase_box.Add(self.allowed_input, flag = wx.ALIGN_RIGHT)
        main_box.Add(phase_box)
        
        add_phase_box = wx.BoxSizer(wx.HORIZONTAL)
        
        add_phase = wx.Button(panel, wx.ID_CLOSE, " + ", style=wx.BU_EXACTFIT)
        add_phase.Bind(wx.EVT_BUTTON, self.OnAddPhase)
        add_phase_box.Add(add_phase, 0, wx.ALL, 10)
        
        add_phase_label = wx.StaticText(panel, -1, "Add New Phase")
        add_phase_box.Add(add_phase_label)
        main_box.Add(add_phase_box, flag = wx.ALIGN_CENTER)
        
        invert_box = wx.BoxSizer(wx.HORIZONTAL)
        
        checkbox = wx.CheckBox(panel, label = "Invert Subset")
        invert_box.Add(checkbox, flag = wx.ALIGN_LEFT)
        main_box.Add(invert_box)
        
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        create = wx.Button(panel, wx.ID_CLOSE, "Create Subset")
        create.Bind(wx.EVT_BUTTON, self.OnCreateSubset)
        button_box.Add(create, 0, wx.ALL, 10)
        
        cancel = wx.Button(panel, wx.ID_CLOSE, "Cancel")
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        button_box.Add(cancel, 0, wx.ALL, 10)
        main_box.Add(button_box, flag = wx.ALIGN_CENTER)
        
        
        panel.SetSizer(main_box)
        panel.Layout()
        
        
    def OnAddPhase(self, event):
        pass
    
    
    def OnCreateSubset(self, event):
        #self.parent.wc_core.create_subset(self.parent.wc_core.opinion_list,
        #                                  self.sort_field,
        #                                  self.accepted_values)
        subset_name = self.name_input.GetValue()
        sort_field_index = self.field_selector.GetCurrentSelection()
        sort_field = self.parent.wc_core.field_names[sort_field_index]
        accepted_values = self.allowed_input.GetValue()
        
        test_list = [subset_name, sort_field, accepted_values]
        
        self.parent.wc_core.subsets[subset_name] = test_list
        self.parent.wc_core.subset_names.append(subset_name)
        self.parent.subset_list.Set(self.parent.wc_core.subset_names)
        print str(test_list)
        self.Destroy()
        
    
    def OnCancel(self, event):
        self.Destroy()
        
    
    def parse_accepted_values(self, value_string):
        '''
        This method should take a string of the entered accepted values
        and return a python list of accepted values.
        '''
        pass
    
    