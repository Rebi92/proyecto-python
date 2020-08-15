import datetime #metodo para fechas
import hashlib #modulo para cifrar la contraseña
import usuarios.conexion as conexion


#conexión a la base de datos
connect=conexion.conectar()
database= connect[0]
cursor= connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre= nombre
        self.apellido= apellido
        self.email= email  
        self.password= password
    
    def registrar(self):
        fecha= datetime.datetime.now()

        #cifrar contraseña
        cifrado= hashlib.sha256()#instanciamos un objeto con el tipo de cifrado que vamos a usar
        cifrado.update(self.password.encode('utf8'))
        #me permite pasarle un dato para cifrarlo
        #encode transformara la variable str a bite para ser cifrada


        sql="INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"# con %s se ingresa los datos de una tupla
        usuario= (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result= [cursor.rowcount, self]

        except:
            result =[0, self]
            
        return result

    def identificar(self):
        #verificar si el usuario esta en la base de datos para logearse
        #consulta para comprobar si existe contraseña
        sql = "SELECT * FROM usuarios WHERE email= %s AND password = %s"
        #cifrar contraseña
        cifrado= hashlib.sha256()#instanciamos un objeto con el tipo de cifrado que vamos a usar
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario= (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result= cursor.fetchone()

        return result


