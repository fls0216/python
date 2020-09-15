import wx
# 실행 : ctrl + shift + F10
# wx 모듈을 사용한 기본 윈도우창 생성

app = wx.App()
frame = wx.Frame(None, title = "test1 입니다")
frame.Show(True)
app.MainLoop()
