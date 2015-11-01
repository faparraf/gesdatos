#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, ConnSchema,ConnectionDataBase
import wx
import InterfazExamen.__init__
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes

class MenuPrincipaladmin(wx.Panel):
    def __init__(self, parent, manipulador):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # InicializaciÛn Panel Padre
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.GetTopLevelParent().SetMenuBar(menuBar)
    
    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
        "Do you really want to close this application?",
        "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
    
    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()  
## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent, manipulador, iddocente):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # InicializaciÛn Panel Padre
        self.SetBackgroundColour('3399FF')
        self.father = manipulador
        self.quote = wx.StaticText(self, label="Docente: "+iddocente, pos=(140, 10))
        self.aparte = wx.StaticText(self, label="", pos=(140, 10))
        #self.CreateStatusBar()

        # parametros basicos generales del registro de un examen
        self.lblname = wx.StaticText(self, label="Nombre Examen :", pos=(100,35))
        self.editname = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        self.lblfecha = wx.StaticText(self, label="Fecha Examen :", pos=(100,65))
        self.editfecha = wx.DatePickerCtrl(self,pos=(0,65), size=(140,22), style=wx.DP_DROPDOWN)
        self.lblhoraini = wx.StaticText(self, label="Hora Inicio :", pos=(100,65))
        self.edithoraini = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.lblhorafin = wx.StaticText(self, label="Hora Fin :", pos=(100,65))
        self.edithorafin = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.lblpuntjae = wx.StaticText(self, label="Puntaje Extra Examen :", pos=(100,95))
        self.editpuntjae = wx.TextCtrl(self, value="", pos=(0, 95), size=(140,-1))
        self.lbltipo = wx.StaticText(self, label="Tipo Examen :", pos=(100,120))
        self.sampleListTipo = []
        query ="SELECT * FROM tipoexamen;"    
        self.temaescogido = ''#se almacenara el identificador del tema escogido
        self.opcionesexamenTema = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesexamenTema))
        for a in self.opcionesexamenTema:
            self.sampleListTipo.append(a[1])
        self.edittipo = wx.ComboBox(self, choices=self.sampleListTipo, style=wx.CB_DROPDOWN)
        self.edittipo.Bind(wx.EVT_COMBOBOX, self.idtemaescogido)
        #self.edittipo = wx.TextCtrl(self, value="", pos=(0, 120), size=(140,-1))
        self.lblcantidad = wx.StaticText(self, label="Cantidad de Preguntas :", pos=(100,150))
        self.editcantidad = wx.TextCtrl(self, value="1", pos=(0, 150), size=(140,-1))
        
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        gs = wx.GridSizer(9, 2, 5, 5) #Creacion grilla de tama√±o
        #--------------Adici√≥n de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tama√±o de la pantalla
        gs.AddMany([(self.quote, 0, wx.ALIGN_CENTER),(self.aparte, 0, wx.ALIGN_CENTER),
                    (self.lblname, 0, wx.ALIGN_CENTER),(self.editname, 0, wx.ALIGN_CENTER),
                    (self.lblfecha, 0, wx.ALIGN_CENTER),(self.editfecha, 0, wx.ALIGN_CENTER),
                    (self.lblhoraini, 0, wx.ALIGN_CENTER),(self.edithoraini, 0, wx.ALIGN_CENTER),
                    (self.lblhorafin, 0, wx.ALIGN_CENTER),(self.edithorafin, 0, wx.ALIGN_CENTER),
                    (self.lblpuntjae, 0, wx.ALIGN_CENTER),(self.editpuntjae, 0, wx.ALIGN_CENTER),
                    (self.lbltipo, 0, wx.ALIGN_CENTER),(self.edittipo, 0, wx.ALIGN_CENTER),
                    (self.lblcantidad, 0, wx.ALIGN_CENTER),(self.editcantidad, 0, wx.ALIGN_CENTER),
                    (self.button, 0, wx.ALIGN_CENTER)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adici√≥n de la grilla de tama√±os al panel padre
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el docente'
        # Definimos los mÈtodos de los eventos
        self.father.registrarExamen(e,self)
    
    def idtemaescogido(self,e):
        'metodo escucha de evento de escoger un tema con fin de saber  el valor de la llave del tema escogido'
        temaexamen = e.GetString()
        fila = 0
        for it in self.sampleListTipo:
            if it == temaexamen:
                self.temaescogido = self.opcionesexamenTema[fila][0]
                break
            fila=fila+1

##-----------------------------------------------------------

class interfazpanelpaso():
        """ Interfaz general utilizado para llamar a los paneles
        con el fin de que con cada panel el usuario pueda
        registrar datos generales del examen a registrar, los estudiantes
        que han de tener que presentar el mismo, las preguntas y las
        respuestas que conforman la evaluacion.

        cada vez que el usuario (en este caso el docente) pase de un paso
        como por ejemplo de registrar los estudiantes que practicaran el
        examen a registrar las preguntas que conformaran el mismo es necesario
        cambiar el panel del interfaz para mantenerse en la estructura Body
        ubicado entre Head y Low."""
        
        def __init__(self, parent,iddocente,topPanel,sizertopPanel):
            """ Metodo usado para iniciar el registro de un nuevo examen
            en sus parametros generales se encuentra el interfaz parent causante
            del llamado de esta clase para reguistrar un nuevo examen, se requere
            de iddocente que guardara el identificador del docente que hizo la peticion
            de un nuevo examen, topPanel usado para el almacenamiento de los objetos
            graficos guardandolos gentro de un panel con barra de desplazamiento, sizertopPanel
            usado como un objeto de wxPython para organizar los elementos que contengan
            los paneles."""
            self.father = parent
            self.topanel = topPanel
            self.sizer = sizertopPanel
            self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
            self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
            queryidexamen = "select count(*) from examen;"
            self.idexamen = self.conexion.connection.ExecuteQuery(queryidexamen)
            self.idexamen = (self.idexamen[0][0])+1
            #self.Bind(wx.EVT_BUTTON, self.registrarExamen,self.button)
            
        def getconexion(self):
            """consutlor que retorna la clase administradora de la base de datos"""
            return self.conexion.connection

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
            self.father.SetSizer(sizer)
            self.father.GetSizer().Layout()
            self.father.Fit()
            
app=wx.App(False)
displaySize= wx.DisplaySize()
frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour('3399FF')
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
iddocente = "4"
manipulador =""#temporal
interfaz = interfazpanelpaso(frame,iddocente,topPanel,sizertopPanel)
sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(MenuPrincipaladmin(topPanel,manipulador),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel,interfaz,iddocente),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()