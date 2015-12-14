#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint
from wx.py.shell import Shell as PyShell


class PanelCompiler(wx.Panel,):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("3399FF")
                
        self.button = wx.Button(self, label="Compilar", pos=(35, 110), size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Compilar,self.button)

        self.button_2 = wx.Button(self, wx.ID_OK, label="Enviar", pos=(35, 170),size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Enviar,self.button_2)
        
        self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
         
        self.shell = PyShell(self.grid_panel)
        self.shell.write("prueba")
        dimensionador = wx.BoxSizer(wx.VERTICAL) 
        dimensionador.Add(self.shell,1 ,wx.EXPAND| wx.ALL,border=10)
        self.grid_panel.SetSizer(dimensionador)
     

    def Compilar(self,event):
        print "Compilando"

       

    def Enviar(self,event):
        print "Enviado"
        
      
