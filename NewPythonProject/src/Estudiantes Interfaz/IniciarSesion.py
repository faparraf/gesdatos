#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import Componentes
import Curso 


class IniciarSesionEstudiante(wx.Panel):
	def __init__(self,parent):
                'Inicia el panel junto con su contenedor'
#--------------Inicializacion Panel Padre--------------
		wx.Panel.__init__(self,parent) 
		self.SetBackgroundColour("3399FF")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
		self.parent=parent
		
#--------------Titulo-------------- 
#--------------Creacion padre hijo--------------
		PanelComponentsLabel = wx.Panel(self) 
		self.label = Component.CreateLabel(PanelComponentsLabel,15,pos=(0,0),label="Iniciar Sesión")
		
		sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
		sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)
		
		PanelComponentsLabel.SetSizer(sizerPanelLabel)
		PanelComponentsLabel.SetBackgroundColour("3399FF")
		
#--------------Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label--------------
#--------------Creacion padre hijo--------------
		PanelComponentsTxtArea1 = wx.Panel(self) 
		PanelComponentsTxtArea2 = wx.Panel(self) 

#--------------label "Usuario"--------------		
		self.labelTxtArea1 = Component.CreateLabel(PanelComponentsTxtArea1,15,pos=(0,0),label="Usuario:")
#--------------txtarea1 para Usuario--------------
		self.TxtArea1 = Component.CreateTextArea(PanelComponentsTxtArea1,pos=(0,0),size=(130,30))
		
#--------------label "password"--------------		
		self.labelTxtArea2 = Component.CreateLabel(PanelComponentsTxtArea2,15,pos=(0,0),label="Password:")
#--------------txtarea2 para password--------------
		self.TxtArea2 = Component.CreateTextArea(PanelComponentsTxtArea2,pos=(0,0),size=(130,30))
		
#--------------Creacion caja de tamaños-txtArea1--------------
		sizerPanelTxtArea1 = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel -label--------------
		sizerPanelTxtArea1.Add(self.labelTxtArea1 , 0, wx.ALIGN_CENTER)
#--------------Adicion del Objeto al panel-txt--------------
		sizerPanelTxtArea1.Add(self.TxtArea1 , 0, wx.ALIGN_CENTER) 
		
#--------------Creacion caja de tamaños	--------------	
		sizerPanelTxtArea2 = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel -label--------------
		sizerPanelTxtArea2.Add(self.labelTxtArea2 , 0, wx.ALIGN_CENTER) 
#--------------Adicion del Objeto al panel-txt--------------
		sizerPanelTxtArea2.Add(self.TxtArea2 , 0, wx.ALIGN_CENTER) 
#--------------Asignación de Color de Fondo-txtArea1--------------				
		PanelComponentsTxtArea1.SetSizer(sizerPanelTxtArea1)
		PanelComponentsTxtArea1.SetBackgroundColour("3399FF") 
#--------------Asignación de Color de Fondo-txtArea2--------------		
		PanelComponentsTxtArea2.SetSizer(sizerPanelTxtArea2)
		PanelComponentsTxtArea2.SetBackgroundColour("3399FF") 
		
#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label-------------
#--------------Creacion padre hijo--------------
		PanelComponentsButtons = wx.Panel(self) 
		
#--------------Creacion button 	Ingresar--------------		
		self.Button1 = Component.CreateButton(PanelComponentsButtons,"Ingresar")
#--------------Creación de Evento para button--------------
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.Button1)
#--------------Creacion caja de tamaños-button1--------------	
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel- button1--------------
		sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) 
		PanelComponentsButtons.SetSizer(sizerPanelButton)
#--------------Asignación de Color de Fondo-------------- 
		PanelComponentsButtons.SetBackgroundColour("white")  
		
#--------------Creacion grilla de tamano 4 filas 1 columna--------------
		gs = wx.GridSizer(3, 1, 30, 30) 
#--------------Adicion de Paneles a la Grilla--------------
		gs.AddMany([(PanelComponentsLabel, 0, wx.ALIGN_CENTER),(PanelComponentsTxtArea1, 0, wx.ALIGN_CENTER),
		(PanelComponentsTxtArea2, 0, wx.ALIGN_CENTER), (PanelComponentsButtons, 0, wx.ALIGN_CENTER)])
#-------------Adicion de la grilla de tamanos al panel padre--------------		
		sizer = wx.BoxSizer(wx.VERTICAL) 
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)

	def OnClick(self,event):
                'Permite el manejo de venetos del Bot�n'
		self.parent.setpanel(Curso.Cursos(self.parent))
