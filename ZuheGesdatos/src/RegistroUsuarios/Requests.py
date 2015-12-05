#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Conexion import Conexion

class Request():    
    #conn= Conexion()
    def __init__(self,puerto): 
        'Inicia la ejecución de la clase'
        self.conn= Conexion(puerto)
           
    def registrarPersona (self,nombre,apellido,documento,fechaNac,correo,correoUni,universidad,usuario,categoria):
        'Registra las personas en la base de datos'   
        #personaid=1;
        personaid= int("%s" %(self.conn.selectQuery("select count(*) from persona")[0]))+1
        universidadid=int("%s" %(self.conn.selectQuery("select id_uni from universidad where nom_uni ='"+universidad+"'")[0]))
        datos=(personaid,nombre,apellido,documento,fechaNac,correo,correoUni,universidadid,usuario,categoria+1)        
        self.conn.insertQuery("insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo,correo_universidad,uni,usuario,idtipopersona) values (%s, '%s', '%s', %s, '%s', '%s', '%s', %s, '%s',%s )" %datos)
        
        if categoria == 0:
            #estudianteid= int("%s" %(self.conn.selectQuery("select count(*) from estudiante")[0]))+1
            datosEstudiante=(personaid,'now',documento)            
            self.conn.insertQuery("insert into estudiante (id_persn,fecha_reg,pass_estu) values (%s,'%s', '%s' )"%datosEstudiante)
            
        if categoria == 1:
            #docenteid= int("%s" %(self.conn.selectQuery("select count(*) from docente")[0]))+1
            datosDocente=(personaid,'now',documento)            
            self.conn.insertQuery("insert into docente (id_persona,reg_fecha,pass_docente) values (%s,'%s', '%s' )"%datosDocente)
        
        
        #datos=(nombre,apellido,documento,fechaNac,telefono,correo,correoUni,universidad,usuario)
        #sql="insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo_universidad,uni,correo,usuario) values"
        #nuevo = Conexion()
        #self.conn.insertQuery(txtsql)
       # print "'%s', '%s', %s, %s, '%s', %s, %s, %s, %s, %s" %datos
        
    def verUniversidad(self,pais):
        'Consulta el listado de universidades' 
        #pais="colombia"
        idpais="%s" %(self.conn.selectQuery("select id_pais from pais where nom_pais ='"+pais+"'"))[0]        
        lista= self.conn.selectQuery("select id_uni,nom_uni from universidad where id_paisuni ="+idpais)
        uni=[]
        for row in lista:
            uni.append( "%s " % row[1])            
        return uni
        #return idpais
    
    def verPais(self):
        'Consulta el listado de paises'
        listap= self.conn.selectQuery("select id_pais,nom_pais from pais")
        pais=[]
        for row in listap:
            pais.append( "%s " % row[1])            
        return pais
        
if __name__ == "__main__":              #ejemplo 
    #dbe = Database()   
    nuevos = Request()
#nuevos.registrar("insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo_universidad,uni,correo,usuario)  values  (7, 'jmari','peres',25262525,'1995-01-03','dsadsa@ggs',1,'affwaf','juanito')")
    print nuevos.verUniversidad("1")
#nuevos.registrarPersona ('nombre','apellido','documento','fechaNac','correo','correoUni','Universidad Distrital         ','usuario',0)