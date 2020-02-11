import wx
import wx.grid as gridlib
from BusinessDetailsPopup import BusinessDetailsPopup


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(500, 500))

        state_choices=["these", "are", "some", "choices"]  ####
        city_choices=["hello", "world", "hello", "world"]  ####

        select_location_sizer = wx.GridBagSizer(0, 0)
        select_location_panel = wx.Panel(self)
        select_location_panel.SetBackgroundColour(wx.WHITE)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "State"),
                                  pos=(0, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_state_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30), choices=state_choices)
        self.select_state_dd.Bind(wx.EVT_COMBOBOX, self.updateGrid)
        select_location_sizer.Add(self.select_state_dd, pos=(0, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "City"),
                                  pos=(1, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_city_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30), choices=city_choices)
        self.select_city_dd.Bind(wx.EVT_COMBOBOX, self.updateGrid)
        select_location_sizer.Add(self.select_city_dd, pos=(1, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.AddGrowableCol(1)

        select_location_panel.SetSizerAndFit(select_location_sizer)

        grid_panel = wx.Panel(self)
        grid_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_results = gridlib.Grid(grid_panel)
        self.grid_results.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.open_more_info)
        grid_sizer.Add(self.grid_results, -1, wx.ALL, 20)

        grid_panel.SetSizerAndFit(grid_sizer)

        sizer = wx.GridBagSizer(0, 0)
        sizer.Add(select_location_panel, pos=(0, 0), span=wx.DefaultSpan, flag=wx.EXPAND)
        sizer.Add(grid_panel, pos=(1, 0), span=wx.DefaultSpan, flag=wx.EXPAND)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableRow(1)
        self.SetSizer(sizer)

        self.business_details = None

    #### on grid cell selection open new window with more info on specified business
    def open_more_info(self, e):
        print("Event triggered")
        if self.business_details is not None:
            self.business_details.Destroy()
        # Query info and create popup (below is an example
        self.business_details = BusinessDetailsPopup(self, name="McDonalds", state="WA", city="Pullman",
                                                no_businesse_state="36", no_businesses_city="2")
        self.business_details.Show()

    #### on new state or city selection, update grid
    def updateGrid(self, e):
        state = self.select_state_dd.GetStringSelection()
        city = self.select_city_dd.GetStringSelection()

        self.grid_results.CreateGrid(numRows=0, numCols=0)  # replace row, col with number of results



class YelpApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'Yelp App')
        frame.Show(True)
        return True


app = YelpApp(0)
app.MainLoop()
