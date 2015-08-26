#!/usr/bin/env python
#coding=utf-8
import pregunta
 
class examen():
    """ Una clase donde se amacenara la informacion de
    un examen por medio de atributos """
    def __init__(self,iddocente):
        'constructor de la clase, requiere de iddocente como identificador del docente'
        print("en docencia con nuevo examen")
        self.docente = iddocente
        self.fechaexamen = [0,0,0]
        self.horainicio = ""
        self.horafin = ""
        self.idestudiantes = []
        self.fechaPresEstu = []
        self.puntajeEstu = []
        self.idexamen = 0
        self.preguntas = []
        self.puntajeExtra = 0
        self.tipoExamen = 0
        self.titulo = ""
        
    # Definimos los métodos de los eventos
     
    def settitulo(self,nuevotitulo):
        'cambia titulo de examen con valor de nuevotitulo'
        self.titulo = nuevotitulo
    
    def sethoraini(self,nuevahoraini):
        'cambia la hora de inicio con valor de nuevahoraini'
        self.horainicio = nuevahoraini
        
    def sethorafin(self,nuevahorafin):
        'cambia la hora de fin con valor de nuevahorafin'
        self.horafin = nuevahorafin
    
    def settipoExamen(self,tipoExamen):
        'cambia tipo de examen con valor de tipoExamen'
        self.tipoExamen = tipoExamen

    def setpuntajeExtra(self,puntajeExtra):
        'cambia puntaje extra de examen con valor de puntajeExtra'
        self.puntajeExtra = puntajeExtra

    def setfechaexamen(self,fechaexamen):
        'cambia fecha de examen con valor de fechaexamen'
        self.fechaexamen = fechaexamen

    def setidestudiantes(self,idestudiantes):
        'cambia los estudiates registrados con valor de idestudiantes'
        self.idestudiantes = idestudiantes

    def setfechaPresEstu(self,fechas):
        'cambia las fechasa presentar examen por parte de estudiante con valor de fechas'
        self.fechaPresEstu = fechas

    def registrarPregunta(self):
        'agrega una nueva pregunta al examen con una nueva clase pregunta'
        nuevoexamen = pregunta.pregunta()
        self.preguntas.append(nuevoexamen)

    def ingresardatosesmaen(self,posicion,Enunciado, Tema, Tipo,Imagen):
        'agrega informacion de una pregunta del examen de numero posicion'
        self.preguntas[posicion].registrardatosgenerales(Enunciado, Tema, Tipo,Imagen)

    def registrarrespuesta (self,i,Opcion, Respuesta,TipoOpcion):
        'agrega informacion de una pregunta del examen de numero i'
        self.preguntas[i].registrarrespuesta(Opcion, Respuesta,TipoOpcion)

    def getidEstudi(self,it):
        'retorna identificador de estudiante de posicion it en la lista'
        return self.idestudiantes[it]

    def getFechaPreEstudi(self,it):
        'retorna fecha de presentar de un extudiante de posicion it'
        return self.fechaPresEstu[it]

    def getpuntajePreEstudi(self,it):
        'retorna putnaje de estudiante de posicion it'
        return self.puntajeEstu[it]

    def gettuplapreguntacrear(self,it):
        'retorna tupla de cada pregunta conteniendo toda la informacion de la pregunta'
        return self.preguntas[it].gettuplapreguntacrear()
