#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid


class Head(wx.Panel,):
    def __init__(self,parent):
        #Encabezado
       	wx.Panel.__init__(self, parent)
	self.SetBackgroundColour('white')
	
	PanelImage1 = wx.Panel(self)
	self.image = wx.Image("Imagenes/Udistrital.png")
	self.image.Rescale(100, 150) 
	self.imageUd = wx.BitmapFromImage(self.image) 
	self.imagen1 = wx.StaticBitmap(PanelImage1, -1, self.imageUd,style=wx.BITMAP_TYPE_PNG)
	PanelImage1.SetBackgroundColour('white')

	PanelText = wx.Panel(self)
	self.text1 = wx.StaticText(PanelText, label="SOFTWARE ACAD�MICO")
        self.font1 = wx.Font(20 ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text1.SetFont(self.font1)

	self.text2 = wx.StaticText(PanelText, label="GESDATOS VERSI�N 1.0")
        self.font2 = wx.Font(20 ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text2.SetFont(self.font2)
	sizertext = wx.BoxSizer(wx.VERTICAL)
	sizertext.Add(self.text1, 0, flag=wx.EXPAND)
	sizertext.Add(self.text2, 0, flag=wx.EXPAND)	
	PanelText.SetSizer(sizertext)
	
	PanelText.SetBackgroundColour('white')
	
	PanelImage2 = wx.Panel(self)
	self.image2 = wx.Image("Imagenes/Gesdatos.jpg")
	self.image2.Rescale(250, 200) 
	self.imageGesdatos = wx.BitmapFromImage(self.image2) 
	self.imagen2 = wx.StaticBitmap(PanelImage2, -1, self.imageGesdatos, style=wx.BITMAP_TYPE_PNG)
	PanelImage2.SetBackgroundColour('white')

	sizer = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(1, 3, 5, 5)

        gs.AddMany([(PanelImage1, 0, wx.ALIGN_CENTER),
            (PanelText, 0, wx.ALIGN_CENTER),
            (PanelImage2, 0, wx.ALIGN_CENTER)])

        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
	self.SetSizer(sizer)


class Low(wx.Panel,):
    def __init__(self,parent):
        #Encabezado
      	wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("white")
	Paneltext = wx.Panel(self)

	sizertext = wx.BoxSizer(wx.VERTICAL)
	self.text1 = wx.StaticText(Paneltext, label="Universidad Distrital Fransisco Jos� de Caldas")
        self.font1 = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text1.SetFont(self.font1)

	self.text2 = wx.StaticText(Paneltext, label="Grupo de Ivestigaci�n Gesdatos")
	self.font2 = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text2.SetFont(self.font2)
	
	self.text3 = wx.StaticText(Paneltext, label="Todos los Derechos Reservados")
	self.font3 = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text3.SetFont(self.font3)
	sizertext.Add(self.text1, 0, wx.ALIGN_CENTER)
	sizertext.Add(self.text2, 0, wx.ALIGN_CENTER)
	sizertext.Add(self.text3, 0, wx.ALIGN_CENTER)
	Paneltext.SetSizer(sizertext)
	Paneltext.SetBackgroundColour("white")
	
	PanelImage1 = wx.Panel(self)
	self.image = wx.Image("Imagenes/simbolo.png")
	self.image.Rescale(60, 60) 
	self.imageUd = wx.BitmapFromImage(self.image) 
	self.imagen1 = wx.StaticBitmap(PanelImage1, -1, self.imageUd,style=wx.BITMAP_TYPE_PNG)
	PanelImage1.SetBackgroundColour('white')
	
	
	gs = wx.GridSizer(2, 1, 5, 5)

        gs.AddMany([(Paneltext, 0, wx.ALIGN_CENTER),(PanelImage1, 0, wx.ALIGN_CENTER)])
	
	sizerPanel = wx.BoxSizer(wx.VERTICAL)
	sizerPanel.Add(gs, 0, wx.ALIGN_CENTER)
	self.SetSizer(sizerPanel)
