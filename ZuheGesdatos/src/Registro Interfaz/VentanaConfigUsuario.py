#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import re
import wx
import wx.lib.scrolledpanel as scrolled
import Componentes
import RequestConfig
from RegistroUsuarios.Requests import Request

class VentanaConfigUsuario(wx.Panel):   
    
	def __init__(self,parent,idusuario,puerto):
                'contructor requiere de parent como interfaz contenedor'
		wx.Panel.__init__(self,parent) # Inicialización Panel Padre
		self.SetBackgroundColour("white")
		Component = Componentes.Component(self) # Instancia Clase Componente
                self.solicitud = Request()         
                self.rconf= RequestConfig.RequestConfig(idusuario,puerto)
                self.persona=self.rconf.ver_persona()
                
  #----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsTitulo = wx.Panel(self) #Creacion padre hijo
		self.labelTitulo = Component.CreateLabel(PanelComponentsTitulo,25,pos=(0,0),label="Config de usuario                        \n") 
		                
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsNombre = wx.Panel(self) #Creacion padre hijo
		self.labelNombre = Component.CreateLabel(PanelComponentsNombre,15,pos=(0,0),label="Nombre:        ")
		self.TxtAreaNombre = Component.CreateImputText(PanelComponentsNombre,pos=(0,0),size=(250,22))                
                self.TxtAreaNombre.SetValue(self.persona.get__nombre())
		sizerPanelNombre = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelNombre.Add(self.labelNombre , wx.RIGHT, wx.EXPAND) # Adicion del Objeto al panel
		sizerPanelNombre.Add(self.TxtAreaNombre , 0, wx.EXPAND) # Adicion del Objeto al panel
		PanelComponentsNombre.SetSizer(sizerPanelNombre)
		PanelComponentsNombre.SetBackgroundColour("white") #Asignación de Color de Fondo 
                                
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsApellido = wx.Panel(self) #Creacion padre hijo
		self.labelApellido = Component.CreateLabel(PanelComponentsApellido,15,pos=(0,0),label="Apellido:        ")
		self.TxtAreaApellido = Component.CreateImputText(PanelComponentsApellido,pos=(0,0),size=(250,22))
                self.TxtAreaApellido.SetValue(self.persona.get__apellido())
		sizerPanelApellido = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelApellido.Add(self.labelApellido ,wx.RIGHT, wx.EXPAND) # Adicion del Objeto al panel
		sizerPanelApellido.Add(self.TxtAreaApellido , 0, wx.EXPAND) # Adicion del Objeto al panel
		PanelComponentsApellido.SetSizer(sizerPanelApellido)
		PanelComponentsApellido.SetBackgroundColour("white") #Asignación de Color de Fondo 
                
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsDocumento = wx.Panel(self) #Creacion padre hijo
		self.labelDocumento = Component.CreateLabel(PanelComponentsDocumento,15,pos=(0,0),label="Documento:   ")
		self.TxtAreaDocumento = Component.CreateIntCtrl(PanelComponentsDocumento,pos=(0,0),size=(250,22))
                self.TxtAreaDocumento.SetValue(int(self.persona.get__documento()))
                self.Bind(wx.EVT_TEXT, self.EvtPanelDocumento, self.TxtAreaDocumento)
		sizerPanelDocumento = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelDocumento.Add(self.labelDocumento , wx.RIGHT, wx.EXPAND) # Adicion del Objeto al panel
		sizerPanelDocumento.Add(self.TxtAreaDocumento , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsDocumento.SetSizer(sizerPanelDocumento)
		PanelComponentsDocumento.SetBackgroundColour("white") #Asignación de Color de Fondo 
                
              
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsCorreo = wx.Panel(self) #Creacion padre hijo
		self.labelCorreo = Component.CreateLabel(PanelComponentsCorreo,15,pos=(0,0),label="Correo:                    ")
		self.TxtAreaCorreo = Component.CreateImputText(PanelComponentsCorreo,pos=(0,0),size=(250,22))	
                self.TxtAreaCorreo.SetValue(self.persona.get__correo())
                sizerPanelCorreo = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelCorreo.Add(self.labelCorreo , wx.RIGHT, wx.EXPAND) # Adicion del Objeto al panel
		sizerPanelCorreo.Add(self.TxtAreaCorreo , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCorreo.SetSizer(sizerPanelCorreo)
		PanelComponentsCorreo.SetBackgroundColour("white")                
                
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsCorreoUni = wx.Panel(self) #Creacion padre hijo
		self.labelCorreoUni = Component.CreateLabel(PanelComponentsCorreoUni,15,pos=(0,0),label="Correo Universidad:  ")
		self.TxtAreaCorreoUni = Component.CreateImputText(PanelComponentsCorreoUni,pos=(0,0),size=(250,22))
                self.TxtAreaCorreoUni.SetValue(self.persona.get__correouni().strip())
		sizerPanelCorreoUni = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelCorreoUni.Add(self.labelCorreoUni , wx.RIGHT, wx.EXPAND) # Adicion del Objeto al panel
		sizerPanelCorreoUni.Add(self.TxtAreaCorreoUni , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCorreoUni.SetSizer(sizerPanelCorreoUni)
		PanelComponentsCorreoUni.SetBackgroundColour("white")
                
#----Creación de un panel de TxtArea, e inclusión  del objeto TxtArea y su Label
		PanelComponentsUsuario = wx.Panel(self) #Creacion padre hijo
		self.labelUsuario = Component.CreateLabel(PanelComponentsUsuario,15,pos=(0,0),label="Usuario:                   ")
		self.TxtAreaUsuario = Component.CreateImputText(PanelComponentsUsuario,pos=(0,0),size=(250,22))
                self.TxtAreaUsuario.SetValue(self.persona.get__usuario().strip())
		sizerPanelUsuario = wx.BoxSizer(wx.HORIZONTAL) #Creacion caja de tamaños
		sizerPanelUsuario.Add(self.labelUsuario , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		sizerPanelUsuario.Add(self.TxtAreaUsuario , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsUsuario.SetSizer(sizerPanelUsuario)
		PanelComponentsUsuario.SetBackgroundColour("white") #Asignación de Color de Fondo 
                
#----Creación de un panel de ComboBox, e inclusión  del objeto ComboBox y su Label
		PanelComponentsCbxPais = wx.Panel(self) #Creacion padre hijo
		self.labelCbxPais = Component.CreateLabel(PanelComponentsCbxPais,15,pos=(0,0),label="Pais:              ")                
		self.CbPais = Component.CreateComboBox(PanelComponentsCbxPais,pos=(0,0),size=250,List=self.solicitud.verPais())#self.solicitud.verPais())
		
                self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.CbPais) #Creación de Evento
		sizerPanelCbxPais = wx.BoxSizer(wx.HORIZONTAL)#Creacion caja de tamaños
		sizerPanelCbxPais.Add(self.labelCbxPais , 0, wx.ALIGN_CENTER,border= 10) # Adicion del Objeto al panel
		sizerPanelCbxPais.Add(self.CbPais , 0, wx.ALIGN_CENTER) # Adicion del Objeto al panel
		PanelComponentsCbxPais.SetSizer(sizerPanelCbxPais)
		PanelComponentsCbxPais.SetBackgroundColour("white") #Asignación de Color de Fondo 
                self.CbPais.Select(int(self.persona.get__pais())-1)
                
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
                self.CbUniversidad.AppendItems(self.solicitud.verUniversidad(self.CbPais.GetValue()))
                self.CbUniversidad.Select(int(self.persona.get__universidad())-1)
                
                
                               
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
                gs2 = wx.BoxSizer(wx.VERTICAL) #Creacion grilla de tamaño
                gs3 = wx.GridSizer(1, 2, 7, 7) #Creacion grilla de tamaño
      #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
		gs1.AddMany([ (PanelComponentsNombre,1,0),
                            (PanelComponentsApellido, 1, 0), (PanelComponentsDocumento, 1, 0),
                            (PanelComponentsCbxPais,0,0)])
                gs2.AddMany([(PanelComponentsCorreo, 0, 0),(PanelComponentsCorreoUni, 0, 0),(PanelComponentsUsuario, 0, 0),
                            (PanelComponentsCbxUniversidad,0,0)])
                gs3.AddMany([gs1,gs2])
                gs.AddMany([(PanelComponentsTitulo,wx.EXPAND,wx.ALIGN_CENTER),(gs3,0,wx.ALIGN_CENTER),
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
            
                #print cate	
                        
        def EvtCbUniversidad(self, event):
            print 'Maneja el evento que realiza el ComboBox con las universidades'
           
        
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
                           
                                if(self.TxtAreaNombre.GetValue()!=self.persona.get__nombre()):
                                    self.rconf.actualizar__nombre(self.TxtAreaNombre.GetValue())
                                
                                if(self.TxtAreaApellido.GetValue()!=self.persona.get__apellido()):
                                    self.rconf.actualizar__apellido(self.TxtAreaApellido.GetValue())
                                    
                                if(self.TxtAreaDocumento.GetValue()!=self.persona.get__documento()):
                                    self.rconf.actualizar__documento(self.TxtAreaDocumento.GetValue())
                                
                                if(self.TxtAreaCorreo.GetValue()!=self.persona.get__correo()):
                                    self.rconf.actualizar__correo(self.TxtAreaCorreo.GetValue())
                                    
                                if(self.TxtAreaCorreoUni.GetValue()!=self.persona.get__correouni()):
                                    self.rconf.actualizar__correouni(self.TxtAreaCorreoUni.GetValue())
                                                                   
                                if(self.CbUniversidad.GetValue()!=self.persona.get__universidad()):
                                    self.rconf.actualizar__universidad(self.CbUniversidad.GetValue())
                                    
                                if(self.TxtAreaUsuario.GetValue()!=self.persona.get__usuario()):
                                    self.rconf.actualizar__usuario(self.TxtAreaUsuario.GetValue())   
                                    
                                wx.MessageBox("La informacion a sido actualizada ","Gesdatos")
                            except:
                                wx.MessageBox("El usuario o documento ya existen ","Gesdatos")
                                
                            
                    else:
                        wx.MessageBox("El area Correo Universidad ingresado no es valido ","Gesdatos")   
                else:                
                    wx.MessageBox("El area Correo ingresado no es valido ","Gesdatos")