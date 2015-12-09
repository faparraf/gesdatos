#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$04-sep-2015 21:40:31$"
import wx,sys,os
import Componentes

class panelpregunta(wx.Panel):
    def __init__(self,parent,manipulador,idpregunta):
        'Inicia la interfaz'
        self.padre = parent
        wx.Panel.__init__(self, parent=parent)
        self.manipulador = manipulador
        self.idpregunta = idpregunta
        self.SetBackgroundColour('#00BF8F')
        self.aparte = wx.StaticText(self, label="", pos=(140, 10))
        query = "select pregunta.enunciado,tema.desc_tema, pregunta.imagen,pregunta.tipopre from pregunta,"
        query += "tema where pregunta.tema = tema.idtema and pregunta.id_pregunta ="+str(self.idpregunta)+";"
        self.generalidadespreguntas = (self.manipulador.getconexion()).ExecuteQuery(query)
        print(self.generalidadespreguntas)
        # parametros basicos generales del registro de un examen
        self.lblenunciado = wx.StaticText(self, label="Tema: "+str(self.generalidadespreguntas[0][1]), pos=(100,35))
        self.lbltema = wx.StaticText(self, label="Enunciado :"+str(self.generalidadespreguntas[0][0]), pos=(100,65))
        if self.generalidadespreguntas[0][3]==1:
            self.panelrespuesta = PanelAbierto(self)
        elif self.generalidadespreguntas[0][3]==2:
            self.panelrespuesta = panelFalsoVerdadero(self)
        elif self.generalidadespreguntas[0][3]==3:
            self.panelrespuesta = PanelOpcionMultiple(self,idpregunta)
        elif self.generalidadespreguntas[0][3]==4:
            self.panelrespuesta = PanelOpcionMultiple(self,idpregunta)
        gs = wx.GridSizer(2,1, 5, 5) #Creacion grilla de tamaño
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.lblenunciado, 0, wx.ALIGN_CENTER),
                    (self.lbltema, 0, wx.ALIGN_CENTER)])
        #panel de la imagen de la pregunta
        PanelImage1 = wx.Panel(self)
        if str(self.generalidadespreguntas[0][2]) != "None":
            img_path = "imgtemp"+str(self.manipulador.getcantimgtemp())+".jpg"
            self.manipulador.setcantimgtemp(self.manipulador.getcantimgtemp()+1)
            open(img_path,'wb').write(str(self.generalidadespreguntas[0][2]))
            self.image = wx.Image(img_path)
            self.image.Rescale(80, 100) 
            self.imageUd = wx.BitmapFromImage(self.image) 
            self.imagen1 = wx.StaticBitmap(PanelImage1, -1, self.imageUd,style=wx.BITMAP_TYPE_PNG)
            PanelImage1.SetBackgroundColour('#00BF8F')
        
        gy = wx.GridSizer(1,2, 5, 5) #Creacion grilla de tamaño
        gy.AddMany([(gs, 0, wx.ALIGN_CENTER),
                    (PanelImage1, 0, wx.ALIGN_CENTER)])
        
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(gy, proportion=1, flag=wx.EXPAND)
        sizer.Add(self.panelrespuesta,  proportion=1, flag=wx.EXPAND)
        
        
        self.SetSizer(sizer)
    def getconexion(self):
        """consutlor que retorna la clase administradora de la base de datos"""
        return self.manipulador.getconexion()

#-----------------------------------------------------------------------------------------

class PanelAbierto(wx.Panel):
    def __init__(self,parent):
        'Se crea el bloc de notas o menu de pesta�as'
        wx.Panel.__init__(self, parent=parent)
        componentes = Componentes.Component(self)
        self.textarea = componentes.CreateTextArea(self,[0, 35],[100,100])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(self.textarea, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

#---------------------------------------------------------------------------------------

class panelFalsoVerdadero(wx.Panel):
    def __init__(self,parent):
        'Se crea el bloc de notas o menu de pesta�as'
        wx.Panel.__init__(self, parent=parent)
        componentes = Componentes.Component(self)
        self.parent=parent
        self.opciones = ["Falso","Verdadero"]
        self.radioBox = componentes.CreateRadioBox(self, "", self.opciones)
        self.radioBox.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.radioBox)
        gs = wx.GridSizer(1, 1, 1, 1) #Creacion grilla de tamaño
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.radioBox, 0, wx.ALIGN_CENTER)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
    def EvtRadioBox(self, event):
        print('La opcion marcada es: ' + str(event.GetString())+' de  la pregunta: '+str(self.parent.idpregunta))

#---------------------------------------------------------------------------------------

class PanelOpcionMultiple(wx.Panel):
    def __init__(self,parent,idpregunta):
        'Se crea el bloc de notas o menu de pesta�as'
        wx.Panel.__init__(self, parent=parent)
        self.parent=parent
        componentes = Componentes.Component(self)
        gs = wx.GridSizer(1, 1, 1, 1) #Creacion grilla de tamaño
        query = "select opcionpreg.respuesta from opcionpreg, pregunta where "
        query += "pregunta.id_pregunta = opcionpreg.id_pregunta and pregunta.id_pregunta = "+str(idpregunta)+";"
        self.opcionpregunta = (parent.getconexion()).ExecuteQuery(query)
        print(self.opcionpregunta)
        #self.opciones = ["Falso","Verdadero"]
        self.radiolist = [self.opcionpregunta[0][0],self.opcionpregunta[1][0],self.opcionpregunta[2][0],self.opcionpregunta[3][0]]
        #for a in range (4):
            #labela = componentes.CreateLabel(self,12,[0,35],self.opcionpregunta[a-1][0])
            #cheackbox = componentes.CreateComboBox(self,[0,35],100,self.opciones)
            #cheackbox.Value = "Falso"
        self.radiobox = componentes.CreateRadioBox(self,"Opciones respuesta",self.radiolist)
        self.radiobox.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.radiobox)
        #gs.Add(labela, 0, wx.ALIGN_CENTER)
        gs.Add(self.radiobox, 0, wx.ALIGN_CENTER)
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
        
    def EvtRadioBox(self, event):
        print('La opcion marcada es: ' + str(event.GetString())+' de  la pregunta: '+str(self.parent.idpregunta))