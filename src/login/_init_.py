#!/usr/bin/env python
# -*- coding: cp1252 -*-
__author__ = "EDUARDO"
__date__ = "$15/10/2015 06:42:15 PM$"
import wx, ConnSchema,ConnectionDataBase
import Correo
import wx
import administradorInterfaz.__init__
import DocenteInterfaz.__init__
#import EstudiantesInterfaz.IniciarSesion
import wx.lib.scrolledpanel as scrolled
import smtplib 
import HeadLow
import Componentes



## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee ingresar y 
    este registrado pueda digitar su usario y su clave."""
    def __init__(self, parent):#, manipulador):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        self.parent=parent
        wx.Panel.__init__(self,parent) # Inicializacion Panel Padre
        self.SetBackgroundColour('3399FF')
        #self.father = manipulador

        # parametros basicos generales del registro de un examen
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se requerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
            
        self.lblusuario = wx.StaticText(self, label="Usuario: ", pos=(100,35))
        self.editusuario = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        self.lblcontra = wx.StaticText(self, label="Contraseña: ", pos=(100,65))
        self.editcontra = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1), style=wx.TE_PASSWORD)
        self.lbltipo = wx.StaticText(self, label="Tipo de Usuario: ", pos=(100,65))
        self.sampleListTipo = []
        query ="SELECT * FROM tipopersona;"
        self.tipoescogido = '' #se almacenara el identificador del tipo escogido
        self.opcionesRoles = self.conexion.connection.ExecuteQuery(query) #consulta de todos los tipos de usuarios
        print("consutla sql de tipos de roles "+str(self.opcionesRoles))
        for a in self.opcionesRoles:
            self.sampleListTipo.append(a[1])
        self.edittipo = wx.ComboBox(self, choices=self.sampleListTipo, style=wx.CB_DROPDOWN)
        self.edittipo.Bind(wx.EVT_COMBOBOX, self.idtipoescogido)
        self.buttoningresar =wx.Button(self, wx.ID_OK, label="Ingresar", pos=(100,65))
        self.buttonolvidar =wx.Button(self, wx.ID_OK, label="Olvidé la contraseña", pos=(0, 35))
        #como crear un boton agregando su evento
        
        self.buttoningresar.Bind(wx.EVT_BUTTON, self.ingresar)
        self.Bind(wx.EVT_BUTTON, self.olvidarcon, self.buttonolvidar)
        gs = wx.GridSizer(9, 2, 5, 5) #Creacion grilla de tamaÃ±o
        #--------------AdiciÃ³n de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaÃ±o de la pantalla
        gs.AddMany([(self.lblusuario, 0, wx.ALIGN_CENTER),(self.editusuario, 0, wx.ALIGN_CENTER),
                    (self.lblcontra, 0, wx.ALIGN_CENTER),(self.editcontra, 0, wx.ALIGN_CENTER),
                    (self.lbltipo, 0, wx.ALIGN_CENTER),(self.edittipo, 0, wx.ALIGN_CENTER),
                    (self.buttoningresar, 0, wx.ALIGN_CENTER),(self.buttonolvidar, 0, wx.ALIGN_CENTER)])
        sizer = wx.BoxSizer(wx.VERTICAL) #AdiciÃ³n de la grilla de tamaÃ±os al panel padre
        sizer.Add(gs, proportion=1, flag=wx.ALIGN_CENTER)
        self.SetSizer(sizer)
    
    def ingresar(self, e):
        'metodo que capturara los datos y los comprobara con la bd para ingresar a su respectiva interfaz'
        tipo= str(self.tipoescogido)
        usuario=self.editusuario.GetValue()
        contrasena=self.editcontra.GetValue()
        if tipo=='1':
            query ="SELECT p.id_persona FROM persona p, estudiante e WHERE p.usuario='"+usuario+"' AND e.pass_estu='"+contrasena+"' AND p.idtipopersona=1 AND p.id_persona=e.id_persn;"
            idusuario=self.conexion.connection.ExecuteQuery(query)
            if idusuario:
                print('ahi')
                print(idusuario + "no lo pide")
                
            else:
                wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        elif tipo=='2':
            query ="SELECT p.id_persona FROM persona p, docente d WHERE p.usuario='"+usuario+"' AND d.pass_docente='"+contrasena+"' AND p.idtipopersona=2 AND p.id_persona=d.id_persona;"
            idusuario=self.conexion.connection.ExecuteQuery(query)
            if idusuario:
                DocenteInterfaz.__init__.MenuPrincipalDocente(str(idusuario[0][0]))
            else:
                wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        elif tipo=='3':
            query ="SELECT p.id_persona FROM persona p, administrador a WHERE p.usuario='"+usuario+"' AND a.pass_adm='"+contrasena+"' AND p.idtipopersona=3 AND p.id_persona=a.id_persn;"
            idusuario=self.conexion.connection.ExecuteQuery(query)
            if idusuario:
                administradorInterfaz.__init__.MenuPrincipaladmin(str(idusuario[0][0]))
            else:
               wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        else:
            wx.MessageBox("Escoja una opción","Gesdatos")
        
    def olvidarcon(self,e):
        'metodo que envia la contrasena al correo registrado si el usuario existe'
        tipo= str(self.tipoescogido)
        usuario=self.editusuario.GetValue()
        if tipo=='1':
            query ="SELECT p.correo, e.pass_estu FROM persona p, estudiante e WHERE p.usuario='"+usuario+"' AND p.idtipopersona=1 AND p.id_persona=e.id_persn"           
            dusuario=self.conexion.connection.ExecuteQuery(query)
            if dusuario:
                print(dusuario)        
                destino = dusuario[0][0]
                text = 'Usuario '+usuario+': Su contrasena es '+dusuario[0][1]
                m = Correo.Correo()
                m.enviar(destino,text,'Recuperacion contraseña')
            else:
               wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        elif tipo=='2':
            query ="SELECT p.correo, d.pass_docente FROM persona p, docente d WHERE p.usuario='"+usuario+"' AND p.idtipopersona=2 AND p.id_persona=d.id_persona"           
            dusuario=self.conexion.connection.ExecuteQuery(query)
            if dusuario:
                print(dusuario)        
                destino = dusuario[0][0]
                text = 'Usuario '+usuario+': Su contrasena es '+dusuario[0][1]
                m = Correo.Correo()
                m.enviar(destino,text,'Recuperacion contraseña')
            else:
               wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        elif tipo=='3':
            query ="SELECT p.correo, a.pass_adm FROM persona p, administrador a WHERE p.usuario='"+usuario+"' AND p.idtipopersona=3 AND p.id_persona=a.id_persn"           
            dusuario=self.conexion.connection.ExecuteQuery(query)
            if dusuario:
                print(dusuario)        
                destino = dusuario[0][0]
                text = 'Usuario '+usuario+': Su contrasena es '+dusuario[0][1]
                m = Correo.Correo()
                m.enviar(destino,text,'Recuperacion contraseña')
            else:
               wx.MessageBox("El usuario con esas características no existe","Gesdatos")
        else:
            wx.MessageBox("Ingrese el usuario y el tipo de usuario","Gesdatos")        
        
 
    def idtipoescogido(self,e):
        'metodo escucha de evento de escoger un tipo con fin de saber el valor del rol escogido'
        tiporol = e.GetString()
        fila = 0
        for it in self.sampleListTipo:
            if it == tiporol:
                self.tipoescogido = self.opcionesRoles[fila][0]
                print(self.tipoescogido)
                break
            fila=fila+1

##-----------------------------------------------------------

        def cambiarpanel(self,nuevopanel):
            """Metodo usado para cambiar un panel en el que ya se
             registró la informacion para el nuevo examen y se requiere
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
frame = wx.Frame(None, wx.ID_ANY, 'ZUHÉ - UD', pos=(0, 0), size=(displaySize[0], displaySize[1]))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour('3399FF')
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()