#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero"
__date__ = "$20-jul-2015 18:52:55$"
import wx, ConnSchema


########################################################################
class dialogoregistroEstudiantes(wx.Panel):
    """ Genera un panel en donde se introducira todos los estudiantes dsponibles
    con el fin de que el docente pueda registrar aquellos que deben registrar el examen"""

    #----------------------------------------------------------------------
    def __init__(self,conexion,parent,manipulador,cantidadpregutnas):
        """Constructor, requiere de conexion como la clase que conecta el
        software con la base de datos, la clase parent como el contenedor
        grafico del panel, manipulador como la clase que se encargara de
        gestionar la informacion a ingresar por este panel y la cantidad de
        preguntas que el examen ha de tener."""
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour("white")
        self.estudiantesescogidos = []
        self.father = manipulador
        self.cantdad = cantidadpregutnas
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Consulta de todos los estudiantes disponibles
        query = "SELECT  estudiante.id_persn, estudiante.fecha_reg, (persona.nom_pers || ' ' || persona.apellido_pers) AS nombrecompleto FROM estudiante, persona WHERE estudiante.id_persn = persona.id_persona;"
        sampleList = conexion.connection.ExecuteQuery(query) #comentado mienstras no este creada la base ded datos
        print(str(sampleList))
        #sampleList = [("123","10/10/2010","Rex Arias"),("124","10/10/2010","Alison C."),("125","10/10/2010","Dante T.")]
        self.listBox1 = wx.ListBox(choices=[],
              name='listBox1', parent=self, pos=wx.Point(8, 48),
              size=wx.Size(184, 256),  style =  wx.LB_HSCROLL
                                           | wx.LB_MULTIPLE
                                           | wx.LB_NEEDED_SB
                                           | wx.LB_SORT)
        self.listBox1.SetBackgroundColour(wx.Colour(255, 255, 128))
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox)
        for text in sampleList:
            item = self.listBox1.Append(str(text[0])+': '+str(text[2]))
        okBtn = wx.Button(self, wx.ID_OK)
        for i in range(self.listBox1.GetCount()):
            self.listBox1.SetSelection(i)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        sizer.Add(self.listBox1, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
        
    def OnListBox1Listbox(self,e):
        'oyente de la lista de estudiantes para saber cuantos estan escogidos'
        estudiante = e.GetString()
        caracestudiantes = estudiante.split(': ',1)#solo hara una particion
        #print(estudiante+" analizando "+str(caracestudiantes)+" "+str(caracestudiantes[0]))
        if caracestudiantes[0] in self.estudiantesescogidos:
            self.estudiantesescogidos.remove(str(caracestudiantes[0]))
        else:
            self.estudiantesescogidos.append(str(caracestudiantes[0]))
        #print(e.GetString())
        
    def registro(self, e):
        'oyente del boton aceptar para gestionar la informacion escogida'
        # Definimos los metodos de los eventos
        self.father.registrarEstudiantes(e,self,self.cantdad)
