#!/usr/bin/env python
# -*- coding: cp1252 -*-
import wx
import Componentes
import panel2
import panel3
#import login.Logeo
import interfazInvitado.__init__ as invitado
#import Registro_Interfaz.__init__
import Presentacion

class Panel1(wx.Panel):
	def __init__(self,parent,port,frame,topPanel,sizertopPanel):
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.SetBackgroundColour("#32506D")
		Component = Componentes.Component(self) # Instancia Clase Componente
		self.parent=parent
		self.topPanel = topPanel
                self.sizertopPanel = sizertopPanel
                self.port = port
                self.frame =  frame
		PanelPresentation = wx.Panel(self) #Creacion panel hijo
		self.Labelpresentation = Component.CreateLabel(PanelPresentation,15,pos=(0,0),label="Participantes del Proyecto")
		self.Presentacion = Presentacion.Presentacion(PanelPresentation,port)
		sizerPanelpresentation = wx.BoxSizer(wx.VERTICAL) #Creacion caja de tamaños
		sizerPanelpresentation.Add(self.Labelpresentation , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelpresentation.Add(self.Presentacion, 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelPresentation.SetSizer(sizerPanelpresentation) 

		 #----Creación de un panel de Buttons, e inclusión  del objeto Buttons y su Label, adicionalmente se incluye en el boton el evento de cambio de panel
		#PanelComponentsButtons = wx.Panel(self) #Creacion padre hijo
		#self.Button1 = Component.CreateButton(PanelComponentsButtons,"Incluir Participante")
		#self.Bind(wx.EVT_BUTTON, self.OnClick,self.Button1)#Creación de Evento
		#self.Button2 = Component.CreateButton(PanelComponentsButtons,"Modificar Información de Participante")
		#self.Bind(wx.EVT_BUTTON, self.Modificar,self.Button2)#Creación de Evento
		#sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		#sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		#sizerPanelButton.Add(self.Button2 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		#PanelComponentsButtons.SetSizer(sizerPanelButton) 
		#PanelComponentsButtons.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 

		 #----Creación de un panel de Buttons, e inclusión  del objeto Buttons y su Label, adicionalmente se incluye en el boton el evento de cambio de panel
		PanelComponentsButtons = wx.Panel(self) #Creacion padre hijo
		self.Button1 = Component.CreateButton(PanelComponentsButtons,"Ingresar")
		self.Bind(wx.EVT_BUTTON, self.ingresar,self.Button1)#Creación de Evento
		self.Button2 = Component.CreateButton(PanelComponentsButtons,"Ingresar como Invitado")
		self.Bind(wx.EVT_BUTTON, self.ingresarcomoinvitado,self.Button2)#Creación de Evento
		self.Button3 = Component.CreateButton(PanelComponentsButtons,"Registrarse")
		self.Bind(wx.EVT_BUTTON, self.registrarse,self.Button3)#Creación de Evento
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelButton.Add(self.Button2 , 0, wx.ALIGN_CENTER)
		sizerPanelButton.Add(self.Button3 , 0, wx.ALIGN_CENTER) # # Adicion del Objeto al panel
		PanelComponentsButtons.SetSizer(sizerPanelButton) 
		PanelComponentsButtons.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 
 
		gs = wx.GridSizer(2, 1, 5, 5) #Creacion grilla de tamaño
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
		gs.AddMany([(PanelComponentsButtons, 0, wx.ALIGN_CENTER),(PanelPresentation, 0, wx.ALIGN_CENTER)])
     
		sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)



##------------------------------Funciones de evento-----------------------------
	#def OnClick(self,event):
	#	self.parent.setpanel(panel2.Panel2(self.parent))
	#def Modificar(self,event):
	#	self.parent.setpanel(panel3.Panel3(self.parent))	
	def ingresar(self,event):
            login.Logeo.LogeoInt(self,port)
        def ingresarcomoinvitado(self,event):
            manipulador = invitado.interfazpanelpaso(self.parent,self.topPanel,self.sizertopPanel,self.port)
            panelinvitado = invitado.Body(self.parent, manipulador)
            self.parent.setpanel(self,panelinvitado)
        def registrarse(self,event):
            Registro_Interfaz.__init__.Body(self)