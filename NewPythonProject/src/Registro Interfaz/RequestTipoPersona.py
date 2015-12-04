 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import TipoPersona   
from RegistroUsuarios.Conexion import Conexion

class RequestTipoPersona:
    
    def __init__(self):
        'Inicia la ejecución de la clase'
        self.conn= Conexion()
        
    def verTipos(self):
        
        'Consulta el listado de roles'
        lista= self.conn.selectQuery("select * from tipopersona")
        roles=[]
        for row in lista:
            tipo=TipoPersona.TipoPersona()
            tipo.set_IdTipoPersona(row[0])
            tipo.set_Tipo(row[1])
            roles.append(tipo)            
        return roles
    
    def verTablas(self):
        lista= self.conn.selectQuery("select * from tabla")
        tablas=[]
        for row in lista:
            tipo=TipoPersona.TipoPersona()
            tipo.set_IdTipoPersona(row[0])
            tipo.set_Tipo(row[2])
            tablas.append(tipo)            
        return tablas
    
    def verTablasRoles(self,idtabla,idrol):
        a
#c=RequestTipoPersona()
#for tip in c.verTipos():
#    print tip