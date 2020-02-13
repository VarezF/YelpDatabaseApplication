import wx
import wx.grid as gridlib
from BusinessDetailsPopup import BusinessDetailsPopup
import csv
import psycopg2


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(600, 500))

        con = psycopg2.connect(database="postgres", user="postgres", password="Spring*2014", host="127.0.0.1", port="5432")
        print("Database opened successfully")
        self.cur = con.cursor()
        self.cur.execute("DROP TABLE Businesses")

        self.cur.execute('''CREATE TABLE Businesses
              (ID VARCHAR PRIMARY KEY     NOT NULL,
              Name TEXT,
              State TEXT,
              City TEXT);''')

        with open('milestone1db.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip first row
            for row in reader:
                self.cur.execute("INSERT INTO Businesses(ID, Name, State, City) VALUES ("
                            + "\'" + row[0] + "\',"
                            + "\'" + row[1] + "\',"
                            + "\'" + row[2] + "\',"
                            + "\'" + row[3] + "\'"
                            ");")

        state_choices = self.getStates()

        select_location_sizer = wx.GridBagSizer(0, 0)
        select_location_panel = wx.Panel(self)
        select_location_panel.SetBackgroundColour(wx.WHITE)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "State"),
                                  pos=(0, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_state_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30), choices=state_choices)
        self.select_state_dd.Bind(wx.EVT_COMBOBOX, self.updateCities)
        select_location_sizer.Add(self.select_state_dd, pos=(0, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.Add(wx.StaticText(select_location_panel, -1, "City"),
                                  pos=(1, 0), span=wx.DefaultSpan, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        self.select_city_dd = wx.ComboBox(select_location_panel, -1, size=(200, 30))
        self.select_city_dd.Bind(wx.EVT_COMBOBOX, self.updateGrid)
        select_location_sizer.Add(self.select_city_dd, pos=(1, 1), span=wx.DefaultSpan, flag=wx.ALL, border=10)

        select_location_sizer.AddGrowableCol(1)

        select_location_panel.SetSizerAndFit(select_location_sizer)

        grid_panel = wx.Panel(self)
        grid_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_results = gridlib.Grid(grid_panel)
        self.grid_results.CreateGrid(numRows=0, numCols=3)  # replace row, col with number of results
        self.grid_results.SetColSize(0, 250)
        self.grid_results.SetColLabelValue(0, "Name")
        self.grid_results.SetColSize(1, 50)
        self.grid_results.SetColLabelValue(1, "State")
        self.grid_results.SetColSize(2, 100)
        self.grid_results.SetColLabelValue(2, "City")
        self.grid_results.Bind(gridlib.EVT_GRID_SELECT_CELL, self.open_more_info)
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
    def open_more_info(self, event):
        if self.business_details is not None:
            self.business_details.Destroy()

        row = event.GetRow()
        name = self.grid_results.GetCellValue(row, 0)
        state = self.grid_results.GetCellValue(row, 1)
        city = self.grid_results.GetCellValue(row, 2)
        # Query info and create popup (below is an example
        self.business_details = BusinessDetailsPopup(self, name=name, state=state, city=city,
                                                no_businesse_state="36", no_businesses_city="2")
        self.business_details.Show()

    #### on new state or city selection, update grid
    def updateCities(self, e):
        if self.select_state_dd.GetSelection() is not None:
            self.select_city_dd.Clear()
            for city in self.getCities(self.select_state_dd.GetStringSelection()):
                self.select_city_dd.Append(city)

    def updateGrid(self, e):
        state = self.select_state_dd.GetStringSelection()
        city = self.select_city_dd.GetStringSelection()

        self.cur.execute("SELECT Name FROM Businesses WHERE City= \'" + city + "\' AND State= \'" + state + "\' ORDER BY Name")
        names = list()
        for tup in self.cur.fetchall():
            names.append(str(tup[0]))

        if len(names) > self.grid_results.NumberRows:
            self.grid_results.AppendRows(len(names) - self.grid_results.NumberRows)

        for row_idx in range(0, len(names)):
            self.grid_results.SetCellValue(row_idx, 0, names[row_idx])
            self.grid_results.SetCellValue(row_idx, 1, state)
            self.grid_results.SetCellValue(row_idx, 2, city)

        self.Layout()
        self.Update()

    def getCities(self, state):
        self.cur.execute("SELECT DISTINCT City  FROM Businesses WHERE state= \'" + state + "\' ORDER BY city")
        rows = self.cur.fetchall()
        cities = list()
        for tup in rows:
            cities.append(str(tup[0]))
        return cities

    def getStates(self):
        self.cur.execute("SELECT DISTINCT State  FROM Businesses  ORDER BY State")
        rows = self.cur.fetchall()
        states = list()
        for tup in rows:
            states.append(str(tup[0]))
        return states



class YelpApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'Yelp App')
        frame.Show(True)
        return True



app = YelpApp(0)
app.MainLoop()
