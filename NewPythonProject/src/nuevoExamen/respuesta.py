#!/usr/bin/env python
#coding=utf-8
 
class respuesta():
    """ Una clase donde se amacenara la informacion de
    una respuesta a una pregunta por medio de atributos """
    def __init__(self):
        self.descripcionOpcion = [];
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
