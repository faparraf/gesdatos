#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RolTabla:
    __idRolTablaInsertar=0
    __idRolTablaSeleccionar=0
    __idRolTablaEliminar=0
    __idRolTablaActualizar=0
    __idTipoPersona=0
    __idTabla=0
    __boolInsertar=False
    __boolSeleccionar=False
    __boolEliminar=False
    __boolActualizar=False

    def __init__(self):
        self.__idRolTablaInsertar
        self.__idRolTablaSeleccionar
        self.__idRolTablaEliminar
        self.__idRolTablaActualizar
        self.__idTipoPersona
        self.__idTabla       
        self.__boolInsertar
        self.__boolSeleccionar
        self.__boolEliminar
        self.__boolActualizar  
        """Documentation"""
        
    def set_IdRolTablaInsertar(self,idroltabla):
        self.__idRolTablaInsertar=idroltabla
        """Documentation"""
        
    def set_IdRolTablaSeleccionar(self,idroltabla):
        self.__idRolTablaSeleccionar=idroltabla
        """Documentation"""
    
    def set_IdRolTablaEliminar(self,idroltabla):
        self.__idRolTablaEliminar=idroltabla
        """Documentation"""
    
    def set_IdRolTablaActualizar(self,idroltabla):
        self.__idRolTablaActualizar=idroltabla
        """Documentation"""
        
    
    def set_IdTipoPersona(self,idtipopersona):
        self.__idTipoPersona=idtipopersona
        """Documentation"""
        
    def set_IdTabla(self,idtabla):
        self.__idTabla=idtabla
        """Documentation"""
    
      
    def set_BoolInsertar(self,bool):
        self.__boolInsertar=bool
        """Documentation"""    
    
    def set_BoolSeleccionar(self,bool):
        self.__boolSeleccionar=bool
        """Documentation"""    
        
    def set_BoolEliminar(self,bool):
        self.__boolEliminar=bool
        """Documentation"""    
    
    def set_BoolActualizar(self,bool):
        self.__boolActualizar=bool
        """Documentation"""  
            
    def get_IdRolTablaInsertar(self):
        return self.__idRolTablaInsertar
        """Documentation"""
        
    def get_IdRolTablaSeleccionar(self):
        return self.__idRolTablaSeleccionar
        """Documentation"""
    
    def get_IdRolTablaEliminar(self):
        return self.__idRolTablaEliminar
        """Documentation"""
    
    def get_IdRolTablaActualizar(self):
        return self.__idRolTablaActualizar
        """Documentation"""
    
    def get_IdTipoPersona(self):
        return self.__idTipoPersona
        """Documentation"""
        
    def get_IdTabla(self):
        return self.__idTabla
        """Documentation"""
    
       
    def get_BoolInsertar(self):
        return self.__boolInsertar
        """Documentation"""    
    
    def get_BoolSeleccionar(self):
        return self.__boolSeleccionar
        """Documentation"""    
        
    def get_BoolEliminar(self):
        return self.__boolEliminar
        """Documentation"""    
    
    def get_BoolActualizar(self):
        return self.__boolActualizar
        """Documentation"""  
    
        