#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import pprint
import  wx.lib.intctrl


class Component(wx.Panel):
	def __init__(self,parent):
	        wx.Panel.__init__(self,parent)  
#-----------------Creación de Label------------

#-----------------Creación de TextArea------------ 
	def CreateIntCtrl(self,parent,pos,size):   
		self.intctrl = wx.lib.intctrl.IntCtrl( parent,pos=(pos[0], pos[1]),value = None, allow_none =True,allow_long = False, size=(size[0],size[1]) )
		return self.intctrl

#-----------------Creación de CalendarCtrl------------      
	def CreateCalendarCtrl(self,parent,pos,size):   
		#self.calc = wx.CalendarCtrl(parent,date=DefaultDateTime, pos=(pos[0], pos[1]), size=(size, -1), style=wx.WANTS_CHARS)
                self.calc =wx.DatePickerCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=wx.DP_DROPDOWN)
		return self.calc

#-----------------Creación de Label------------
	def CreateLabel(self,parent,fonsize,pos,label):  
		self.label = wx.StaticText(parent, label=label, pos=(pos[0], pos[1]))
		self.font = wx.Font(fonsize ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.label.SetFont(self.font)
		return self.label

#-----------------Creación de ComboBox------------      
	def CreateComboBox(self,parent,pos,size,List):   
		self.cbx = wx.ComboBox(parent, pos=(pos[0], pos[1]), size=(size, -1), choices=List, style=wx.CB_READONLY)
		return self.cbx
    
#-----------------Creación de TextArea------------ 
	def CreateTextArea(self,parent,pos,size):   
		self.txtarea = wx.TextCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=wx.TE_MULTILINE)
		return self.txtarea

#-----------------Creación de InputText------------ 

        def CreateImputText (self,parent,pos,size):
                self.txtimp = wx.TextCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=0)
		return self.txtimp
#-----------------Creación de RadioBox------------ 
	def CreateRadioBox(self,parent,label,radioList):
		self.RadioBox = wx.RadioBox(parent, -1, label, (10, 10), wx.DefaultSize,radioList, 2, wx.RA_SPECIFY_COLS)
		return self.RadioBox

#-----------------Creación de Grilla------------ 	
	def CreateGrid(self,parent,rows,colums,titles,width):
		self.Grid=wx.grid.Grid(parent)
		self.Grid.CreateGrid(rows,colums)
		for i in range(0,colums):
			self.Grid.SetColLabelValue(i,titles[0])
			self.Grid.SetColSize(i,width)	
		return self.Grid

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

	
	def EventComboBox(self, event):
		print("Mi evento")	

	def EvtComboBox(self, event):
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxSchema(self, event):
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxTable(self, event):
		print('Evento de combo box: %s' % event.GetString())
