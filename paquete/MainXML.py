import xml.etree.ElementTree as ET
from paquete import BaseDeDatos, GestorAlquiler, GestorVehiculo,Utiles

def submenuAlquiler(root):
    check=True
    checkTodos=True
    while (check):
        opcion = input("Seleccione una opcion para Alquileres:\n1.Alta\n2.Buscar\n3.Modificar\n4.Mostrar Todos\n0.Salir")
        if(opcion=='1'):
            GestorAlquiler.crear(root)
            print("¿Desea realizar otra alta?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.crear(root)
        elif (opcion == '2'):
            GestorAlquiler.buscarMostrar(root)
        elif(opcion=='3'):
            GestorAlquiler.modificar(root)
            print("¿Desea realizar otra alta?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.modificar(root)
        elif(opcion=='4'):
            while (checkTodos):
                #No se como lo has montado tu pero esto es lo que dice la practica, cambia lo que veas
                opcion = input("Como desea consultar Alquileres:\n1.Todos los Alquileres\n2.Alquileres por vehiculo\n3.Alquileres por DNI\n0.Salir")
                if(opcion=='1'):
                    GestorAlquiler.mostrar(root)
                elif (opcion == '2'):
                    GestorAlquiler.buscarMostrarTodosVehiculo(root)
                elif (opcion == '3'):
                    GestorAlquiler.buscarMostrarTodosDni(root)
                elif (opcion == '0'):
                    checkTodos=False
        elif(opcion == '0'):
            check = False
        else:
            print("Valor no valido")
        
def submenuVehiculo(root):
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Vehiculos:\n1.Alta\n2.Buscar\n3.Modificar\n4.Borrar\n5.Mostrar Todos\n0.Salir")
        if(opcion=='1'):            
            GestorVehiculo.crear(root)
            print("¿Desea realizar otra alta?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.crear(root)
        elif (opcion == '2'):
            GestorVehiculo.buscar(root)
        elif(opcion=='3'):
            GestorVehiculo.modificar(root)
            print("¿Desea realizar otra modificacion?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.modificar(root)
        elif(opcion=='4'):
            GestorVehiculo.borrar(root)
            print("¿Desea realizar otra baja?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.borrar(root)
        elif(opcion=='5'):
            GestorVehiculo.mostrarTodos(root)
        elif(opcion == '0'):
            check = False
        else:
            print("Valor no valido")
    
print('Inicio del programa')
arbol = ""
root = ""
arbol,root=BaseDeDatos.comprobarArchivo(arbol,root)
check = True
while (check):
    opcion = input("Seleccione una opcion:\n1.Vehiculos\n2.Alquileres\n0.Salir")
    if(opcion=='1'):
        submenuVehiculo(root[0])
    elif (opcion == '2'):
        submenuAlquiler(root[1])
    elif(opcion == '0'):
        BaseDeDatos.guardarArchivo(root)
        check = False
    else:
        print("Valor no valido")
print('Fin del programa')
