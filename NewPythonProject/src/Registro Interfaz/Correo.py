import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Correo: 
    __username = '_____@hotmail.com' #poner correo que enviara el email
    __password ='______'            #password del correo
    __server= smtplib.SMTP('smtp.live.com')
    
    def __init__(self):
        self.__username
        self.__password
        self.__server
        
    def enviar(self,destino, text,asunto):            
        msg = MIMEMultipart()
        msg['From'] =self.__username
        msg['To'] = destino
        msg['Subject'] = asunto
        msg['body']=text
        msg.attach(MIMEText(text))       
        self.__server.ehlo()
        self.__server.starttls()
        self.__server.ehlo()
        self.__server.login(self.__username,self.__password)
        self.__server.sendmail(self.__username,destino,msg.as_string())
        self.__server.quit()

#ejemplo para envio
#destino = _____@____.com'
#text = 'email from python'
#m= Correo()
#m.enviar(destino,text,'prueba')