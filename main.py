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
    """)
    
    hazE1= acciones.Acciones()
    accion= input("¿Que quieres hacer?: ")
    accion= accion.lower()

    if accion=="r":
        hazE1.registro()                          

    elif accion=="l":
        hazE1.login()
        
        



