#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import Componentes
import ConnectionDataBase
import ConnSchema
import pprint


class PanelShell(wx.Panel,):
	def __init__(self, parent,connection,*args, **kwds):
		self.parent = parent
		self.conn = connection
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Panel.__init__(self, parent)
		self.componentes = Componentes.Component(self)
		self.SetBackgroundColour("3399FF")
		self.buttonActualizar = self.componentes.CreateButton(self,"Ejecutar")
		self.Bind(wx.EVT_BUTTON, self.ejecutarQuery,self.buttonActualizar)
		self.textAreaQuery = self.componentes.CreateTextArea(self,pos=(200,20),size=(620,300))
		self.textAreaQuery.SetForegroundColour(wx.WHITE)
		self.textAreaQuery.SetBackgroundColour(wx.BLACK)
		self.textAreaQuery.SetEditable(0)
	

	def ejecutarQuery(self,text):
		try:
			sql = self.parent.panelQuery.getValue()
			matrix = self.conn.ExecuteQuery(sql)
			tittles = self.conn.GetLastTittles()
			matrix.insert(0, tittles)
			text = self.formatText(matrix)
		except Exception as err:
				text = 'Error: '+str(err.pgcode)
				self.conn.ExtecuteRollBack()
		self.textAreaQuery.SetValue(text)

	def formatText(self, matrix):
		s = [[str(e) for e in row] for row in matrix]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		text = '\n'.join(table)
		return text
