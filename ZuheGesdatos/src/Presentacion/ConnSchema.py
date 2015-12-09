#!/usr/bin/env python
# -*- coding: cp1252 -*
import ConnectionDataBase

class ConnSchema():
    def __init__(self,localhost,gesdatos,user,password,port):
        self.connection = ConnectionDataBase.Connection(localhost,gesdatos,user,password,port)

    def ObtenerInvolucrados(self):
        sql = ("SELECT concat('Participante:  ',nombres) ,concat(' Proyecto:  ',proyecto_curricular.nombre) FROM estudiante_involucrado,proyecto_curricular,periodo Where estudiante_involucrado.id_proyecto = proyecto_curricular.id_proyecto and  periodo.id_periodo = estudiante_involucrado.id_periodo")
        ret = self.connection.ExecuteQuery(sql)
        return ret
    def ObtenerFacultades(self):
    	sql = ("SELECT id_facultad,nombre from facultad")
        ret = self.connection.ExecuteQuery(sql)
        return ret
    def ObtenerProyectos(self,facultad):
     	sql = ("SELECT id_proyecto, nombre  from proyecto_curricular where id_facultad="+facultad)
     	print (sql)
     	ret = self.connection.ExecuteQuery(sql)
     	return ret
    def InsertarParticipante(self,codigo,id_proyecto,id_periodo,nombres,trabajo):
     	sql = "INSERT INTO estudiante_involucrado(id_periodo, id_proyecto, codigo, nombres, trabajo) VALUES ("+str(id_periodo)+","+str(id_proyecto)+",'"+codigo+"','"+nombres+"','"+trabajo+"')"
     	#sql1='INSERT INTO  estudiante_involucrado(id_periodo, id_proyecto, codigo, nombres, trabajo) VALUES (%s,%s, %s,%s, %s)',(id_periodo, id_proyecto,+"'"+codigo+"'","'"+nombres+"'","'"+trabajo+"'")
      	ret = self.connection.Execute(sql)
     	return ret
           
        


    