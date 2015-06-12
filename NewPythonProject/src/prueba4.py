#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd
class Console(cmd.Cmd):

    prompt = "> "
    
        
    def __init__ (self):
       
        cmd.Cmd.__init__(self)

    def set_globvar_Query():
        globvar = "S"
        return globvar 

    def do_Consulta (self, answer):
        if answer == str(set_globvar_Query()):
            print "Consulta Correcta Procesando"
        else:
            print "Consulta Incorrecta" 
 
    def do_quit (self, exit):
        print "Adios"
        return True

    def help_quit (self):
        print "Conmandos"

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == "__main__":
    console = Console()
    try:
        console.cmdloop("Inserte la Consulta")
    except KeyboardInterrupt:
        console.do_quit(None)
