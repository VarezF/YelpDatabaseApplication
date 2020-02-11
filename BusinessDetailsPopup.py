import wx
import wx.grid as gridlib


class BusinessDetailsPopup(wx.Frame):
    def __init__(self, parent, name, state, city, no_businesse_state, no_businesses_city):
        wx.Frame.__init__(self, parent, title="Business Details", size=wx.Size(700, 300))
        self.SetBackgroundColour(wx.WHITE)
        sizer = wx.GridBagSizer(0, 0)

        sizer.Add(wx.StaticText(self, -1, "Business Name"),
                  pos=(0, 0), span=wx.DefaultSpan, flag=wx.ALL, border=10)
        self.business_name_label = wx.StaticText(self, -1, name)
        sizer.Add(self.business_name_label, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)

        sizer.Add(wx.StaticText(self, -1, "State"),
                  pos=(1, 0), span=wx.DefaultSpan, flag=wx.ALL, border=10)
        self.business_name_label = wx.StaticText(self, -1, state)
        sizer.Add(self.business_name_label, pos=(1, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)

        sizer.Add(wx.StaticText(self, -1, "City"),
                  pos=(2, 0), span=wx.DefaultSpan, flag=wx.ALL, border=10)
        self.business_name_label = wx.StaticText(self, -1, city)
        sizer.Add(self.business_name_label, pos=(2, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)

        sizer.Add(wx.StaticText(self, -1, "Number of businesses in " + str(state)),
                  pos=(3, 0), span=wx.DefaultSpan, flag=wx.ALL, border=10)
        self.business_name_label = wx.StaticText(self, -1, no_businesse_state)
        sizer.Add(self.business_name_label, pos=(3, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)

        sizer.Add(wx.StaticText(self, -1, "Number of businesses in " + str(city)),
                  pos=(4, 0), span=wx.DefaultSpan, flag=wx.ALL, border=10)
        self.business_name_label = wx.StaticText(self, -1, no_businesses_city)
        sizer.Add(self.business_name_label, pos=(4, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)

        sizer.AddGrowableCol(1)
        self.SetSizerAndFit(sizer)

        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.onClose)

    def onClose(self):
        self.Destroy()

