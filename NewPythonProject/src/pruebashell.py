#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx

class Shell():
    def __init__ (self,parent):
        'Inicia la interfaz y su contenedor'
        wx.Shell.__init__(self, parent)
        self.prueba= wx.Shell.write(self, "Prueba")
