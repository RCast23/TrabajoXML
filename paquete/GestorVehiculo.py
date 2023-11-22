import xml.etree.ElementTree as ET
from paquete.Utiles import escanerMatricula, escanerAlfanumerico, \
    escanerNumerico, escanerAlfabetico, escanerNumericoDecimal, confirmacion


def crear(rootVehiculo):
    check = True
    
    # Preguntar como se estan autoasignando valores
    # Uso temporal de id introducida manualmente
    
    print("Dame una matricula")
    scanMatricula = escanerMatricula()  # que llame a utiles con un escaner  que verifique
    if(scanMatricula == None or buscarMatricula(scanMatricula, rootVehiculo) != None):
        check = False
        
    if(check):
        print("Dame una marca y modelo")
        scanMarcaModelo = escanerAlfanumerico()
        if(scanMarcaModelo == None):
            check = False
    
    if(check):
        # No termino de entender la diferencia entre numerico y numerico decimal
        print("Dame un Anno De Fabricacion")
        scanAnno = escanerNumerico()
        if(scanAnno == None):
            check = False
    
    if(check):
        # No termino de entender la diferencia entre numerico y numerico decimal
        print("Dame una tarifa por dia")
        scanTarifa = escanerNumerico()
        if(scanTarifa == None):
            check = False
    
    if(check):
        print("Dame un estado del vehiculo")
        scan = escanerAlfabetico()
        if(scan == None):
            check = False
    
    if(check):
        scan=input("dame el ID")
        vehiculo = ET.SubElement(rootVehiculo, 'Vehiculo', {'vehiculoID':scan})
        matricula = ET.SubElement(vehiculo, 'Matricula')
        matricula.text = scanMatricula
        marcaYmodelo = ET.SubElement(vehiculo, 'Marca_Y_Modelo')
        marcaYmodelo.text = scanMarcaModelo
        annoDeFabricacion = ET.SubElement(vehiculo, 'Anno_De_Fabricacion')
        annoDeFabricacion.text = scanAnno
        tarifa = ET.SubElement(vehiculo, 'Tarifa')
        tarifa.text = scanTarifa
        estadoVehiculo = ET.SubElement(vehiculo, 'Estado_Vehiculo')
        estadoVehiculo.text = scan
        print("Coche creado")
        
    
def borrar(rootVehiculo):  # Requiere confirmacion
    vehiculo = buscarVehiculo(rootVehiculo)
    if(vehiculo != None):
        mostrarTodos(vehiculo)
        print("¿Desea confirmar la baja del vehiculo?")
        if(confirmacion()):
            rootVehiculo.remove(vehiculo)
            print("Vehiculo eliminado")


def modificar(rootVehiculo):  # Requiere confirmacion
    vehiculo = buscarVehiculo(rootVehiculo)
    if(vehiculo != None):
        mostrarTodos(vehiculo)
        check = True
        while(check):
            print('''Introduzca el campo que se quiere modificar:
1.ID vehiculo\n2. Matricula\n3.Marca y modelo\n4.Anno de fabricacion
5.Tarifa\n6.Estado del vehiculo\n0.Salir''')
            
            numOpcion = escanerNumerico()
            if(numOpcion == '1'):
                print("Introduzca la nueva ID del vehiculo")
                scan = escanerNumerico()
                #Introducir comprobacion de atributo ya existente
                if(scan != None):
                    print("¿Desea confirmar la modificacion")
                    if(confirmacion()):
                        vehiculo.set('vehiculoID', scan)
                    
            elif(numOpcion == '2'):
                print("Introduzca la nueva matricula del vehiculo")
                scan = escanerMatricula()
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(confirmacion()):
                        vehiculo[0].text = scan
                    
            elif(numOpcion == '3'):
                print("Introduzca la nueva marca y modelo del vehiculo")
                scan = escanerAlfanumerico()
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(confirmacion()):
                        vehiculo[1].text = scan
                    
            elif(numOpcion == '4'):
                # Los Annos probablemente necesiten su propio scanner
                print("Introduzca el nuevo anno de fabricacion del vehiculo")
                scan = escanerNumericoDecimal()()
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(confirmacion()):
                        vehiculo[2].text = scan
                    
            elif(numOpcion == '5'):
                print("Introduzca la nueva tarifa del vehiculo")
                scan = escanerNumerico()
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(confirmacion()):
                        vehiculo[3].text = scan
                    
            elif(numOpcion == '6'):
                print("Introduzca el nuevo estado del vehiculo")
                scan = escanerAlfabetico()
                if(scan != None):
                    print("¿Desea confirmar la modificacion?")
                    if(confirmacion()):
                        vehiculo[4].text = scan
                    
            elif(numOpcion == '0'):
                check = False
                
            else:
                print("Valor no valido")
        
    else:
        print("No se ha encontrado el vehiculo")

    
def buscarVehiculo(agenda):
    matricula = input("Introduzca la matricula del vehiculo")
    return buscarMatricula(matricula, agenda)

    
def buscarMatricula(matricula, vehiculo):
    i = 0;
    try:
        while(True):
            aux = vehiculo[i][0].text            
            if(matricula == aux):
                print("Vehiculo encontrado")
                return vehiculo[i]
            i += 1
    except:
        print("No se ha encontrado el vehiculo")
        return None
    

def mostrarTodos(rootVehiculo):
    print(rootVehiculo.tag, end="")
    # Para recorrer los atributos. Los atributos estan en un diccionario
    for attr in rootVehiculo.attrib:
        attrName = attr
        attrValue = rootVehiculo.attrib[attr]
        print("\t", attrName, ":", attrValue, " ", end="")
    print("\n\t", rootVehiculo.text)
    for n in rootVehiculo:
        mostrarTodos(n)
