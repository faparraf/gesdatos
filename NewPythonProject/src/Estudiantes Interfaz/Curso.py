#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Componentes
import ElegirExamen

class Cursos(wx.Panel):
	def __init__(self,parent):
#--------------Inicializacion Panel Padre--------------
		wx.Panel.__init__(self,parent) 
		self.SetBackgroundColour("3399FF")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
		self.parent=parent
		
#--------------Titulo-------------- 
#--------------Creacion padre hijo--------------
		PanelComponentsLabel = wx.Panel(self) 
#--------------Label "Miscursos"--------------
		self.label = Component.CreateLabel(PanelComponentsLabel,15,pos=(0,0),label="Mis Cursos")
		
		sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
		sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)
		
		PanelComponentsLabel.SetSizer(sizerPanelLabel)
		PanelComponentsLabel.SetBackgroundColour("3399FF")
		
#--------------Creación de un panel de Grid, e inclusión  del objeto Grid y su Label--------------
#--------------reacion padre hijo--------------
		PanelComponentsGrid = wx.Panel(self) 
		titles = ['Curso', 'Docente']
		self.Grid = Component.CreateGrid(PanelComponentsGrid,4,2,titles,75)
#--------------Creacion caja de tamaños--------------
		sizerPanelGrid = wx.BoxSizer(wx.VERTICAL)
#--------------Adicion del Objeto al panel--------------
		sizerPanelGrid.Add(self.Grid , 0, wx.ALIGN_CENTER)  
		PanelComponentsGrid.SetSizer(sizerPanelGrid)
#--------------Asignación de Color de Fondo-------------- 
		PanelComponentsGrid.SetBackgroundColour("3399FF") 
		
#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label--------------
#--------------Creacion padre hijo--------------
		PanelComponentsButtons = wx.Panel(self) 
		
		self.Button1 = Component.CreateButton(PanelComponentsButtons,"Seleccionar")
#--------------Creación de Evento--------------
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.Button1)

#--------------Creacion caja de tamaños--------------
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) 
		PanelComponentsButtons.SetSizer(sizerPanelButton)
#--------------Asignación de Color de Fondo-------------- 
		PanelComponentsButtons.SetBackgroundColour("3399FF") 
		
#--------------Creacion grilla de tamano 3 filas 1 columna--------------
		gs = wx.GridSizer(3, 1, 0, 0) 
#--------------Adicion de Paneles a la Grilla--------------
		gs.AddMany([(PanelComponentsLabel, 0, wx.ALIGN_CENTER),(PanelComponentsGrid, 0, wx.ALIGN_CENTER),
		(PanelComponentsButtons, 0, wx.ALIGN_CENTER)])
		
#--------------Adicion de la grilla de tamanos al panel padre--------------	
	
		sizer = wx.BoxSizer(wx.VERTICAL) 
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
		
	def OnClick(self,event):
		self.parent.setpanel(ElegirExamen.ElegirExamen(self.parent))
