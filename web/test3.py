import wx
# 간단한 로그인 프로그램

class LoginFrame(wx.Frame):
    #생략가능
    panel = None
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.loginUI()
        self.Show(True)

    def loginUI(self):
        # 부모클래스에서도 사용이 가능하게 해준다.
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="ID : ", pos=(5, 5))
        wx.StaticText(self.panel, label="pass : ", pos=(5, 40))

        self.m_id=wx.TextCtrl(self.panel, pos = (50, 5), size=(200, -1))
        self.m_pw=wx.TextCtrl(self.panel, pos=(50, 40))

        btn1 = wx.Button(self.panel, label="일반버튼", pos=(5, 100) ,size=(70, -1))
        btn2 = wx.ToggleButton(self.panel, label="토글버튼", pos=(95, 100), size=(70, -1))
        btn3 = wx.Button(self.panel, label="종료", pos=(185, 100), size=(70, -1))

        #btn1.Bind(wx.EVT_BUTTON, self.onBtn1)
        #btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onBtn2)
        #btn3.Bind(wx.EVT_BUTTON, self.onBtn3)

        # 하나의 메서드로 처리
        btn1.id = 1
        btn1.Bind(wx.EVT_BUTTON, self.onButtonHandler)
        btn2.id = 2
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onButtonHandler)
        btn3.id = 3
        btn3.Bind(wx.EVT_BUTTON, self.onButtonHandler)

    """
    def onBtn1(self, e):
        dlg = wx.MessageDialog(self, "로그인되었습니다.", "로그인", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

        self.m_id.SetLabelText("tiger")
        self.m_pw.SetLabelText("1111")
    def onBtn2(self, e):
        # print(e.GetEventObject())
        # print(e.GetEventObject().GetValue())
        if e.GetEventObject().GetValue():
            self.panel.SetBackgroundColour(wx.Colour(0, 0, 255))
            self.panel.Refresh()
        else:
            self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.panel.Refresh()

    def onBtn3(self, e):
        self.Close()
    """

    # 위의 세개의 메서드를 하나의 메서드로 합치기
    def onButtonHandler(self, e):
        #print(e.GetEventObject().id)
        if e.GetEventObject().id==1:
            dlg = wx.MessageDialog(self, "로그인되었습니다.", "로그인", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

            self.m_id.SetLabelText("tiger")
            self.m_pw.SetLabelText("1111")
        elif e.GetEventObject().id==2:
            if e.GetEventObject().GetValue():
                self.panel.SetBackgroundColour(wx.Colour(0, 0, 255))
                self.panel.Refresh()
            else:
                self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
                self.panel.Refresh()
        else:
            self.Close()

if __name__ == "__main__":
    app = wx.App()
    LoginFrame(None, "로그인", (300, 170))
    app.MainLoop()


