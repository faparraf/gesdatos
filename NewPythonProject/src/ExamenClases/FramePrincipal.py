#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes


## Head
##-----------------------------------------------------------
class Head(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		self.SetBackgroundColour("white")
		head = HeadLow.Head(self)
		sizerhead = wx.BoxSizer(wx.VERTICAL)
		sizerhead.Add(head,0,wx.EXPAND|wx.ALL,border=10)
		self.SetSizer(sizerhead)
##-----------------------------------------------------------

## Body
##-----------------------------------------------------------
class Body(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.SetBackgroundColour("white")
		Component = Componentes.Component(self) # Instancia Clase Componente
    
      #----Creación de un panel de ComboBox, e inclusión  del objeto ComboBox y su Label
		PanelComponentsCbx = wx.Panel(self) #Creacion padre hijo
		self.labelCbx = Component.CreateLabel(PanelComponentsCbx,15,pos=(0,0),label="My ComboBox:")
		self.Cb1 = Component.CreateComboBox(PanelComponentsCbx,pos=(0,0),size=150,List=["Perro","Gato"])
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.Cb1) #Creación de Evento
		sizerPanelCbx = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbx.Add(self.labelCbx , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbx.Add(self.Cb1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbx.SetSizer(sizerPanelCbx)
		PanelComponentsCbx.SetBackgroundColour("white") #Asignación de Color de Fondo 

      #----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsTxtArea = wx.Panel(self) #Creacion padre hijo
		self.labelTxtArea = Component.CreateLabel(PanelComponentsTxtArea,15,pos=(0,0),label="My TextArea:")
		self.TxtArea1 = Component.CreateTextArea(PanelComponentsTxtArea,pos=(0,0),size=(100,100))
		sizerPanelTxtArea = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelTxtArea.Add(self.labelTxtArea , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelTxtArea.Add(self.TxtArea1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsTxtArea.SetSizer(sizerPanelTxtArea)
		PanelComponentsTxtArea.SetBackgroundColour("white") #Asignación de Color de Fondo 

      #----Creación de un panel de CheckBox, e inclusión  del objeto CheckBox y su Label
		PanelComponentsCheckBox = wx.Panel(self) #Creacion padre hijo
		self.labelCheckBox = Component.CreateLabel(PanelComponentsCheckBox,15,pos=(0,0),label="My CheckBox:")
		labels=["Label1","Label2","Label3","Label4","Label5"]
		self.CheckBox = Component.CreateCheckBox(5,PanelComponentsCheckBox,labels,size=(70,30))
		sizerPanelCheckBox = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCheckBox.Add(self.labelCheckBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelCheckBox.Add(self.CheckBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCheckBox.SetSizer(sizerPanelCheckBox)
		PanelComponentsCheckBox.SetBackgroundColour("white") #Asignación de Color de Fondo 

      #----Creación de un panel de RadioBox, e inclusión  del objeto RadioBox y su Label
		PanelComponentsRadioBox = wx.Panel(self) #Creacion padre hijo
		self.labelRadioBox = Component.CreateLabel(PanelComponentsRadioBox,15,pos=(0,0),label="My RadioBox:")
		radioList = ['azul', 'rojo', 'amarillo', 'naranja', 'verde', 'lila', 'negro', 'gris']
		self.RadioBox = Component.CreateRadioBox(PanelComponentsRadioBox,"My RadioList",radioList)
		self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.RadioBox)#Creación de Evento
		sizerPanelRadioBox = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelRadioBox.Add(self.labelRadioBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelRadioBox.Add(self.RadioBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsRadioBox.SetSizer(sizerPanelRadioBox)
		PanelComponentsRadioBox.SetBackgroundColour("white") #Asignación de Color de Fondo 

      #----Creación de un panel de Grid, e inclusión  del objeto Grid y su Label
		PanelComponentsGrid = wx.Panel(self) #Creacion padre hijo
		self.labelGrid= Component.CreateLabel(PanelComponentsGrid,15,pos=(0,0),label="My Grid")
		titles = ['title1', 'title2', 'title3', 'title4']
		self.Grid = Component.CreateGrid(PanelComponentsGrid,4,4,titles,75)
		sizerPanelGrid = wx.BoxSizer(wx.VERTICAL)#Creacion caja de tamaños
		sizerPanelGrid.Add(self.labelGrid , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelGrid.Add(self.Grid , 0, wx.ALIGN_CENTER)  # Adicion del Objeto al panel
		PanelComponentsGrid.SetSizer(sizerPanelGrid)
		PanelComponentsGrid.SetBackgroundColour("white") #Asignación de Color de Fondo 

	
      #----Creación de un panel de Buttons, e inclusión  del objeto Buttons y su Label
		PanelComponentsButtons = wx.Panel(self) #Creacion padre hijo
		self.labelButton= Component.CreateLabel(PanelComponentsButtons,15,pos=(0,0),label="My Button:")
		self.Button1 = Component.CreateButton(PanelComponentsButtons,"Label Button",(80,50))
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.Button1)#Creación de Evento
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelButton.Add(self.labelButton , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelButton.Add(self.Button1 , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsButtons.SetSizer(sizerPanelButton) 
		PanelComponentsButtons.SetBackgroundColour("white") #Asignación de Color de Fondo 
    

 
		gs = wx.GridSizer(6, 1, 8, 8) #Creacion grilla de tamaño
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
		gs.AddMany([(PanelComponentsTxtArea, 0, wx.ALIGN_CENTER),
		(PanelComponentsCbx, 0, wx.ALIGN_CENTER),(PanelComponentsCheckBox, 0, wx.ALIGN_CENTER),
		(PanelComponentsRadioBox, 0, wx.ALIGN_CENTER),(PanelComponentsGrid, 0, wx.ALIGN_CENTER),
		(PanelComponentsButtons, 0, wx.ALIGN_CENTER)])
     
		sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)



##------------------------------Funciones de evento-----------------------------
	def EvtRadioBox(self, event):
		self.TxtArea1.AppendText("Evento RabioBox")
	def EvtComboBox(self, event):
		self.TxtArea1.AppendText("Evento ComboBox")
	def OnClick(self,event):
		self.TxtArea1.AppendText("Evento Boton")


      
##-----------------------------------------------------------

## Low
##-----------------------------------------------------------
class Low(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.SetBackgroundColour("white")
		sizerlow = wx.BoxSizer(wx.VERTICAL)
		low = HeadLow.Low(self)
		sizerlow.Add(low,0,wx.EXPAND|wx.ALL,border=10)
		self.SetSizer(sizerlow)

##-----------------------------------------------------------



app=wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(900,900))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour("white")
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
sizertopPanel.Add(Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()
