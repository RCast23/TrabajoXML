import xml.etree.ElementTree as ET
import paquete.Utiles

def crear(alquileres,root):
    continuarCreando=True
    while(continuarCreando):
        continuar=True
        #---------------------------------------
        alquiler = ET.Element('Alquiler',{'alquilerID':'atributo'})#llamar al metodo que te crea un identificador automatico
        alquiler.text=''
        #-----------------------------------------
        if(continuar):
            print("Dame una matricula de vehiculo") 
            scan=paquete.Utiles.escanerMatricula()
            if(scan!=None): 
                nodo=paquete.GestorVehiculo.buscarMatricula(scan, root[0])
                if(nodo!=None):
                    idVehiculo = ET.SubElement(alquiler, 'ID_Vehiculo',{'matricula':scan})
                    idVehiculo.text =nodo.attrib['vehiculoID']
                else:
                    continuar=False
                    print ('No existe ese vehiculo')
                    print('Se cancelara la creacion de este alquiler')
            else:
                continuar=False
                print('Se cancelara la creacion de este alquiler')
        
        if(continuar):
            print("Dame un ID de cliente")
            scan=paquete.Utiles.escanerDni()
            if(scan!=None):
                idCliente = ET.SubElement(alquiler, 'ID_Cliente')
                idCliente.text =scan
            else:
                continuar=False
                print('Se cancelara la creacion de este alquiler')
        
        if(continuar):
            print("Dame una fecha de inicio")
            scan=paquete.Utiles.escanerFecha()
            if(scan!=None ):
                fechaInicio = ET.SubElement(alquiler, 'Fecha_Inicio')
                fechaInicio.text =scan
            else:
                continuar=False
                print('Se cancelara la creacion de este alquiler')
        if(continuar):
            print("Dame una fecha de finalizacion")
            scan=paquete.Utiles.escanerFecha()
            if(scan!=None ):
                fechaFinal = ET.SubElement(alquiler, 'Fecha_Final')
                fechaFinal.text =scan
                
                fechaDevolucion = ET.SubElement(alquiler, 'Fecha_Devolucion')
                fechaDevolucion.text ='-'
            else:
                continuar=False
                print('Se cancelara la creacion de este alquiler')
        
        if(continuar):
            print("Dame un kilometraje inicial") 
            scan=paquete.Utiles.escanerNumericoDecimal()
            if(scan!=None ):
                kilometrajeInicial = ET.SubElement(alquiler, 'Kilometraje_Inicial')
                kilometrajeInicial.text =scan
                
                kilometrajeFinal = ET.SubElement(alquiler, 'Kilometraje_Final')
                kilometrajeFinal.text ='-'
                
                precioFinal = ET.SubElement(alquiler, 'Precio_Final')
                precioFinal.text ='-'
                
                recargo = ET.SubElement(alquiler, 'Recargo')
                recargo.text ='De momento 0'
                
                alquileres.append(alquiler) 
                print('Has añadido un nuevo alquiler a la lista de alquileres')
            else:
                continuar=False
                print('Se cancelara la creacion de este alquiler')
    
    return 0

def modificar(alquileres,root):
    print("Introduce la matricula del vehiculo que quieres ver")
    vehiculo=paquete.Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("Introduce el dni del cliente que quieres ver")
        dni=paquete.Utiles.escanerDni()
        if(dni!=None):
            nodo=buscarPosicionMatriculaDni(alquileres,vehiculo,dni)
    continuar=True
    idAlquiler=None
    idVehiculo=None
    idCliente=None
    fechaInicio=None
    fechaFinal=None
    fechaDevolucion=None
    kilometrajeInicial=None
    kilometrajeFinal=None
    precioFinal=None
    recargo=None
    while(continuar):
        if(nodo!=None):
            print("Introcuce el campo que quieres modificar\n1.ID Alquiler\n2.ID Vehiculo\n3.ID Cliente\n4.Fecha Inicio\n5.Fecha Final\n6.Fecha Devolucion\n7.Kilometraje Inicial\n8.Kilometraje Final\n9.Precio Final\n10.Recargo\n0.Salir")
            opcion=paquete.Utiles.escanerNumerico()
            if(opcion=="1"):
                print("Dame una ID de alquiler") 
                scan=paquete.Utiles.escanerNumerico()#-----------------------------------------------
                if(scan!=None):
                    if(buscarPosicionId(alquileres,scan)==None):
                        print("No he encontrado otro alquiler con ID igual, es decir el ID introducido es valido")
                        idAlquiler=scan
                    else:
                        print("Ya existe un alquiler con ese ID")
            elif(opcion=="2"):
                print("Dame una matricula de vehiculo") 
                scan=paquete.Utiles.escanerMatricula()
                if(scan!=None): 
                    nodoVehiculo=paquete.GestorVehiculo.buscarMatricula(scan, root[0])
                    if(nodoVehiculo!=None):
                        idVehiculo =nodoVehiculo.attrib['vehiculoID']
                    else:
                        print ('No existe ese vehiculo')
            elif(opcion=="3"):
                print("Dame una DNI de cliente") 
                scan=paquete.Utiles.escanerDni()
                if(scan!=None):
                    idCliente=scan
            elif(opcion=="4"):
                print("Dame una fecha de inicio") 
                scan=paquete.Utiles.escanerFecha()
                if(scan!=None):
                    fechaInicio=scan
            elif(opcion=="5"):
                print("Dame una fecha final") 
                scan=paquete.Utiles.escanerFecha()
                if(scan!=None):
                    fechaFinal=scan
            elif(opcion=="6"):
                print("Dame una fecha de devolucion") 
                scan=paquete.Utiles.escanerFecha()
                if(scan!=None):
                    fechaDevolucion=scan
            elif(opcion=="7"):
                print("Dame un kilometraje inicial") 
                scan=paquete.Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeInicial=scan
            elif(opcion=="8"):
                print("Dame un kilometraje final") 
                scan=paquete.Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeFinal=scan
            elif(opcion=="9"):
                print("Dame un precio final") 
                scan=paquete.Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    precioFinal=scan
            elif(opcion=="10"):
                print("Dame un recargo") 
                scan=paquete.Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    recargo=scan
            elif(opcion=="0"):
                continuar=False
            else:
                print("Escribe un numero dentro de las opciones posibles")
        else:
            continuar=False
    if(nodo!=None):
        print("¿Quieres guardar los cambios realizados?\n Si o No")
        if(paquete.Utiles.confirmacion()):
            print("Los cambios realizados tomaran efecto")
            if(idAlquiler != None):
                nodo.attrib['alquilerID']=idAlquiler
            if(idVehiculo!=None):
                nodo[0].text=idVehiculo
            if(idCliente!=None):
                nodo[1].text=idCliente
            if(fechaInicio!=None):
                nodo[2].text=fechaInicio
            if(fechaFinal!=None):
                nodo[3].text=fechaFinal
            if(fechaDevolucion!=None):
                nodo[4].text=fechaDevolucion
            if(kilometrajeInicial!=None):
                nodo[5].text=kilometrajeInicial
            if(kilometrajeFinal!=None):
                nodo[6].text=kilometrajeFinal
            if(precioFinal!=None):
                nodo[7].text=precioFinal
            if(recargo!=None):
                nodo[8].text=recargo
    return 0
def buscarMostrarTodosVehiculo(alquileres):
    print("Introduce la matricula de los alquileres que quieres ver")
    vehiculo=paquete.Utiles.escanerMatricula()
    if(vehiculo!=None):
        ninguno=True
        for x in alquileres:
            if(x[0].attrib['matricula'].lower()==vehiculo.lower()):
                print("He ecnontrado: ",x.text)
                paquete.Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("No se ha encontrado ningun alquiler con esa matricula")
    return 0
def buscarMostrarTodosDni(alquileres):
    print("Introduce el dni de los alquileres que quieres ver")
    dni=paquete.Utiles.escanerDni()
    if(dni!=None):
        ninguno=True
        for x in alquileres:
            if(x[1].text.lower()==dni.lower()):
                print("He ecnontrado: ",x.text)
                paquete.Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("No se ha encontrado ningun alquiler con ese Dni")
    return 0
def buscarMostrarMatriculaDni(alquileres):
    print("Introduce la matricula del vehiculo que quieres ver")
    vehiculo=paquete.Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("Introduce el dni del cliente que quieres ver")
        dni=paquete.Utiles.escanerDni()
        if(dni!=None):
            ninguno=True
            for x in alquileres:
                if( x[0].attrib['matricula'].lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
                    print("He ecnontrado: ",x.text)
                    paquete.Utiles.recorrer(x)
                    ninguno=False
            if(ninguno):
                print("No se ha encontrado ningun alquiler con esa Matricula y Dni")
    return 0
def buscarPosicionMatriculaDni(alquileres,vehiculo,dni):
    cont=0
    opciones=[]
    for x in alquileres:
        if(x[0].attrib['matricula'].lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
            print(cont,"-He ecnontrado: ",x.text)
            paquete.Utiles.recorrer(x)
            opciones.append(cont)
            print(opciones)
            ninguno=False
        cont+=1
    if(ninguno):
        print("No se ha encontrado ningun alquiler con esa Matricula y Dni")
    else:
        print ("Elige el alquiler que quieres seleccionar")
        scan=paquete.Utiles.escanerNumerico()
        if(scan!=None):
            if(int(scan) in set(opciones)):
                for x in alquileres:
                    if(x == alquileres[int(scan)]):
                        return x
    return None
def buscarPosicionId(alquileres,idAlquiler):
    nodo=0
    for x in alquileres:
        if(x.attrib['alquilerID'].lower()==idAlquiler):
            print("-He ecnontrado: ",x.text)
            paquete.Utiles.recorrer(x)
            return nodo
        nodo+=1
    return None
def mostrar(alquileres):
    paquete.Utiles.recorrer(alquileres)
    return 0




