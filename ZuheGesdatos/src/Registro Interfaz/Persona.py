import TipoPersona   


class Persona:   
    
    __idpersona=0
    __nombre=""
    __apellido=""
    __documento=0
    __fechanacimiento=""
    __correo=""
    __correouni=""
    __usuario=""
    __universidad=""
    __pais=0
    
    
    def __init__(self):
        """Documentation"""
        self.__idpersona;
        self.__nombre;
        self.__apellido;
        self.__documento;
        self.__fechanacimiento;
        self.__correo;
        self.__correouni;
        self.__usuario;
        self.__universidad;
        self.__pais;
        
    def get__idpersona(self):
        """Documentation"""
        return self.__idpersona
    
    def set__idpersona(self,idpersona):
        """Documentation"""
        self.__idpersona=idpersona
        
    def get__nombre(self):
        """Documentation"""
        return self.__nombre
    
    def set__nombre(self,nombre):
        """Documentation"""
        self.__nombre=nombre
        
    def get__apellido(self):
        """Documentation"""
        return self.__apellido
    
    def set__apellido(self,apellido):
        """Documentation"""
        self.__apellido=apellido
        
    def get__documento(self):
        """Documentation"""
        return self.__documento
    
    def set__documento(self,documento):
        """Documentation"""
        self.__documento=documento
        
    def get__fechanacimiento(self):
        """Documentation"""
        return self.__fechanacimiento
    
    def set__fechanacimiento(self,fechanacimiento):
        """Documentation"""
        self.__fechanacimiento=fechanacimiento
        
    def get__correo(self):
        """Documentation"""
        return self.__correo
    
    def set__correo(self,correo):
        """Documentation"""
        self.__correo=correo
        
    def get__correouni(self):
        """Documentation"""
        return self.__correouni
    
    def set__correouni(self,correouni):
        """Documentation"""
        self.__correouni=correouni
        
    def get__usuario(self):
        """Documentation"""
        return self.__usuario
    
    def set__usuario(self,usuario):
        """Documentation"""
        self.__usuario=usuario
        
    def get__universidad(self):
        """Documentation"""
        return self.__universidad
    
    def set__universidad(self,universidad):
        """Documentation"""
        self.__universidad=universidad    
        
    def get__pais(self):
        """Documentation"""
        return self.__pais
    
    def set__pais(self,pais):
        """Documentation"""
        self.__pais=pais    
        
                      
    def prueba(self):
        tipo= TipoPersona.TipoPersona()
        tipo.set_IdTipoPersona(5)
        tipo.set_Tipo("alumno")
        ##tipo.idTipoPersona=6
        tipo.set_IdTipoPersona(8)
        return tipo
        #print tipo.get_IdTipoPersona()
        
    
#pers=Persona()
#t=pers.prueba()
#print t.get_IdTipoPersona()
#print t.get_Tipo()
                