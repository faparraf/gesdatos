#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TipoPersona:
    """Clase Objeto TipoPersona"""
    __idTipoPersona=0
    __tipo=""
    
    def __init__(self):
        """Inicializa atributos de clase"""
        self.__idTipoPersona
        self.__tipo
    
    def __str__(self):
        """funcion que imprimer el objeto"""
        return str(self.__idTipoPersona) +".  "+ self.__tipo
    
    "genera setters y getters de atributos"""
    
    def set_IdTipoPersona(self,idtipopersona):
        self.__idTipoPersona=idtipopersona
        """Documentation"""
    
    def set_Tipo(self,tipopersona):
        self.__tipo=tipopersona
        """Documentation"""
        
    def get_Tipo(self):
        return self.__tipo
        """Documentation"""    

    def get_IdTipoPersona(self):
        return self.__idTipoPersona
        