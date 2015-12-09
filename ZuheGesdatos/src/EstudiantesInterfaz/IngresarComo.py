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
		self.SetBackgroundColour("#00BF8F")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
		self.parent=parent
#--------------Titulo-------------- 
#--------------Creacion padre hijo--------------
		PanelComponentLabel = wx.Panel(self) 
		self.label= Component.CreateLabel(PanelComponentLabel,15,pos=(0,0),label="Iniciar Sesión:")
                PanelComponentsCbx = wx.Panel(self) #Creacion padre hijo
		self.labelCbx = Component.CreateLabel(PanelComponentsCbx,15,pos=(0,0),label="Ingresar como:  ")
		self.Cb1 = Component.CreateComboBox(PanelComponentsCbx,pos=(0,0),size=150,List=["Estudiante","Profesor","Invitado"])
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.Cb1)
                sizerPanelCbx = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbx.Add(self.labelCbx , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbx.Add(self.Cb1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbx.SetSizer(sizerPanelCbx)
		PanelComponentsCbx.SetBackgroundColour("3399FF") #Asignación de Color de Fondo 
		sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
		sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)		
		PanelComponentLabel.SetSizer(sizerPanelLabel)
		PanelComponentLabel.SetBackgroundColour("3399FF")

#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label--------------
#--------------creacion padre hijo-ButtonE- Estudiante--------------
		PanelComponentsButtonE = wx.Panel(self) 		
#--------------Creacion del button estudiante--------------		
		self.ButtonE = Component.CreateButton(PanelComponentsButtonE,"Siguiente")
#--------------Creacion de Evento--------------
		self.ButtonE.Bind(wx.EVT_BUTTON, self.OnClickE,self.ButtonE)


#--------------Creacion caja de tamanos--------------	
		sizerPanelButtonE = wx.BoxSizer(wx.VERTICAL) 
#--------------Adicion del Objeto al panel--------------
		sizerPanelButtonE.Add(self.ButtonE , 0, wx.ALIGN_CENTER) 
		
		PanelComponentsButtonE.SetSizer(sizerPanelButtonE) 
#--------------Asignacion de Color de Fondo para button estudiante--------------
		PanelComponentsButtonE.SetBackgroundColour("3399FF") 
		
#--------------Creacion grilla de tamano 5 filas 1 columna--------------  
		gs = wx.GridSizer(5, 1, 30, 30) 
#--------------Adicion de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamano de la pantalla--------------
		gs.AddMany([(PanelComponentLabel, 0, wx.ALIGN_CENTER),(PanelComponentsCbx, 0, wx.ALIGN_CENTER),(PanelComponentsButtonE, 0, wx.ALIGN_CENTER)])
#--------------Adicion de la grilla de tamanos al panel padre--------------    
		sizer = wx.BoxSizer(wx.VERTICAL) 
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
			
##------------------------------Funciones de evento-----------------------------
        def EvtComboBox(self, event):
		self.TxtArea1.AppendText("Evento ComboBox")
	def OnClickE(self,event):
                'Permite el manejo del evento del Botón'
		self.parent.setpanel(IniciarSesion.IniciarSesionEstudiante(self.parent))
		