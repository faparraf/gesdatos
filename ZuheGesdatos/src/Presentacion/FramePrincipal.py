#!/usr/bin/env python
# -*- coding: cp1252 -*-
import datostunnel.__init__ as Ptunel
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
import panel1
import panel2
from sshtunnel import SSHTunnelForwarder
## Head
##--------------------Instacia de la clase head con sus respectivos componentes graficos---------------------------------------
class Head(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour("#00BF8F")
		head = HeadLow.Head(self)
		sizerhead = wx.BoxSizer(wx.VERTICAL)
		sizerhead.Add(head,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerhead)
##-----------------------------------------------------------

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
	def __init__(self,parent,port,frame,topPanel,sizertopPanel):
		self.parent=parent
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.panel=panel1.Panel1(self,port,frame,topPanel,sizertopPanel) ## En esta linea se Agrega el Panel de inicio
		self.SetBackgroundColour("#32506D") # Color de Fondo del panel
		self.sizerbody=wx.BoxSizer(wx.VERTICAL)
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=5)
		self.SetSizer(self.sizerbody)
		
	#metodo setpanel, se encarga de reemplazar el panel actual por otro
	def setpanel(self,paneltemp):
		self.panel.Hide()
		self.panel=paneltemp
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=0)
		self.panel.Show(True)
		self.Layout()
		self.parent.Layout()     	
##-----------------------------------------------------------

## Low
##--------------------Instacia de la clase low con sus respectivos componentes graficos---------------------------------------
class Low(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("#F7F7F7")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------


##------- Inicializacion del Frame e inclusion de los paneles Head, Body y Head
TunelParametros = Ptunel.paramtunnel() 
port1=int(TunelParametros.getporttunnel())
port2=5432
app=wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, 'ZUHÉ - UD', pos=(0, 0), size=(900,900)) #Creacion de objeto wx.Frame
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame) #creacion de panel padre
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour("#00BF8F")
sizertopPanel=wx.BoxSizer(wx.VERTICAL) #creacion de caja de tamaños
            
with SSHTunnelForwarder(
	(TunelParametros.getidirserver(),port1),
	ssh_password=TunelParametros.getpasuser(),
	ssh_username=TunelParametros.getuser(),
	remote_bind_address=(TunelParametros.getlocalip(),port2)) as server: 
            randomport = server.local_bind_port
            print(randomport)
            Body= Body(topPanel,randomport,frame,topPanel,sizertopPanel) 
            #Inclusion de los tres paneles
            sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=0)
            sizertopPanel.Add(Body,0,wx.EXPAND|wx.ALL,border=0)
            sizertopPanel.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=0)
            topPanel.SetSizer(sizertopPanel)
            frame.Show()
            frame.Update()
            frame.Layout()
            app.MainLoop()




