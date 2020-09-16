# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)


        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"거래처명", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer9.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_txtName = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_txtName, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"전화번호", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer9.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_txtTel = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_txtTel, 0, wx.ALL, 5)

        self.m_btnInsert = wx.Button(self.m_panel4, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_btnInsert, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer9)
        self.m_panel4.Layout()
        bSizer9.Fit(self.m_panel4)
        bSizer7.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl4 = wx.ListCtrl(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 120),wx.LC_REPORT)
        bSizer10.Add(self.m_listCtrl4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel5.SetSizer(bSizer10)
        self.m_panel5.Layout()
        bSizer10.Fit(self.m_panel5)
        bSizer7.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"거래수", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer11.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_staCount = wx.StaticText(self.m_panel6, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staCount.Wrap(-1)
        bSizer11.Add(self.m_staCount, 0, wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer11)
        self.m_panel6.Layout()
        bSizer11.Fit(self.m_panel6)
        bSizer7.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.m_listCtrl4.InsertColumn(0,"거래처이름", width=200)
        self.m_listCtrl4.InsertColumn(0, "전화번호", width=200)

        self.m_btnInsert.Bind(wx.EVT_BUTTON, self.onInsert)

        self.Centre(wx.BOTH)

    def onInsert(self, e):
        name = self.m_txtName.GetValue()
        tel = self.m_txtTel.GetValue()

        i = self.m_listCtrl4.InsertItem(1000, 0)
        self.m_listCtrl4.SetItem(i, 0, name)
        self.m_listCtrl4.SetItem(i, 1, tel)

        self.m_staCount.SetLabelText(str(self.m_listCtrl4.GetItemCount()))

        self.m_txtName.SetValue("")
        self.m_txtTel.SetValue("")
        self.m_txtName.SetFocus()

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    MyFrame2(None).Show(True)
    app.MainLoop()