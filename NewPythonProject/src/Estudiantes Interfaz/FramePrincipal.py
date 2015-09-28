#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
import IngresarComo
import IniciarSesion

## Head
##-----------------------------------------------------------
class Head(wx.Panel):
	def __init__(self,parent):
                'Inicio del encabezado de la interfaz'
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
	def __init__(self,parent):
                'Inicio del cuerpo de la interfaz'
		self.parent=parent
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.panel=IngresarComo.IngresarComo(self) ## En esta linea se Agrega el Panel de inicio
		self.SetBackgroundColour("#696969") # Color de Fondo del panel
		self.sizerbody=wx.BoxSizer(wx.VERTICAL)
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=5)
		self.SetSizer(self.sizerbody)
		
	#metodo setpanel, se encarga de reemplazar el panel actual por otro
	def setpanel(self,paneltemp):
                'Permite la visualizaci�n del panel'
		self.panel.Hide()
		self.panel=paneltemp
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=0)
		self.panel.Show(True)
		self.Layout()
		self.parent.Refresh()
		self.parent.Update()
		
##-----------------------------------------------------------

## Low
##-----------------------------------------------------------
class Low(wx.Panel):
	def __init__(self,parent):
                'Inicio del pie de p�gina de la interfaz'
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("#696969")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------

app=wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, 'ZUHÉ - UD', pos=(0, 0), size=(900,500))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour("#696969")
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
Body= Body(topPanel)
sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=0)
sizertopPanel.Add(Body,0,wx.EXPAND|wx.ALL,border=0)
sizertopPanel.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=0)
topPanel.SetSizer(sizertopPanel)
frame.Show()
frame.Update()
frame.Layout()
app.MainLoop()