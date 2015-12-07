#!/usr/bin/env python
# -*- coding: cp1252 -*-
import wx
import ConnSchema
import pprint
## Head
##-----------------------------------------------------------
__docformat__ = "restructuredtext"  
class Presentacion(wx.Panel):
	"""Clase Presentacion, es una clase de tipo panel que contiene la informacion de los Participantes del proyecto
	y los eventos asociados a la visualizacion y efectos del objeto."""
	def __init__(self,parent,port):
		"""Constructor de la clase Presentacion.
		 :param parent:, padre del objeto 
            :param style:, Estilo del objeto 
            :param size:, dimensiones del objeto"""
		wx.Panel.__init__(self, parent, size=(500,260),style=wx.RAISED_BORDER)
		"""Inicializa el objeto Panel.
		    :param parent:, padre del objeto 
            :param style:, Estilo del objeto 
            :param size:, dimensiones del objeto"""
		self.SetBackgroundColour('#00BF8F')
		#Arreglo de Nombres
		db = ConnSchema.ConnSchema("localhost","examen","adminexamen","pasexamen",str(port))
		involucrados = db.ObtenerInvolucrados()
		Participantes = ""
		for j in range(len(involucrados)):
			for x in range(len(involucrados[j])):
				Participantes = Participantes +" "+str(involucrados[j][x])
			Participantes= Participantes +"\n"
	
		#Creacion Objeto Texto
		self.text1 = wx.StaticText(self, label=Participantes,pos=(20,50) ,size=(100,20*len(Participantes)))
		self.text1.SetForegroundColour(('#32506D'))
		self.font = wx.Font(10 ,wx.DECORATIVE, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
		self.text1.SetFont(self.font)
				
		#Objeto Timer
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.Movimiento, self.timer)

        #Eventos de Mouse
		self.Bind(wx.EVT_ENTER_WINDOW, self.detener)
		self.Bind(wx.EVT_LEAVE_WINDOW, self.iniciar)
		self.text1.Bind(wx.EVT_ENTER_WINDOW, self.detener)
		self.text1.Bind(wx.EVT_LEAVE_WINDOW, self.iniciar)
			
	def iniciar(self, event):
		"""Inicia el objeto Timer."""
		self.timer.Start(50)

	def detener(self, event):
		"""Detiene el objeto Timer."""
		self.timer.Stop()	

	def Movimiento(self, event):
		"""Obtiene la posicion del objeto de texto y la modifica con el fin de generar el movimiento."""
		h = self.text1.GetPosition()
		if(h[1]>=-100):
			self.text1.SetPosition((h[0] ,h[1] - 6))
		else:
			self.text1.SetPosition((50 ,260))