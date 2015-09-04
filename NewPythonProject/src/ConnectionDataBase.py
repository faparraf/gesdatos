import psycopg2
import sys

class Connection():
    
    def __init__(self,host,dbname,user,password,port):
        conn_string = "host='"+host+"' dbname='"+dbname+"' user='"+user+"' port='"+port+"' password='"+password+"'"
        print "Connnecting to database\n ->%s"% (conn_string)
        self.conn = psycopg2.connect(conn_string)
        self.querys = self.conn.cursor()
        print "Connected!\n"

    def ExecuteQuery(self, queryString):
        self.querys.execute(queryString)
        return self.querys.fetchall()
    
    def ExecuteQueryWithoutreturn(self, queryString):
        self.querys.execute(queryString)
        self.conn.commit()               
            #print 'Error %s' % e
    
