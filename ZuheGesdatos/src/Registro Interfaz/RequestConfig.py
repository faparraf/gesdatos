# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from RegistroUsuarios.Conexion import Conexion

class RequestConfig:
    
    __idpersona=""
    
    def __init__(self,idpersona):
        self.__idpersona=idpersona
        
        'Inicia la ejecución de la clase'
        self.conn= Conexion()        
    
    def ver_persona(self):
        
        lista= self.conn.selectQuery('select * from "Tabla"')
        tablas=[]
        for row in lista:
            tipo=TipoPersona.TipoPersona()
            tipo.set_IdTipoPersona(row[0])
            tipo.set_Tipo(row[1])
            tablas.append(tipo)            
        return tablas
                                    
    def actualizar__nombre(self,nombre):
        self.conn.insertQuery('update persona set nom_pers='+nombre+' where id_persona ='+str(self.__idpersona))
    
    def actualizar__apellido(self,apellido):
        self.conn.insertQuery('update persona set nom_pers='+apellido+' where id_persona ='+str(self.__idpersona))
        
    def actualizar__documento(self,documento):
        self.conn.insertQuery('update persona set nom_pers='+documento+' where id_persona ='+str(self.__idpersona))    
       
    def actualizar__fechanacimiento(self,fechanacimiento):
        self.conn.insertQuery('update persona set nom_pers='+fechanacimiento+' where id_persona ='+str(self.__idpersona))
        
    def actualizar__correo(self,correo):
        self.conn.insertQuery('update persona set nom_pers='+correo+' where id_persona ='+str(self.__idpersona))
        
    def actualizar__correouni(self,correouni):
        self.conn.insertQuery('update persona set nom_pers='+correouni+' where id_persona ='+str(self.__idpersona))
        
    def actualizar__usuario(self,usuario):
        self.conn.insertQuery('update persona set nom_pers='+usuario+' where id_persona ='+str(self.__idpersona))
        
    def actualizar__universidad(self,universidad):
        self.conn.insertQuery('update persona set nom_pers='+universidad+' where id_persona ='+str(self.__idpersona))   
        
    def actualizar__pais(self,pais):
        self.conn.insertQuery('update persona set nom_pers='+pais+' where id_persona ='+str(self.__idpersona))  