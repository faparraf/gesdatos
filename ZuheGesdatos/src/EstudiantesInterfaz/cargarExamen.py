#!/usr/bin/env python
# -*- coding: utf-8 -*-__author__ = "Usus"
__date__ = "$18/10/2015 06:07:30 PM$"
import ConnSchema,ConnectionDataBase,wx, panelPregunta
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes

def iniciarverexamen(idexamen):
    'Permite ver el examen creado'
    app=wx.App(False)
    displaySize= wx.DisplaySize()
    frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
    DialogoExamen(frame,idexamen)
    frame.Show()
    app.MainLoop()

#----------------------------------------------------------------------------

class DialogoExamen(wx.Dialog):
    #----------------------------------------------------------------------
    def __init__(self,parent,idexamen):
        """Constructor"""
        displaySize= wx.DisplaySize()
        wx.Dialog.__init__(self, parent, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
        self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
        self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
        query ="select examen.titulo_exa, persona.nom_pers || ' ' ||persona.apellido_pers, examen.tiempo_exa_inicio, examen.tiempo_exa_fin "
        query += "from persona, examen, docente where docente.id_persona = persona.id_persona and examen.id_dcnte = docente.id_persona and examen.id_exa = "+str(idexamen)+";"    
        self.generalidadexamen = (self.conectordatabase).ExecuteQuery(query) #consulta de todos los tipos de examen
        print str(self.generalidadexamen)
        gs = wx.GridSizer(3, 2, 1, 1) #Creacion grilla de tamaño
        topPanel= scrolled.ScrolledPanel(parent)
        panel =wx.Panel(topPanel)
        self.lblname = wx.StaticText(panel, label="Nombre Examen : "+str(self.generalidadexamen[0][0]), pos=(0, 35))
        self.docente = wx.StaticText(panel, label="Docente :"+str(self.generalidadexamen[0][1]), pos=(100, 35))
        self.lblhoraini = wx.StaticText(panel, label="Hora Inicio :"+str(self.generalidadexamen[0][2]), pos=(0, 65))
        self.lblhorafin = wx.StaticText(panel, label="Hora Fin: "+str(self.generalidadexamen[0][3]), pos=(100, 65))
        self.enviar = wx.Button(panel, wx.ID_OK,label="Enviar")
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.lblname, 0, wx.ALIGN_CENTER),(self.docente, 0, wx.ALIGN_CENTER),
                    (self.lblhoraini, 0, wx.ALIGN_CENTER),(self.lblhorafin, 0, wx.ALIGN_CENTER),
                    (self.enviar,0,wx.FIXED_MINSIZE)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        #sizer.Add(self.enviar, proportion=1,flag=wx.FIXED_MINSIZE)
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(sizer)
        topPanel.SetupScrolling(scroll_y=True)
        topPanel.SetBackgroundColour('#00BF8F')
        sizertopPanel=wx.BoxSizer(wx.VERTICAL)
        sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(panel, 0,wx.EXPAND|wx.ALL,border=10)
        sizertopPanel.Add(InterfazExamen(topPanel,idexamen,self.conectordatabase,self.conexion),0,wx.EXPAND|wx.ALL,border=5)
        sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
        topPanel.SetSizer(sizertopPanel)
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
            nb.AddPage(nuevopanel, "Pregunta "+str(self.cantidadpreguntas))
        
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
