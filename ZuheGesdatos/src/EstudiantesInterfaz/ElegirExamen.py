#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import Componentes
import cargarExamen

class ElegirExamen(wx.Panel):
	def __init__(self,parent):
                'Constructor de la interfaz que recibe su contenedor'
 #--------------Inicializacion Panel Padre--------------
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("3399FF")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
        	self.parent=parent
#--------------Instancia Clase ComponenteTitulo--------------

#--------------Creacion padre hijo--------------
		PanelComponentsLabel = wx.Panel(self) 
		self.label = Component.CreateLabel(PanelComponentsLabel,15,pos=(0,0),label="Examenes")
		
		sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
		sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)
		
		PanelComponentsLabel.SetSizer(sizerPanelLabel)
#--------------Asignacion de color a panel--------------
		PanelComponentsLabel.SetBackgroundColour("3399FF")
		
#--------------Creaci贸n de un panel de Grid, e inclusi贸n  del objeto Grid y su Label--------------
#--------------Creacion padre hijo--------------
		PanelComponentsGrid = wx.Panel(self) 
		titles = ['Nombre','Tipo','Fecha','Hora']
		self.Grid = Component.CreateGrid(PanelComponentsGrid,4,4,titles,75)
#--------------Creacion caja de tama帽os--------------
		sizerPanelGrid = wx.BoxSizer(wx.VERTICAL)
#--------------Adicion del Objeto al panel--------------
		sizerPanelGrid.Add(self.Grid , 0, wx.ALIGN_CENTER)  
		PanelComponentsGrid.SetSizer(sizerPanelGrid)
#--------------Asignaci贸n de Color de Fondo--------------
		PanelComponentsGrid.SetBackgroundColour("3399FF")  
		
#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Labe--------------
#--------------Creacion padre hijo--------------
		PanelComponentsButtons = wx.Panel(self) 
#--------------A帽adir button1 "comenzar" --------------		
		self.Button1 = Component.CreateButton(PanelComponentsButtons,"Comenzar")
#--------------Creaci贸n de Evento Button--------------
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.Button1)
#--------------Creacion caja de tama帽os--------------		
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL)
#--------------Adicion del Objeto al panel- button1 --------------
		sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) 
		PanelComponentsButtons.SetSizer(sizerPanelButton) 
#--------------Asignaci贸n de Color de Fondo --------------
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

	def OnClick(self,e):
                'Permite establecer el evento del Bot髇'
		#from ElegirExamen import elegirExamen 
		#ElegirExamen = elegirExamen()
		#ElegirExamen.Show
                print ("cargando examen")
                verexamen = cargarExamen.iniciarverexamen(6)
