""" 
Proyecto Python y Mysql
-Abrir asistente
-Login o regsitro
-Si elegimos login, identifica al usuriao y nos preguntará
-Crear nota, mostrar notas, borrarlas
 """
 
from usuarios import acciones
    

if __name__ == "__main__":
        
    print(""" 
    ACCIONES DISPONIBLES
        -[R]egistro
        -[L]ogin
    """)# se solicita una opción
    
    #se instancia un objeto de tipo acciones
    hazE1= acciones.Acciones()
    accion= input("¿Que quieres hacer?: ")
    accion= accion.lower()

    if accion=="r":
        #se usa la función resgistro de nuestro objeto 
        hazE1.registro()                          

    elif accion=="l":
        #se usa la función resgistro de nuestro objeto
        hazE1.login()
        
        



