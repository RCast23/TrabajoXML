import BaseDeDatos, GestorAlquiler, GestorVehiculo, Utiles

def submenuAlquiler(rootAlquiler):
    '''
    Menu para seleccionar las opciones disponibles para alquileres
    :param rootAlquiler: Elemento del arbol XML que contiene todos los alquileres
    '''
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("\nSeleccione una opcion para Alquileres:\n1.Alta\n2.Buscar\n3.Modificar\n4.Mostrar Todos\n5.Finalizar alquiler\n0.Salir")
        
        #Opcion para crear un nuevo alquiler
        if(opcion=='1'):
            GestorAlquiler.crear(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otro alta
            print("\n¿Desea realizar otro alquiler?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.crear(rootAlquiler,root)
                BaseDeDatos.guardarArchivo(root)
                print("\n¿Desea realizar otro alquiler?(Si o no)")
                
        #Opcion para buscar un alquiler
        elif (opcion == '2'):
            GestorAlquiler.buscarMostrarMatriculaDni(rootAlquiler)
            
        #Opcion para modificar un alquiler
        elif(opcion=='3'):
            GestorAlquiler.modificar(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otra modificacion
            print("\n¿Desea realizar la modificacion de otro alquiler?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.modificar(rootAlquiler,root)
                BaseDeDatos.guardarArchivo(root)
                print("\n¿Desea realizar la modificacion de otro alquiler?(Si o no)")
        
        #Opcion para mostrar todos los alquileres en general o con restriccion por DNI o Matricula
        elif(opcion=='4'):
            #Variable para el bucle que ofrece las opciones de mostrar todos
            checkTodos=True
            while (checkTodos):
                opcion = input("\nComo desea consultar Alquileres:\n1.Todos los Alquileres\n2.Alquileres por vehiculo\n3.Alquileres por DNI\n0.Salir")
                if(opcion=='1'):
                    GestorAlquiler.mostrar(rootAlquiler)
                elif (opcion == '2'):
                    GestorAlquiler.buscarMostrarTodosVehiculo(rootAlquiler)
                elif (opcion == '3'):
                    GestorAlquiler.buscarMostrarTodosDni(rootAlquiler)
                elif (opcion == '0'):
                    checkTodos=False
                    
        #Opcion para finalizar un alquiler
        elif(opcion == '5'):
            GestorAlquiler.finalizarAlquiler(rootAlquiler,root)
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otra finalizacion
            print("\n¿Desea finalizar otro alquiler?(Si o no)")
            while(Utiles.confirmacion()):
                GestorAlquiler.finalizarAlquiler(rootAlquiler,root)
                print("\n¿Desea finalizar otro alquiler?(Si o no)")
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("\nValor no valido")
    
        
def submenuVehiculo(root):
    '''
    Menu para seleccionar las opciones disponibles para vehiculos
    :param root: Elemento raiz del documento XML
    '''
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("\nSeleccione una opcion para Vehiculos:\n1.Alta\n2.Buscar\n3.Modificar\n4.Borrar\n5.Mostrar Todos\n0.Salir")
        
        #Opcion para crear un nuevo vehiculo
        if(opcion=='1'):            
            GestorVehiculo.crear(root)
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otro alta
            print("\n¿Desea realizar otra alta?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.crear(root)
                BaseDeDatos.guardarArchivo(root)
                print("\n¿Desea realizar otra alta?(Si o no)")
                
        #Opcion para buscar un vehiculo
        elif (opcion == '2'):
            vehiculo = GestorVehiculo.buscarVehiculo(root[0])
            if(vehiculo!=None):
                Utiles.recorrer()
            
            
        #Opcion para modificar un vehiculo
        elif(opcion=='3'):
            GestorVehiculo.modificar(root)
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otra modificacion
            print("\n¿Desea realizar la modificacion de otro vehiculo?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.modificar(root)
                BaseDeDatos.guardarArchivo(root)
                print("\n¿Desea realizar la modificacion de otro vehiculo?(Si o no)")
        
        #Opcion para borrar un vehiculo        
        elif(opcion=='4'):
            GestorVehiculo.borrar(root[0])
            BaseDeDatos.guardarArchivo(root)
            #Se comprueba en con el metodo confirmacion si se quiere hacer otra baja
            print("\n¿Desea realizar otra baja?(Si o no)")
            while(Utiles.confirmacion()):
                GestorVehiculo.borrar(root[0])
                BaseDeDatos.guardarArchivo(root)
                print("\n¿Desea realizar otra baja?(Si o no)")
                
        #Opcion para mostrar todos los vehiculos  
        elif(opcion=='5'):
            GestorVehiculo.mostrarTodos(root[0])
            
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
            
        else:
            print("\nValor no valido")
            

print('Inicio del programa')
#Se crean variables para el arbol XML y la raiz y se intenta cargar el arbol. Si falla crea uno nuevo
root = ""
root=BaseDeDatos.comprobarArchivo(root)
BaseDeDatos.guardarArchivo(root)

#Bucle de opciones del menu principal
check = True
while (check):
    opcion = input("\nSeleccione una opcion:\n1.Vehiculos\n2.Alquileres\n0.Salir")
    
    #Opcion para llamar al menu de vehiculos
    if(opcion=='1'):
        submenuVehiculo(root)
    
    #Opcion para llamar al menu de alquileres    
    elif (opcion == '2'):
        submenuAlquiler(root[1])
    
    #Opcion para salir    
    elif(opcion == '0'):
        check = False
        
    else:
        print("\nValor no valido")
        
print('Fin del programa')
