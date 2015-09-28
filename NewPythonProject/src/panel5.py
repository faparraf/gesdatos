#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint
from wx.py.shell import Shell as PyShell


class Panel5(wx.Panel,):
    def __init__(self, parent):
        'Constructor para crear un panel que recibe como par�metro su contenedor'
        wx.Panel.__init__(self, parent)
     
        self.button = wx.Button(self, label="Compilar", pos=(35, 110), size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Compilar,self.button)

        self.button_2 = wx.Button(self, label="Enviar", pos=(35, 170),size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Enviar,self.button_2)
        
        self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
         
        self.shell = PyShell(self.grid_panel)
        self.shell.write("prueba")
        dimensionador = wx.BoxSizer(wx.VERTICAL) 
        dimensionador.Add(self.shell,1 ,wx.EXPAND| wx.ALL,border=10)
        self.grid_panel.SetSizer(dimensionador)
     
    def Compilar(self,event):
        'Retorna un mensaje indicando la compilaci�n'
        print "Compilando"

    def Enviar(self,event):
        'Retorna un mensaje indicando el envio'
        print "Enviado"
    