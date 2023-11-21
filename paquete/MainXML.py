import xml.etree.ElementTree as ET
from paquete import BaseDeDatos, GestorAlquiler, GestorVehiculo

def submenuAlquiler(root):
    while (check):
        opcion = input("Seleccione una opcion para Alquileres:\n1.Alta\n2.Buscar\n3.Modificar\n4.Mostrar Todos\n0.Salir")
        if(opcion=='1'):
            GestorAlquiler.crear(root)
        elif (opcion == '2'):
            GestorAlquiler.buscar(root)
        elif(opcion=='3'):
            GestorAlquiler.modificar(root)
        elif(opcion=='4'):
            while (check):
                #No se como lo has montado tu pero esto es lo que dice la practica, cambia lo que veas
                opcion = input("Como desea consultar Alquileres:\n1.Todos los Alquileres\n2.Alquileres por vehiculo\n3.Alquileres por DNI\n0.Salir")
                if(opcion=='1'):
                    GestorAlquiler.mostrar(root)
                elif (opcion == '2'):
                    GestorAlquiler.buscarMostrarTodosVehiculo(root)
                elif (opcion == '3'):
                    GestorAlquiler.buscarMostrarTodosDni(root)
                elif (opcion == '0'):
                    check=False
        elif(opcion == '0'):
            check = False
        else:
            print("Valor no valido")
        
def submenuVehiculo(root):
    while (check):
        opcion = input("Seleccione una opcion para Vehiculos:\n1.Alta\n2.Buscar\n3.Modificar\n4.Mostrar Todos\n0.Salir")
        if(opcion=='1'):
            GestorAlquiler.crear(root)
        elif (opcion == '2'):
            GestorAlquiler.buscar(root)
        elif(opcion=='3'):
            GestorAlquiler.modificar(root)
        elif(opcion=='4'):
            GestorAlquiler.mostrar(root)
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
        submenuVehiculo(root)
    elif (opcion == '2'):
        submenuAlquiler(root)
    elif(opcion == '0'):
        BaseDeDatos.guardarArchivo(root)
        check = False
    else:
        print("Valor no valido")
print('Fin del programa')
