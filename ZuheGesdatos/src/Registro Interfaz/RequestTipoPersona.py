 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import TipoPersona   
import RolTabla
from RegistroUsuarios.Conexion import Conexion

class RequestTipoPersona:
    
    def __init__(self,puerto):
        'Inicia la ejecución de la clase'
        self.conn= Conexion(puerto)
        
    def verTipos(self):
        
        'Consulta el listado de roles'
        lista= self.conn.selectQuery('select * from tipopersona')
        roles=[]
        for row in lista:
            tipo=TipoPersona.TipoPersona()
            tipo.set_IdTipoPersona(row[0])
            tipo.set_Tipo(row[1])
            roles.append(tipo)            
        return roles
    
    def verTablas(self):
        lista= self.conn.selectQuery('select * from "Tabla"')
        tablas=[]
        for row in lista:
            tipo=TipoPersona.TipoPersona()
            tipo.set_IdTipoPersona(row[0])
            tipo.set_Tipo(row[1])
            tablas.append(tipo)            
        return tablas
    
    def verTablaRoles(self,idtabla,idtipopersona):
        lista= self.conn.selectQuery('select * from "PermisoTabla" where "idTipoPersona" ='+str(idtipopersona)+' and "idTabla" ='+str(idtabla))
        rolTabla = RolTabla.RolTabla()
        
        #p=[]
        for row in lista:  
            rolTabla.set_IdTipoPersona(row[1])
            rolTabla.set_IdTabla(row[3])
            if(row[2]==1): #seleccionar
                rolTabla.set_IdRolTablaSeleccionar(row[0])
                rolTabla.set_BoolSeleccionar(row[4])
            if(row[2]==2): #insertar
                rolTabla.set_IdRolTablaInsertar(row[0])
                rolTabla.set_BoolInsertar(row[4])
            if(row[2]==3): #actualizar
                rolTabla.set_IdRolTablaActualizar(row[0])
                rolTabla.set_BoolActualizar(row[4])
            if(row[2]==4): #eliminar
                rolTabla.set_IdRolTablaEliminar(row[0])
                rolTabla.set_BoolEliminar(row[4])  
            
        #print rolTabla.get_IdTabla    
        #p.append(rolTabla)
        return rolTabla   
    
    def actualizarRolTabla(self,idroltabla,bool):
        self.conn.insertQuery('update "PermisoTabla" set permiso='+str(bool)+' where "IdRolTabla" ='+str(idroltabla))
#c=RequestTipoPersona()
#for tip in c.verTipos():
#    print tip