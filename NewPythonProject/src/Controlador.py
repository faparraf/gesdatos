import wx
import panel1
import panel2
import panel3
import panel4
import panel5
import Tabla
import wx.lib.scrolledpanel as scrolled
import ConnectionDataBase

conn = ConnectionDataBase.Connection("localhost","DBPrueba","postgres","12345")
app=wx.App(False)
frame = wx.Frame(None,-1, title="Consultas", size=(900,900))
wx.InitAllImageHandlers()
topPanela= scrolled.ScrolledPanel(frame)
topPanela.SetupScrolling(scroll_y=True)

Panel1 = panel1.Panel1(topPanela,conn)
Panel2 = panel2.Panel2(topPanela,conn)
Panel3 = panel3.Titulo1(topPanela)
Panel4 = panel3.Titulo2(topPanela)
Panel5 = panel3.Titulo3(topPanela)
Panel6 = panel4.Panel4(topPanela,conn)
Panel7 = panel5.Panel5(topPanela)

sizer= wx.BoxSizer(wx.VERTICAL)
sizer.Add(Panel3,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel1,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel4,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel2,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel5,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel6,0,wx.EXPAND|wx.ALL,border=10)
sizer.Add(Panel7,0,wx.EXPAND|wx.ALL,border=10)
topPanela.SetSizer(sizer)

frame.Show()
app.MainLoop()



