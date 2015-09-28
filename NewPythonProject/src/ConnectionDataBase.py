#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import psycopg2
import sys

class Connection():
    
    def __init__(self,host,dbname,user,password,port):
        'Inicia la clase que recibe los datos para establecer la conexión'
        conn_string = "host='"+host+"' dbname='"+dbname+"' user='"+user+"' port='"+port+"' password='"+password+"'"
        print "Connnecting to database\n ->%s"% (conn_string)
        self.conn = psycopg2.connect(conn_string)
        self.querys = self.conn.cursor()
        print "Connected !\n"

    def ExecuteQuery(self, queryString):
        'Ejecuta las sentencias'
        self.querys.execute(queryString)
        return self.querys.fetchall()
    
    def ExecuteQueryWithoutreturn(self, queryString):
        'Ejecuta las sentencias y retorna los resultados'
        self.querys.execute(queryString)
        self.conn.commit()               
            #print 'Error %s' % e
            
    def InsertwithaImage(self, queryString,file):
        'Realiza un insert con una imagen enviandola como un tipo Binary'
        mypic=open(file,'rb').read()
        self.querys.execute(queryString,(psycopg2.Binary(mypic),))
        self.conn.commit()               
            #print 'Error %s' % e
