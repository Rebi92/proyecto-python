import mysql.connector
import datetime #metodo para fechas

#conexión a la base de datos
database= mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "",
    database= "master_python",
    port= 3306
)

cursor= database.cursor(buffered= True)


print(database)

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre= nombre
        self.apellido= apellido
        self.email= email
        self.password= password
    
    def registrar(self):
        fecha= datetime.datetime.now()
        sql="INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"# con %s se ingresa los datos de una tupla
        usuario= (self.nombre, self.apellido, self.email, self.password, fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result= [cursor.rowcount, self]

        except:
            result =[0, self]
            
        return result

    def identificar(self):
        return self.nombre

