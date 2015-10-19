#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import PanelSelect
import PanelJoin
import Title
import PanelWhere
import PanelCompiler
import panelQuery
import wx.lib.scrolledpanel as scrolled


#app=wx.App(False)
#frame = wx.Frame(None,-1, title="Consultas", size=(900,900))
#wx.InitAllImageHandlers()

class BodyQuery(wx.Panel):
	def __init__(self,parent,conn):
		self.parent=parent
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		PanelSelect = PanelSelect.PanelSelect(self,conn)
		PanelJoin = PanelJoin.PanelJoin(self,conn)
		Title1 = Title.Title1(self)
		Title2 = Title.Title2(self)
		Title3 = Title.Title3(self)
		PanelWhere = PanelWhere.PanelWhere(self,conn)
		PanelCompiler = PanelCompiler.PanelCompiler(self)
		panelQuery = panelQuery.PanelQuery(self,conn,PanelSelect)

		sizer= wx.BoxSizer(wx.VERTICAL)
		sizer.Add(Title1,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(PanelSelect,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(Title2,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(PanelJoin,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(Title3,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(PanelWhere,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(PanelCompiler,0,wx.EXPAND|wx.ALL,border=10)
		sizer.Add(panelQuery,0,wx.EXPAND|wx.ALL,border=10)
		topPanela.SetSizer(sizer)





