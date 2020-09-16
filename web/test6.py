import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)

        panel1 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel1.SetBackgroundColour("Blue")

        panel2 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel2.SetBackgroundColour("Red")

        box = wx.BoxSizer(wx.VERTICAL)
        # 객체 명, 비율, 전체면적 사용여부(expand = 전체면적사용)
        box.Add(panel1, 3, wx.EXPAND)
        box.Add(panel2, 1, wx.EXPAND)

        self.SetSizer(box)

        self.Show(True)


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "자주 사용하는 컨트롤 연습", (600, 600))
    app.MainLoop()