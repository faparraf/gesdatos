#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
import VentanaRegistroUsuarios
import VentanaConfigUsuario
import VentanaRoles

## Head
##-----------------------------------------------------------
class Head(wx.Panel):
	def __init__(self,parent):
                'Inicia el encabezado de la interfaz'
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour("#696969")
		head = HeadLow.Head(self)
		sizerhead = wx.BoxSizer(wx.VERTICAL)
		sizerhead.Add(head,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerhead)
##-----------------------------------------------------------

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
	def __init__(self,parent,port):
                'Inicia el cuerpo de la interfaz'
		self.parent=parent
                wx.Panel.__init__(self,parent) # InicializaciÃ³n Panel Padre
		self.panel1=VentanaRegistroUsuarios.VentanaRegistroUsuarios(self,port) ## En esta linea se Agrega el Panel de inicio
		self.panel=VentanaConfigUsuario.VentanaConfigUsuario(self,2,port)
                self.panel=VentanaRoles.VentanaRoles(self,port)
                self.SetBackgroundColour("white") # Color de Fondo del panel
		self.sizerbody=wx.BoxSizer(wx.VERTICAL)
		self.sizerbody.Add(self.panel1,0,wx.EXPAND|wx.ALL,border=5)
		self.SetSizer(self.sizerbody)
		
	#metodo setpanel, se encarga de reemplazar el panel actual por otro
	def setpanel(self,paneltemp):
                'Permite la visualización y ajuste del panel'
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
                'Inicia el pie de página de la interfaz'
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("#696969")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=0)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------

#app=wx.App(False)
#frame = wx.Frame(None, wx.ID_ANY, 'ZUHÃ‰ - UD', pos=(0, 0), size=( wx.EXPAND|wx.ALL,wx.EXPAND|wx.ALL))
#menubar = wx.MenuBar()
#topPanel= scrolled.ScrolledPanel(frame)
#topPanel.SetupScrolling(scroll_y=True)
#topPanel.SetBackgroundColour("#696969")
#sizertopPanel=wx.BoxSizer(wx.VERTICAL)
#Body= Body(topPanel)
#sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=0)
#sizertopPanel.Add(Body,0,wx.EXPAND|wx.ALL,border=0)
#sizertopPanel.Add(Low(topPanel),wx.ALIGN_BOTTOM,wx.ALIGN_CENTER)
#topPanel.SetSizer(sizertopPanel)
#frame.Show()
#frame.Update()
#frame.Layout()
#app.MainLoop()