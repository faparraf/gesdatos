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
        'Constructor que requiere de un parent como interfaz contendor y manipulador para que acceda a la información'
        app=wx.App(False)
        displaySize= wx.DisplaySize()
        wx.Frame.__init__(self, None, pos=(0, 0), size=(displaySize[0], displaySize[1]))
        displaySize= wx.DisplaySize()
        topPanel= scrolled.ScrolledPanel(self)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour('#00BF8F')
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
            "¿Realmente quiere salir?",
            "Confirmar Salida", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_OK:
                self.Destroy()

## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    def __init__(self,parent,idestudiante,idcurso, localport):
        'Constructor de la interfaz que recibe su contenedor'
#--------------Inicializacion Panel Padre--------------
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour("#00BF8F")
#--------------Instancia Clase Componente--------------
        Component = Componentes.Component(self) 
        self.parent=parent
        self.idestudiante=idestudiante
        self.idcurso = idcurso
        self.localport = str(localport)

        queryexamencurso = "select examen.id_exa, examen.titulo_exa, tipoexamen.desc_tipoexa, examen.fecha,  "
        queryexamencurso += "examen.tiempo_exa_inicio, examen.tiempo_exa_fin from examen, curso_examen, tipoexamen "
        queryexamencurso += "where curso_examen.id_curso = "+ str(self.idcurso)+" and curso_examen.id_examen = examen.id_exa "
        queryexamencurso += "and examen.tipoexa = tipoexamen.id_tipoexa order by examen.fecha, examen.tiempo_exa_inicio "
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",self.localport)
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
        PanelComponentsLabel.SetBackgroundColour("#00BF8F")
		                
         
        if len(self.examenescurso) == 0:
            label0 = Component.CreateLabel(self,12,pos=(0,0),label= 'El curso no tiene exámenes asignados')
            grilla = wx.GridSizer(1, 1, 0, 0)
            grilla.Add(label0,0, wx.ALIGN_CENTER)
        else:
            grilla = wx.GridSizer(len(self.examenescurso)+1, 7, 0, 0)
            labelTitulo1 = Component.CreateLabel(self,12,pos=(0,0),label= 'Código')
            labelTitulo2 = Component.CreateLabel(self,12,pos=(0,0),label= 'Nombre')
            labelTitulo3 = Component.CreateLabel(self,12,pos=(0,0),label= 'Tipo')
            labelTitulo4 = Component.CreateLabel(self,12,pos=(0,0),label= 'Fecha')
            labelTitulo5 = Component.CreateLabel(self,12,pos=(0,0),label= 'Hora Inicio')
            labelTitulo6 = Component.CreateLabel(self,12,pos=(0,0),label= 'Hora Final')
            labelTitulo7 = Component.CreateLabel(self,12,pos=(0,0),label= ' ')

            grilla.Add(labelTitulo1,0, wx.ALIGN_CENTER)
            grilla.Add(labelTitulo2,0, wx.ALIGN_CENTER)
            grilla.Add(labelTitulo3,0, wx.ALIGN_CENTER)        
            grilla.Add(labelTitulo4,0, wx.ALIGN_CENTER)        
            grilla.Add(labelTitulo5,0, wx.ALIGN_CENTER)        
            grilla.Add(labelTitulo6,0, wx.ALIGN_CENTER)        
            grilla.Add(labelTitulo7,0, wx.ALIGN_CENTER)        
               
        for a in range (len(self.examenescurso)):
            
            labelExamen1 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][0]))
            labelExamen2 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][1]))
            labelExamen3 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][2]))
            labelExamen4 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][3]))
            labelExamen5 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][4]))
            labelExamen6 = Component.CreateLabel(self,12,pos=(0,0),label= str(self.examenescurso[a][5]))
           
            buttonExamen = Component.CreateButton(self,"Seleccionar")
            buttonExamen.idexam = self.examenescurso[a][0]
            buttonExamen.Bind(wx.EVT_BUTTON, self.OnClick, buttonExamen)
            
            grilla.Add(labelExamen1,0, wx.ALIGN_CENTER)
            grilla.Add(labelExamen2,0, wx.ALIGN_CENTER)
            grilla.Add(labelExamen3,0, wx.ALIGN_CENTER)
            grilla.Add(labelExamen4,0, wx.ALIGN_CENTER)
            grilla.Add(labelExamen5,0, wx.ALIGN_CENTER)
            grilla.Add(labelExamen6,0, wx.ALIGN_CENTER)
            grilla.Add(buttonExamen,0, wx.ALIGN_CENTER)

#--------------Creacion grilla de tamano 2 filas 1 columna--------------
        gs = wx.GridSizer(2, 1, 0, 0) 
#--------------Adicion de Paneles a la Grilla--------------
        gs.AddMany([(PanelComponentsLabel, 0, wx.ALIGN_CENTER),(grilla, 0, wx.ALIGN_CENTER)])
#--------------Adicion de la grilla de tamanos al panel padre--------------	
        sizer = wx.BoxSizer(wx.VERTICAL) 
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

    def OnClick(self,event):
            'Permite establecer el evento del Botón'
            print ("cargando examen")
            idexamen = event.GetEventObject().idexam
            verexamen = cargarExamen.iniciarverexamen(idexamen)