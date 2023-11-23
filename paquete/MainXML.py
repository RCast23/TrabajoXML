import xml.etree.ElementTree as ET
from paquete import BaseDeDatos, GestorAlquiler, GestorVehiculo,Utiles

def submenuAlquiler(rootAlquiler):
    check=True
    checkTodos=True
    while (check):
        opcion = input("Seleccione una opcion para Alquileres:\n1.Alta\n2.Buscar\n3.Modificar\n4.Mostrar Todos\n5.Finalizar alquiler\n0.Salir")
        
        if(opcion=='1'):
            GestorAlquiler.crear(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea realizar otro alquiler?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.crear(rootAlquiler)
                BaseDeDatos.guardarArchivo(root)
                print("¿Desea realizar otro alquiler?(Si o no)")
                
        elif (opcion == '2'):
            GestorAlquiler.buscarMostrarMatriculaDni(rootAlquiler)
            
        elif(opcion=='3'):
            GestorAlquiler.modificar(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea realizar otra moificacion?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.modificar(rootAlquiler)
                BaseDeDatos.guardarArchivo(root)
                print("¿Desea realizar otra moificacion?(Si o no)")
                
        elif(opcion=='4'):
            while (checkTodos):
                #No se como lo has montado tu pero esto es lo que dice la practica, cambia lo que veas
                opcion = input("Como desea consultar Alquileres:\n1.Todos los Alquileres\n2.Alquileres por vehiculo\n3.Alquileres por DNI\n0.Salir")
                if(opcion=='1'):
                    GestorAlquiler.mostrar(rootAlquiler)
                elif (opcion == '2'):
                    GestorAlquiler.buscarMostrarTodosVehiculo(rootAlquiler)
                elif (opcion == '3'):
                    GestorAlquiler.buscarMostrarTodosDni(rootAlquiler)
                elif (opcion == '0'):
                    checkTodos=False
        elif(opcion == 5):
            #GestorAlquiler.finalizarAlquiler(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea finalizar otro alquiler?(Si o no)")
            while(Utiles.confirmacion()):
                #GestorAlquiler.finalizarAlquiler(rootAlquiler,root)
                print("¿Desea finalizar otro alquiler?(Si o no)")
        elif(opcion == '0'):
            check = False
        else:
            print("Valor no valido")
        
def submenuVehiculo(rootVehiculo):
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Vehiculos:\n1.Alta\n2.Buscar\n3.Modificar\n4.Borrar\n5.Mostrar Todos\n0.Salir")
        
        if(opcion=='1'):            
            GestorVehiculo.crear(rootVehiculo)
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea realizar otra alta?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.crear(rootVehiculo)
                BaseDeDatos.guardarArchivo(root)
                print("¿Desea realizar otra alta?(Si o no)")
                
        elif (opcion == '2'):
            Utiles.recorrer(GestorVehiculo.buscarVehiculo(rootVehiculo[0]))
            
        elif(opcion=='3'):
            GestorVehiculo.modificar(rootVehiculo)
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea realizar la modificacion de otro vehiculo?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.modificar(rootVehiculo)
                BaseDeDatos.guardarArchivo(root)
                print("¿Desea realizar la modificacion de otro vehiculo?(Si o no)")
                
        elif(opcion=='4'):
            GestorVehiculo.borrar(rootVehiculo[0])
            BaseDeDatos.guardarArchivo(root)
            print("¿Desea realizar otra baja?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.borrar(rootVehiculo[0])
                BaseDeDatos.guardarArchivo(root)
                print("¿Desea realizar otra baja?(Si o no)")
                
        elif(opcion=='5'):
            GestorVehiculo.mostrarTodos(rootVehiculo[0])
            
        elif(opcion == '0'):
            check = False
            
        else:
            print("Valor no valido")
            

#Al salir vuelve a iniciarse solo una vez, no se por que
print('Inicio del programa')
arbol = ""
root = ""
arbol,root=BaseDeDatos.comprobarArchivo(arbol,root)
BaseDeDatos.guardarArchivo(root)
check = True
while (check):
    opcion = input("Seleccione una opcion:\n1.Vehiculos\n2.Alquileres\n0.Salir")
    if(opcion=='1'):
        submenuVehiculo(root)
    elif (opcion == '2'):
        submenuAlquiler(root[1])
    elif(opcion == '0'):
        check = False
    else:
        print("Valor no valido")
print('Fin del programa')
