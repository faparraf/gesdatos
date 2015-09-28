#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.lib.scrolledpanel as scrolled
import Componentes
import IniciarSesion

class IngresarComo(wx.Panel):
	def __init__(self,parent):
                'Inicio la interfaz, que recibe a parent como contenedor'
#--------------Inicializacion Panel Padre--------------
		wx.Panel.__init__(self,parent) 
		self.SetBackgroundColour("3399FF")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
		self.parent=parent
#--------------Titulo-------------- 
#--------------Creacion padre hijo--------------
		PanelComponentLabel = wx.Panel(self) 
		self.label= Component.CreateLabel(PanelComponentLabel,15,pos=(0,0),label="Ingresa a la aplicaciÃ³n como:")
		sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
		sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)		
		PanelComponentLabel.SetSizer(sizerPanelLabel)
		PanelComponentLabel.SetBackgroundColour("3399FF")

#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label--------------
#--------------creacion padre hijo-ButtonE- Estudiante--------------
		PanelComponentsButtonE = wx.Panel(self) 
#--------------creacion padre hijo ButtonI-Invitados--------------
		PanelComponentsButtonI = wx.Panel(self)
#--------------creacion padre hijo ButtonP-Profesores--------------
		PanelComponentsButtonP = wx.Panel(self)
#--------------creacion padre hijo ButtonP-Profesores--------------
		PanelComponentsButtonR = wx.Panel(self)
		
#--------------Creacion del button estudiante--------------		
		self.ButtonE = Component.CreateButton(PanelComponentsButtonE,"Estudiante")
#--------------Creacion de Evento--------------
		self.ButtonE.Bind(wx.EVT_BUTTON, self.OnClickE,self.ButtonE)

#--------------Creacion del button Invitado--------------		
		self.ButtonI= Component.CreateButton(PanelComponentsButtonI,"Invitado")
#--------------Creacion de Evento--------------
		self.ButtonI.Bind(wx.EVT_BUTTON, self.OnClickI,self.ButtonI)
		
#--------------Creacion del button Profesor--------------		
		self.ButtonP= Component.CreateButton(PanelComponentsButtonP,"Docente")
#--------------Creacion de Evento--------------
		self.ButtonP.Bind(wx.EVT_BUTTON, self.OnClickP,self.ButtonP)
		
#--------------Creacion del button Profesor--------------		
		self.ButtonR= Component.CreateButton(PanelComponentsButtonR,"Registro")
#--------------Creacion de Evento--------------
		self.ButtonR.Bind(wx.EVT_BUTTON, self.OnClickR,self.ButtonR)

#--------------Creacion caja de tamanos--------------	
		sizerPanelButtonE = wx.BoxSizer(wx.VERTICAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButtonE.Add(self.ButtonE , 0, wx.ALIGN_CENTER) 

#--------------Creacion caja de tamanos--------------		
		sizerPanelButtonI = wx.BoxSizer(wx.VERTICAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButtonI.Add(self.ButtonI , 0, wx.ALIGN_CENTER) 

#--------------Creacion caja de tamanos--------------	
		sizerPanelButtonP = wx.BoxSizer(wx.VERTICAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButtonP.Add(self.ButtonP , 0, wx.ALIGN_CENTER) 
		
#--------------Creacion caja de tamanos--------------	
		sizerPanelButtonR = wx.BoxSizer(wx.VERTICAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButtonR.Add(self.ButtonR , 0, wx.ALIGN_CENTER) 
		
		PanelComponentsButtonE.SetSizer(sizerPanelButtonE) 
#--------------Asignacion de Color de Fondo para button estudiante--------------
		PanelComponentsButtonE.SetBackgroundColour("3399FF") 
		
		PanelComponentsButtonI.SetSizer(sizerPanelButtonI) 
#--------------Asignacion de Color de Fondo para button Invitados--------------
		PanelComponentsButtonI.SetBackgroundColour("3399FF") 
		
		PanelComponentsButtonP.SetSizer(sizerPanelButtonP) 
#--------------Asignacion de Color de Fondo para button Profesores--------------
		PanelComponentsButtonP.SetBackgroundColour("3399FF")
		
		PanelComponentsButtonR.SetSizer(sizerPanelButtonR) 
#--------------Asignacion de Color de Fondo para button Registro--------------
		PanelComponentsButtonR.SetBackgroundColour("3399FF")  

#--------------Creacion grilla de tamano 5 filas 1 columna--------------  
		gs = wx.GridSizer(5, 1, 30, 30) 
#--------------Adicion de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamano de la pantalla--------------
		gs.AddMany([(PanelComponentLabel, 0, wx.ALIGN_CENTER),(PanelComponentsButtonE, 0, wx.ALIGN_CENTER),
		(PanelComponentsButtonI, 0, wx.ALIGN_CENTER),(PanelComponentsButtonP, 0, wx.ALIGN_CENTER),
		(PanelComponentsButtonR, 0, wx.ALIGN_CENTER)])
#--------------Adicion de la grilla de tamanos al panel padre--------------    
		sizer = wx.BoxSizer(wx.VERTICAL) 
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
			
##------------------------------Funciones de evento-----------------------------
	def OnClickE(self,event):
                'Permite el manejo del evento del Botón'
		self.parent.setpanel(IniciarSesion.IniciarSesionEstudiante(self.parent))
		
	def OnClickI(self,event):
                'Permite el manejo del evento del Botón'
		self.parent.setpanel(IniciarSesion.IniciarSesionEstudiante(self.parent))
                
	def OnClickP(self,event):
                'Permite el manejo del evento del Botón'
		self.parent.setpanel(IniciarSesion.IniciarSesionEstudiante(self.parent))
                
	def OnClickR(self,event):
                'Permite el manejo del evento del Botón'
		self.parent.setpanel(IniciarSesion.IniciarSesionEstudiante(self.parent))
		