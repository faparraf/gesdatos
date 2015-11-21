#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, ConnSchema,ConnectionDataBase
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes
import nuevoExamen.__init__
#from sshtunnel import SSHTunnelForwarder
# Identificdores en el menu
ID_AGREGAR_EXAMEN = wx.NewId ()

class MenuPrincipalDocente(wx.Frame):
    def __init__(self,iddocente,localport):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        self.localport = str(localport)
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",self.localport)#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        self.iddocente = iddocente
        app=wx.App(False)
        displaySize= wx.DisplaySize()
        wx.Frame.__init__(self, None, pos=(0, 0), size=(displaySize[0], displaySize[1]))
        displaySize= wx.DisplaySize()
        topPanel= scrolled.ScrolledPanel(self)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour('3399FF')
        sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(Body(topPanel,iddocente,self.localport),0,wx.EXPAND|wx.ALL,border=10)
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
        menu = wx.Menu()
        m_agregartema = menu.Append(ID_AGREGAR_EXAMEN,"&Examen", "Agregar nuevo Examen")
        self.Bind(wx.EVT_MENU, self.agregar, m_agregartema, id=ID_AGREGAR_EXAMEN)
        menuBar.Append(menu, "&Examen")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&Sobre nosotros", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Ayuda")
        self.SetMenuBar(menuBar)
        self.Show()
        app.MainLoop()
        self.GetSizer().Layout()
        self.Fit()
    
    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
        "øRealmente quiere salir?",
        "Confirmar Salida", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
    
    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()
        
    def agregar(self,event):
        parametro = event.GetId()
        if parametro == ID_AGREGAR_EXAMEN:
            interfaz = nuevoExamen.__init__.interfazpanelpaso(self,self.iddocente,self.topPanel,self.sizer,self.localport)
            panelagregar = nuevoExamen.__init__.BodyNuevoExamen(self.topPanel,interfaz,self.iddocente)
        self.cambiarpanel(panelagregar)
    
    def getconexion(self):
            """consutlor que retorna la clase administradora de la base de datos"""
            return self.conexion.connection
    
    def regresarpanelprincipal(self):
        panel_original = Body(self.topPanel,self.iddocente)
        self.cambiarpanel(panel_original)
    
    def cambiarpanel(self,nuevopanel):
        """Metodo usado para cambiar un panel en el que ya se
            registrÛ la informacion para el nuevo examen y se requiere
            que el siguiente paso en el registro de un nuevo examen se muestre
            requiere como parametro el nuevo panel "nuevopanel" en el que se va a
            reemplazar el ya utlizado"""
        #siempre se cambia en la poscion 2 ya que es la del body
        sizer = self.sizer
        sizer.Hide(0)
        sizer.Remove(0)
        sizer.Hide(0)
        sizer.Remove(0)
        sizer.Hide(0)
        sizer.Remove(0)
        sizer.Add(HeadLow.Head(self.topanel),0,wx.EXPAND|wx.ALL,border=10)
        sizer.Add(nuevopanel,0,wx.EXPAND|wx.ALL,border=10)
        sizer.Add(HeadLow.Low(self.topanel),0,wx.EXPAND|wx.ALL,border=10)
        self.topanel.SetSizer(self.sizer)
        self.SetSizer(sizer)
        self.GetSizer().Layout()
        self.Fit()
        
## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent, iddocente,localport):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # InicializaciÛn Panel Padre
        self.SetBackgroundColour('3399FF')
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",localport)#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        queryidexamen = "select (nom_pers||' '||apellido_pers) from persona where id_persona = "+iddocente+";"
        self.nombre = self.conexion.connection.ExecuteQuery(queryidexamen)
        self.nombre = (self.nombre[0][0])
        self.quote = wx.StaticText(self, label="Bienvenido Docente: "+self.nombre, pos=(140, 10))
        self.aparte = wx.StaticText(self, label="", pos=(140, 10))
        gs = wx.GridSizer(1, 2, 1, 1) #Creacion grilla de tama√±o
        #--------------Adici√≥n de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tama√±o de la pantalla
        gs.AddMany([(self.quote, 0, wx.ALIGN_CENTER),(self.aparte, 0, wx.ALIGN_CENTER),
                    ])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adici√≥n de la grilla de tama√±os al panel padre
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
            

#with SSHTunnelForwarder(
#	('200.69.103.79', 22),
#	ssh_password="gesdatosestudent",
#	ssh_username="estgesdatos",
#	remote_bind_address=('127.0.0.1', 5432)) as server:
#            iddocente = "4"
#            MenuPrincipalDocente(iddocente,server.local_bind_port)