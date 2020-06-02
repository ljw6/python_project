# -*- coding: utf-8 -*-
import wx
import wx.xrc
import wx.html
import wx.html2
from hhsh import process
from feiyan import search
from news_check import proces
from word_cloud import main
import webbrowser as wb
class window2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"能不能好好说话", pos=wx.DefaultPosition, size=wx.Size(-1, 561))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        big_box = wx.BoxSizer(wx.VERTICAL)

        self.logo = wx.StaticBitmap(self, wx.ID_ANY,
                                    wx.Bitmap(u"C:\\Users\\吕佳伟\\Pictures\\logo.bmp", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        big_box.Add(self.logo, 0, wx.ALL, 5)

        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        box = wx.BoxSizer(wx.VERTICAL)

        grid_size = wx.GridBagSizer(0, 0)
        grid_size.SetFlexibleDirection(wx.BOTH)
        grid_size.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        grid_size.SetMinSize(wx.Size(-1, 12))
        self.text1 = wx.TextCtrl(self.panel, wx.ID_ANY, u"输入", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.text1.SetMaxLength(100)
        grid_size.Add(self.text1, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.search = wx.Button(self.panel, wx.ID_ANY, u"检索", wx.DefaultPosition, wx.DefaultSize, 0)
        grid_size.Add(self.search, wx.GBPosition(0, 16), wx.GBSpan(1, 1), wx.ALL, 5)

        box.Add(grid_size, 1, wx.EXPAND, 5)

        self.text2 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                 wx.TE_READONLY|wx.TE_MULTILINE)
        self.text2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.text2.SetMinSize(wx.Size(620, -1))
        self.text2.SetMaxSize(wx.Size(620, -1))

        box.Add(self.text2, 5, wx.ALL, 5)

        self.panel.SetSizer(box)
        self.panel.Layout()
        box.Fit(self.panel)
        big_box.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(big_box)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.search.Bind(wx.EVT_BUTTON, self.fuction1)
        self.Show(True)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def fuction1(self, event):
        x = self.text1.GetValue()
        s=''
        name,res = process(x)
        for r in res:
            s = r+"\n"+s
        self.text2.SetValue(s)


class News(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"新闻工具", pos=wx.DefaultPosition, size=wx.Size(545, 441))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"新闻热点", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button3, 0, wx.ALL, 5)

        self.panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        box = wx.BoxSizer(wx.VERTICAL)

        grid_size = wx.GridBagSizer(0, 0)
        grid_size.SetFlexibleDirection(wx.BOTH)
        grid_size.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        grid_size.SetMinSize(wx.Size(-1, 12))
        self.biaoti = wx.TextCtrl(self.panel3, wx.ID_ANY, u"输入标题", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.biaoti.SetMaxLength(100)
        grid_size.Add(self.biaoti, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.check = wx.Button(self.panel3, wx.ID_ANY, u"检索", wx.DefaultPosition, wx.DefaultSize, 0)
        grid_size.Add(self.check, wx.GBPosition(0, 16), wx.GBSpan(1, 1), wx.ALL, 5)

        box.Add(grid_size, 1, wx.EXPAND, 5)

        self.anwser = wx.TextCtrl(self.panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                  wx.TE_READONLY)
        self.anwser.SetFont( wx.Font( 28, 70, 90, 92, False, wx.EmptyString ) )
        self.anwser.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.anwser.SetMinSize(wx.Size(620, -1))
        self.anwser.SetMaxSize(wx.Size(620, -1))

        box.Add(self.anwser, 5, wx.ALL, 5)

        self.panel3.SetSizer(box)
        self.panel3.Layout()
        box.Fit(self.panel3)
        bSizer7.Add(self.panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.hot)
        self.check.Bind(wx.EVT_BUTTON, self.biaotidang)
        self.Show(True)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def hot(self, event):
        main()

    def biaotidang(self, event):
        st = self.biaoti.GetValue()
        s = proces(st)
        self.anwser.SetValue(s)

class Feiyan(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"国内疫情", pos=wx.DefaultPosition,
                          size=wx.Size(644, 512))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, u"输入省份", wx.Point(-1, -1), wx.Size(400, -1), 0)
        self.m_textCtrl3.SetMinSize(wx.Size(620, -1))
        self.m_textCtrl3.SetMaxSize(wx.Size(640, -1))

        bSizer22.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"查询", wx.Point(-1, -1), wx.Size(620, -1), 0)
        bSizer22.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"feiyan2.bmp",
                                                                    wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.Size(-1, -1), 0)
        bSizer22.Add(self.m_bitmap2, 0, wx.ALL, 5)

        self.SetSizer(bSizer22)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.jieshou)
        self.Show(True)
    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def jieshou(self, event):
        x = self.m_textCtrl3.GetValue()
        search(x)
class window1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"工具盒子", pos=wx.DefaultPosition, size=wx.Size(763, 582))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.feiyan = wx.BitmapButton(self, wx.ID_ANY,
                                      wx.Bitmap(u"feiyan.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.feiyan, 0, wx.ALL, 5)

        gSizer1.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.biaoti = wx.BitmapButton(self, wx.ID_ANY,
                                      wx.Bitmap(u"news.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.biaoti, 0, wx.ALL, 5)

        gSizer1.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.hhsh = wx.BitmapButton(self, wx.ID_ANY,
                                    wx.Bitmap(u"speak1.bmp", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.hhsh, 0, wx.ALL, 5)

        gSizer1.Add(bSizer12, 1, wx.EXPAND, 5)

        # self.SetSizer(gSizer1)
        # self.Layout()
        #
        # self.Centre(wx.BOTH)
        #
        bSizer91 = wx.BoxSizer(wx.VERTICAL)

        self.mine = wx.BitmapButton(self, wx.ID_ANY,
                                    wx.Bitmap(u"four.bmp", wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer91.Add(self.mine, 0, wx.ALL, 5)

        gSizer1.Add(bSizer91, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.feiyan.Bind(wx.EVT_BUTTON, self.f)
        self.biaoti.Bind(wx.EVT_BUTTON, self.c)
        self.hhsh.Bind(wx.EVT_BUTTON, self.h)
        self.mine.Bind(wx.EVT_BUTTON,self.tomine)
        self.Show(True)
    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def f(self, event):
        Feiyan(None)
    def c(self, event):
        News(None)
    def h(self, event):
        window2(None)
    def tomine(self, event):
        wb.open("https://github.com/ljw6/python_project")

#
# ###########################################################################
# ## Class window1
# ###########################################################################
#

app = wx.App(False)
x=window1(None)
app.MainLoop()