#!/usr/bin/env python
#coding=utf-8
import respuesta
 
class pregunta():
    """ Una clase donde se amacenara la informacion de
    una pregunta por medio de atributos """
    def __init__(self):
        'constructor de la clase'
        self.Enunciado = ""
        self.fechaCreacion = [0,0,0]
        self.tema = ""
        self.idpregunta = 0
        self.puntaje = 0
        self.respuestas = []
        self.tipoPregunta = ""
        #ingreso de variable
        self.imagen = "url"
     
    # Definimos los métodos de los eventos
     
    def registrardatosgenerales(self,Enunciado, Tema, Tipo, Url):
        'ingreso de datos de una pregunta como Enunciado, Tema y Tipo de pregunta'
        # Creamos una ventana de diálogo con un botón de ok. wx.OK es una ID estàndard de wxWidgets.
        self.Enunciado = Enunciado
        self.tema = Tema
        self.tipoPregunta = Tipo
        #ingreso de variable
        self.imagen = Url

    def registrarrespuesta(self,Opcion,Respuesta,TipoRespuesta):
        'registra respuesta como la opcion de la respuesta y el valor de la respuesta'
        nuevarespuesta = respuesta.respuesta()
        nuevarespuesta.setopcionpregunta(Opcion)
        nuevarespuesta.setrespuesta(Respuesta)
        nuevarespuesta.settipoOpcion(TipoRespuesta)
        self.respuestas.append(nuevarespuesta)

    def gettuplapreguntacrear(self):
        """retorna una tupla con el identificador de la pregunta, la fecha de creacion,
        el enunciado, la imagen, el puntaje, el tema y el tipo de pregunta"""
        return (self.idpregunta,self.fechaCreacion,self.Enunciado,
                self.imagen,self.puntaje,self.tema,self.tipoPregunta,self.imagen)
                #ingreso de variable
