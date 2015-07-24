# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Conexion import Conexion

class Request():    
    #conn= Conexion()
    def __init__(self):  
        self.conn= Conexion()
           
    def registrarPersona (self,nombre,apellido,documento,fechaNac,correo,correoUni,universidad,usuario,categoria):
        personaid= int("%s" %(self.conn.selectQuery("select count(*) from persona")[0]))+1
        universidadid=int("%s" %(self.conn.selectQuery("select id_uni from universidad where nom_uni ='"+universidad+"'")[0]))
        if categoria == 0:   
            datos=(personaid,nombre,apellido,documento,fechaNac,correo,correoUni,universidadid,usuario)
            txtsql= "insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo,correo_universidad,uni,usuario) values (%s, '%s', '%s', %s, '%s', '%s', '%s', %s, '%s' )" %datos
            self.conn.insertQuery(txtsql)
        
        
        
        
                
            
            #print int("%s" %(self.conn.selectQuery("select count(*) from persona")[0]))+1
        
        #datos=(nombre,apellido,documento,fechaNac,telefono,correo,correoUni,universidad,usuario)
        #sql="insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo_universidad,uni,correo,usuario) values"
        #nuevo = Conexion()
        #self.conn.insertQuery(txtsql)
       # print "'%s', '%s', %s, %s, '%s', %s, %s, %s, %s, %s" %datos
        
    def verUniversidad(self):
        lista= self.conn.selectQuery("select id_uni,nom_uni from universidad")
        uni=[]
        for row in lista:
            uni.append( "%s " % row[1])            
        return uni        
        #nuevo = Conexion()
        #print(self.conn.selectQuery(txtsql))
        
if __name__ == "__main__":              #ejemplo 
   # dbe = Database()   
   nuevos = Request()
   #nuevos.registrar("insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo_universidad,uni,correo,usuario)  values  (7, 'jmari','peres',25262525,'1995-01-03','dsadsa@ggs',1,'affwaf','juanito')")
   #print nuevos.verUniversidad()
   nuevos.registrarPersona ('nombre','apellido','documento','fechaNac','correo','correoUni','Universidad Distrital         ','usuario',0)