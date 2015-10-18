import TipoPersona   


class Persona:   
    
    
    def __init__(self):
        """Documentation"""
        
    def prueba(self):
        tipo= TipoPersona.TipoPersona()
        tipo.set_IdTipoPersona(5)
        tipo.set_Tipo("alumno")
        ##tipo.idTipoPersona=6
        tipo.set_IdTipoPersona(8)
        return tipo
        #print tipo.get_IdTipoPersona()
        
    
pers=Persona()
t=pers.prueba()
print t.get_IdTipoPersona()
print t.get_Tipo()
                