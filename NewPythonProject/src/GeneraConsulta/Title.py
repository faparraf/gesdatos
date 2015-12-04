#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
class Title1(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        wx.Panel.__init__(self, parent,size=(100,100))
	self.SetBackgroundColour("3399FF")
        self.text = wx.StaticText(self, label="SElECCIÓN y FUNCIONES", pos=(0, 0))
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)
  

class Title2(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        wx.Panel.__init__(self, parent,size=(100,100))
	self.SetBackgroundColour("3399FF")
        self.text = wx.StaticText(self, label="OPERACIÓN JOIN", pos=(0, 0))
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)

class Title3(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("3399FF")
        self.text = wx.StaticText(self, label="CONDICIÓN (WHERE)", pos=(0, 0))
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)
        
class Title4(wx.Panel,):
    def __init__(self, parent,*args, **kwds):
        wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("3399FF")
        self.text = wx.StaticText(self, label="COMPILADOR", pos=(0, 0))
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.text.SetFont(self.font)
        
