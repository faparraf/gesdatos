#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import re
import wx
import wx.lib.scrolledpanel as scrolled
import Componentes
from RegistroUsuarios.Requests import Request

class VentanaRoles(wx.Panel):   
    
	def __init__(self,parent):
                'contructor requiere de parent como interfaz contenedor'
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.SetBackgroundColour("white")
		Component = Componentes.Component(self) # Instancia Clase Componente
                self.solicitud = Request()                             
                
  #----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsTitulo = wx.Panel(self) #Creacion padre hijo
		self.labelTitulo = Component.CreateLabel(PanelComponentsTitulo,25,pos=(0,0),label="Asignacion de Permisos\n") 
		                
  #----Creación de un panel de ComboBox, e inclusión  del objeto ComboBox y su Label
		PanelComponentsCbxUniversidad = wx.Panel(self) #Creacion padre hijo
		self.labelCbxUniversidad = Component.CreateLabel(PanelComponentsCbxUniversidad,15,pos=(0,0),label="Universidad:             ")                
		self.CbUniversidad = Component.CreateComboBox(PanelComponentsCbxUniversidad,pos=(0,0),size=250,List="")
		self.Bind(wx.EVT_COMBOBOX, self.EvtCbUniversidad, self.CbUniversidad) #Creación de Evento
		sizerPanelCbxUniversidad = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbxUniversidad.Add(self.labelCbxUniversidad , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbxUniversidad.Add(self.CbUniversidad , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbxUniversidad.SetSizer(sizerPanelCbxUniversidad)
		PanelComponentsCbxUniversidad.SetBackgroundColour("white") #Asignación de Color de Fondo               
                         
#----CreaciÃ³n de un panel de CheckBox, e inclusiÃ³n  del objeto CheckBox y su Label
                PanelComponentsCheckBox = wx.Panel(self) #Creacion padre hijo
                self.labelCheckBox = Component.CreateLabel(PanelComponentsCheckBox,15,pos=(0,0),label="My CheckBox:")
                labels=[]
                x=1
                while(x<4):                   
                    labels.append("Label1")
                    x=x+1 
                    #print x
                self.CheckBox = Component.CreateCheckBox(3,PanelComponentsCheckBox,labels,size=(70,30))
                sizerPanelCheckBox = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaÃ±os
                sizerPanelCheckBox.Add(self.labelCheckBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
                sizerPanelCheckBox.Add(self.CheckBox , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
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
                gs1 = wx.BoxSizer(wx.VERTICAL) #Creacion grilla de tamaño
                
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
		gs1.AddMany([ (PanelComponentsCbxUniversidad,1,0),(PanelComponentsCheckBox,1,0)])
                
                gs.AddMany([(PanelComponentsTitulo,wx.EXPAND,wx.ALIGN_CENTER),(gs1,0,0),
                            (PanelComponentsBConfirmar, wx.EXPAND, wx.ALIGN_CENTER)])
                                
                #gs2 = wx.GridSizer(3, 1, 7, 7)
                #gs2.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER,0,0),(gs)])
                #
                #gs3 = wx.GridSizer(1, 2, 7, 7)
                #gs3.AddMany([(PanelComponentsTitulo,0,wx.ALIGN_CENTER)])
     
                sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
		sizer.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
                
        def EvtComboBox(self, event):
            'Maneja el evento que realiza el ComboBox'
            self.CbUniversidad.Clear()
            self.CbUniversidad.AppendItems(self.solicitud.verUniversidad(self.CbPais.GetValue()))
            self.CbUniversidad.Append("Otra...")
                #print cate	
                        
        def EvtCbUniversidad(self, event):
            'Maneja el evento que realiza el ComboBox con las universidades'
            if self.CbUniversidad.GetValue() == "Otra...":               
                print "ad"
            
        def EvtRadioBox(self, event):
            'Maneja el evento que realiza el RadioBox'
            print self.ClcFechaNac.GetValue().FormatISODate()
                           
        def EvtPanelDocumento(self, event):
                'Maneja el evento que realiza el panel'
                print "pot"   
                    
        def OnClick(self,event):
            'Maneja el evento que realiza el Botón'
            #
            if self.TxtAreaNombre.GetValue() == "": 
                wx.MessageBox("El area de Nombre esta vacia ","Gesdatos")#,wx.OK|wx.CANCEL)
            elif self.TxtAreaApellido.GetValue()=="":
                 wx.MessageBox("El area de Apellido esta vacia ","Gesdatos")
            elif self.TxtAreaDocumento.GetValue()==None:
                wx.MessageBox("El area de Documento esta vacia ","Gesdatos")            
            elif self.TxtAreaCorreo.GetValue()=="":
                wx.MessageBox("El area de Correo esta vacia ","Gesdatos")
            elif self.TxtAreaCorreoUni.GetValue()=="":
                wx.MessageBox("El area de Correo Universidad esta vacia ","Gesdatos")
            elif self.CbPais.GetValue()=="":
                wx.MessageBox("El area de Pais esta sin seleccionar ","Gesdatos")
            elif self.CbUniversidad.GetValue()=="":
                wx.MessageBox("El area de Universidad esta sin seleccionar ","Gesdatos")
            elif self.TxtAreaUsuario.GetValue()=="":
                wx.MessageBox("El area de Usuario esta vacia ","Gesdatos")
            else:
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',self.TxtAreaCorreo.GetValue().lower()):
                
                    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',self.TxtAreaCorreoUni.GetValue().lower()):
                    
                        if wx.MessageBox("Desea realizar el registro ","Gesdatos",wx.OK|wx.CANCEL) ==16:
                            print "picho ok"                        
                        else:
                            try:
                                self.solicitud.registrarPersona(self.TxtAreaNombre.GetValue(),self.TxtAreaApellido.GetValue(),
                                                                self.TxtAreaDocumento.GetValue(),self.ClcFechaNac.GetValue().FormatISODate(),
                                                                self.TxtAreaCorreo.GetValue(),self.TxtAreaCorreoUni.GetValue(),
                                                                self.CbUniversidad.GetValue(),self.TxtAreaUsuario.GetValue(),
                                                                self.RbCategoria.GetSelection())
                            except :
                                wx.MessageBox("El documento o usuario ya existen ","Gesdatos")
                                self.solicitud = Request()   
                    else:
                        wx.MessageBox("El area Correo Universidad ingresado no es valido ","Gesdatos")   
                else:                
                    wx.MessageBox("El area Correo ingresado no es valido ","Gesdatos")