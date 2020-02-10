import wx
import wx.grid as gridlib


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(500, 500))

        select_location_sizer = wx.GridBagSizer(0, 0)
        select_location_panel = wx.Panel(self)
        select_location_panel.SetBackgroundColour(wx.WHITE)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "State"),
                                  pos=(0, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_state_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30))
        select_location_sizer.Add(self.select_state_dd, pos=(0, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "City"),
                                  pos=(1, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_city_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30))
        select_location_sizer.Add(self.select_city_dd, pos=(1, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.AddGrowableCol(1)

        select_location_panel.SetSizerAndFit(select_location_sizer)

        grid_panel = wx.Panel(self)
        grid_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_results = gridlib.Grid(grid_panel)
        self.grid_results.CreateGrid(12, 8)
        self.grid_results.Bind(gridlib.EVT_GRID_SELECT_CELL, self.openMoreInfo())
        grid_sizer.Add(self.grid_results, -1, wx.ALL, 20)

        grid_panel.SetSizerAndFit(grid_sizer)

        sizer = wx.GridBagSizer(0, 0)
        sizer.Add(select_location_panel, pos=(0, 0), span=wx.DefaultSpan, flag=wx.EXPAND)
        sizer.Add(grid_panel, pos=(1, 0), span=wx.DefaultSpan, flag=wx.EXPAND)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableRow(1)
        self.SetSizer(sizer)

    def openMoreInfo(self):
        return


class YelpApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'Yelp App')
        frame.Show(True)
        return True


app = YelpApp(0)
app.MainLoop()
