#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import cmd

class Console(cmd.Cmd):
    prompt = "> "
       
    def __init__ (self):
        'Inicia la clase'
        cmd.Cmd.__init__(self)

    def set_globvar_Query():
        'Genera una consulta'
        globvar = "S"
        return globvar 

    def do_Consulta (self, answer):
        'Realiza la consulta y retorna la respuesta'
        if answer == str(set_globvar_Query()):
            print "Consulta Correcta Procesando"
        else:
            print "Consulta Incorrecta" 
 
    def do_quit (self, exit):
        'Inica la salida de la aplicación'
        print "Adios"
        return True

    def help_quit (self):
        'Muestra ayuda'
        print "Conmandos"

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == "__main__":
    console = Console()
    try:
        console.cmdloop("Inserte la Consulta")
    except KeyboardInterrupt:
        console.do_quit(None)
