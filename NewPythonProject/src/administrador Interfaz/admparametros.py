#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, ConnSchema,ConnectionDataBase

## Body nuevo tema
##-----------------------------------------------------------el):
class paneltema(wx.Panel):
    """ Una clase personalizada .para agregar un nuevo tema
    donde se podra elegir por medio de la accion si editar o agregar parametro"""
    def __init__(self, parent,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicialización Panel Padre
        self.SetBackgroundColour('3399FF')
        
## Body nuevo tipo pregunta
##-----------------------------------------------------------el):
class paneltipopregunta(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicialización Panel Padre
        self.SetBackgroundColour('3399FF')

## Body nuevo tipo opcion
##-----------------------------------------------------------el):
class paneltipoopcion(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicialización Panel Padre
        self.SetBackgroundColour('3399FF')
        
## Body nuevo tipo examen
##-----------------------------------------------------------el):
class paneltipoexamen(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent,accion):
        'contructor requiere de parent como interfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicialización Panel Padre
        self.SetBackgroundColour('3399FF')