#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "User"
__date__ = "$10/12/2015 08:45:17 PM$"
# Este modulo se encargara de entregar al docente un reporte de sus calificaciones obtenidas

#----------------------------------------------------------------------------

class Panelgeneral(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self,parent,puerto,iddocente):
        """Constructor"""
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",str(puerto))#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        self.generalidadexamen = (self.conectordatabase).ExecuteQuery(query) #consulta de todos los tipos de examen
        print str(self.generalidadexamen)
        gs = wx.GridSizer(3, 2, 1, 1) #Creacion grilla de tamaño
        panel =wx.Panel(self)
        self.lblcurso = wx.StaticText(panel, label="Cursos : "+str(self.generalidadexamen[0][0]), pos=(0, 35))
        self.sampleListcurso = []
        query ="select e.id_exa, e.titulo_exa, c.id_curso, c.nom_curso from examen e, curso c, curso_examen ce "
        query+=+"where ce.id_examen = e.id_exa and ce.id_curso =c.id_curso and e.id_dcnte="+str(iddocente)+";"    
        self.opcionesexamencurso = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesexamencurso))
        for a in self.opcionesexamencurso:
            self.sampleListcurso.append(a[3])
        self.editcurso = wx.ComboBox(self, choices=self.sampleListcurso, style=wx.CB_DROPDOWN)
        self.sampleListexamen = []
        self.lblexamen = wx.StaticText(panel, label="Examenes :"+str(self.generalidadexamen[0][1]), pos=(100, 35))
        self.editexamen = wx.ComboBox(self, choices=self.sampleListexamen, style=wx.CB_DROPDOWN)
        self.enviar = wx.Button(panel, wx.ID_OK,label="Enviar")
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.lblcurso, 0, wx.ALIGN_CENTER),(self.editcurso, 0, wx.ALIGN_CENTER),
                    (self.lblexamen, 0, wx.ALIGN_CENTER),(self.editexamen, 0, wx.ALIGN_CENTER),
                    (self.enviar,0,wx.FIXED_MINSIZE)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        #sizer.Add(self.enviar, proportion=1,flag=wx.FIXED_MINSIZE)
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(sizer)
        sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        sizertopPanel.Add(panel, 0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(InterfazExamen(self,idexamen,self.conectordatabase,self.conexion),0,wx.EXPAND|wx.ALL,border=10)
        self.SetSizer(sizertopPanel)

class InterfazExamen(wx.Panel):
    def __init__(self,parent,idexamen,conectordatabase,conexion):
        'Se crea el menu de pesta�as'
        wx.Panel.__init__(self, parent=parent)
        self.cantimgtemp =0
        nb = wx.Notebook(self)
        self.conectordatabase = conectordatabase
        self.conexion = conexion
        query = "select examenpreg.id_prgnta from examenpreg, examen where examenpreg.id_examen = examen.id_exa and examen.id_exa = "+str(idexamen)+";"
        self.idpreguntas = (self.conectordatabase).ExecuteQuery(query)
        print str(self.idpreguntas)
        self.cantidadpreguntas = 0
        for it in self.idpreguntas:
            # A�adimos los paneles con Addpage
            idpregunta = (self.idpreguntas[self.cantidadpreguntas])
            print("creando pregunta "+str(idpregunta))
            nuevopanel = panelPregunta.panelpregunta(nb,self,idpregunta[0])#se pone de la posicion 0 porque se retorna una lista de un solo elemento
            self.cantidadpreguntas=self.cantidadpreguntas+1
            nb.AddPage(nuevopanel, "pregunta "+str(self.cantidadpreguntas))
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        #sizer.Add(self.enviar, proportion=1,flag=wx.FIXED_MINSIZE)
        sizer.Add(nb, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
    def getconexion(self):
        """consutlor que retorna la clase administradora de la base de datos"""
        return self.conexion.connection
    def getcantimgtemp(self):
        'Obtiene la imagen'
        return self.cantimgtemp
    def setcantimgtemp(self,nuevacant):
        'Se asigna la imagen'
        self.cantimgtemp = nuevacant
        
#iniciarverexamen("4")