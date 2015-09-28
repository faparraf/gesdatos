#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx

class Titulo1(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        'Inicia la crecioón de encabezados para las tablas'
        wx.Panel.__init__(self, parent)
        self.text = wx.StaticText(self, label="SElECCIÃ“N y FUNCIONES", pos=(400, 10))
        self.font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)

#-----------------------------------------------------------------------------------

class Titulo2(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        'Inicia la crecioón de encabezados para las tablas'
        wx.Panel.__init__(self, parent)
        self.text = wx.StaticText(self, label="OPERACIÃ“N JOIN", pos=(400, 10))
        self.font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)

#-----------------------------------------------------------------------------------

class Titulo3(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        'Inicia la crecioón de encabezados para las tablas'
        wx.Panel.__init__(self, parent)
        self.text = wx.StaticText(self, label="CONDICIÃ“N (WHERE)", pos=(400, 10))
        self.font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)
        
