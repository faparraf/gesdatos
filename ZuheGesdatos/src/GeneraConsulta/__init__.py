#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
import ConnectionDataBase
import BodyQuery

########################################################################
class MyDialogSql(wx.Dialog):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,puerto):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Dialog")
        topPanel= scrolled.ScrolledPanel(self)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour("#696969")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=0)
        self.body = Body(topPanel,puerto)
        sizer.Add(self.body,0,wx.EXPAND|wx.ALL,border=0)
        sizer.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=0)
        topPanel.SetSizer(sizer)
        #self.SetSizer(sizer)
    def getsqlresult(self):
        return self.body.getsqlresult()
## Head
##-----------------------------------------------------------
class Head(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour("3399FF")
		head = HeadLow.Head(self)
		sizerhead = wx.BoxSizer(wx.VERTICAL)
		sizerhead.Add(head,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerhead)
##-----------------------------------------------------------

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
	def __init__(self,parent,puerto):
		self.parent=parent
		self.conn = ConnectionDataBase.Connection("localhost","mundiales","adminexamen","pasexamen",puerto)
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.BodyQuery=BodyQuery.BodyQuery(self, self.conn) ## En esta linea se Agrega el Panel de inicio
		self.SetBackgroundColour("#696969") # Color de Fondo del panel
		self.sizerbody=wx.BoxSizer(wx.VERTICAL)
		self.sizerbody.Add(self.BodyQuery,0,wx.EXPAND|wx.ALL,border=5)
                aceptar = wx.Button(self, wx.ID_OK, label="Aceptar")
		self.sizerbody.Add(aceptar,0,wx.ALL,border=5)
		self.SetSizer(self.sizerbody)
		
	#metodo setpanel, se encarga de reemplazar el panel actual por otro
	def setpanel(self,paneltemp):
		self.panel.Hide()
		self.panel=paneltemp
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=0)
		self.panel.Show(True)
		self.Layout()
		self.parent.Refresh()
		self.parent.Update()

        def getsqlresult(self):
            return self.BodyQuery.getsqlresult()
      	
##-----------------------------------------------------------

## Low
##-----------------------------------------------------------
class Low(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("#696969")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------



#app=wx.App(False)
#frame = wx.Frame(None, wx.ID_ANY, 'ZUHÉ - UD', pos=(0, 0), size=(900,900))
#menubar = wx.MenuBar()
#topPanel= scrolled.ScrolledPanel(frame)
#topPanel.SetupScrolling(scroll_y=True)
#topPanel.SetBackgroundColour("#696969")
#sizertopPanel=wx.BoxSizer(wx.VERTICAL)
#Body= Body(topPanel,"5434")
#sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=0)
#sizertopPanel.Add(Body,0,wx.EXPAND|wx.ALL,border=0)
#sizertopPanel.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=0)
#topPanel.SetSizer(sizertopPanel)
#frame.Show()
#frame.Update()
#frame.Layout()
#app.MainLoop()




