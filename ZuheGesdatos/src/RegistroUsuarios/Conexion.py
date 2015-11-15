#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import psycopg2, psycopg2.extras  
#from Registro import Registro
# importar libreria psycopg2 para permitir la conexion con postgres


class Conexion:                  
    'Clase que permitira la comunicacion con la base de datos'     
    host = "127.0.0.1"           
    user = "adminexamen"
    passwd = "pasexamen"
    port="5432"
    db = "examen"
    
    def __init__(self):
        'Constructor que inicia las funciones de la clase'  
        self.connection = psycopg2.connect( database=self.db,
                                           user= self.user,
                                           password= self.passwd,
                                           host= self.host,
                                           port = self.port
                                           )
        self.cur = self.connection.cursor()  #cursor

    def insertQuery(self,txtsql):                 #funcion querry para interactuar con la BD  
        'Permite la inserción sql de los datos'  
        self.cur.execute(txtsql)
        self.connection.commit()               
            #print 'Error %s' % e
            
    def selectQuery(self,txtsql):
        'Permite la consulta sql de los datos' 
        self.cur.execute(txtsql)        
        datos = self.cur.fetchall() 
        return datos
    
    def finalizarConexion(selfself):
        'Finaliza la conexión' 
        self.cur.close()
        self.connection.close()    

#if __name__ == "__main__":              #ejemplo 
    #dbe = Database()   
    #print "hola"
   #nuevo =  Registro() 
#    nuevo.registrar();
    #q = "SELECT * FROM estudiante"     #sentencia sql
    #print(dbe.query(q))                 #como se llama la funcion querry
    #dbe=Registro();
    #print(dbe.registrar(juan,1,1,1,1,1))
