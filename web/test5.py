import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.controlsUI()
        self.Show(True)


    def controlsUI(self):
        self.panel = wx.Panel(self)

        # Text 컨트롤
        wx.StaticText(self.panel, label = '********기타 컴포넌트********', pos=(20,5))
        wx.StaticText(self.panel, label='이름 : ', pos=(20, 70))
        self.txtName = wx.TextCtrl(self.panel, value="초기값", pos=(65, 70))
        self.Bind(wx.EVT_TEXT, self.onText, self.txtName)


        #체크박스 생성
        self.chk = wx.CheckBox(self.panel, label="결혼여부 ", pos=(20, 120))
        self.Bind(wx.EVT_CHECKBOX, self.onCheck, self.chk)

        # 결과값 출력(여러줄 출력 가능, 읽기 전용)
        self.txtShow = wx.TextCtrl(self.panel, pos=(20, 400), size=(320,150), style=wx.TE_MULTILINE | wx.TE_READONLY)

        #RadioBox 생성
        self.rb = wx.RadioBox(self.panel, label="좋아하는 색상은?", pos=(20, 170), choices=["빨강", "초록","파랑","노랑"])
        self.rb.Bind(wx.EVT_RADIOBOX, self.onRadio)
        # = self.Bind(wx.EVT_RADIOBOX, self.onRadio, self.rb)

        # comboBox 컨트롤
        cboData = ["빨강", "초록","파랑","노랑"]
        self.cbo = wx.ComboBox(self.panel, pos=(20,260), choices=cboData)
        self.cbo.Bind(wx.EVT_COMBOBOX, self.onRadio)


    def onText(self, e):
        self.txtShow.AppendText("Text : {}\n".format(e.GetString()))

    def onCheck(self, e):
        self.txtShow.AppendText("Check : {}\n".format(e.IsChecked()))

    def onRadio(self, e):
        self.txtShow.AppendText("Radio : {}\n".format(e.GetString()))

    def onCombo(self, e):
        self.txtShow.AppendText("Combo : {}\n".format(e.GetString()))


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "자주 사용하는 컨트롤 연습", (400, 600))
    app.MainLoop()