#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero"
__date__ = "$20-jul-2015 18:52:55$"
 
class respuesta():
    """ Una clase donde se amacenara la informacion de
    una respuesta a una pregunta por medio de atributos """
    def __init__(self):
        self.tipoOpcion = '';
        self.opcionpregunta = "";
        self.idprespuesta = 0;
        self.respuesta = "";
        
    # Definimos los métodos de los eventos
     
    def setopcionpregunta(self,opcionpregunta):
        'cambia la opcion de la respuesta con valor de opcionpregunta'
        self.opcionpregunta = opcionpregunta

    def setrespuesta(self,respuesta):
        'cambia el valor de la respuesta con valor del parametro respuesta'
        self.respuesta = respuesta
        
    def settipoOpcion(self,nuevotipo):
        'cambia el valor de lel tipo de opcion con valor del parametro nuevotipo'
        self.tipoOpcion = nuevotipo
