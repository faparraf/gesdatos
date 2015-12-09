#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, ConnSchema,ConnectionDataBase
import wx
import InterfazExamen.__init__
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes


## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent, manipulador):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicialización Panel Padre
        self.SetBackgroundColour('3399FF')
        self.father = manipulador
        self.quote = wx.StaticText(self, label="Invitado", pos=(140, 10))
        self.aparte = wx.StaticText(self, label="", pos=(140, 10))
        #self.CreateStatusBar()

        # parametros basicos generales del registro de un examen
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #INSERCION DE TIPO DE EXAMEN
        self.lbltipo = wx.StaticText(self, label="Tema Examen :", pos=(100,120))
        self.sampleListTipo = []
        query ="SELECT * FROM tema;"    
        self.temaescogido = ''#se almacenara el identificador del tema escogido
        self.opcionesexamenTema = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesexamenTema))
        for a in self.opcionesexamenTema:
            self.sampleListTipo.append(a[2])
        self.edittipo = wx.ComboBox(self, choices=self.sampleListTipo, style=wx.CB_DROPDOWN)
        self.edittipo.Bind(wx.EVT_COMBOBOX, self.idtemaescogido)
        
        self.hbox1.Add(self.lbltipo, flag=wx.RIGHT, border=8)
        self.hbox1.Add(self.edittipo, flag=wx.RIGHT, border=8)
        self.lblcod = wx.StaticText(self, label="Codigo Examen :", pos=(100,65))
        self.editcod = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.eventotexto, self.editcod)
        self.hbox1.Add(self.lblcod, flag=wx.RIGHT, border=8)
        self.hbox1.Add(self.editcod, flag=wx.RIGHT, border=8)
        
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        self.listBox1 = wx.ListBox(choices=[],
              name='listBox1', parent=self, pos=wx.Point(8, 48),
              size=wx.Size(184, 256),  style =  wx.LB_HSCROLL
                                           | wx.LB_NEEDED_SB
                                           | wx.LB_SORT)
        self.listBox1.SetBackgroundColour(wx.Colour(255, 255, 128))
        self.examenesDisponibles();
        sizer = wx.BoxSizer(wx.VERTICAL) #AdiciÃ³n de la grilla de tamaÃ±os al panel padre
        sizer.Add(self.quote, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        sizer.Add(self.aparte, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        sizer.Add(self.hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        sizer.Add(self.listBox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        sizer.Add(self.button, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        self.SetSizer(sizer)
    
    def eventotexto(self,e):
        'Metodo usado para actualizar lista de examenes disponibles, esto se hace porque el evento de llamar a texto'
        'requiere de la variable e que es el escucha del editor de texto'
        self.examenesDisponibles()
    
    def examenesDisponibles(self):
        'metodo encargado de buscar en la base ded atos los examenes disponibles'
        self.sampleList = []
        self.listBox1.Clear()
        query ="SELECT DISTINCT id_exa, titulo_exa FROM examen,examenpreg, pregunta where id_prgnta=id_pregunta"
        query+= " and id_exa=id_examen and  CAST(tema AS TEXT) LIKE '"+str(self.temaescogido)+"%'"
        query+= " and  CAST(id_exa AS TEXT) LIKE '"+self.editcod.GetValue()+"%';"    
        print(query)
        self.sampleList = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.sampleList))
        for text in self.sampleList:
            item = self.listBox1.Append(str(text[0])+': '+str(text[1]))
        return self.sampleList
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el docente'
        # Definimos los métodos de los eventos
        idexam = self.listBox1.GetString(self.listBox1.GetSelection ()) 
        self.idexamen = ((idexam[0]).split(': ',0))[0]#solo hara una particion
        print("Examen a ver "+str(self.idexamen))
        self.father.iniciarinterfazExamen(self.idexamen)
    
    def idtemaescogido(self,e):
        'metodo escucha de evento de escoger un tema con fin de saber  el valor de la llave del tema escogido'
        temaexamen = e.GetString()
        fila = 0
        for it in self.sampleListTipo:
            if it == temaexamen:
                self.temaescogido = self.opcionesexamenTema[fila][0]
                break
            fila=fila+1
        self.examenesDisponibles()

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
        
        def __init__(self, parent,topPanel,sizertopPanel,puerto):
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
            self.puerto = puerto
            self.sizer = sizertopPanel
            self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",str(puerto))#se rquerie de datos para conexion a motor
            self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
            #self.Bind(wx.EVT_BUTTON, self.registrarExamen,self.button)
        
        def getconexion(self):
            """consutlor que retorna la clase administradora de la base de datos"""
            return self.conexion.connection
        
        def iniciarinterfazExamen(self,idexamen):
            verexamen = InterfazExamen.__init__.iniciarverexamen(idexamen,self.puerto)
            res = verexamen.ShowModal()
            if res == wx.ID_OK:
                print("examen contestado")
            verexamen.Destroy()
            
#app=wx.App(False)
#displaySize= wx.DisplaySize()
#frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
#menubar = wx.MenuBar()
#topPanel= scrolled.ScrolledPanel(frame)
#topPanel.SetupScrolling(scroll_y=True)
#topPanel.SetBackgroundColour('3399FF')
#sizertopPanel=wx.BoxSizer(wx.VERTICAL)
#interfaz = interfazpanelpaso(frame,topPanel,sizertopPanel,"5434")
#sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
#sizertopPanel.Add(Body(topPanel,interfaz),0,wx.EXPAND|wx.ALL,border=10)
#sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
#topPanel.SetSizer(sizertopPanel)
#frame.Show()
#app.MainLoop()