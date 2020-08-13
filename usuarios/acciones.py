class Acciones:

    def registro(self):
        print("\nOk!! Vamos a resgistrarte en el sistema....")

        self.nombre= input("¿Cual es tu nombre?: ")
        self.apellido= input("¿Cual es tu apellido?:")
        self.email= input("Introduce tu email: ")
        self.password= input('Introduce tu contraseña: ')
    
    def login(self):
        print("\nVale!! Identificate en el sistema")
        self.email= input("Introduce tu email: ")
        self.password= input('Introduce tu contraseña: ')
        

    def validarCorreo(self):
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

        return email