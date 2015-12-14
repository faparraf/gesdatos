#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
		self.querys.execute(queryString)
		return self.querys.fetchall()

	def ExtecuteRollBack(self):
		self.querys.execute('ROLLBACK')

	def GetLastTittles(self):
		return [desc[0] for desc in self.querys.description]
