#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Romero, Jhoan Villa"
__date__ = "$20-jul-2015 18:52:55$"
import wx, os, examen, interfazregistrarpregunta, ConnSchema,ConnectionDataBase, dialogoregistroEstudiantes
import wx
import wx.lib.scrolledpanel as scrolled
import HeadLow
import Componentes



## Body
##-----------------------------------------------------------el):
class Body(wx.Panel):
    """ Una clase personalizada de frame donde el usuario que desee registrar un nuevo examen
        podra ingresar datos como el nombre del examen, la fecha del examen,
        el puntaje extra del examen, el tipo del examen y la cantidad de preguntas que este tendra."""
    def __init__(self, parent, manipulador, iddocente):
        'contructor requiere de parent como inrfaz contenedor y manipulador como clase que accedera a la informacion'
        wx.Panel.__init__(self,parent) # Inicializaci�n Panel Padre
        self.SetBackgroundColour("white")
        self.father = manipulador
        self.quote = wx.StaticText(self, label="Docente: "+iddocente, pos=(140, 10))
        self.aparte = wx.StaticText(self, label="", pos=(140, 10))
        #self.CreateStatusBar()

        # parametros basicos generales del registro de un examen
        self.lblname = wx.StaticText(self, label="Nombre Examen :", pos=(100,35))
        self.editname = wx.TextCtrl(self, value="", pos=(0, 35), size=(140,-1))
        self.lblfecha = wx.StaticText(self, label="Fecha Examen :", pos=(100,65))
        self.editfecha = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.lblhoraini = wx.StaticText(self, label="Hora Inicio :", pos=(100,65))
        self.edithoraini = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.lblhorafin = wx.StaticText(self, label="Hora Fin :", pos=(100,65))
        self.edithorafin = wx.TextCtrl(self, value="", pos=(0, 65), size=(140,-1))
        self.lblpuntjae = wx.StaticText(self, label="Puntaje Extra Examen :", pos=(100,95))
        self.editpuntjae = wx.TextCtrl(self, value="", pos=(0, 95), size=(140,-1))
        self.lbltipo = wx.StaticText(self, label="Tipo Examen :", pos=(100,120))
        self.sampleListTipo = []
        query ="SELECT * FROM tipoexamen;"    
        self.temaescogido = ''#se almacenara el identificador del tema escogido
        self.opcionesexamenTema = (self.father.getconexion()).ExecuteQuery(query) #consulta de todos los tipos de examen
        print("consutla sql de tipos de examen "+str(self.opcionesexamenTema))
        for a in self.opcionesexamenTema:
            self.sampleListTipo.append(a[1])
        self.edittipo = wx.ComboBox(self, choices=self.sampleListTipo, style=wx.CB_DROPDOWN)
        self.edittipo.Bind(wx.EVT_COMBOBOX, self.idtemaescogido)
        #self.edittipo = wx.TextCtrl(self, value="", pos=(0, 120), size=(140,-1))
        self.lblcantidad = wx.StaticText(self, label="Cantidad de Preguntas :", pos=(100,150))
        self.editcantidad = wx.TextCtrl(self, value="1", pos=(0, 150), size=(140,-1))
        
        #como crear un boton agregando su evento
        self.button =wx.Button(self, wx.ID_OK, label="Siguiente", pos=(50, 170))
        self.Bind(wx.EVT_BUTTON, self.registro,self.button)
        gs = wx.GridSizer(9, 2, 5, 5) #Creacion grilla de tamaño
        #--------------Adición de Paneles a la Grilla, esta grilla permite que los paneles se ajuste al tamaño de la pantalla
        gs.AddMany([(self.quote, 0, wx.ALIGN_CENTER),(self.aparte, 0, wx.ALIGN_CENTER),
                    (self.lblname, 0, wx.ALIGN_CENTER),(self.editname, 0, wx.ALIGN_CENTER),
                    (self.lblfecha, 0, wx.ALIGN_CENTER),(self.editfecha, 0, wx.ALIGN_CENTER),
                    (self.lblhoraini, 0, wx.ALIGN_CENTER),(self.edithoraini, 0, wx.ALIGN_CENTER),
                    (self.lblhorafin, 0, wx.ALIGN_CENTER),(self.edithorafin, 0, wx.ALIGN_CENTER),
                    (self.lblpuntjae, 0, wx.ALIGN_CENTER),(self.editpuntjae, 0, wx.ALIGN_CENTER),
                    (self.lbltipo, 0, wx.ALIGN_CENTER),(self.edittipo, 0, wx.ALIGN_CENTER),
                    (self.lblcantidad, 0, wx.ALIGN_CENTER),(self.editcantidad, 0, wx.ALIGN_CENTER),
                    (self.button, 0, wx.ALIGN_CENTER)])
        sizer = wx.BoxSizer(wx.VERTICAL) #Adición de la grilla de tamaños al panel padre
        sizer.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
    
    def registro(self, e):
        'metodo que atendera el boton siguiente y registrara la informacion ingresada por el docente'
        # Definimos los m�todos de los eventos
        self.father.registrarExamen(e,self)
    
    def idtemaescogido(self,e):
        'metodo escucha de evento de escoger un tema con fin de saber  el valor de la llave del tema escogido'
        temaexamen = e.GetString()
        fila = 0
        for it in self.sampleListTipo:
            if it == temaexamen:
                self.temaescogido = self.opcionesexamenTema[fila][0]
                break
            fila=fila+1

##-----------------------------------------------------------


class interfazpanelpaso():
        """ Interfaz general utilizado para llamar a los paneles
        con el fin de que con cada panel el usuario pueda
        registrar datos generales del examen a registrar, los estudiantes
        que han de tener que presentar el mismo, las preguntas y las
        respuestas que conforman la evaluacion.

        cada vez que el usuario (en este caso el docente) pase de un paso
        como por ejemplo de registrar los estudiantes que practicaran el
        examen a registrar las preguntas que conformaran el mismo es necesario
        cambiar el panel del interfaz para mantenerse en la estructura Body
        ubicado entre Head y Low."""
        def __init__(self, parent,iddocente,topPanel,sizertopPanel):
            """ Metodo usado para iniciar el registro de un nuevo examen
            en sus parametros generales se encuentra el interfaz parent causante
            del llamado de esta clase para reguistrar un nuevo examen, se requere
            de iddocente que guardara el identificador del docente que hizo la peticion
            de un nuevo examen, topPanel usado para el almacenamiento de los objetos
            graficos guardandolos gentro de un panel con barra de desplazamiento, sizertopPanel
            usado como un objeto de wxPython para organizar los elementos que contengan
            los paneles."""
            self.father = parent
            self.topanel = topPanel
            self.sizer = sizertopPanel
            self.nuevoexamen = examen.examen(str(iddocente))
            self.conectordatabase = ConnectionDataBase.Connection("localhost","examen","adminexamen","pasexamen","5434")#se rquerie de datos para conexion a motor
            self.conexion = ConnSchema.ConnSchema(self.conectordatabase)
            #self.Bind(wx.EVT_BUTTON, self.registrarExamen,self.button)
        def registrarExamen(self,e,panel):
            """ Utilizado para extraer la informaci�n del panel de registro general
            de datos generales de un nuevo examen para almacenarlos en la clase nuevoexamen
            requiere de el evento del boton que llamo a este metodo y el panel en donde se encuentra el boton"""
            # Creamos una ventana de di�logo con un bot�n de ok. wx.OK es una ID est�ndard de wxWidgets.
            print ("registrando 1 paso")
            nombre = panel.editname.GetValue()
            fecha = panel.editfecha.GetValue()
            puntaje = panel.editpuntjae.GetValue()
            tipo = str(panel.temaescogido)
            horaini = panel.edithoraini.GetValue()
            horafin = panel.edithorafin.GetValue()
            cantidadpreguntas = panel.editcantidad.GetValue()
            self.nuevoexamen.settitulo(nombre)
            self.nuevoexamen.setfechaexamen(fecha)
            self.nuevoexamen.setpuntajeExtra(puntaje)
            self.nuevoexamen.settipoExamen(tipo)
            self.nuevoexamen.sethoraini(horaini)
            self.nuevoexamen.sethorafin(horafin)
            print ("hola "+nombre+" "+fecha+" "+puntaje+" "+tipo)
            #self.registrarEstudiantes(cantidadpreguntas)
            #registrar estudiante
            conexion = self.conexion
            dlg = dialogoregistroEstudiantes.dialogoregistroEstudiantes(conexion,self.topanel,self,cantidadpreguntas)
            self.cambiarpanel(dlg)
        
        def registrarexamenbasedatos(self):
            """Parte final de registro de examen, subirlo a la base de datos una vez
            se hallan ingresado todos los datos"""
            #registro de generalidades del examen
            queryidexamen = "select count(*) from examen;"
            idexamen = self.conexion.connection.ExecuteQuery(queryidexamen)
            idexamen = (idexamen[0][0])+1
            insert = 'INSERT INTO examen ("id_exa","id_dcnte","titulo_exa","fecha","tipoexa","tiempo_exa_inicio","tiempo_exa_fin")VALUES ('
            insert +=str(idexamen)+","+self.nuevoexamen.docente+",'"+self.nuevoexamen.titulo
            insert +="','"+self.nuevoexamen.fechaexamen+"',"+self.nuevoexamen.tipoExamen
            insert +=",'"+str(self.nuevoexamen.horainicio)+"','"+str(self.nuevoexamen.horafin)+"');"
            print(insert)
            self.conexion.connection.ExecuteQuery(insert)
            #registro de preguntas y opciones de preguntas
            queryidpregunta = "select count(*) from pregunta;"
            idpregunta = self.conexion.connection.ExecuteQuery(queryidpregunta)
            idpregunta = (idpregunta[0][0])
            queryidrespuesta = "select count(*) from opcionpreg;"
            idrespuesta = self.conexion.connection.ExecuteQuery(queryidrespuesta)
            idrespuesta = (idrespuesta[0][0])
            for pregunta in self.nuevoexamen.preguntas:
                idpregunta = idpregunta+1
                if (pregunta.imagen!='...'):
                    insertpregunta = 'INSERT INTO pregunta ("tipopre","fecha_cre","enunciado","imagen","tema","id_pregunta")'
                    insertpregunta += "VALUES ("+str(pregunta.tipoPregunta)+",'"+str(pregunta.fechaCreacion)+"','"+str(pregunta.Enunciado)
                    insertpregunta += "',lo_import('"+str(pregunta.imagen)+"'),"+str(pregunta.tema)+",'"+str(idpregunta)+"');"
                else:
                    insertpregunta = 'INSERT INTO pregunta ("tipopre","fecha_cre","enunciado","tema","id_pregunta")'
                    insertpregunta += "VALUES ("+str(pregunta.tipoPregunta)+",'"+str(pregunta.fechaCreacion)+"','"+str(pregunta.Enunciado)
                    insertpregunta += "',"+str(pregunta.tema)+",'"+str(idpregunta)+"');"
                self.conexion.connection.ExecuteQuery(insertpregunta)
                print (insertpregunta)
                for respuesta in pregunta.respuestas:
                    idrespuesta = idrespuesta+1
                    insertrespuesta = 'INSERT INTO opcionpreg ("id_opc_pre","tipo_op","id_pregunta","desc_opcion","respuesta")'
                    insertrespuesta += "VALUES ('"+str(idrespuesta)+"',"+str(respuesta.tipoOpcion)+","+str(idpregunta)+",'"+respuesta.opcionpregunta+"','"+respuesta.respuesta+"');"
                    print (insertrespuesta)
                    self.conexion.connection.ExecuteQuery(insertrespuesta)
                #union entre el examen y las preguntas
                insertexapreg = 'INSERT INTO examenpreg ("id_prgnta","puntaje_preg","id_examen")'
                insertexapreg += "VALUES ("+str(idrespuesta)+","+str(pregunta.puntaje)+","+str(idexamen)+");"
                print (insertexapreg)
                self.conexion.connection.ExecuteQuery(insertexapreg)
        
        def generarpanelespreguntas(self,opcionespreguntas,it):
            """ usado para cada una de las preguntas que el examen
                necesita, opcionespreguntas es la lista  de los tipos de preguntas
                que la base de datos entrega, it es  el numero de pregunta a registrar"""
            if ( int(self.cantidadpreguntas)>it):
                self.nuevoexamen.registrarPregunta()
                dlg = interfazregistrarpregunta.dialogoregistropregunta(self.topanel,self,i=it,opcionespreguntas=opcionespreguntas)
                self.cambiarpanel(dlg)
            else:
                self.registrarexamenbasedatos()
                termino = wx.Panel(self.topanel)
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(wx.StaticText(termino, label="Registro Termino Exitosamente"))
                termino.SetSizer(sizer)
                self.cambiarpanel(termino)
        
        def registrarpreguntas(self,panel,e,i):
            """ Utilizado para extraer la informaci�n del panel de registro de preguntas
            para almacenarlos en la clase nuevoexamen requiere del panel donde se ingreso la informacion,
            el evento e del boton que llamo a este metodo y el numero de pregunta registrada"""
            #self.quote = wx.StaticText(self, label=dlg.comboBox1.GetValue(), pos=(20, 30))
            Enunciado = panel.editEnunciado.GetValue()
            Tema = str(panel.temaescogido)
            Tipo = panel.editTipo.GetValue()
            #ingreso de variable
            Imagen = panel.lblImagenRu.GetLabel()
            print ("hola "+Enunciado+" "+Tema+" "+Tipo+" "+Imagen)
            self.tiporespuestaelegido = ''
            for tiposbasedatos in self.opcionespreguntas:
                if tiposbasedatos[1] == Tipo:
                    self.tiporespuestaelegido = tiposbasedatos[0] 
                    #ingreso de variable
            self.nuevoexamen.ingresardatosesmaen(i,Enunciado, Tema, self.tiporespuestaelegido,Imagen)
            self.generarpanelrespuesta(Tipo,i)
                
        def generarpanelrespuesta(self,Tipo,i):
            """ Metodo utilizado para llamar al interfaz de registro de la respuesta
            a cada pregunta registrada, requiere de el tipodepregunta que fue registrada "tipo",
            y el numero de pregunta que se esta registrando"""
            sirespeusta = False;
            opcionespreguntas = self.opcionespreguntas
            print("tipo de respuesta elegido "+Tipo+" , "+str(opcionespreguntas))
            if Tipo == opcionespreguntas[0][1]:#Opcion multiple unica respuesta
                print("elegido respuesta falso verdadero")
                sirespeusta = True
                dlgres = interfazregistrarpregunta.dialogoregistrorespuestafalseoverdadero(self.topanel,self,i)
            elif Tipo == opcionespreguntas[1][1]:#falso verdadero
                print("elegido Opcion multiple multiple respuesta")
                sirespeusta = True
                dlgres = interfazregistrarpregunta.dialogoregistrorespuestaopcionmultiplemultiple(self.topanel,self,i)
            elif Tipo == opcionespreguntas[2][1]:#Opcion multiple multiple respuesta
                print("elegido Opcion multiple unica respuesta")
                sirespeusta = True
                dlgres = interfazregistrarpregunta.dialogoregistrorespuestaopcionmultipleunico(self.topanel,self,i)
            if sirespeusta:
                self.cambiarpanel(dlgres)
            else:
                self.generarpanelespreguntas(self.opcionespreguntas,i+1)

        def registrarrespuesta(self,e,panel,i):
            """ Utilizado para extraer la informaci�n del panel de registro de respuesta
            para almacenarlos en la clase nuevoexamen requiere del evento e del boton que llamo a este metodo,
            el panel donde se ingreso la informacion y el numero de respuesta registrada"""
            #self.quote = wx.StaticText(self, label=dlg.comboBox1.GetValue(), pos=(20, 30))
            for it in range(panel.cantidadropciones):
                Opcion = panel.editOpcion[it].GetValue()
                Respuesta = panel.editRespuesta[it].GetValue()
                print ("hola "+Opcion+" "+Respuesta)
                self.nuevoexamen.registrarrespuesta(i,Opcion, Respuesta,self.tiporespuestaelegido)
            self.generarpanelespreguntas(self.opcionespreguntas,i+1)

        def registrarEstudiantes(self,e,panel,cantidadpreguntas):
            """ Utilizado para extraer la informaci�n del panel de registrar estudiantes
            para almacenarlos en la clase nuevoexamen requiere del evento e del boton que llamo a este metodo,
            el panel donde se ingreso la informacion y la cantidad de preguntas del examen"""
            #self.quote = wx.StaticText(self, label=dlg.comboBox1.GetValue(), pos=(20, 30))
            EstudiantesAsignados = panel.estudiantesescogidos
            self.nuevoexamen.setidestudiantes(EstudiantesAsignados)
            print("valor "+str(EstudiantesAsignados) ) 
            query ="SELECT * FROM tipopegrunta;"            
            self.opcionespreguntas = self.conexion.connection.ExecuteQuery(query) #comentado mienstras no este creada la base ded datos
            #opcionespreguntas = [(1,"PreguntaAbierta"),(2,"Falso Verdadero"),(3,"Opcion Multiple Unica Respuesta"),(4,"Opcion Multiple Multiple Respuesta")]
            self.cantidadpreguntas = cantidadpreguntas
            self.generarpanelespreguntas(self.opcionespreguntas,0)
            
        def getconexion(self):
            """consutlor que retorna la clase administradora de la base de datos"""
            return self.conexion.connection

        def cambiarpanel(self,nuevopanel):
            """Metodo usado para cambiar un panel en el que ya se
             registr� la informacion para el nuevo examen y se requiere
             que el siguiente paso en el registro de un nuevo examen se muestre
             requiere como parametro el nuevo panel "nuevopanel" en el que se va a
             reemplazar el ya utlizado"""
            #siempre se cambia en la poscion 2 ya que es la del body
            sizer = self.sizer
            sizer.Hide(0)
            sizer.Remove(0)
            sizer.Hide(0)
            sizer.Remove(0)
            sizer.Hide(0)
            sizer.Remove(0)
            sizer.Add(HeadLow.Head(self.topanel),0,wx.EXPAND|wx.ALL,border=10)
            sizer.Add(nuevopanel,0,wx.EXPAND|wx.ALL,border=10)
            sizer.Add(HeadLow.Low(self.topanel),0,wx.EXPAND|wx.ALL,border=10)
            self.topanel.SetSizer(self.sizer)
            self.father.SetSizer(sizer)
            self.father.GetSizer().Layout()
            self.father.Fit()
            


app=wx.App(False)
displaySize= wx.DisplaySize()
frame = wx.Frame(None, wx.ID_ANY, 'Full display size', pos=(0, 0), size=(displaySize[0], displaySize[1]))
menubar = wx.MenuBar()
topPanel= scrolled.ScrolledPanel(frame)
topPanel.SetupScrolling(scroll_y=True)
topPanel.SetBackgroundColour("white")
sizertopPanel=wx.BoxSizer(wx.VERTICAL)
iddocente = "1"
interfaz = interfazpanelpaso(frame,iddocente,topPanel,sizertopPanel)
sizertopPanel.Add(HeadLow.Head(topPanel),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(Body(topPanel,interfaz,iddocente),0,wx.EXPAND|wx.ALL,border=10)
sizertopPanel.Add(HeadLow.Low(topPanel),0,wx.EXPAND|wx.ALL,border=10)
topPanel.SetSizer(sizertopPanel)
frame.Show()
app.MainLoop()

