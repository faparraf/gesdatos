#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "User"
__date__ = "$10/12/2015 08:45:17 PM$"
import ConnSchema,ConnectionDataBase,wx
import HeadLow
import wx.lib.scrolledpanel as scrolled
import wx.grid
# Este modulo se encargara de entregar al docente un reporte de sus calificaciones obtenidas

#----------------------------------------------------------------------------

class Panelgeneral(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self,parent,puerto,iddocente):
        """Constructor"""
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen",str(puerto))#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        gs = wx.GridSizer(3, 2, 1, 1) #Creacion grilla de tamaño
        self.panel =wx.Panel(self)
        self.examenelegigo = ''
        self.cursoelegigo = ''
        self.lblcurso = wx.StaticText(self.panel, label="Cursos : ", pos=(0, 35))
        self.sampleListcurso = []
        query ="select e.id_exa, e.titulo_exa, c.id_curso, c.nom_curso from examen e, curso c, curso_examen ce "
        query+="where ce.id_examen = e.id_exa and ce.id_curso =c.id_curso and e.id_dcnte="+str(iddocente)+";"    
        self.opcionesexamencurso = (self.conectordatabase).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesexamencurso))
        self.sampleListcurso=self.getdistinticcursos(self.opcionesexamencurso)
        print('cursos a mostrar '+str(self.sampleListcurso))
        self.editcurso = wx.ComboBox(self.panel, choices=self.sampleListcurso, style=wx.CB_DROPDOWN)
        self.editcurso.Bind(wx.EVT_COMBOBOX, self.actualizarexamenes)
        self.sampleListexamen = ['                                 ']#se pone asi para que el combobox tenga un buen ancho
        self.lblexamen = wx.StaticText(self.panel, label="Examenes :", pos=(100, 35))
        self.editexamen = wx.ComboBox(self.panel, choices=self.sampleListexamen, style=wx.CB_DROPDOWN) 
        self.editexamen.Bind(wx.EVT_COMBOBOX, self.examenelegido)
        
        self.enviar = wx.Button(self.panel, wx.ID_OK,label="Enviar")
        self.Bind(wx.EVT_BUTTON, self.creartablanotas,self.enviar)
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.lblcurso, 0, wx.ALIGN_CENTER),(self.editcurso, 0, wx.ALIGN_CENTER),
                    (self.lblexamen, 0, wx.ALIGN_CENTER),(self.editexamen, 0, wx.ALIGN_CENTER),
                    (self.enviar,0,wx.FIXED_MINSIZE)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        #sizer.Add(self.enviar, proportion=1,flag=wx.FIXED_MINSIZE)
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        self.sizertopPanel.Add(self.panel, 0,wx.EXPAND|wx.ALL,border=10)
        tabla = InterfazNotas(self,0,0,self.conectordatabase,self.conexion)
        self.sizertopPanel.Add(tabla, 0,wx.EXPAND|wx.ALL,border=10)
        #sizertopPanel.Add(InterfazExamen(self,idexamen,self.conectordatabase,self.conexion),0,wx.EXPAND|wx.ALL,border=10)
        self.SetSizer(self.sizertopPanel)
    
    def getdistinticcursos(self,list):
        'retornara la lista de todos los distintios cursos encontrados en la consulta hecha anteriormente'
        'se tiene como parametro la busqueda hecha en el metodo de inicio'
        'se asume por la busqueda que la columna 3 es la de los nombre de los cursos'
        resultado = []
        for a in list:
            if not a[3] in resultado:
                resultado.append(a[3])
        return resultado
    
    def actualizarexamenes(self,e):
        'oyenete del comobobox de cursos para mostrar examenes de cursos elejidos'
        'se asume que el campo 2 es el correspondiene a nombres de examenes'
        self.editexamen.Clear()
        curso = e.GetString()
        for it in self.opcionesexamencurso:
            if it[3] == curso:
                self.editexamen.Append(str(it[0])+" : "+str(it[1]))
                self.cursoelegigo = str(it[2])

    def examenelegido(self,e):
        examen = e.GetString()
        self.examenelegigo = examen.split(" : ")[0]
        print('examen elegido '+str(self.examenelegigo)+' curso elegido  '+self.cursoelegigo)
    
    def creartablanotas(self,e):
        if not(self.examenelegigo=='' or self.cursoelegigo==''):
            tabla = InterfazNotas(self,self.examenelegigo,self.cursoelegigo,self.conectordatabase,self.conexion)
            sizer = self.sizertopPanel
            sizer.Hide(0)
            sizer.Remove(0)
            sizer.Hide(0)
            sizer.Remove(0)
            sizer.Add(self.panel,0,wx.EXPAND|wx.ALL,border=10)
            sizer.Add(tabla,0,wx.EXPAND|wx.ALL,border=10)
            self.SetSizer(sizer)
            self.GetSizer().Layout()
            self.Fit()
        
           
        
    
class InterfazNotas(wx.grid.Grid):
    def __init__(self,parent,idexamen,idcurso,conectordatabase,conexion):
        'Clase que representa la tabla de resultados de notas de estudiantes'
        wx.grid.Grid.__init__(self, parent, -1)
        self.conectordatabase = conectordatabase
        self.conexion = conexion
        #query = "select p.apellido_pers||' '||p.nom_pers,e.id_alum from (persona p left join examenalumno e on e.id_alum = p.id_persona) inner join examencurso ex "
        #query+="on ex.cod_exacur = e.cod_exacurso;"
        query = "select p.id_persona,p.apellido_pers||' '||p.nom_pers,puntaje_alum from  curso_examen cex, curso_estudiante ces,persona p left join examenalumno e on e.id_alum = p.id_persona "
        query+="where p.id_persona = ces.id_persn and ces.id_curso = cex.id_curso and cex.id_curso = "+str(idcurso)+" and cex.id_Examen = "+str(idexamen)+";"
        self.notas = (self.conectordatabase).ExecuteQuery(query)
        print str(self.notas)
        if (len(self.notas)>0):
            self.CreateGrid(len(self.notas), len(self.notas[0]))
            self.SetColLabelValue(0, "Codigo")
            self.SetColLabelValue(1, "Nombre")
            self.SetColLabelValue(2, "Calificaci�n")
            itestudiante = 0
            for notaestudiante in self.notas:
                itcaracteristica=0
                self.SetRowLabelValue(itestudiante, str(itestudiante+1))
                for caracteritica in notaestudiante:
                    self.SetCellValue(itestudiante, itcaracteristica, str(caracteritica))
                    itcaracteristica+=1
                itestudiante+=1
        else:
            self.CreateGrid(0,3)
            self.SetColLabelValue(0, "Codigo")
            self.SetColLabelValue(1, "Nombre")
            self.SetColLabelValue(2, "Calificaci�n")
    def getconexion(self):
        """consutlor que retorna la clase administradora de la base de datos"""
        return self.conexion.connection

#app=wx.App(False)
#displaySize= wx.DisplaySize()
#frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
#menubar = wx.MenuBar()
#topPanel= scrolled.ScrolledPanel(frame)
#topPanel.SetupScrolling(scroll_y=True)
#topPanel.SetBackgroundColour('3399FF')
#sizertopPanel=wx.BoxSizer(wx.VERTICAL)
#iddocente = "4"
#sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
#sizertopPanel.Add(Panelgeneral(topPanel,"5434","4"),0,wx.EXPAND|wx.ALL,border=10)
#sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
#topPanel.SetSizer(sizertopPanel)
#frame.Show()
#app.MainLoop()