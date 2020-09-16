import wx
import os

"""
Dialog(대화상자)
--------------------
1. Built in Dialog
    - Common Dialog(공통 대화상자), System Dialog
2. User Define Dialog
3. 실행방식
    1) model
    2) modaless
"""

# 로그인 클래스
class LoginFrame(wx.Dialog):
    #생략가능
    panel = None
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.loginUI()

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

        # 하나의 메서드로 처리
        btn1.id = 1
        btn1.Bind(wx.EVT_BUTTON, self.onButtonHandler)
        btn2.id = 2
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onButtonHandler)
        btn3.id = 3
        btn3.Bind(wx.EVT_BUTTON, self.onButtonHandler)


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

# 메인 윈도우----------------------------------------------------------------------------------------------------
class MainFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.memoUI()
        self.Show(True)

    def memoUI(self):
        self.CreateStatusBar()

        menuBar = wx.MenuBar()
        menu = wx.Menu()

        menu.Append(100, "Message Dialog", "메시지 대화상자 보이기")
        menu.Append(101, "Color Dialog", "색상 대화상자 보이기")
        menu.Append(102, "File Dialog", "파일 대화상자 보이기")
        menu.Append(200, "Login", "로그인 대화상자 보이기")

        menuBar.Append(menu, "다이얼로그")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onMessage, id=100)
        self.Bind(wx.EVT_MENU, self.onColor, id=101)
        self.Bind(wx.EVT_MENU, self.onFile, id=102)
        self.Bind(wx.EVT_MENU, self.onLogin, id=200)

    def onMessage(self, e):
        self.SetStatusText("메시지 대화상자 선택")
        dlg = wx.MessageDialog(self, "오늘 하루도 열심히...", "메시지박스", wx.OK | wx.ICON_INFORMATION)

        dlg.ShowModal()
    def onColor(self,e):
        self.SetStatusText("색상 대화상자 선택")
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        result = dlg.ShowModal()
        # 확인 버튼을 눌렀을 때
        if result == wx.ID_OK:
            color=dlg.GetColourData()
            self.SetStatusText("당신이 선택한 색상은 {} 입니다.".format(str(color.GetColour().Get())))

    def onFile(self,e):
        self.SetStatusText("파일 대화상자 선택")
        dlg = wx.FileDialog(self, "파일 선택", "c:\\", "", "*.*", style=wx.ID_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print(path)
            filename = os.path.basename(path)
            print(filename)
            self.SetStatusText("당신이 선택한 파일은 {} 입니다.".format(filename))


    def onLogin(self, e):
        self.SetStatusText("로그인 대화상자 선택")

        #클래스 객체 생성
        dlg = LoginFrame(None, "로그인", (300, 170))
        dlg.ShowModal()
        dlg.Destroy()




if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "다이얼로그 연습", (600, 400))
    app.MainLoop()