import psycopg2, psycopg2.extras  
#from Registro import Registro
# importar libreria psycopg2 para permitir la conexion con postgres


class Conexion:                  #Clase que permitira la comunicacion con la base de datos     
    host = "localhost"           
    user = "postgres"
    passwd = "miclave"
    db = "ExamenDB"
    
    def __init__(self):
        self.connection = psycopg2.connect( database=self.db,
                                           user= self.user,
                                           password= self.passwd,
                                           host= self.host)
        self.cur = self.connection.cursor()  #cursor

    def insertQuery(self,txtsql):                 #funcion querry para interactuar con la BD
        #print  texto
        self.cur.execute(txtsql)#"insert into persona (id_persona,nom_pers, apellido_pers,di_pers,fecha_nac,correo_universidad,uni,correo,usuario)  values  (3, 'juan','peres',25262525,'1995-01-03','dsadsa@ggs',1,'affwaf','juanito')");
        self.connection.commit()
        
        #return self.cur.fetchall()
    def selectQuery(self,txtsql):
        self.cur.execute(txtsql)        
        datos = self.cur.fetchall()    
        return datos
    
    def finalizarConexion(selfself):
        self.cur.close()
        self.connection.close()
    #def __del__(self):             #funcion para finalizar conexion OP
       # self.connection.close()    

#if __name__ == "__main__":              #ejemplo 
    #dbe = Database()   
    #print "hola"
   #nuevo =  Registro() 
#    nuevo.registrar();
    #q = "SELECT * FROM estudiante"     #sentencia sql
    #print(dbe.query(q))                 #como se llama la funcion querry
    #dbe=Registro();
    #print(dbe.registrar(juan,1,1,1,1,1))
    
    
    



