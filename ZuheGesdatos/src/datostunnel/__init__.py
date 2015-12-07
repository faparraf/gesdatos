#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero"
__date__ = "$3/12/2015 10:24:29 AM$"

import base64
##-----------------------------------------------------------

class paramtunnel():
        """ Clase realizada para generar por mediod e codificacion los parametros que el
        aplicativo necesita para generar un tunnel al servidor del grupo deinvestigacion."""
        
        def __init__(self):
            """ Metodo que inicia los parametros."""
            txtfile = "strkenc"           #ponemos el archivo a encriptar
            txt_text = base64.decodestring(open(txtfile,"rb").read())  #indicamos que habra el txtfile (archivo.txt) y codifique la cadena a base64 y el resultado lo ponga entre comillas """
            #print txt_text.split("\r\n")    #imprime en la pantalla txt_text que contiene el resultado codificado a base64
            self.dirserver = str(txt_text.split("\r\n")[0])
            self.porttunnel = str(txt_text.split("\r\n")[1])
            self.pasuser = str(txt_text.split("\r\n")[2])
            self.user= str(txt_text.split("\r\n")[3])
            self.localip = str(txt_text.split("\r\n")[4])
            self.databaseserverport= "5432"
            
        
        def getidirserver(self):
            """consultor que retorna la direccion IP del servidor"""
            return self.dirserver
        
        def getporttunnel(self):
            """consultor que retorna la el puerto para el tunnel del servidor"""
            return self.porttunnel
        
        def getuser(self):
            """consultor que retorna el usuario para rar tunnel"""
            return self.user
        
        def getpasuser(self):
            """consultor que retorna la contraseña del usuario del servidor"""
            return self.pasuser
        
        def getlocalip(self):
            """consultor que retorna la dirrecion del servidor de base de datos"""
            return self.localip
        
        def getdatabaseserverport(self):
            """consultor que retorna el puerto del servidor de base de datos"""
            return self.databaseserverport
tunnel = paramtunnel()