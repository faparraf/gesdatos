#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
import wx.grid
import wx.animate
import sys, os


class Head(wx.Panel,):
    def __init__(self,parent):
        'Inicia la parte del encabezado.'
        #Encabezado
       	wx.Panel.__init__(self, parent)
	self.SetBackgroundColour('3399FF')
	
	PanelImage1 = wx.Panel(self)
	script_dir = sys.path[0]
        img_path = os.path.join(script_dir, "../Imagenes/Udistrital.png")
       	self.image = wx.Image(img_path)
        self.image.Rescale(80, 100) 
	self.imageUd = wx.BitmapFromImage(self.image) 
	self.imagen1 = wx.StaticBitmap(PanelImage1, -1, self.imageUd,style=wx.BITMAP_TYPE_PNG)
	PanelImage1.SetBackgroundColour('3399FF')

	PanelText = wx.Panel(self)
	self.text1 = wx.StaticText(PanelText, label="ZUHÉ - UD")
        self.font1 = wx.Font(20 ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text1.SetFont(self.font1)

	self.text2 = wx.StaticText(PanelText, label="SOFTWARE ACADÉMICO 1.0")
        self.font2 = wx.Font(13 ,wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text2.SetFont(self.font2)
	sizertext = wx.BoxSizer(wx.VERTICAL)
	sizertext.Add(self.text1, 0, flag=wx.ALIGN_CENTER)
	sizertext.Add(self.text2, 0, flag=wx.ALIGN_CENTER)	
	PanelText.SetSizer(sizertext)
	
	PanelText.SetBackgroundColour('3399FF')
	
	PanelImage2 = wx.Panel(self)
        script_dir = sys.path[0]
        img_path = os.path.join(script_dir, "../Imagenes/sologesdatos.gif")
        self.gif = wx.animate.Animation(img_path)
        ctrl = wx.animate.AnimationCtrl(PanelImage2, -1, self.gif)
        ctrl.SetUseWindowBackgroundColour()
        ctrl.Play()
	PanelImage2.SetBackgroundColour('3399FF')

	sizer = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(1, 3, 5, 5)

        gs.AddMany([(PanelImage1, 0, wx.ALIGN_CENTER),
            (PanelText, 0, wx.ALIGN_CENTER),
            (PanelImage2, 0, wx.ALIGN_CENTER)])

        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
	self.SetSizer(sizer)

##-----------------------------------------------------------

class Low(wx.Panel,):
    def __init__(self,parent):
        'Inicia la parte del pie de p�gina.'
        #Pie de Pagina
      	wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("3399FF")
	Paneltext = wx.Panel(self)

	sizertext = wx.BoxSizer(wx.VERTICAL)
	self.text1 = wx.StaticText(Paneltext, label="Universidad Distrital Fransisco José de Caldas")
        self.font1 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text1.SetFont(self.font1)

	self.text2 = wx.StaticText(Paneltext, label="Grupo de Investigación Gesdatos")
	self.font2 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text2.SetFont(self.font2)
	
	self.text3 = wx.StaticText(Paneltext, label="Todos los Derechos Reservados")
	self.font3 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.text3.SetFont(self.font3)
	sizertext.Add(self.text1, 0, wx.ALIGN_CENTER)
	sizertext.Add(self.text2, 0, wx.ALIGN_CENTER)
	sizertext.Add(self.text3, 0, wx.ALIGN_CENTER)
	Paneltext.SetSizer(sizertext)
	Paneltext.SetBackgroundColour("3399FF")
	
	PanelImage1 = wx.Panel(self)
	script_dir = sys.path[0]
        img_path = os.path.join(script_dir, "../Imagenes/simbolo.png")
        self.image = wx.Image(img_path)
        self.image.Rescale(50, 50) 
	self.imageUd = wx.BitmapFromImage(self.image) 
	self.imagen1 = wx.StaticBitmap(PanelImage1, -1, self.imageUd,style=wx.BITMAP_TYPE_PNG)
	PanelImage1.SetBackgroundColour('3399FF')
	
	gs = wx.GridSizer(2, 1, 5, 5)

        gs.AddMany([(Paneltext, 0, wx.ALIGN_CENTER),(PanelImage1, 0, wx.ALIGN_CENTER)])
	
	sizerPanel = wx.BoxSizer(wx.VERTICAL)
	sizerPanel.Add(gs, 0, wx.ALIGN_CENTER)
	self.SetSizer(sizerPanel)
