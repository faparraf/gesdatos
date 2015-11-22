#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"

import wx, ConnSchema,ConnectionDataBase
import ElegirExamen
import wx.lib.scrolledpanel as scrolled
import Componentes
import HeadLow

"""class Cursos(wx.Frame):
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
        "縍ealmente quiere salir?",
        "Confirmar Salida", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()"""
##-----------------------------------------------------------                
## Mis Cursos
##-----------------------------------------------------------el):
class miscursos(wx.Panel):    
    def __init__(self,parent,idestudiante,frame):
        self.parent=parent
        'Constructor que recibe a parent como contenedor'
#--------------Inicializacion Panel Padre--------------
	wx.Panel.__init__(self,parent) 
	self.SetBackgroundColour("3399FF")
               
#--------------Instancia Clase Componente--------------
	Component = Componentes.Component(self) 
	self.parent=parent
        self.frame=frame
        self.idestudiante=idestudiante
        
        querymiscursos = "select curso.id_curso, curso.nom_curso, persona.id_persona, (persona.nom_pers||' '||persona.apellido_pers) from curso, "
        querymiscursos += "persona, curso_estudiante,docente where curso_estudiante.id_persn = 3 and "
        querymiscursos += "curso_estudiante.id_curso = curso.id_curso and curso.id_prof = docente.id_persona "
        querymiscursos += "and docente.id_persona = persona.id_persona"
        
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        self.miscursos = self.conexion.connection.ExecuteQuery(querymiscursos)
        
#--------------Creacion padre hijo--------------
	PanelComponentsLabel = wx.Panel(self) 
#--------------Label "Miscursos"--------------
	self.label = Component.CreateLabel(PanelComponentsLabel,15,pos=(0,0),label="Mis Cursos")
		
	sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
	sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)
	
        PanelComponentsLabel.SetSizer(sizerPanelLabel)
        PanelComponentsLabel.SetBackgroundColour("3399FF")

        grilla = wx.GridSizer(len(self.miscursos)+1, 4, 0, 0) 
        labelTitulo1 = Component.CreateLabel(self,12,pos=(0,0),label= 'C骴igo')
        labelTitulo2 = Component.CreateLabel(self,12,pos=(0,0),label= 'Nombre')
        labelTitulo3 = Component.CreateLabel(self,12,pos=(0,0),label= 'Docente')
        labelTitulo4 = Component.CreateLabel(self,12,pos=(0,0),label= ' ')
        
        grilla.Add(labelTitulo1,0, wx.ALIGN_CENTER)
        grilla.Add(labelTitulo2,0, wx.ALIGN_CENTER)
        grilla.Add(labelTitulo3,0, wx.ALIGN_CENTER)        
        grilla.Add(labelTitulo4,0, wx.ALIGN_CENTER)        
        
        for a in range (len(self.miscursos)):
            
            labelCurso = Component.CreateLabel(self,12,pos=(0,0),label= str(self.miscursos[a][0]))
            labelCurso2 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.miscursos[a][1]))
            labelCurso3 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.miscursos[a][3]))
            
            xw1 = wx.CheckBox(self, -1 ,'', (15, 30))
            xw1.SetValue(False)
            xw1.Bind(wx.EVT_RADIOBUTTON, self.OnClick, xw1 ,id = int(self.miscursos[a][0]))
            
            grilla.Add(labelCurso,0, wx.ALIGN_CENTER)
            grilla.Add(labelCurso2,0, wx.ALIGN_CENTER)
            grilla.Add(labelCurso3,0, wx.ALIGN_CENTER)
            grilla.Add(xw1,0, wx.ALIGN_CENTER)
                            
#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label--------------
#--------------Creacion padre hijo--------------
	PanelComponentsButtons = wx.Panel(self) 
		
	self.Button1 = Component.CreateButton(PanelComponentsButtons,"Seleccionar")
#--------------Creaci贸n de Evento--------------
	self.Bind(wx.EVT_BUTTON, self.OnClick)

#--------------Creacion caja de tama帽os--------------
	sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel--------------
	sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) 
	PanelComponentsButtons.SetSizer(sizerPanelButton)
#--------------Asignaci贸n de Color de Fondo-------------- 
	PanelComponentsButtons.SetBackgroundColour("3399FF") 
        
#--------------Creacion grilla de tamano 3 filas 1 columna--------------
	gs = wx.GridSizer(4, 1, 0, 0) 
#--------------Adicion de Paneles a la Grilla--------------
	gs.AddMany([(PanelComponentsLabel, 0, wx.ALIGN_CENTER),(grilla, 0, wx.ALIGN_CENTER)
        ,(PanelComponentsButtons, 0, wx.ALIGN_CENTER)])
		
#--------------Adicion de la grilla de tamanos al panel padre--------------	
	
	sizer = wx.BoxSizer(wx.VERTICAL) 
	sizer.Add(gs, proportion=1, flag=wx.EXPAND)
	self.SetSizer(sizer)
        		
    def OnClick(self,event):
        'Identifica el evento del Bot髇.'
        self.idcurso = str('2')
        interfaz = ElegirExamen.Body(self.parent,self.idestudiante,self.idcurso)
        self.frame.cambiarpanel(interfaz)
 
 ##-----------------------------------------------------------                
## BuscarCursos
##-----------------------------------------------------------el):
class buscarcursos(wx.Panel):    
    def __init__(self,parent,idestudiante,frame):
        self.parent=parent
        'Constructor que recibe a parent como contenedor'
#--------------Inicializacion Panel Padre--------------
	wx.Panel.__init__(self,parent) 
	self.SetBackgroundColour("3399FF")
               
#--------------Instancia Clase Componente--------------
	Component = Componentes.Component(self) 
	self.parent=parent
        self.frame=frame
        self.idestudiante=idestudiante
        
        querybuscarcursos = "select curso.id_curso, curso.nom_curso, persona.id_persona, (persona.nom_pers||' '||persona.apellido_pers) "
        querybuscarcursos += "from curso, persona, docente where curso.id_prof = docente.id_persona and "
        querybuscarcursos += "docente.id_persona = persona.id_persona order by curso.id_curso"
        
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        self.buscarcursos = self.conexion.connection.ExecuteQuery(querybuscarcursos)
        
#--------------Creacion padre hijo--------------
	PanelComponentsLabel = wx.Panel(self) 
#--------------Label "Buscar cursos"--------------
	self.label = Component.CreateLabel(PanelComponentsLabel,15,pos=(0,0),label="Buscar Cursos")
		
	sizerPanelLabel = wx.BoxSizer(wx.VERTICAL)
	sizerPanelLabel.Add(self.label, 0, wx.ALIGN_CENTER)
	
        PanelComponentsLabel.SetSizer(sizerPanelLabel)
        PanelComponentsLabel.SetBackgroundColour("3399FF")

        grilla = wx.GridSizer(len(self.buscarcursos)+1, 4, 0, 0) 
        labelTitulo1 = Component.CreateLabel(self,12,pos=(0,0),label= 'C骴igo')
        labelTitulo2 = Component.CreateLabel(self,12,pos=(0,0),label= 'Nombre')
        labelTitulo3 = Component.CreateLabel(self,12,pos=(0,0),label= 'Docente')
        labelTitulo4 = Component.CreateLabel(self,12,pos=(0,0),label= ' ')
        
        grilla.Add(labelTitulo1,0, wx.ALIGN_CENTER)
        grilla.Add(labelTitulo2,0, wx.ALIGN_CENTER)
        grilla.Add(labelTitulo3,0, wx.ALIGN_CENTER)        
        grilla.Add(labelTitulo4,0, wx.ALIGN_CENTER)        
        
        for a in range (len(self.buscarcursos)):
            
            labelCurso = Component.CreateLabel(self,12,pos=(0,0),label= str(self.buscarcursos[a][0]))
            labelCurso2 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.buscarcursos[a][1]))
            labelCurso3 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.buscarcursos[a][3]))
            buttonCurso = Component.CreateButton(self,"Inscribir")
            buttonCurso.Bind(wx.EVT_BUTTON, self.OnClick)
            
            grilla.Add(labelCurso,0, wx.ALIGN_CENTER)
            grilla.Add(labelCurso2,0, wx.ALIGN_CENTER)
            grilla.Add(labelCurso3,0, wx.ALIGN_CENTER)
            grilla.Add(buttonCurso,0, wx.ALIGN_CENTER)
                            
#--------------Creacion de un panel de Buttons, e inclusion  del objeto Buttons y su Label--------------
#--------------Creacion padre hijo--------------
	PanelComponentsButtons = wx.Panel(self) 
		
	self.Button1 = Component.CreateButton(PanelComponentsButtons,"Inscribir")
#--------------Creaci贸n de Evento--------------
	self.Bind(wx.EVT_BUTTON, self.OnClick)

#--------------Creacion caja de tama帽os--------------
	sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) 
#--------------Adicion del Objeto al panel--------------
	sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) 
	PanelComponentsButtons.SetSizer(sizerPanelButton)
#--------------Asignaci贸n de Color de Fondo-------------- 
	PanelComponentsButtons.SetBackgroundColour("3399FF") 
        
#--------------Creacion grilla de tamano 3 filas 1 columna--------------
	gs = wx.GridSizer(4, 1, 0, 0) 
#--------------Adicion de Paneles a la Grilla--------------
	gs.AddMany([(PanelComponentsLabel, 0, wx.ALIGN_CENTER),(grilla, 0, wx.ALIGN_CENTER)
        ,(PanelComponentsButtons, 0, wx.ALIGN_CENTER)])
		
#--------------Adicion de la grilla de tamanos al panel padre--------------	
	
	sizer = wx.BoxSizer(wx.VERTICAL) 
	sizer.Add(gs, proportion=1, flag=wx.EXPAND)
	self.SetSizer(sizer)
		
    def OnClick(self,event):
        'Identifica el evento del Bot髇.'
        interfaz = miscursos(self.parent,self.idestudiante,self.frame)
        self.frame.cambiarpanel(interfaz)