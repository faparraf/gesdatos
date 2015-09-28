#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.grid

class Panel2(wx.Panel):
    def __init__(self,parent):
        'Inicia la creación de las tablas que contendran los datos en la interfaz'
        wx.Panel.__init__(self,parent)
        panelhijo = wx.Panel(self)

        TheGrid = wx.grid.Grid(panelhijo)
        TheGrid.CreateGrid(5,5)
        TheGrid.SetColLabelValue(0,"Tabla")
        TheGrid.SetColLabelValue(1,"Columna")
        TheGrid.SetColLabelValue(2,"Alias")
        TheGrid.SetColLabelValue(3,"Funcion")
        TheGrid.SetColLabelValue(4,"Gestion")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(TheGrid,wx.EXPAND)
        panelhijo.SetSizer(sizer)
