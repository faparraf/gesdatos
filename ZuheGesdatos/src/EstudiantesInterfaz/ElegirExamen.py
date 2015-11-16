#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx, ConnSchema,ConnectionDataBase
import Componentes
import wx.lib.scrolledpanel as scrolled
import cargarExamen

class ElegirExamen(wx.Frame):
    def __init__(self):
        'Constructor que requiere de un parent como interfaz contendor y manipulador para que acceda a la informaci髇'
        app=wx.App(False)
        displaySize= wx.DisplaySize()
        wx.Frame.__init__(self, None, pos=(0, 0), size=(displaySize[0], displaySize[1]))
        displaySize= wx.DisplaySize()
        topPanel= scrolled.ScrolledPanel(self)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour('3399FF')
        sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        #sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        #sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
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
            "縍ealmente quiere salir?",
            "Confirmar Salida", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_OK:
                self.Destroy()

## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
	def __init__(self,parent,idestudiante,idcurso):
                'Constructor de la interfaz que recibe su contenedor'
 #--------------Inicializacion Panel Padre--------------
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("3399FF")
#--------------Instancia Clase Componente--------------
		Component = Componentes.Component(self) 
        	self.parent=parent
                self.idestudiante=idestudiante
                self.idcurso = idcurso
                
                queryexamencurso = "select examen.id_exa, examen.titulo_exa, examen.tiempo_exa_inicio, "
                queryexamencurso += "examen.tiempo_exa_fin, examen.tipoexa, examen.fecha from examen, curso_examen "
                queryexamencurso += "where curso_examen.id_curso = "+idcurso+" and curso_examen.id_examen = examen.id_exa"
                
                self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
                self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
                self.examenescurso = self.conexion.connection.ExecuteQuery(queryexamencurso)
                
                print (self.examenescurso)
                
                
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
                print ("cargando examen")
                verexamen = cargarExamen.iniciarverexamen(6)