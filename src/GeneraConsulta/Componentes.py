#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import wx.lib.agw.hyperlink as hl
import pprint

class Component(wx.Panel):
	def __init__(self,parent):
	        wx.Panel.__init__(self,parent)  
#-----------------Creación de Label------------
	def CreateLabel(self,parent,fonsize,pos,label):  
		self.label = wx.StaticText(parent, label=label, pos=(pos[0], pos[1]))
		self.font = wx.Font(fonsize ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.label.SetFont(self.font)
		return self.label

#-----------------Creación de ComboBox------------      
	def CreateComboBox(self,parent,pos,size,List):   
		self.cbx = wx.ComboBox(parent, pos=(pos[0], pos[1]), size=(size, -1), choices=List, style=wx.CB_DROPDOWN)
		return self.cbx
    
#-----------------Creación de TextArea------------ 
	def CreateTextArea(self,parent,pos,size):   
		self.txtarea = wx.TextCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=wx.TE_MULTILINE)
		return self.txtarea
#-----------------Creación de Hyperlink-----------

	def CreateHyperLink(self,parent,name,link):
		self.hyper = hl.HyperLinkCtrl(parent, -1, name, pos=(100, 100),URL=link)
		return self.hyper

#-----------------Creación de RadioBox------------ 
	def CreateRadioBox(self,parent,label,radioList):
		self.RadioBox = wx.RadioBox(parent, -1, label, (10, 10), wx.DefaultSize,radioList, 2, wx.RA_SPECIFY_COLS)
		return self.RadioBox

#-----------------Creación de Grilla------------ 	
	def CreateGrid(self,parent,rows,colums,titles,width):
		self.Grid=wx.grid.Grid(parent)
		self.Grid.CreateGrid(rows,colums)
		for i in range(0,colums):
			self.Grid.SetColLabelValue(i,titles[i])
			self.Grid.SetColSize(i,width)	
		return self.Grid

#-----------------------------------------------
	def CreateListctrl(self,parent,titles,lenghs,size):
		self.listctrl = wx.ListCtrl(parent, size=(size[0],size[1]), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		for i in range(len(titles)):
			self.listctrl.InsertColumn(i, titles[i], width=lenghs[i])
		return self.listctrl

#-----------------Creación de Boton------------ 	
	def CreateButton(self,parent,label):
		self.Button =wx.Button(parent,label=label)
		return self.Button

#-----------------Creación de CheckBox------------ 	
	def CreateCheckBox(self,number,parent,labels,size):
		CheckBoxList=[]
		if number>=1 :
			for i in range(1,number+1):
				print(i)
				CheckBoxList.append(wx.CheckBox(parent,label=labels[i-1],size=(size[0],size[1]), style=0))
			if number==1:
				gridCheckBox = wx.GridSizer(1, 1, 5, 5)
				gridCheckBox.AddMany([(CheckBoxList[0], 0, wx.ALIGN_CENTER)])
			if number%2==0:
				gridCheckBox = wx.GridSizer(number/2, 2, 5, 5)
				for j in range(len(CheckBoxList)):
					gridCheckBox.AddMany([(CheckBoxList[j], 0, wx.ALIGN_CENTER)])
			if number%2!=0:
				gridCheckBox = wx.GridSizer((number+1)/2, 2, 5, 5)
				for k in range(len(CheckBoxList)):
					gridCheckBox.AddMany([(CheckBoxList[k], 0, wx.ALIGN_CENTER)])
		return gridCheckBox
#-----------------------------------------------------redireccion-c------------

	def setpanel(self,panel):
		panel.Show(True)
		
		
		
		
	def EventComboBox(self, event):
		print("Mi evento")
	
	
            
             

	def EvtComboBox(self, event):
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxSchema(self, event):
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxTable(self, event):
		print('Evento de combo box: %s' % event.GetString())

   
    
        
