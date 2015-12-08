#!/usr/bin/env python
# -*- coding: cp1252 -*-
__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.grid
import pprint
import wx.lib.intctrl
import wx.lib.agw.hyperlink as hl
import wx.lib.intctrl


class Component(wx.Panel):
	def __init__(self,parent):
                'Inicia la interfaz.'
	        wx.Panel.__init__(self,parent) 
                
#-----------------Creación de Label------------
	def CreateLabel(self,parent,fonsize,pos,label):  
                'Permite la creación de un Label (etiqueta).'
		self.label = wx.StaticText(parent, label=label, pos=(pos[0], pos[1]))
		self.label.SetForegroundColour(('#FFFFFF'))
		self.font = wx.Font(fonsize ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)	  
                self.font = wx.Font(fonsize ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		self.label.SetFont(self.font)
		return self.label

#-----------------Creación de ComboBox------------      
	def CreateComboBox(self,parent,pos,size,List): 
                'Permite la creación de un ComboBox.'
		self.cbx = wx.ComboBox(parent, pos=(pos[0], pos[1]), size=(size, -1), choices=List, style=wx.CB_DROPDOWN)
		return self.cbx

#-----------------Creación de CalendarCtrl------------      
	def CreateCalendarCtrl(self,parent,pos,size):
                'Permite la creación de un Calendario.'
                self.calc =wx.DatePickerCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=wx.DP_DROPDOWN)
		return self.calc
        
#-----------------Creación de TextArea------------ 
	def CreateTextArea(self,parent,pos,size):  
                'Permite la creación de un TextArea.'
		self.txtarea = wx.TextCtrl(parent,pos=(pos[0], pos[1]), size=(size[0],size[1]), style=wx.TE_MULTILINE)
		return self.txtarea

#-----------------Creación de Hyperlink-----------
	def CreateHyperLink(self,parent,name,link):
                'Permite la creación de un HyperLink.'
		self.hyper = hl.HyperLinkCtrl(parent, -1, name, pos=(100, 100),URL=link)
		self.hyper.SetForegroundColour(('#FFFFFF'))
		self.hyper.SetBackgroundColour('#32506D') 
		return self.hyper

#-----------------Creaciónn de RadioBox------------ 
	def CreateRadioBox(self,parent,label,radioList):
                'Permite la creación de un RadioBox.'
		self.RadioBox = wx.RadioBox(parent, -1, label, (10, 10), wx.DefaultSize,radioList, 2, wx.RA_SPECIFY_COLS)
		self.RadioBox.SetForegroundColour('#FFFFFF')
		return self.RadioBox

#-----------------Creación de Grilla------------ 	
	def CreateGrid(self,parent,rows,colums,titles,width):
                'Permite la creación de un Grid.'
		self.Grid=wx.grid.Grid(parent)
		self.Grid.CreateGrid(rows,colums)
		for i in range(0,colums):
			self.Grid.SetColLabelValue(i,titles[0])
			self.Grid.SetColSize(i,width)	
		return self.Grid            
    
#---------------Creción de Lista de Control-----------------------------
	def CreateListctrl(self,parent,titles,lenghs,size):
                'Permite crear una lista de control'
		self.listctrl = wx.ListCtrl(parent, size=(size[0],size[1]), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		for i in range(len(titles)):
			self.listctrl.InsertColumn(i, titles[i], width=lenghs[i])
		return self.listctrl
            
#-----------------Creación de Boton------------ 	
	def CreateButton(self,parent,label):
                'Permite la creación de un Botón.'
		self.Button =wx.Button(parent,label=label)
		self.Button.SetForegroundColour('#FFFFFF')
		self.Button.SetBackgroundColour('#32506D') 
		return self.Button            

#-----------------Creación de CheckBox----------------------------------------------------- 	
	def CreateCheckBox(self,number,parent,labels,size):
                'Permite la creación de un CheckBox.'
		CheckBoxList=[]
		if number>=1 :
			for i in range(1,number+1):
				self.ck1=wx.CheckBox(parent,label=labels[i-1],size=(size[0],size[1]), style=0)
				self.ck1.SetForegroundColour('#FFFFFF')
				CheckBoxList.append(self.ck1)

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
            
#-----------------Creación de Notebook----------------------------------------------------- 
	def CreateNotebook(self,parent,numberpages,labels,size):
                'Permite crear un Notebook'
		self.Notebook = wx.Notebook(parent, size=(size[0],size[1]))
		self.panel = wx.Panel(self.Notebook )
		self.Notebook.AddPage(self.panel, labels[0])	
		for i in range(numberpages-1):	
			self.panel = wx.Panel(self.Notebook )
			self.Notebook.AddPage(self.panel, labels[i+1])
		return self.Notebook
			
#-----------------------------------------------------redireccion-c------------
	def setpanel(self,panel):
		panel.Show(True)

#-----------------Creación de un evento del CheckBox------------ 	
	def EventComboBox(self, event):
                'Identifica el evento del ComboBox.'
		print("Mi evento")
	
        def EvtComboBox(self, event):
                'Identifica el evento del ComboBox.'
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxSchema(self, event):
                'Identifica el evento del ComboBox.'
		print('Evento de combo box: %s' % event.GetString())

	def EvtComboBoxTable(self, event):
                'Identifica el evento del ComboBox.'
		print('Evento de combo box: %s' % event.GetString())
