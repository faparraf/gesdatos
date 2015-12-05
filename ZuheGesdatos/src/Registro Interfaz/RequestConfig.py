#!/usr/bin/env python
# -*- coding: utf-8 -*-

from RegistroUsuarios.Conexion import Conexion
import Persona
class RequestConfig:
    """Clase DAO que implementa los Request con la BD"""
    
    __idpersona=""
    
    def __init__(self,idpersona,puerto):
        """Inicializa atributos de la clase"""
        self.__idpersona=idpersona
        
        'Inicia la ejecución de la clase'
        self.conn= Conexion(puerto)        
    
    def ver_persona(self):
        """metodo que retorna una persona asociada a la clase"""
        
        lista= self.conn.selectQuery('select p.nom_pers, p.apellido_pers, p.di_pers, p.fecha_nac, p.correo, p.correo_universidad, p.usuario, p.uni, u.id_paisuni from persona p, universidad u where p.id_persona='+str(self.__idpersona)+' and u.id_uni = p.uni')
        persona = Persona.Persona()    
        for row in lista:            
            persona.set__nombre(row[0])
            persona.set__apellido(row[1])
            persona.set__documento(row[2])
            persona.set__fechanacimiento(row[3])
            persona.set__correo(row[4])
            persona.set__correouni(row[5])
            persona.set__usuario(row[6])
            persona.set__universidad(row[7])           
            persona.set__pais(row[8])  
            
        return persona
     
                                    
    """Metodos que actualizan segun el dato recibido"""                                
    def actualizar__nombre(self,nombre):
        self.conn.insertQuery("update persona set nom_pers='"+nombre+"' where id_persona ="+str(self.__idpersona))
    
    def actualizar__apellido(self,apellido):
        self.conn.insertQuery("update persona set apellido_pers='"+apellido+"' where id_persona ="+str(self.__idpersona))
        
    def actualizar__documento(self,documento):
        self.conn.insertQuery("update persona set di_pers="+str(documento)+" where id_persona ="+str(self.__idpersona))    
       
    def actualizar__fechanacimiento(self,fechanacimiento):
        self.conn.insertQuery("update persona set fecha_nac='"+fechanacimiento+"' where id_persona ="+str(self.__idpersona))
        
    def actualizar__correo(self,correo):
        self.conn.insertQuery("update persona set correo='"+correo+"' where id_persona ="+str(self.__idpersona))
        
    def actualizar__correouni(self,correouni):
        self.conn.insertQuery("update persona set correo_universidad='"+correouni+"' where id_persona ="+str(self.__idpersona))
        
    def actualizar__usuario(self,usuario):
        self.conn.insertQuery("update persona set usuario='"+usuario+"' where id_persona ="+str(self.__idpersona))
            
    def actualizar__universidad(self,universidad):
        universidadid=int("%s" %(self.conn.selectQuery("select id_uni from universidad where nom_uni ='"+universidad+"'")[0]))
        self.conn.insertQuery("update persona set uni="+str(universidadid)+" where id_persona ="+str(self.__idpersona))   
   