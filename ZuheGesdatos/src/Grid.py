#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.grid

class Form(wx.Frame):
    def __init__(self):
        'Inicia la creación de un Grid'
        wx.Frame.__init__(self,parent=None,title="Paneles")
        panel = wx.Panel(self)

        TheGrid = wx.grid.Grid(panel)
        TheGrid.CreateGrid(5,5)
        TheGrid.SetColLabelValue(0,"Tabla")
        TheGrid.SetColLabelValue(1,"Columna")
        TheGrid.SetColLabelValue(2,"Alias")
        TheGrid.SetColLabelValue(3,"Funcion")
        TheGrid.SetColLabelValue(4,"Gestion")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(TheGrid,wx.EXPAND)
        panel.SetSizer(sizer)

app=wx.App()
frame = Form().Show()
app.MainLoop()
