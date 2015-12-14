#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import PanelSelect
import PanelJoin
import Title
import PanelWhere
import PanelShell
import panelQuery
import wx.lib.scrolledpanel as scrolled
import pprint


#app=wx.App(False)
#frame = wx.Frame(None,-1, title="Consultas", size=(900,900))
#wx.InitAllImageHandlers()

class BodyQuery(wx.Panel):
	def __init__(self,parent,conn):
		self.parent=parent
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		
		self.Box1 = wx.BoxSizer(wx.VERTICAL)		
		self.Title1 = Title.Title1(self)		
		self.PanelSelect = PanelSelect.PanelSelect(self,conn)
		self.rowsselect = self.PanelSelect.GetRowsValue()
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(self.rowsselect)
		self.Box1.Add(self.Title1,0,wx.ALIGN_CENTER|wx.ALL,border=10)
		self.Box1.Add(self.PanelSelect,0,wx.GROW|wx.ALIGN_CENTER|wx.ALL,border=10)


		self.Title2 = Title.Title2(self)
		self.PanelJoin = PanelJoin.PanelJoin(self,conn)
		self.Box1.Add(self.Title2,0,wx.ALIGN_CENTER|wx.ALL,border=10)		
		self.Box1.Add(self.PanelJoin,0,wx.ALIGN_CENTER|wx.ALL,border=10)
		
		
		self.Title3 = Title.Title3(self)
		self.PanelWhere = PanelWhere.PanelWhere(self,conn)
		self.Box1.Add(self.Title3,0,wx.ALIGN_CENTER|wx.ALL,border=10)		
		self.Box1.Add(self.PanelWhere,0,wx.ALIGN_CENTER|wx.ALL,border=10)		

		
		self.panelShell = PanelShell.PanelShell(self,conn)
		self.panelQuery = panelQuery.PanelQuery(self,conn,self.rowsselect)
		self.Box1.Add(self.panelQuery,0,wx.ALIGN_CENTER|wx.ALL,border=10)
		self.Box1.Add(self.panelShell,0,wx.ALIGN_CENTER|wx.ALL,border=10)


		self.sizer= wx.BoxSizer(wx.VERTICAL)
		self.gs = wx.GridSizer(1, 1, 1, 1)
		self.gs.AddMany([(self.Box1, 0, wx.ALIGN_CENTER)])

		self.sizer.Add(self.gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(self.sizer)

        def getsqlresult(self):
            return self.panelQuery.getValue()