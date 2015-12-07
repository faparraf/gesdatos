#!/usr/bin/env python
# -*- coding: cp1252 -*-
import wx
import wx.grid
import pprint
import Componentes
import wx.calendar
import panel1
import ConnSchema


class Panel3(wx.Panel,):
    def __init__(self, parent,port):
        
        wx.Panel.__init__(self, parent)
        self.db = ConnSchema.ConnSchema("localhost","examen","adminexamen","pasexamen",str(port))
        self.parent=parent
        Component = Componentes.Component(self)



        PanelComponentslistctrl = wx.Panel(self) #Creacion padre hijo
        self.labellistctrl= Component.CreateLabel(PanelComponentslistctrl,15,pos=(0,0),label="My listctrl:")
        titles2 = ['Participante', 'Proyecto', 'Trabajo','Periodo']
        lenghs = [100, 120, 160, 300]
        self.listctrl = Component.CreateListctrl(PanelComponentslistctrl,titles2,lenghs,size=(300,300))
        sizerPanellistctrl = wx.BoxSizer(wx.VERTICAL) #Creacion caja de tamaños
        sizerPanellistctrl.Add(self.labellistctrl , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        sizerPanellistctrl.Add(self.listctrl , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
        PanelComponentslistctrl.SetSizer(sizerPanellistctrl) 
        PanelComponentslistctrl.SetBackgroundColour("#32506D") #Asignación de Color de Fondo 
       
        db = ConnSchema.ConnSchema()
        involucrados = db.ObtenerInvolucrados()
       