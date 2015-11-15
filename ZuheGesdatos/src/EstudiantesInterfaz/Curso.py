#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"

import wx, ConnSchema,ConnectionDataBase
import ElegirExamen
import wx.lib.scrolledpanel as scrolled
import Componentes
import HeadLow


class Cursos(wx.Frame):
    def __init__(self):
        'Constructor que requiere de un parent como interfaz contendor y manipulador para que acceda a la informaci�n'
        app=wx.App(False)
        displaySize= wx.DisplaySize()
        wx.Frame.__init__(self, None, pos=(0, 0), size=(displaySize[0], displaySize[1]))
        displaySize= wx.DisplaySize()
        topPanel= scrolled.ScrolledPanel(self)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour('3399FF')
        sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        topPanel.SetSizer(sizertopPanel)
        self.sizer = sizertopPanel
        self.topPanel = topPanel
        self.topanel=topPanel
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #Genracion de menu Principal que controlara el interfaz
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "&salir\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&Archivo")
        self.SetMenuBar(menuBar)
        self.Show()
        app.MainLoop()
        self.GetSizer().Layout()
        self.Fit()   

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
        "�Realmente quiere salir?",
        "Confirmar Salida", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
##-----------------------------------------------------------                
## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    
    def __init__(self,parent,idestudiante):
        self.parent=parent
        'Constructor que recibe a parent como contenedor'
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
#-------------Creacion caja de tamaños--------------
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
        'Identifica el evento del Bot�n.'
        interfaz = ElegirExamen.Body(self)            
        #.cambiarpanel(interfaz)
        Cursos.cambiarpanel(self,ElegirExamen.ElegirExamen)