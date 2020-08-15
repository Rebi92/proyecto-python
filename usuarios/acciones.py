import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a resgistrarte en el sistema....")

        #ingreso de datos personales
        nombre= input("¿Cual es tu nombre?: ")
        apellido= input("¿Cual es tu apellido?:")
        email= input("Introduce tu email: ")
        password= input('Introduce tu contraseña: ')

        #instanciamos un objeto de tipo usuario, y se les envian al constructor los datos
        usuario= modelo.Usuario(nombre,apellido,email, password)
        registro= usuario.registrar()

        if registro[0]>=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nno te has registrado correctamente")



    
    def login(self):
        print("\nVale!! Identificate en el sistema")
        try:
            email= input("Introduce tu email: ")
            password= input('Introduce tu contraseña: ')

            usuario= modelo.Usuario('','',email , password)
            login= usuario.identificar()
            print(login)

            #comparamos si el email introducido es el mismo de la bd
            if email == login[3]:
                print(f'\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}')
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)#sacar el nombre del error
            print(f'Login incorrecto!! intentalo mas tarde')



    """ def validarCorreo(self):
        #se validara si el correo ingresado es realmente el que el 
        #usuario desea
        email = input("Introduce el correo: ")
        con_email= input("Confirmar correo: ")
        email= email.lower() #transformar a minuscula
        con_email= con_email.lower()#transformar a minuscula

        while True:
            if email == con_email:
                print('Email correcto!!')
                email=email
                break
            else:
                print("El correo no coincide")

        return email """