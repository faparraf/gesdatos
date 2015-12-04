#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import Componentes
import ConnectionDataBase
import ConnSchema
import pprint


class PanelQuery(wx.Panel,):
	def __init__(self, parent,connection,rowsselect,*args, **kwds):
		self.parent = parent
		self.rowsselect = rowsselect
		self.conn = connection
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Panel.__init__(self, parent)
		self.componentes = Componentes.Component(self)
		self.SetBackgroundColour("3399FF")
		self.buttonActualizar = self.componentes.CreateButton(self,"Actualizar")
		self.Bind(wx.EVT_BUTTON, self.ActualizarQuery,self.buttonActualizar)
		self.textAreaQuery = self.componentes.CreateTextArea(self,pos=(200,20),size=(620,300))
	

	def ActualizarQuery(self,event):
		datosSelect = self.parent.PanelSelect.GetRowsValue()
		tablas=[]
		value = "SELECT "
		if(len(datosSelect)==0):
			value += "* "
		else:
			for j in datosSelect:
				tablas.append(j[0])
				value += j[0]+"."+j[1]+" "
				if(j[2]!=0):
					value += "AS "+j[2]
				if(j!=datosSelect[len(datosSelect)-1]):
					value += ", "

		value += "FROM "
		datosJoin = self.parent.PanelJoin.GetRowsValue()
		if(len(datosJoin)==0):
			tablas = list(set(tablas))
			for tabla in tablas:
				value += str(tabla)
				if(tabla != tablas[len(tablas)-1]):
					value += ", "
		else:
			value += ""
		self.textAreaQuery.SetValue(value)

	def getValue(self):
		return self.textAreaQuery.GetValue()
