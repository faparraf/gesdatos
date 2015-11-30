#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RolTabla:
    """Clase Objeto Rol Tabla"""
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
        """Inicializa los atributos de la clase"""
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
        
        
    """Genera setterss y getters de la clase"""               
        
    def set_IdRolTablaInsertar(self,idroltabla):
        self.__idRolTablaInsertar=idroltabla
      
        
    def set_IdRolTablaSeleccionar(self,idroltabla):
        self.__idRolTablaSeleccionar=idroltabla
        
    
    def set_IdRolTablaEliminar(self,idroltabla):
        self.__idRolTablaEliminar=idroltabla
       
    
    def set_IdRolTablaActualizar(self,idroltabla):
        self.__idRolTablaActualizar=idroltabla
        
        
    
    def set_IdTipoPersona(self,idtipopersona):
        self.__idTipoPersona=idtipopersona
        
        
    def set_IdTabla(self,idtabla):
        self.__idTabla=idtabla
    
    
      
    def set_BoolInsertar(self,bool):
        self.__boolInsertar=bool
        
    
    def set_BoolSeleccionar(self,bool):
        self.__boolSeleccionar=bool
       
        
    def set_BoolEliminar(self,bool):
        self.__boolEliminar=bool
           
    
    def set_BoolActualizar(self,bool):
        self.__boolActualizar=bool
    
            
    def get_IdRolTablaInsertar(self):
        return self.__idRolTablaInsertar
       
        
    def get_IdRolTablaSeleccionar(self):
        return self.__idRolTablaSeleccionar
        
    
    def get_IdRolTablaEliminar(self):
        return self.__idRolTablaEliminar
       
    
    def get_IdRolTablaActualizar(self):
        return self.__idRolTablaActualizar
       
    
    def get_IdTipoPersona(self):
        return self.__idTipoPersona
       
        
    def get_IdTabla(self):
        return self.__idTabla
        
    
       
    def get_BoolInsertar(self):
        return self.__boolInsertar
          
    
    def get_BoolSeleccionar(self):
        return self.__boolSeleccionar
          
        
    def get_BoolEliminar(self):
        return self.__boolEliminar
          
    
    def get_BoolActualizar(self):
        return self.__boolActualizar
        
    
        