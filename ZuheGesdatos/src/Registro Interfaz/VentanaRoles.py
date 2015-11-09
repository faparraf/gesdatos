#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import re
import wx
import wx.lib.scrolledpanel as scrolled
import Componentes
#from RegistroUsuarios.Requests import Request
import RequestTipoPersona
import TipoPersona
import RolTabla

class VentanaRoles(wx.Panel):   
    
	def __init__(self,parent):
                'contructor requiere de parent como interfaz contenedor'
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.SetBackgroundColour("white")
		Component = Componentes.Component(self) # Instancia Clase Componente
                self.rTipoPersona = RequestTipoPersona.RequestTipoPersona()  
                self.roltab = RolTabla.RolTabla()
                
  #----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsTitulo = wx.Panel(self) #Creacion padre hijo
		self.labelTitulo = Component.CreateLabel(PanelComponentsTitulo,25,pos=(0,0),label="Asignacion de Permisos\n") 
		                
                #----Creación de un panel de ComboBox, e inclusión  del objeto ComboBox y su Label
		PanelComponentsCbxRol = wx.Panel(self) #Creacion padre hijo
		self.labelCbxRol = Component.CreateLabel(PanelComponentsCbxRol,15,pos=(0,0),label="Rol: ")
                listica=[]
                for tip in self.rTipoPersona.verTipos():
                    listica.append(tip.get_Tipo())
		self.CbRol = Component.CreateComboBox(PanelComponentsCbxRol,pos=(0,0),size=250,List=listica)#self.solicitud.verPais())
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.CbRol) #Creación de Evento
		sizerPanelCbxRol = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbxRol.Add(self.labelCbxRol , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbxRol.Add(self.CbRol , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbxRol.SetSizer(sizerPanelCbxRol)
		PanelComponentsCbxRol.SetBackgroundColour("white") #Asignación de Color de Fondo 
                
                 #----Creación de un panel de ComboBox, e inclusión  del objeto ComboBox y su Label
		PanelComponentsCbxTabla = wx.Panel(self) #Creacion padre hijo
		self.labelCbxTabla = Component.CreateLabel(PanelComponentsCbxTabla,15,pos=(0,0),label="Tabla:")
                self.CbTabla = Component.CreateComboBox(PanelComponentsCbxTabla,pos=(0,0),size=250,List=[])#self.solicitud.verPais())
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox2, self.CbTabla) #Creación de Evento
		sizerPanelCbxTabla = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbxTabla.Add(self.labelCbxTabla , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbxTabla.Add(self.CbTabla , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbxTabla.SetSizer(sizerPanelCbxTabla)
		PanelComponentsCbxTabla.SetBackgroundColour("white") #Asignación de Color de Fondo 
                         
#----CreaciÃ³n de un panel de CheckBox, e inclusiÃ³n  del objeto CheckBox y su Label
                PanelComponentsCheckBox = wx.Panel(self) #Creacion padre hijo
                
                #labels=["Insertar","Seleccionar","Eliminar","Actualizar"]                
                #self.CheckBox = Component.CreateCheckBox(4,PanelComponentsCheckBox,labels,size=(75,30))
                self.CheckInsertar = Component.CreateCheck(PanelComponentsCheckBox,"Insertar",size=(75,30))
                self.CheckSeleccionar = Component.CreateCheck(PanelComponentsCheckBox,"Seleccionar",size=(75,30))
                self.CheckEliminar = Component.CreateCheck(PanelComponentsCheckBox,"Eliminar",size=(75,30))
                self.CheckActualizar = Component.CreateCheck(PanelComponentsCheckBox,"Actualizar",size=(75,30))
                sizerPanelCheckBox = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaÃ±os
                 # Adicion del Objeto al panel
                sizerPanelCheckBox.Add(self.CheckInsertar , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
                sizerPanelCheckBox.Add(self.CheckSeleccionar , 0, wx.ALIGN_CENTER)
                sizerPanelCheckBox.Add(self.CheckEliminar , 0, wx.ALIGN_CENTER)
                sizerPanelCheckBox.Add(self.CheckActualizar , 0, wx.ALIGN_CENTER)
                
                PanelComponentsCheckBox.SetSizer(sizerPanelCheckBox)
                PanelComponentsCheckBox.SetBackgroundColour("3399FF") #AsignaciÃ³n de Color de Fondo 

                     
                
#----Creación de un panel de Buttons, e inclusión  del objeto Buttons y su Label
		PanelComponentsBConfirmar = wx.Panel(self) #Creacion padre hijo		
		self.BConfirmar = Component.CreateButton(PanelComponentsBConfirmar,"Confirmar")
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.BConfirmar)#Creación de Evento
		sizerPanelButton = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelButton.Add(self.BConfirmar , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsBConfirmar.SetSizer(sizerPanelButton) 
		PanelComponentsBConfirmar.SetBackgroundColour("white") #Asignación de Color de Fondo 
                

                
                
                gs = wx.BoxSizer(wx.VERTICAL) #Creacion grilla de tamaño
                gs1 = wx.BoxSizer(wx.HORIZONTAL) #Creacion grilla de tamaño
                
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
		gs1.AddMany([(PanelComponentsCbxTabla,wx.EXPAND,0),(PanelComponentsCheckBox,wx.EXPAND,0)])
                
                gs.AddMany([(PanelComponentsTitulo,wx.EXPAND,wx.ALIGN_CENTER), (PanelComponentsCbxRol,wx.EXPAND,wx.ALIGN_CENTER),
                (gs1,0,wx.ALIGN_CENTER),(PanelComponentsBConfirmar, wx.EXPAND, wx.ALIGN_CENTER)])
                                
                #gs2 = wx.GridSizer(3, 1, 7, 7)
                #gs2.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER,0,0),(gs)])
                #
                #gs3 = wx.GridSizer(1, 2, 7, 7)
                #gs3.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER)])
     
                sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
                
        def EvtComboBox(self, event):
            self.CbTabla.Clear()
            #self.CbTabla.AppendItems(self.solicitud.verUniversidad(self.CbPais.GetValue()))
            'Maneja el evento que realiza el panel'
            lista=[]
            print self.CbRol.GetCurrentSelection()+1 
            for tab in self.rTipoPersona.verTablas():
                lista.append(tab.get_Tipo())
            self.CbTabla.AppendItems(lista)
            
        def EvtComboBox2(self, event):
            
            #self.CbTabla.AppendItems(self.solicitud.verUniversidad(self.CbPais.GetValue()))
            'Maneja el evento que realiza el panel'
            #roltab = RolTabla.RolTabla()
            self.roltab =self.rTipoPersona.verTablaRoles(self.CbTabla.GetCurrentSelection()+1 ,self.CbRol.GetCurrentSelection()+1)
            #print str(roltab.get_BoolSeleccionar())
            #print str(roltab.get_IdTabla())
            self.CheckSeleccionar.SetValue(self.roltab.get_BoolSeleccionar())
            self.CheckInsertar.SetValue(self.roltab.get_BoolInsertar())
            self.CheckActualizar.SetValue(self.roltab.get_BoolActualizar())
            self.CheckEliminar.SetValue(self.roltab.get_BoolEliminar())
            
            print str(self.CbRol.GetCurrentSelection()+1) +" "+ str(self.CbTabla.GetCurrentSelection()+1)
            
            
            
                
            #print "pot"   
                    
        def OnClick(self,event):
            'Maneja el evento que realiza el Botón'
            #           
            if self.CbRol.GetValue()=="":
                wx.MessageBox("El area de Rol esta sin seleccionar ","Gesdatos")
            elif self.CbTabla.GetValue()=="":
                wx.MessageBox("El area de Tabla esta sin seleccionar ","Gesdatos")
            else:
                if(self.roltab.get_BoolSeleccionar()!=self.CheckSeleccionar.GetValue()):
                    self.rTipoPersona.actualizarRolTabla(self.roltab.get_IdRolTablaSeleccionar(),self.CheckSeleccionar.GetValue())
                    #print "entro"+str(self.roltab.get_IdRolTabla())
                elif(self.roltab.get_BoolInsertar()!=self.CheckInsertar.GetValue()):
                    self.rTipoPersona.actualizarRolTabla(self.roltab.get_IdRolTablaInsertar(),self.CheckInsertar.GetValue())
                elif(self.roltab.get_BoolActualizar()!=self.CheckActualizar.GetValue()):
                    self.rTipoPersona.actualizarRolTabla(self.roltab.get_IdRolTablaActualizar(),self.CheckActualizar.GetValue())
                elif(self.roltab.get_BoolEliminar()!=self.CheckEliminar.GetValue()):
                    self.rTipoPersona.actualizarRolTabla(self.roltab.get_IdRolTablaEliminar(),self.CheckEliminar.GetValue())                
                
                print self.roltab.get_BoolSeleccionar()
                print self.CheckActualizar.GetValue()
            
                