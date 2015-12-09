#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import ConnectionDataBase

class ConnSchema():
    def __init__(self, conn):
        'Inicia la conexión y la interfaz'
        self.connection = conn

    def GetTables(self,schema):
        'Obtiene las tablas'
        ret = self.connection.ExecuteQuery("SELECT table_name FROM information_schema.tables WHERE table_schema ='public' AND table_catalog = '"+schema+"'")
        for i in range(len(ret)):
            ret[i] = str(ret[i][0])
        return ret

    def GetColumns(self,schema,table):
        'Obtiene los campos de una tabla'
        ret = self.connection.ExecuteQuery("SELECT column_name FROM information_schema.columns WHERE table_schema ='public' AND table_catalog ='"+schema+"' AND table_name ='"+table+"'")
        for i in range(len(ret)):
            ret[i] = str(ret[i][0])
        return ret

    def GetPrimaryKeys(self,schema,table):
        'Obtiene las llaves primarias de una tabla'
        ret = self.connection.ExecuteQuery("SELECT kcu.column_name from information_schema.table_constraints AS tc JOIN 		information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_catalog ='"+schema+"' AND kcu.table_name = '"+table+"'")
        for i in range(len(ret)):
            ret[i] = str(ret[i][0])
        return ret

    def GetForeignTables(self,schema,table,column):
        'Obtiene las llaves foráneas de una tabla'
        ret = self.connection.ExecuteQuery("SELECT destination FROM (SELECT ccu.table_name, kcu.table_name AS destination FROM information_schema.table_constraints AS tc JOIN  information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name JOIN information_schema.constraint_column_usage AS ccu ON kcu.constraint_name = ccu.constraint_name WHERE tc.table_catalog ='"+schema+"' AND ((kcu.table_name = '"+table+"' AND kcu.column_name = '"+column+"')OR (ccu.table_name = '"+table+"' AND ccu.column_name = '"+column+"'))AND tc.constraint_type = 'FOREIGN KEY'UNION SELECT  ccu.table_name, kcu.table_name as origin FROM information_schema.table_constraints AS tc JOIN  information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name JOIN information_schema.constraint_column_usage AS ccu ON kcu.constraint_name = ccu.constraint_name WHERE tc.table_catalog ='"+schema+"' AND ((kcu.table_name = '"+table+"' AND kcu.column_name = '"+column+"')OR (ccu.table_name = '"+table+"' AND ccu.column_name = '"+column+"'))AND tc.constraint_type = 'FOREIGN KEY') AS temp")
        for i in range(len(ret)):
            ret[i] = str(ret[i][0])
        return ret

    def GetForeignKeys(self,schema,table,column,foreignTable):
        'Obtiene las llaves primarias de una tabla'
	sql = "SELECT ccu.column_name AS destination FROM information_schema.table_constraints AS tc JOIN  information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name JOIN information_schema.constraint_column_usage AS ccu ON kcu.constraint_name = ccu.constraint_name WHERE tc.table_catalog ='"+schema+"' AND ((kcu.table_name = '"+table+"' AND kcu.column_name = '"+column+"' AND ccu.table_name = '"+foreignTable+"') OR (ccu.table_name = '"+table+"' AND ccu.column_name = '"+column+"' AND kcu.table_name = '"+foreignTable+"')) AND tc.constraint_type = 'FOREIGN KEY'UNION SELECT kcu.column_name as origin FROM information_schema.table_constraints AS tc JOIN  information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name JOIN information_schema.constraint_column_usage AS ccu ON kcu.constraint_name = ccu.constraint_name WHERE tc.table_catalog ='"+schema+"' AND ((kcu.table_name = '"+table+"' AND kcu.column_name = '"+column+"' AND ccu.table_name = '"+foreignTable+"') OR (ccu.table_name = '"+table+"' AND ccu.column_name = '"+column+"' AND kcu.table_name = '"+foreignTable+"')) AND tc.constraint_type = 'FOREIGN KEY'";        
	print (sql)	
	ret = self.connection.ExecuteQuery(sql)
        for i in range(len(ret)):
            ret[i] = str(ret[i][0])
        return ret
    def ObtenerInvolucrados(self):
        sql = ("SELECT concat('Participante:  ',nombres) ,concat(' Proyecto:  ',proyecto_curricular.nombre)  FROM estudiante_involucrado,proyecto_curricular,periodo Where estudiante_involucrado.id_proyecto = proyecto_curricular.id_proyecto and  periodo.id_periodo = estudiante_involucrado.id_periodo")
        ret = self.connection.ExecuteQuery(sql)
        return ret
