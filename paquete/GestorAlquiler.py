import xml.etree.ElementTree as ET
import MainXML
import BaseDeDatos 
import Utiles

def crear(alquileres):
    continuarCreando=True
    while(continuarCreando):
        continuar=True
        #---------------------------------------
        alquiler = ET.Element('Alquiler',{'alquilerID':atributo})
        #-----------------------------------------
        print("Dame una matricula de vehiculo") 
        scan=Utiles.escanerMatricula()
        if(scan!=None and continuar): 
            nodo=GestorVehiculo.buscarMatricula(scan, MainXML.root[0])
            if(nodo!=None):
                idVehiculo = ET.SubElement(alquiler, 'ID_Vehiculo')
                idVehiculo.text =nodo.attrib['vehiculoID']
            else:
                continuar=False
                print ('No existe ese vehiculo')
        else:
            continuar=False
        
        print("Dame un ID de cliente")
        scan=Utiles.escanerDni()
        if(scan!=None and continuar):
            idCliente = ET.SubElement(alquiler, 'ID_Cliente')
            idCliente.text =scan
        else:
            continuar=False
                
        print("Dame una fecha de inicio")
        scan=Utiles.escanerFecha()
        if(scan!=None and continuar):
            fechaInicio = ET.SubElement(alquiler, 'Fecha_Inicio')
            fechaInicio.text =scan
        else:
            continuar=False
        print("Dame una fecha de finalizacion")
        scan=Utiles.escanerFecha()
        if(scan!=None and continuar):
            fechaFinal = ET.SubElement(alquiler, 'Fecha_Final')
            fechaFinal.text =scan
            
            fechaDevolucion = ET.SubElement(alquiler, 'Fecha_Devolucion')
            fechaInicio.text ='-'
        else:
            continuar=False
            
        print("Dame un kilometraje inicial") 
        scan=Utiles.escanerNumericoDecimal()
        if(scan!=None and continuar):
            kilometrajeInicial = ET.SubElement(alquiler, 'Kilometraje_Inicial')
            kilometrajeInicial.text =scan
            
            kilometrajeFinal = ET.SubElement(alquiler, 'Kilometraje_Final')
            kilometrajeFinal.text ='-'
            
            precioFinal = ET.SubElement(alquiler, 'Precio_Final')
            precioFinal.text ='-'
            
            recargo = ET.SubElement(alquiler, 'Recargo')
            recargo.text ='De momento 0'
            
            alquileres.append(alquiler) 
            print('Has añadido un nuevo alquilerç a la lista de alquileres')
        else:
            continuar=False
        print ("Quieres continuar crendo alquileres?")
        if(Utiles.confirmacion()==False):
            continuarCreando=False
    
    return 0

def modificar(root):
    print("Introduce la matricula del vehiculo que quieres ver")
    vehiculo=Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("Introduce el dni del cliente que quieres ver")
        dni=Utiles.escanerDni()
        if(dni!=None):
            nodo=buscarPosicionMatriculaDni(top,vehiculo,dni)
    continuar=True
    while(continuar):
        if(nodo!=None):
            idAlquiler
            idVehiculo
            idCliente
            fechaInicio
            fechaFinal
            fechaDevolucion
            kilometrajeInicial
            kilometrajeFinal
            precioFinal
            recargo
            
            print("Introcuce el campo que quieres modificar\n1 ID Alquiler\n2 ID Vehiculo\n3 ID Cliente\n4 Fecha Inicio\n5 Fecha Final\n6 Fecha Devolucion\n7 Kilometraje Inicial\n8 Kilometraje Final\n9 precio Final\n10 Recargo\n0 Salir")
            opcion=Utiles.escanerNumerico()
            if(opcion=="1"):
                scan=Utiles.escanerNumerico()#-----------------------------------------------
                if(scan!=None):
                    if(buscarPosicionId(alquileres,scan)==None):
                        idAlquiler=scan
            elif(opcion=="2"):
                print("Dame una matricula de vehiculo") 
                scan=Utiles.escanerMatricula()
                if(scan!=None): 
                    nodo=GestorVehiculo.buscarMatricula(scan, MainXML.root[0])
                    if(nodo!=None):
                        idVehiculo =nodo.attrib['vehiculoID']
                    else:
                        print ('No existe ese vehiculo')
            elif(opcion=="3"):
                scan=Utiles.escanerDni()
                if(scan!=None):
                    idCliente=scan
            elif(opcion=="4"):
                scan=Utiles.escanerFecha()
                if(scan!=None):
                    fechaInicio=scan
            elif(opcion=="5"):
                scan=Utiles.escanerFecha()
                if(scan!=None):
                    fechaFinal=scan
            elif(opcion=="6"):
                scan=Utiles.escanerFecha()
                if(scan!=None):
                    fechaDevolucion=scan
            elif(opcion=="7"):
                scan=Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeInicial=scan
            elif(opcion=="8"):
                scan=Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeFinal=scan
            elif(opcion=="9"):
                scan=Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    precioFinal=scan
            elif(opcion=="10"):
                scan=Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    recargo=scan
            elif(opcion=="0"):
                continuar=False
            else:
                print("Escribe un numero dentro de las opciones posibles")
            
        else:
            print("No encontrado ningun alquiler con la matricula de ese coche y ese dni de cliente")
            continuar=False
    if(nodo!=None):
        print("Quieres guardar los cambios realizados?")
        if(Utiles.confirmacion()):
            if(idAlquiler != None):
                root[nodo].attrib['alquilerID']=idAlquiler
            if(idVehiculo!=None):
                root[nodo][0].text=idVehiculo
            if(idCliente!=None):
                root[nodo][1].text=idCliente
            if(fechaInicio!=None):
                root[nodo][2].text=fechaInicio
            if(fechafinal!=None):
                root[nodo][3].text=fechafinal
            if(fechaDevolucion!=None):
                root[nodo][4].text=fechaDevolucion
            if(kilometrajeInicial!=None):
                root[nodo][5].text=kilometrajeInicial
            if(kilometrajeFinal!=None):
                root[nodo][6].text=kilometrajeFinal
            if(precioFinal!=None):
                root[nodo][7].text=precioFinal
            if(recargo!=None):
                root[nodo][8].text=recargo
    return 0
def buscarMostrarTodosVehiculo(alquileres):
    print("Introduce la matricula de los alquileres que quieres ver")
    vehiculo=Utiles.escanerMatricula()
    if(vehiculo!=None):
        ninguno=True
        for x in alquileres:
            if(x[0].text.lower()==texto.lower()):
                print("He ecnontrado: ",x.text)
                Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("No se ha encontrado ningun alquiler con esa matricula")
    return 0
def buscarMostrarTodosDni(alquileres):
    print("Introduce el dni de los alquileres que quieres ver")
    dni=Utiles.escanerDni()
    if(dni!=None):
        ninguno=True
        for x in alquileres:
            if(x[1].text.lower()==texto.lower()):
                print("He ecnontrado: ",x.text)
                Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("No se ha encontrado ningun alquiler con ese Dni")
    return 0
def buscarMostrarMatriculaDni(alquileres):
    print("Introduce la matricula del vehiculo que quieres ver")
    vehiculo=Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("Introduce el dni del cliente que quieres ver")
        dni=Utiles.escanerDni()
        if(dni!=None):
            ninguno=True
            for x in alquileres:
                if( x[0].text.lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
                    print("He ecnontrado: ",x.text)
                    Utiles.recorrer(x)
                    ninguno=False
            if(ninguno):
                print("No se ha encontrado ningun alquiler con esa Matricula y Dni")
    return 0
def buscarPosicionMatriculaDni(alquileres,vehiculo,dni):
    cont=0
    opciones=[]
    for x in alquileres:
        if(x[0].text.lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
            print(cont,"-He ecnontrado: ",x.text)
            Utiles.recorrer(x)
            opciones.append(cont)
        cont+=1
    
    nodo=0
    print ("Elige el alquiler que quieres seleccionar")
    scan=Utiles.escanerNumerico()
    if(scan in opciones):
        for x in alquileres:
            if(x == alquileres[scan]):
                print(cont,"-He ecnontrado: ",x.text)
                Utiles.recorrer(x)
                return nodo
            nodo+=1
    return None
def buscarPosicionId(alquileres,id):
    nodo=0
    for x in alquileres:
        if(x.attrib['alquilerID'].lower()==id):
            print(cont,"-He ecnontrado: ",x.text)
            Utiles.recorrer(x)
            return nodo
        nodo+=1
    return None
def mostrar(root):
    Utiles.recorrer(root)
    return 0




