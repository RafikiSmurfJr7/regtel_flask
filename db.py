import mysql.connector

class DataBaseConnection:
    
    def __init__(self, username,password,host,database):
        self.cnx = self.connect(username,password,host,database)


    def connect(self,username,password,host,database):
        
        try:
            self.cnx = mysql.connector.connect(user=username,password=password,host=host,database=database)
            return self.cnx
        
        except mysql.connector.Error as err:
            print("Error")


    def getData(self, query):
        cursor = self.cnx.cursor()
        
        cursor.execute(query)
        
        return cursor.fetchall()

    def insertData(self):
        cursor = self.cnx

    def close(self):
        
        self.cnx.close()



