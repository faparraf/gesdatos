#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, ConnSchema,ConnectionDataBase

## Body nuevo tema
##-----------------------------------------------------------el):
class paneltema(wx.Panel):
    """ Una clase personalizada .para agregar un nuevo tema
    donde se podra elegir por medio de la accion si editar o agregar parametro"""
    def __init__(self, parent,manipulador,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.lblid_bd = wx.StaticText(self, label="Base de datos escogida :", pos=(100,35))
        self.sampleListBase = []
        query ="SELECT id_base,nom_base FROM base;"    
        self.baseescogida = ''#se almacenara el identificador del tema escogido
        self.opcionesbase = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesbase))
        self.sampleListBase.append('')
        for a in self.opcionesbase:
            self.sampleListBase.append(a[1])
        self.edittipo = wx.ComboBox(self, choices=self.sampleListBase, style=wx.CB_DROPDOWN)
        self.lbldesc = wx.StaticText(self, label="Descripcion Tema :", pos=(100,35))
        self.editdesc = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbldesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editdesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblid_bd, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.edittipo, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.button, 0, wx.ALL|wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        self.edittipo.Bind(wx.EVT_COMBOBOX, self.idbaseescogida)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el administrador'
        # Definimos los m�todos de los eventos
        queryidpregunta = "select count(*) from tema;"
        idtema = (self.father.getconexion()).ExecuteQuery(queryidpregunta)
        idtema = (idtema[0][0])+1
        if self.baseescogida!='':
            inserttema = 'INSERT INTO tema ("idtema","id_bd","desc_tema")'
            inserttema += "VALUES ("+str(idtema)+","+str(self.baseescogida)+",'"+str(self.editdesc.GetValue())+"');"
            print (inserttema)
        else:
            inserttema = 'INSERT INTO tema ("idtema","desc_tema")'
            inserttema += "VALUES ("+str(idtema)+",'"+str(self.editdesc.GetValue())+"');"
            print (inserttema)
        (self.father.getconexion()).ExecuteQueryWithoutreturn(inserttema)
        dlg = wx.MessageDialog(self, 
            "Registro exitoso",
            "Confirmacion", wx.OK|wx.CANCEL)
        result = dlg.ShowModal()
        dlg.Destroy()
        self.father.regresarpanelprincipal()
    
    def idbaseescogida(self,e):
        'metodo escucha de evento de escoger un tema con fin de saber  el valor de la llave del tema escogido'
        baseescogida = e.GetString()
        fila = 0
        if baseescogida != '':
            for it in self.sampleListBase:
                if it == baseescogida:
                    self.baseescogida = self.opcionesbase[fila][0]
                    break
                fila=fila+1
        else:
            self.baseescogida = ''
## Body nuevo tipo pregunta
##-----------------------------------------------------------el):
class paneltipopregunta(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,manipulador,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.lbldesc = wx.StaticText(self, label="Descripcion Tipo de Pregunta :", pos=(100,35))
        self.editdesc = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbldesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editdesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.button, 0, wx.ALL|wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el administrador'
        # Definimos los m�todos de los eventos# Definimos los m�todos de los eventos
        queryidpregunta = "select count(*) from tipopegrunta;"
        idtema = (self.father.getconexion()).ExecuteQuery(queryidpregunta)
        idtema = (idtema[0][0])+1
        inserttema = 'INSERT INTO tipopegrunta ("id_tipopre","desc_tipopreg")'
        inserttema += "VALUES ("+str(idtema)+",'"+str(self.editdesc.GetValue())+"');"
        print (inserttema)
        (self.father.getconexion()).ExecuteQueryWithoutreturn(inserttema)
        dlg = wx.MessageDialog(self, 
            "Registro exitoso",
            "Confirmacion", wx.OK|wx.CANCEL)
        result = dlg.ShowModal()
        dlg.Destroy()
        self.father.regresarpanelprincipal()

## Body nuevo tipo opcion
##-----------------------------------------------------------el):
class paneltipoopcion(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,manipulador,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.lbldesc = wx.StaticText(self, label="Descripcion Tipo de Opcion Pregunta :", pos=(100,35))
        self.editdesc = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbldesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editdesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.button, 0, wx.ALL|wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el administrador'
        # Definimos los m�todos de los eventos# Definimos los m�todos de los eventos
        queryidpregunta = "select count(*) from tipoopcion;"
        idtema = (self.father.getconexion()).ExecuteQuery(queryidpregunta)
        idtema = (idtema[0][0])+1
        inserttema = 'INSERT INTO tipoopcion ("id_tipoop","desc_tipoopc")'
        inserttema += "VALUES ("+str(idtema)+",'"+str(self.editdesc.GetValue())+"');"
        print (inserttema)
        (self.father.getconexion()).ExecuteQueryWithoutreturn(inserttema)
        dlg = wx.MessageDialog(self, 
            "Registro exitoso",
            "Confirmacion", wx.OK|wx.CANCEL)
        result = dlg.ShowModal()
        dlg.Destroy()
        self.father.regresarpanelprincipal()
        
## Body nuevo tipo examen
##-----------------------------------------------------------el):
class paneltipoexamen(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,manipulador,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.lbldesc = wx.StaticText(self, label="Descripcion Tipo de Examen :", pos=(100,35))
        self.editdesc = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbldesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editdesc, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.button, 0, wx.ALL|wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el administrador'
        # Definimos los m�todos de los eventos# Definimos los m�todos de los eventos
        queryidpregunta = "select count(*) from tipoexamen;"
        idtema = (self.father.getconexion()).ExecuteQuery(queryidpregunta)
        idtema = (idtema[0][0])+1
        inserttema = 'INSERT INTO tipoexamen ("id_tipoexa","desc_tipoexa")'
        inserttema += "VALUES ("+str(idtema)+",'"+str(self.editdesc.GetValue())+"');"
        print (inserttema)
        (self.father.getconexion()).ExecuteQueryWithoutreturn(inserttema)
        dlg = wx.MessageDialog(self, 
            "Registro exitoso",
            "Confirmacion", wx.OK|wx.CANCEL)
        result = dlg.ShowModal()
        dlg.Destroy()
        self.father.regresarpanelprincipal()