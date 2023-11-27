import xml.etree.ElementTree as ET
import paquete.Utiles
from paquete.Utiles import recorrer, escanerMatricula, escanerEstadoVehiculo


def crear(root):
    '''
    Metodo para crear un nuevo vehiculo
    :param root: Elemento raiz del documento XML
    '''
    
    #Variable para comprobar que si el alta debe parar o seguir 
    check = True
    
    #Se escanea la matricula y si el valor devuelto es None o ya hay un vehiculo con esa matricula se para el alta
    print("Dame una matricula")
    scanMatricula = paquete.Utiles.escanerMatricula()
    if(scanMatricula == None or buscarMatricula(scanMatricula, root[0]) != None):
        check = False
        
    #Se escanea la descripcion del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("Dame una descripcion (Marca y modelo)")
        scanMarcaModelo = paquete.Utiles.escanerTexto()
        if(scanMarcaModelo == None):
            check = False
    
    #Se escanea el anno de fabricacion del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("Dame un Anno De Fabricacion")
        scanAnno = paquete.Utiles.escanerYear()
        if(scanAnno == None):
            check = False
    
    #Se escanea la tarifa de alquiler del vehiculo y si el valor devuelto es None se para el alta
    if(check):
        print("Dame una tarifa por dia")
        scanTarifa = paquete.Utiles.escanerNumericoDecimal()
        if(scanTarifa == None):
            check = False
    
    #Si todos los datos han sido introducidos correctamente se crea el nuevo vehiculo y se guardan
    if(check):
        vehiculo = ET.SubElement(root[0], 'Vehiculo', {'vehiculoID':paquete.Utiles.autoasignarIDVehiculo(root)})
        vehiculo.text = '_'
        matricula = ET.SubElement(vehiculo, 'Matricula')
        matricula.text = scanMatricula 
        marcaYmodelo = ET.SubElement(vehiculo, 'Descripcion')
        marcaYmodelo.text = scanMarcaModelo
        annoDeFabricacion = ET.SubElement(vehiculo, 'Anno_De_Fabricacion')
        annoDeFabricacion.text = scanAnno
        tarifa = ET.SubElement(vehiculo, 'Tarifa')
        tarifa.text = scanTarifa
        estadoVehiculo = ET.SubElement(vehiculo, 'Estado_Vehiculo')
        #El vehiculo creado tendra el estado Disponible de forma predeterminada
        estadoVehiculo.text = 'Disponible'
        print("Vehiculo creado")
    else:
        print('No se ha creado vehiculo')
        
    
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
        print("¿Desea confirmar la baja del vehiculo?")
        if(paquete.Utiles.confirmacion()):
            rootVehiculo.remove(vehiculo)
            print("Vehiculo eliminado")
        else:
            print("Vehiculo no eliminado")

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
            numOpcion = paquete.Utiles.escanerNumerico()
            if(numOpcion == '1'):
                print("Introduzca la nueva ID del vehiculo")
                scan = paquete.Utiles.escanerID(root)
                #Se comprueba que el ID es valido y se pide confirmacion de la modificacion
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        paquete.Utiles.modificarIDVehiculoCascada(root, vehiculo.get('ID_Vehiculo'), scan)
                        vehiculo.set('vehiculoID', scan)
            
            #Opcion para modificar la matricula del vehiculo        
            elif(numOpcion == '2'):
                print("Introduzca la nueva matricula del vehiculo")
                scan = paquete.Utiles.escanerMatricula() 
                #Se comprueba que la matricula es valida y se pide confirmacion de la modificacion
                if(scan != None and buscarMatricula(scan, root[0]) == None):
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        paquete.Utiles.modificarMatriculaVehiculoCascada(root, vehiculo[0].text, scan)
                        vehiculo[0].text = scan
                else:
                    print("No se ha modificado la matricula")
                    
            #Opcion para modificar la descripcion del vehiculo  
            elif(numOpcion == '3'):
                print("Introduzca la nueva descripcion del vehiculo (Marca y modelo)")
                scan = paquete.Utiles.escanerTexto()
                #Se comprueba que la descripcion es valida y se pide confirmacion de la modificacion
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        vehiculo[1].text = scan
                    
            #Opcion para modificar el anno de fabricacion del vehiculo 
            elif(numOpcion == '4'):
                print("Introduzca el nuevo anno de fabricacion del vehiculo")
                scan = paquete.Utiles.escanerYear()
                #Se comprueba que el anno de fabricacion es valido y se pide confirmacion de la modificacion
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        vehiculo[2].text = scan
                    
            #Opcion para modificar la tarifa del vehiculo
            elif(numOpcion == '5'):
                print("Introduzca la nueva tarifa del vehiculo")
                scan = paquete.Utiles.escanerNumericoDecimal()
                #Se comprueba que la tarifa es valida y se pide confirmacion de la modificacion
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        vehiculo[3].text = scan
                    
            #Opcion para modificar el estado del vehiculo 
            elif(numOpcion == '6'):
                scan = escanerEstadoVehiculo()
                if(scan != None):
                    #Se comprueba que el estado es valido y se pide confirmacion de la modificacion
                    print("¿Desea confirmar la modificacion?")
                    if(paquete.Utiles.confirmacion()):
                        vehiculo[4].text = scan
                    
            #Opcion para salir del menu
            elif(numOpcion == '0'):
                check = False
                
            else:
                print("Valor no valido")
        
    else:
        print("No se ha encontrado el vehiculo")
    print('Fin modificacion vehiculo')

    
def buscarVehiculo(root):
    '''
    Metodo para buscar un vehiculo
    :param root: Elemento raiz del documento XML
    :return Devuelve un vehiculo o None si no encuentra ninguno
    '''
    print("Introduzca la matricula del vehiculo")
    matricula = escanerMatricula();
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
                print("Vehiculo encontrado")
                return root[i]
            i += 1
            
    #Si el bucle llega a una posicion inexistente salta la excepcion y devuelve None
    except:
        print("No se ha encontrado el vehiculo")
        return None
    

def mostrarTodos(rootVehiculo):
    '''
    Metodo para mostrar todos los vehiculos
    :param rootVehiculo: Elemento del XML que contiene todos los vehiculos
    '''
    recorrer(rootVehiculo)
