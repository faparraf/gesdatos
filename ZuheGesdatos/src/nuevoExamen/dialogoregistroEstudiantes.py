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
        self.cursosescogidos = []
        self.father = manipulador
        self.cantdad = cantidadpregutnas
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Consulta de todos los estudiantes disponibles
        query = "SELECT estudiante.id_persn, estudiante.fecha_reg, (persona.nom_pers || ' ' || persona.apellido_pers) AS nombrecompleto, curso.nom_curso,curso.id_curso FROM estudiante, persona,curso,curso_estudiante WHERE estudiante.id_persn = persona.id_persona and curso.id_curso = curso_estudiante.id_curso and curso_estudiante.id_persn = estudiante.id_persn and curso.id_prof="+manipulador.iddocente+";"
        sampleList = conexion.connection.ExecuteQuery(query) #comentado mienstras no este creada la base ded datos
        print(str(sampleList))
        #sampleList = [("123","10/10/2010","Rex Arias"),("124","10/10/2010","Alison C."),("125","10/10/2010","Dante T.")]
        self.listBox1 = wx.ListBox(choices=[],
              name='listBox1', parent=self, pos=wx.Point(8, 48),
              size=wx.Size(184, 256),  style =  wx.LB_HSCROLL
                                           | wx.LB_MULTIPLE
                                           | wx.LB_NEEDED_SB
                                           | wx.LB_SORT)
        self.cursos = wx.ListBox(choices=[],
              name='listBox2', parent=self, pos=wx.Point(196, 48),
              size=wx.Size(184, 256),  style =  wx.LB_HSCROLL
                                           | wx.LB_MULTIPLE
                                           | wx.LB_NEEDED_SB
                                           | wx.LB_SORT)
        self.listBox1.SetBackgroundColour(wx.Colour(255, 255, 128))
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox)
        self.cursos.Bind(wx.EVT_LISTBOX, self.listcursos)
        for text in sampleList:
            cursoi = str(text[4])+": "+str(text[3])
            choices = [self.cursos.GetString(i) for i in range(self.cursos.GetCount())]
            print("mis choices" +str(choices))
            if not cursoi in choices:
                item = self.cursos.Append(cursoi)
            #item = self.listBox1.Append(str(text[0])+': '+str(text[2]))
        self.estudiantesmaestro = sampleList
        okBtn = wx.Button(self, wx.ID_OK)
        self.listBox1.Disable()
        for i in range(self.listBox1.GetCount()):
            self.listBox1.SetSelection(i)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        sizerlist = wx.BoxSizer(wx.HORIZONTAL)
        sizerlist.Add(self.cursos, 0, wx.ALL|wx.CENTER, 5)
        sizerlist.Add(self.listBox1, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(sizerlist, 0, wx.ALL|wx.CENTER, 5)
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
    
    def listcursos(self,e):
        'oyente para la lista de cursos'
        curso = e.GetString()
        caraccurso = curso.split(': ',1)
        if caraccurso[0] in self.cursosescogidos:
            self.actualizarlistaestudiantes(0)
            self.cursosescogidos.remove(str(caraccurso[0]))
        else:
            self.cursosescogidos.append(str(caraccurso[0]))
            self.actualizarlistaestudiantes(1)
    
    def actualizarlistaestudiantes(self,siagregar):
        'metodo usado para asegurarse de que se muestre en la lista de estudiantes aquellos que se encuentren en los cursos seleccionados'
        if siagregar:
            for estudiante in self.estudiantesmaestro:
                cursoi = str(estudiante[4])
                if cursoi in self.cursosescogidos:
                    self.listBox1.Append(str(estudiante[0])+': '+str(estudiante[2]))
                    self.estudiantesescogidos.append(str(estudiante[0]))
        else:
            for estudiante in self.estudiantesmaestro:
                cursoi = str(estudiante[4])
                if cursoi in self.cursosescogidos:
                    for i in range(len(self.estudiantesescogidos)):
                        print("mirando "+str(self.estudiantesescogidos[i])+" "+str(estudiante[0]))
                        if str(self.estudiantesescogidos[i])==str(estudiante[0]):
                            self.listBox1.Delete(i)
                            self.estudiantesescogidos.remove(str(estudiante[0]))
                            break
        for i in range(self.listBox1.GetCount()):
            self.listBox1.Select(i)
        #print("mi lista de cursos "+str(self.cursosescogidos))
    
    def registro(self, e):
        'oyente del boton aceptar para gestionar la informacion escogida'
        # Definimos los metodos de los eventos
        self.father.registrarEstudiantes(e,self,self.cantdad)
