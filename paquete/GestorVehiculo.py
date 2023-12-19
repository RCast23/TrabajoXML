import xml.etree.ElementTree as ET
import Utiles
from Utiles import recorrer, escanerMatricula, escanerEstadoVehiculo


def crear(root):
    '''
    Metodo para crear un nuevo vehiculo
    :param root: Elemento raiz del documento XML
    '''
    
    #Variable para comprobar que si el alta debe parar o seguir 
    check = True
    vehiculo = ET.Element('Vehiculo', {'vehiculoID': Utiles.autoasignarIDVehiculo(root)})
    #Se escanea la matricula y si el valor devuelto es None o ya hay un vehiculo con esa matricula se para el alta
    print("\nIntroduzca una matricula")
    scanMatricula =  Utiles.escanerMatricula()
    if(scanMatricula == None or buscarMatricula(scanMatricula, root[0]) != None):
        check = False
    else:
        matricula = ET.SubElement(vehiculo, 'Matricula')
        matricula.text = scanMatricula 
        
    #Se escanea la descripcion del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("\nIntroduzca una descripcion (Marca y modelo)")
        scanMarcaModelo =  Utiles.escanerTexto()
        if(scanMarcaModelo == None):
            check = False
        else:
            marcaYmodelo = ET.SubElement(vehiculo, 'Descripcion')
            marcaYmodelo.text = scanMarcaModelo
    
    #Se escanea el anno de fabricacion del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("\nIntroduzca un Anno De Fabricacion")
        scanAnno =  Utiles.escanerYear()
        if(scanAnno == None):
            check = False
        else:
            annoDeFabricacion = ET.SubElement(vehiculo, 'Anno_De_Fabricacion')
            annoDeFabricacion.text = scanAnno
    
    #Se escanea la tarifa de alquiler del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("\nIntroduzca una tarifa por dia")
        scanTarifa =  Utiles.escanerNumericoDecimal()
        if(scanTarifa == None):
            check = False
        else:
            tarifa = ET.SubElement(vehiculo, 'Tarifa')
            tarifa.text = scanTarifa
    
    #Si todos los datos han sido introducidos correctamente se crea el nuevo vehiculo y se guardan
    if(check):
        estadoVehiculo = ET.SubElement(vehiculo, 'Estado_Vehiculo')
        #El vehiculo creado tendra el estado Disponible de forma predeterminada
        estadoVehiculo.text = 'Disponible'
        root[0].append(vehiculo)
        print("\nVehiculo creado")
    else:
        print('\nNo se ha creado vehiculo')
        
    
def borrar(rootVehiculo):  # Requiere confirmacion
    '''
    Metodo para borrar un vehiculo
    :param rootVehiculo: Elemento del XML que contiene todos los vehiculos
    '''
    #Se busca vehiculo y si se encuentra se muestra
    vehiculo = buscarVehiculo(rootVehiculo)
    if(vehiculo != None):
        mostrarTodos(vehiculo)
        #Se pide confirmacion para borrar el vehiculo
        print("\n¿Desea confirmar la baja del vehiculo?(Si o no)")
        if( Utiles.confirmacion()):
            rootVehiculo.remove(vehiculo)
            print("\nVehiculo eliminado")
        else:
            print("\nVehiculo no eliminado")

def modificar(root):  # Requiere confirmacion
    '''
    Metodo para modificar un vehiculo
    :param root: Elemento raiz del documento XML
    '''
    #Se busca el vehiculo que se quiere modificar
    vehiculo = buscarVehiculo(root[0])
    #Si se ha encontrado un vehiculo se muestra y se muestra el menu de modificar
    if(vehiculo != None):
        mostrarTodos(vehiculo)
        
        #Variable que controla el bucle que ofrece las opciones
        check = True
        while(check):
            print('''Introduzca el campo que se quiere modificar:
1.ID vehiculo\n2.Matricula\n3.Descripcion(Marca y modelo)\n4.Anno de fabricacion
5.Tarifa\n6.Estado del vehiculo\n0.Salir''')
            
            #Opcion para modificar la ID del vehiculo
            numOpcion = Utiles.escanerNumerico()
            if(numOpcion == '1'):
                print("\nIntroduzca la nueva ID del vehiculo")
                scan = Utiles.escanerID(root)
                #Se comprueba que el ID es valido y se pide confirmacion de la modificacion
                if(scan != None):
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if( Utiles.confirmacion()):
                        Utiles.modificarIDVehiculoCascada(root, vehiculo.get('ID_Vehiculo'), scan)
                        vehiculo.set('vehiculoID', scan)
            
            #Opcion para modificar la matricula del vehiculo        
            elif(numOpcion == '2'):
                print("\nIntroduzca la nueva matricula del vehiculo")
                scan = Utiles.escanerMatricula() 
                #Se comprueba que la matricula es valida y se pide confirmacion de la modificacion
                if(scan != None and buscarMatricula(scan, root[0]) == None):
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if(Utiles.confirmacion()):
                        Utiles.modificarMatriculaVehiculoCascada(root, vehiculo[0].text, scan)
                        vehiculo[0].text = scan
                else:
                    print("\nNo se ha modificado la matricula")
                    
            #Opcion para modificar la descripcion del vehiculo  
            elif(numOpcion == '3'):
                print("\nIntroduzca la nueva descripcion del vehiculo (Marca y modelo)")
                scan = Utiles.escanerTexto()
                #Se comprueba que la descripcion es valida y se pide confirmacion de la modificacion
                if(scan != None):
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if(Utiles.confirmacion()):
                        vehiculo[1].text = scan
                    
            #Opcion para modificar el anno de fabricacion del vehiculo 
            elif(numOpcion == '4'):
                print("\nIntroduzca el nuevo anno de fabricacion del vehiculo")
                scan = Utiles.escanerYear()
                #Se comprueba que el anno de fabricacion es valido y se pide confirmacion de la modificacion
                if(scan != None):
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if(Utiles.confirmacion()):
                        vehiculo[2].text = scan
                    
            #Opcion para modificar la tarifa del vehiculo
            elif(numOpcion == '5'):
                print("\nIntroduzca la nueva tarifa del vehiculo")
                scan = Utiles.escanerNumericoDecimal()
                #Se comprueba que la tarifa es valida y se pide confirmacion de la modificacion
                if(scan != None):
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if(Utiles.confirmacion()):
                        vehiculo[3].text = scan
                    
            #Opcion para modificar el estado del vehiculo 
            elif(numOpcion == '6'):
                scan = escanerEstadoVehiculo()
                if(scan != None):
                    #Se comprueba que el estado es valido y se pide confirmacion de la modificacion
                    print("\n¿Desea confirmar la modificacion?(Si o no)")
                    if(Utiles.confirmacion()):
                        vehiculo[4].text = scan
                    
            #Opcion para salir del menu
            elif(numOpcion == '0'):
                check = False
                
            else:
                print("\nValor no valido")
        
    else:
        print("\nNo se ha encontrado el vehiculo")
    print('\nFin modificacion vehiculo')

    
def buscarVehiculo(root):
    '''
    Metodo para buscar un vehiculo
    :param root: Elemento raiz del documento XML
    :return Devuelve un vehiculo o None si no encuentra ninguno
    '''
    print("\nIntroduzca la matricula del vehiculo")
    matricula = escanerMatricula();
    print(matricula)
    if(matricula==None):
        print("\nNo se ha encontrado el vehiculo")
    else:
        return buscarMatricula(matricula, root)

    
def buscarMatricula(matricula, root):
    '''
    Metodo para buscar un vehiculo por su matricula
    :param matricula: String que contiene la matricula del vehiculo a buscar
    :param root: Elemento raiz del documento XML
    :return Devuelve un vehiculo o None si no encuentra ninguno
    '''
    #Variable para elegir el vehiculo
    i = 0;
    try:
        #Se crea un bucle para comprobar el campo 0 de todos los vehiculos y 
        #si coincide con la introducida se devuelve ese vehiculo
        while(True):
            aux = root[i][0].text            
            if(matricula == aux):
                print("\nVehiculo encontrado")
                return root[i]
            i += 1
            
    #Si el bucle llega a una posicion inexistente salta la excepcion y devuelve None
    except:
        print("\nNo se ha encontrado el vehiculo")
        return None
    

def mostrarTodos(rootVehiculo):
    '''
    Metodo para mostrar todos los vehiculos
    :param rootVehiculo: Elemento del XML que contiene todos los vehiculos
    '''
    recorrer(rootVehiculo)
