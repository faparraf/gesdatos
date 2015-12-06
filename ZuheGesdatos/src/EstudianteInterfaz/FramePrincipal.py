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

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
	def __init__(self,parent):
                'Inicio del cuerpo de la interfaz'
		self.parent=parent
		wx.Panel.__init__(self,parent) # InicializaciÃ³n Panel Padre
		self.panel=IngresarComo.IngresarComo(self) ## En esta linea se Agrega el Panel de inicio
		self.SetBackgroundColour('3399FF') # Color de Fondo del panel
		self.sizerbody=wx.BoxSizer(wx.VERTICAL)
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=5)
		self.SetSizer(self.sizerbody)
		
	#metodo setpanel, se encarga de reemplazar el panel actual por otro
	def setpanel(self,paneltemp):
                'Permite la visualización del panel'
		self.panel.Hide()
		self.panel=paneltemp
		self.sizerbody.Add(self.panel,0,wx.EXPAND|wx.ALL,border=0)
		self.panel.Show(True)
		self.Layout()
		self.parent.Refresh()
		self.parent.Update()
		
##-----------------------------------------------------------

app=wx.App(False)
displaySize= wx.DisplaySize()
frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour('3399FF')
sizertopPanel=wx.BoxSizer(wx.VERTICAL)

sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()