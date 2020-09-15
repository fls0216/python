import wx
# ws.Frame을 상속받아 메모장으로 만들기

class ChildFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.gui()


    def gui(self):
        # 메뉴 디자인 : 고정식 메뉴(Pull Down), 이동식 메뉴
        # MenuBar, Menu, MenuItem
        menubar=wx.MenuBar()
        mnuFile=wx.Menu()
        mnuEdit=wx.Menu()

        mnuFile_new =  wx.MenuItem(mnuFile, wx.ID_NEW, "New", "New Document")
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "open", "파일 열기")
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "Eixt", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.AppendSeparator()
        mnuFile.Append(mnuFile_open)
        mnuFile.AppendSeparator()
        mnuFile.Append(mnuFile_exit)
        menubar.Append(mnuFile, "파일")
        menubar.Append(mnuEdit, "편집")
        self.SetMenuBar(menubar)

        # 입력이 가능하게 설정(여러줄 입력 가능하게)
        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # 이벤트와 코드를 연결한다.
        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)
        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit)

        # 윈도우가 나타날 위치 지정
        # self.Move(100, 50)
        # 화면 가운데에 윈도우 나타나게해줌
        self.Center()
        self.Show(True)

    def onNew(self, ev):
        self.txtA.SetLabelText("새 문서를 선택하였습니다.")
    def onOpen(self, ev):
        # self.txtA.SetLabelText("파일 열기를 선택하였습니다.")
        # 파일 열기
        f = open("C:\\Users\\Hyelin\\bigdata\\0824터미널명령.txt","r")
        data  = f.read()
        # 읽어오기
        self.txtA.SetLabelText(data)
        f.close()
    def onExit(self, ev):
        self.txtA.SetLabelText("프로그램 종료를 선택하였습니다.")
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    ChildFrame(None, "간단한 메모장", (400, 600))
    app.MainLoop()