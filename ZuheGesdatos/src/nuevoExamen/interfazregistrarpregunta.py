#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero"
__date__ = "$20-jul-2015 18:52:55$"
import wx

########################################################################
class dialogoregistropregunta(wx.Panel):
    """panel de registro de pregunta donde se solicitar informacion por cada
    pregunta como el enuniado, el tema y el tipo de pregunta que es"""

    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i,opcionespreguntas):
        """Constructor, parent como el objeto contenedor del panel,
        manipulador como a clase que getiona la informacion de cada pregunta,
        i como el numero de rpegunta que se esta registrando y opaciones de
        preguntas como las opciones disponibles de acuerdo a la base de datos."""
        wx.Panel.__init__(self,parent)
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.it = i
        self.lblEnunciado = wx.StaticText(self, label="Enunciado :")
        self.editEnunciado = wx.TextCtrl(self, value="")
        self.lblTema = wx.StaticText(self, label="Tema :")
        #self.editTema = wx.TextCtrl(self, value="")
        self.sampleListTema = []
        self.temaescogido = ""
        query ="SELECT * FROM tema;"            
        self.opcionespreguntasTema = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los temas registrados
        print("consutla sql de temas de pregunta "+str(self.opcionespreguntasTema))
        for a in self.opcionespreguntasTema:
            self.sampleListTema.append(a[2])
        print("lista resultante "+str(self.sampleListTema))
        self.editTema = wx.ComboBox(self, choices=self.sampleListTema, style=wx.CB_DROPDOWN)
        self.editTema.Bind(wx.EVT_COMBOBOX, self.idtemaescogido)
        self.lblTipo = wx.StaticText(self, label="Tipo Pregunta: ")
        
        #self.editTipo = wx.TextCtrl(self, value="")
        self.sampleList = []
       
        print("consutla sql de tipos de pregunta "+str(opcionespreguntas))
        for a in opcionespreguntas:
            self.sampleList.append(a[1])
        print("lista resultante "+str(self.sampleList))
        self.editTipo = wx.ComboBox(self, choices=self.sampleList, style=wx.CB_DROPDOWN)
        #creacion de file chooser
        self.lblImagen = wx.StaticText(self, label="Ilustracion de Imagen: ")
        self.lblImagenRu = wx.StaticText(self, label="...")
        btnImagen = wx.Button(self, wx.ID_OK, label="Agregar", pos=(50, 170))
        okBtn = wx.Button(self, wx.ID_OK)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lblEnunciado, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editEnunciado, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblTema, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editTema, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblTipo, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editTipo, 0, wx.ALL|wx.CENTER, 5)
        #ingreso de elementos
        sizer.Add(self.lblImagen, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblImagenRu, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btnImagen, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        okBtn.Bind(wx.EVT_BUTTON, self.registro)
        btnImagen.Bind(wx.EVT_BUTTON, self.agregarImagen)
        self.SetSizer(sizer)
    
    def idtemaescogido(self,e):
        'metodo escucha de evento de escoger un tema con fin de saber  el valor de la llave del tema escogido'
        temapregunta = e.GetString()
        fila = 0
        for it in self.sampleListTema:
            if it == temapregunta:
                self.temaescogido = self.opcionespreguntasTema[fila][0]
                break
            fila=fila+1
    
    def registro(self, e):
        'oyente del boton para registrar las preguntas'
        # Definimos los metodos de los eventos
        self.father.registrarpreguntas(self,e,self.it)
    
    def agregarImagen(self, e):
        'oyente del boton para agragar la imagen de la pregunta'
        # Acivamos el File Chooser
        openFileDialog = wx.FileDialog(self, "Buscar Imagen", "", "",
                                       "Archivos JGP (*.jpg)|*.jpg|Archivos PNG (*.png)|*.png|Archivos GIF (*.gif)|*.gif", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        print(str(openFileDialog.GetPath()))
        self.lblImagenRu.SetLabel(str(openFileDialog.GetPath()))

##-----------------------------------------------------------        
        
class dialogoregistrorespuestaopcionmultiplemultiple(wx.Panel):
    """panel de registro de respuesta de tipo opcion multiple con multiple
    respuesta"""

    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, l manipulador
        como la calse que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.it = i
        self.editOpcion = []
        self.sampleList = ['Correcto', 'Incorrecto']
        self.editRespuesta = []
        self.cantidadropciones = 5
        for it in range(self.cantidadropciones):
            self.editRespuesta.append(wx.TextCtrl(self, value=""))
            self.editOpcion.append(wx.ComboBox(self, value="Incorrecto", choices=self.sampleList, style=wx.CB_DROPDOWN))
        
        okBtn = wx.Button(self, wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        for it in range(self.cantidadropciones):
            sizerit = wx.BoxSizer(wx.HORIZONTAL)
            self.lblRespuesta = wx.StaticText(self, label="Opcion:")
            sizerit.Add(self.lblRespuesta, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editRespuesta[it], 0, wx.ALL|wx.CENTER, 5)
            self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
            sizerit.Add(self.lblOpcion, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editOpcion[it], 0, wx.ALL|wx.CENTER, 5)
            sizer.Add(sizerit, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
        
    def registro(self, e):
        'oyente del boton para registrar las repsuestas'
        # Definimos los metodos de los eventos
        self.father.registrarrespuesta(e,self,self.it)

##-----------------------------------------------------------

class dialogoregistrorespuestafalseoverdadero(wx.Panel):
    """panel de registro de respuesta de tipo falso verdadero"""
    
    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, el manipulador
        como la clase que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.it = i
        self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
        self.editOpcion = []
        self.editOpcion.append(wx.TextCtrl(self, value="Correcto"))
        self.lblRespuesta = wx.StaticText(self, label="Respuesta:")
        self.sampleList = ['Falso', 'Verdadero']
        self.editRespuesta = []
        self.cantidadropciones = 1
        self.editRespuesta.append(wx.ComboBox(self, choices=self.sampleList, style=wx.CB_DROPDOWN))
        
        okBtn = wx.Button(self, wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lblOpcion, 0, wx.ALL|wx.CENTER, 5)
        for it in self.editOpcion:
            sizer.Add(it, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblRespuesta, 0, wx.ALL|wx.CENTER, 5)
        for it in self.editRespuesta:
            sizer.Add(it, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
        
    def registro(self, e):
        'oyente del boton para registrar las repsuestas'
        # Definimos los metodos de los eventos
        self.father.registrarrespuesta(e,self,self.it)

##-----------------------------------------------------------

class dialogoregistrorespuestaopcionmultipleunico(wx.Panel):
    """panel de registro de respuesta de tipo opcion multiple con unica
    respuesta"""

    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, el manipulador
        como la clase que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
	self.SetBackgroundColour("#32506D") # Color de Fondo del panel
        self.father = manipulador
        self.it = i
        self.editOpcion = []
        self.sampleList = ['Correcto', 'Incorrecto']
        self.editRespuesta = []
        self.cantidadropciones = 4
        for it in range(self.cantidadropciones):
            self.editRespuesta.append(wx.TextCtrl(self, value=""))
            self.editOpcion.append(wx.ComboBox(self, choices=self.sampleList, style=wx.CB_DROPDOWN))
        
        okBtn = wx.Button(self, wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        for it in range(self.cantidadropciones):
            sizerit = wx.BoxSizer(wx.HORIZONTAL)
            self.lblRespuesta = wx.StaticText(self, label="Opcion:")
            sizerit.Add(self.lblRespuesta, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editRespuesta[it], 0, wx.ALL|wx.CENTER, 5)
            self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
            sizerit.Add(self.lblOpcion, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editOpcion[it], 0, wx.ALL|wx.CENTER, 5)
            self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editOpcion[it])
            sizer.Add(sizerit, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
        
    def EvtComboBox(self, event):
        if (event.GetString()=='Correcto'):
            opcion = 'Incorrecto'
        else:
            opcion = 'Correcto'
        for it in range(self.cantidadropciones):
            if (self.editOpcion[it].GetValue()!=event.GetString()):
                self.editOpcion[it].SetValue(opcion)
                
    def registro(self, e):
        'oyente del boton para registrar las repsuestas'
        # Definimos los metodos de los eventos
        self.father.registrarrespuesta(e,self,self.it)
