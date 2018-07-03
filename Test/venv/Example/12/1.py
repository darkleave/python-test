#图形用户界面

#最成熟的跨平台PythonGUI工具包——wxPython

#支持Python的流行GUI工具包

#Tkinter 使用Tk平台，很容易得到，半标准
#wxpython 基于wxWindows.跨平台越来越流行
#PythonWin 只能在Windows上使用,使用了本机的Windows GUI功能.
#Java Swing 只能用于Jython.使用本机的Java GUI
#PyGTK 使用GTK平台，在linux上很流行
#PyQt 使用Qt平台，跨平台

#12.3 使用wxPython 创建示例GUI应用程序

"""

import wx
app = wx.App()

win = wx.Frame(None,title="Simple Editor",size=(410,335))

#增加按钮
#使用关键字参数增加标签和标题t
#设置按钮位置
loadButton =  wx.Button(win,label='Open',pos=(225,5),size=(80,25))
saveButton = wx.Button(win,label='Save',pos=(315,5),size=(80,25))

filename = wx.TextCtrl(win,pos=(5,5),size=(210,25))

conents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE | wx.HSCROLL)


win.Show()

app.MainLoop()




"""
#12.3.2 窗口和组件

#窗口(Window)也成为框架(Frame),它是wx.Frame 类的实例.
#wx框架中的部件都是由它们的父部件使用构造函数的第一个参数构建的.

#使用尺寸器

import wx
import pprint

#事件处理函数

def load(event):
    pprint.pprint(filename)
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    pprint.pprint(filename)
    file = open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()




app = wx.App()

win = wx.Frame(None,title="Simple Editor",size=(410,335))

bkg = wx.Panel(win)


loadButton =  wx.Button(bkg,label='Open')
saveButton = wx.Button(bkg,label='Save')

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()

hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton, proportion=0,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)

#绑定事件
loadButton.Bind(wx.EVT_BUTTON,load)
saveButton.Bind(wx.EVT_BUTTON,save)




win.Show()



app.MainLoop()


