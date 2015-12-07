#!/usr/bin/env python
# -*- coding: cp1252 -*-
import wx
import wx.grid
import pprint
import Componentes
import wx.calendar
import panel1
import ConnSchema


class Panel2(wx.Panel,):
    def __init__(self, parent,port):
        
        wx.Panel.__init__(self, parent)
        self.db = ConnSchema.ConnSchema("localhost","examen","adminexamen","pasexamen",str(port))
        self.parent=parent
        Component = Componentes.Component(self)
        
        self.listfacultades = self.db.ObtenerFacultades()
        for i in range(len(self.listfacultades)):
            self.listfacultades[i] = str(self.listfacultades[i][0])+")"+str(self.listfacultades[i][1])
        
        self.listproyecto=[]
        PanelComponentsCbx = wx.Panel(self) #Creacion padre hijo
        self.labelCbx1 = Component.CreateLabel(PanelComponentsCbx,12,pos=(0,0),label="Seleccion su Facultad")
        self.Cb1 = Component.CreateComboBox(PanelComponentsCbx,pos=(0,0),size=150,List=self.listfacultades)
        self.Bind(wx.EVT_COMBOBOX, self.EvtCombo1, self.Cb1)
        self.labelCbx2 = Component.CreateLabel(PanelComponentsCbx,12,pos=(0,0),label="Seleccione su Proyecto Curricular:")
        self.Cb2 = Component.CreateComboBox(PanelComponentsCbx,pos=(0,0),size=150,List=self.listproyecto)
        self.labelCalendarinicio = Component.CreateLabel(PanelComponentsCbx,15,pos=(0,0),label="Fecha de Inicio:")
        self.Calendarinicio = wx.calendar.CalendarCtrl(PanelComponentsCbx, -1, wx.DateTime_Now())
        self.labelTxtArea3 = Component.CreateLabel(PanelComponentsCbx,12,pos=(0,0),label="Ingrese el Módulo en el que trabajo:")
        self.TxtArea3 = Component.CreateTextArea(PanelComponentsCbx,pos=(0,0),size=(200,20))
        
        
        sizerPanelCbx = wx.BoxSizer(wx.VERTICAL)#Creacion caja de tamaños
        sizerPanelCbx.Add(self.labelCbx1 , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.Cb1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.labelCbx2 , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.Cb2 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.labelTxtArea3 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.TxtArea3 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.labelCalendarinicio , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
        sizerPanelCbx.Add(self.Calendarinicio , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
   
        
        PanelComponentsCbx.SetSizer(sizerPanelCbx)
        PanelComponentsCbx.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 

        

        




        PanelComponentsTxtArea = wx.Panel(self) #Creacion padre hijo

        PanelComponentsButtons = wx.Panel(PanelComponentsTxtArea) #Creacion padre hijo
        self.Button1 = Component.CreateButton(PanelComponentsButtons,"Regresar")
        self.Bind(wx.EVT_BUTTON, self.Regresar,self.Button1)#Creación de Evento
        self.Button2 = Component.CreateButton(PanelComponentsButtons,"Registrar")
        self.Bind(wx.EVT_BUTTON, self.Registrar,self.Button2)#Creación de Evento
        self.Button3 = Component.CreateButton(PanelComponentsButtons,"Modificar")
        self.Bind(wx.EVT_BUTTON, self.Modificar,self.Button3)#Creación de Evento
        sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
        sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelButton.Add(self.Button2 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        PanelComponentsButtons.SetSizer(sizerPanelButton) 
        PanelComponentsButtons.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 

        self.labelTxtArea1= Component.CreateLabel(PanelComponentsTxtArea,12,pos=(0,0),label="Ingrese su Nombre:")
        self.TxtArea1 = Component.CreateTextArea(PanelComponentsTxtArea,pos=(0,0),size=(200,20))

        self.labelTxtArea2 = Component.CreateLabel(PanelComponentsTxtArea,12,pos=(0,0),label="Ingrese su codigo:")
        self.TxtArea2 = Component.CreateTextArea(PanelComponentsTxtArea,pos=(0,0),size=(200,20))

        

        self.labelCalendarfin = Component.CreateLabel(PanelComponentsTxtArea,15,pos=(0,0),label="Fecha Fin:")
        self.Calendarfin = wx.calendar.CalendarCtrl(PanelComponentsTxtArea, -1, wx.DateTime_Now())
        
        sizerPanelTxtArea = wx.BoxSizer(wx.VERTICAL) #Creacion caja de tamaños
        sizerPanelTxtArea.Add(PanelComponentsButtons , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.labelTxtArea1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.TxtArea1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.labelTxtArea2 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.TxtArea2 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.labelCalendarfin , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanelTxtArea.Add(self.Calendarfin , 0, wx.ALIGN_BOTTOM) # Adicion del Objeto al panel
        PanelComponentsTxtArea.SetSizer(sizerPanelTxtArea)
        PanelComponentsTxtArea.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 
     	

       
        
        gs = wx.GridSizer(1, 2, 5, 5) #Creacion grilla de tamaño
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(PanelComponentsCbx, 0, wx.ALIGN_TOP),(PanelComponentsTxtArea, 0, wx.ALIGN_BOTTOM)])
     
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(gs, proportion=1, flag=wx.ALIGN_CENTER)
        self.SetSizer(sizer)
    

    def Regresar(self,event):
        self.parent.setpanel(panel1.Panel1(self.parent))
    def Modificar(self,event):
        self.parent.setpanel(panel1.Panel1(self.parent))    

    def Registrar(self,event):
        
        Proyecto = self.Cb2.GetStringSelection()[:1]
        Inicio = self.Calendarinicio.GetDate()
        Nombre = self.TxtArea1.GetValue()
        Codigo = self.TxtArea2.GetValue()
        Trabajo = self.TxtArea3.GetValue()
        Fin =  self.Calendarfin.GetDate()
        print Inicio  
        result =self.db.InsertarParticipante(Codigo,Proyecto,1,Nombre,Trabajo)
        self.parent.setpanel(panel1.Panel1(self.parent))
       
    def EvtCombo1(self,event):
        facultad = event.GetString()[:1]
        self.listproyecto= self.db.ObtenerProyectos(facultad)
        for i in range(len(self.listproyecto)):
            self.listproyecto[i] = str(self.listproyecto[i][0])+")"+str(self.listproyecto[i][1])
        self.Cb2.SetItems(self.listproyecto)



       
        
        
        
        #DataBase
        
          #pp.pprint(self.connCategoria.GetCategorias())
      
        

           
        
