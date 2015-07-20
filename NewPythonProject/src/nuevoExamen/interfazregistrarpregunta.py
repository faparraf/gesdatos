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
        self.SetBackgroundColour("white")
        self.father = manipulador
        self.it = i
        self.lblEnunciado = wx.StaticText(self, label="Enunciado :")
        self.editEnunciado = wx.TextCtrl(self, value="")
        self.lblTema = wx.StaticText(self, label="Tema :")
        self.editTema = wx.TextCtrl(self, value="")
        self.lblTipo = wx.StaticText(self, label="Tipo Pregunta :")
        #self.editTipo = wx.TextCtrl(self, value="")
        self.sampleList = []
        for a in opcionespreguntas:
            self.sampleList.append(a[1])
        print(str(self.sampleList))
        self.editTipo = wx.ComboBox(self, choices=self.sampleList, style=wx.CB_DROPDOWN)
        
        okBtn = wx.Button(self, wx.ID_OK)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lblEnunciado, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editEnunciado, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblTema, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editTema, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.lblTipo, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.editTipo, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        self.SetSizer(sizer)
    def registro(self, e):
        'oyente del boton para registrar las preguntas'
        # Definimos los metodos de los eventos
        self.father.registrarpreguntas(self,e,self.it)
        
class dialogoregistrorespuestaopcionmultiplemultiple(wx.Panel):
    """panel de registro de respuesta de tipo opcion multiple con multiple
    respuesta"""

    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, l manipulador
        como la calse que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour("white")
        self.father = manipulador
        self.it = i
        self.editOpcion = []
        self.sampleList = ['Correcto', 'Incorrecto']
        self.editRespuesta = []
        self.cantidadropciones = 5
        for it in range(self.cantidadropciones):
            self.editRespuesta.append(wx.TextCtrl(self, value=""))
            self.editOpcion.append(wx.ComboBox(self, choices=self.sampleList, style=wx.CB_DROPDOWN))
        
        okBtn = wx.Button(self, wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.registro,okBtn)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        for it in range(self.cantidadropciones):
            sizerit = wx.BoxSizer(wx.HORIZONTAL)
            self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
            sizerit.Add(self.lblOpcion, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editOpcion[it], 0, wx.ALL|wx.CENTER, 5)
            self.lblRespuesta = wx.StaticText(self, label="Respuesta:")
            sizerit.Add(self.lblRespuesta, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editRespuesta[it], 0, wx.ALL|wx.CENTER, 5)
            sizer.Add(sizerit, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
    def registro(self, e):
        'oyente del boton para registrar las repsuestas'
        # Definimos los metodos de los eventos
        self.father.registrarrespuesta(e,self,self.it)

class dialogoregistrorespuestafalseoverdadero(wx.Panel):
    """panel de registro de respuesta de tipo falso verdadero"""
    
    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, el manipulador
        como la clase que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour("white")
        self.father = manipulador
        self.it = i
        self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
        self.editOpcion = []
        self.editOpcion.append(wx.TextCtrl(self, value="Correcta"))
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

class dialogoregistrorespuestaopcionmultipleunico(wx.Panel):
    """panel de registro de respuesta de tipo opcion multiple con unica
    respuesta"""

    #----------------------------------------------------------------------
    def __init__(self,parent,manipulador,i):
        """Constructor, requiere del objeto parent que contiene el panel, el manipulador
        como la clase que gestiona la informacion a registrar y el numero de pregunta i a registrar"""
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour("white")
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
            self.lblOpcion = wx.StaticText(self, label="Opcion Respuesta:")
            sizerit.Add(self.lblOpcion, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editOpcion[it], 0, wx.ALL|wx.CENTER, 5)
            self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editOpcion[it])
            self.lblRespuesta = wx.StaticText(self, label="Respuesta:")
            sizerit.Add(self.lblRespuesta, 0, wx.ALL|wx.CENTER, 5)
            sizerit.Add(self.editRespuesta[it], 0, wx.ALL|wx.CENTER, 5)
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
