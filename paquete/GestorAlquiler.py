import xml.etree.ElementTree as ET
import Utiles, GestorVehiculo
from Utiles import comprobarKilometraje

def crear(alquileres,root):
    '''
    Esta funcion se encarga de pedir y comprobar todos los datos necesarios para crear un nuevo alquiler
    :param alquileres:Un diccionario con todos los alquileres 
    :param root:Un diccionario que contiene todos los alquileres y vehiculos 
    '''
    continuar=True#Variable que se usa para en el caso de que algun campo sea introducido mal el programa no te pregunte los demas campos 
    #---------------------------------------
    alquiler = ET.Element('Alquiler',{'alquilerID': Utiles.autoasignarIDAlquier(root)})#Creamos un nuevo elemento sobre el cual trabajaremos
    #-----------------------------------------
    if(continuar):
        print("\nIntroduzca una matricula de vehiculo") 
        scan= Utiles.escanerMatricula()
        if(scan!=None): 
            nodo= GestorVehiculo.buscarMatricula(scan, root[0])#Comprobamos que el vehiculo existe
            if(nodo!=None):
                if(nodo[4].text!='Averiado'):
                    idVehiculo = ET.SubElement(alquiler, 'ID_Vehiculo',{'matricula':scan,'tarifa':nodo[3].text})
                    idVehiculo.text =nodo.attrib['vehiculoID']
                else:
                    continuar=False
                    print("\nLo sentimos pero ese vehiculo no esta disponible actualmente")
            else:
                continuar=False
                print ('\nNo existe ese vehiculo')
                print('\nSe cancelara la creacion de este alquiler')
        else:
            continuar=False
            print('\nSe cancelara la creacion de este alquiler')
    
    if(continuar):
        print("\nIntroduzca un ID de cliente")
        scan= Utiles.escanerDni()
        if(scan!=None):
            idCliente = ET.SubElement(alquiler, 'ID_Cliente')
            idCliente.text =scan
        else:
            continuar=False
            print('\nSe cancelara la creacion de este alquiler')
    
    if(continuar):
        print("\nIntroduzca una fecha de inicio")
        fInicio= Utiles.escanerFecha()
        if(fInicio!=None ):
            if( Utiles.confirmarFecha(fInicio)):#Comprobamos que la fecha es superior o igual al dia de hoy
                if( Utiles.comprobarDisponibilidad(fInicio, root,"")):#Comprobamos que el vehiculo introducido esta disponible en esa fecha
                    fechaInicio = ET.SubElement(alquiler, 'Fecha_Inicio')
                    fechaInicio.text =fInicio
                else:
                    continuar=False
                    print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
            else:
                continuar=False
                print("\nNo puedes introducir una fecha que sea inferior a hoy")
        else:
            continuar=False
            print('\nSe cancelara la creacion de este alquiler')
    if(continuar):
        print("\nIntroduzca una fecha de finalizacion")
        fFinal= Utiles.escanerFecha()
        if(fFinal!=None ):
            if( Utiles.fechaDevolucionSuperior(fInicio,fFinal)!=None):#Comprobamos que la fecha es superior a la de inicio
                if( Utiles.comprobarDisponibilidad(fInicio, root,"")):#Comporbamos que el vehiculo esta disponible en esa fecha
                    fechaFinal = ET.SubElement(alquiler, 'Fecha_Final')
                    fechaFinal.text =fFinal
                    
                    fechaDevolucion = ET.SubElement(alquiler, 'Fecha_Devolucion')
                    fechaDevolucion.text ='-'
                else:
                    continuar=False
                    print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
            else:
                print('\nSe cancelara la creacion de este alquiler')
                print('\nPorque has introducido una fecha final inferior a la de inicio')
                continuar=False
        else:
            continuar=False
            print('\nSe cancelara la creacion de este alquiler')
    
    if(continuar):
        print("\nIntroduzca un kilometraje inicial") 
        scan= Utiles.escanerNumericoDecimal()
        if(scan!=None):
            if(comprobarKilometraje(scan,root)):#Comprobamos que el kilometraje es superior o igual al kilometraje final en el resto de alquileres de ese vehiculo
                kilometrajeInicial = ET.SubElement(alquiler, 'Kilometraje_Inicial')
                kilometrajeInicial.text =scan
                #A continuacion metemos el resto de campos que se rellenan solos o no hace falta introducir para crear un alquiler
                kilometrajeFinal = ET.SubElement(alquiler, 'Kilometraje_Final')
                kilometrajeFinal.text ='-'
                
                precioFinal = ET.SubElement(alquiler, 'Precio_Final')
                dias= Utiles.fechaDevolucionSuperior(fInicio,fFinal)#Calcular el precio final de el alquiler
                precioFinal.text =str(float(nodo[3].text)*float(dias))
                
                recargo = ET.SubElement(alquiler, 'Recargo')
                recargo.text ='De momento 0'
                
                alquileres.append(alquiler) 
                print('\nHas añadido un nuevo alquiler a la lista de alquileres')
            else:
                continuar=False
                print('\nEl kilometraje inicial es inferior a un kilometraje final anterior')
        else:
            continuar=False
            print('\nSe cancelara la creacion de este alquiler')
    
    return 0
def finalizarAlquiler(alquileres,root):
    '''
    Esta funcion se encarga de buscar un alquiler y despues pedir y comprobar todos los datos necesarios para finalizar un alquiler
    :param alquileres:Un diccionario con todos los alquileres 
    :param root:Un diccionario que contiene todos los alquileres y vehiculos
    '''
    nodo=None
    fechaDevolucion=None
    kilometrajeFinal=None
    precioFinal=None
    recargo=None
    continuar=True
    print("\nIntroduce la matricula del vehiculo que quieres ver")
    vehiculo= Utiles.escanerMatricula()
    nodoVehiculo= GestorVehiculo.buscarMatricula(vehiculo, root[0])
    if(vehiculo!=None):
        print("\nIntroduce el dni del cliente que quieres ver")
        dni= Utiles.escanerDni()
        if(dni!=None):
            nodo=buscarPosicionMatriculaDni(alquileres,vehiculo,dni)
    
    
    if(nodo!=None):
        if(nodoVehiculo==None):
            print("\nA pesar de que el vehiculo ya no existe puedes finalizar el alquiler")
        tarifa=nodo[0].attrib['tarifa']#Obtenemos la tarifa del vehiculo buscado
        print("\nIntroduzca una fecha de devolucion") 
        scan= Utiles.escanerFecha()
        if(scan!=None):
            if( Utiles.fechaDevolucionSuperior(nodo[2].text,scan)!=None):#Comprobamos que la fecha de devolucion es duperior a la de inicio
                fechaDevolucion=scan
            else:
                continuar=False
                print("\nLa fecha de devolucion no puede ser inferior a la de inicio")
        else:
            continuar=False
        if(continuar):
            print("\nIntroduzca un kilometraje final")
            scan= Utiles.escanerNumericoDecimal()
            if(scan!=None):
                if(comprobarKilometraje(scan, root)):#Comprobamos que el kilometraje final es superior al inicial
                    kilometrajeFinal=scan
                else:
                    print('\nEl kilometraje introducido es inferior al maximo kilometraje introducido')
                    continuar=False
            else:
                continuar=False
            extra= Utiles.fechaDevolucionSuperior(nodo[3].text,fechaDevolucion)#Calculamos la cantidad de dias que el cliente a devuelto tarde el vehiculo
            precio= Utiles.fechaDevolucionSuperior(nodo[2].text,nodo[3].text)#Calculamos la cantidad de dias que hay entre la fecha inicio y final del alquiler
            if(extra!=None):
                recargo=float(22)+float(tarifa)*float(extra)#Calculamos el recargo
            else:
                recargo=0
            if(precio!=None):
                precioFinal=float(tarifa)*float(precio)#Volvemos a calcular el precio final
        if(continuar):
            print("\n¿Seguro que quieres finalizar el alquiler?(Si o no)")
            if( Utiles.confirmacion()): 
                nodo[4].text=fechaDevolucion
                nodo[6].text=kilometrajeFinal
                if(recargo!=None):#Si hay recargo ponemos el recargo adecuado si no el recargo sera 0
                    nodo[8].text=str(recargo)
                if(precioFinal!=None):
                    nodo[7].text=str(precioFinal+recargo)
            
    return 0
def modificar(alquileres,root):
    '''
    Esta funcion busca y muestra un alquiler del cual podras modificar todos los campos que quieras siguiendo una serie de validaciones para al final con confirmacion cambiar los datos
    :param alquileres:Un diccionario con todos los alquileres 
    :param root:Un diccionario que contiene todos los alquileres y vehiculos
    '''
    nodo=None
    print("\nIntroduce la matricula del vehiculo que quieres ver")
    vehiculo= Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("\nIntroduce el dni del cliente que quieres ver")
        dni= Utiles.escanerDni()
        if(dni!=None):
            nodo=buscarPosicionMatriculaDni(alquileres,vehiculo,dni)
    #Inicimos todas las variables a None para asi poder compararlas siempre
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
    while(continuar):#Este bucle nos permite modificar todos los datos de un mismo alquiler hasta que queramos finalizar y nos pedira confirmacion para que los cambios se realicen
        if(nodo!=None):
            print("\nIntrocuce el campo que quieres modificar\n1.ID Alquiler\n2.ID Vehiculo\n3.ID Cliente\n4.Fecha Inicio\n5.Fecha Final\n6.Fecha Devolucion\n7.Kilometraje Inicial\n8.Kilometraje Final\n9.Precio Final\n10.Recargo\n0.Salir")
            opcion=input()
            if(opcion=="1"):#Este Switch es el que nos permite elegir que campo queremos modificar
                print("\nIntroduzca una ID de alquiler") 
                scan= Utiles.escanerNumerico()
                if(scan!=None):
                    if(buscarPosicionId(alquileres,scan)==None):
                        print("\nNo he encontrado otro alquiler con ID igual, es decir el ID introducido es valido")
                        idAlquiler=scan
                    else:
                        print("\nYa existe un alquiler con ese ID")
            elif(opcion=="2"):
                print("\nIntroduzca una matricula de vehiculo") 
                scan= Utiles.escanerMatricula()
                if(scan!=None): 
                    nodoVehiculo= GestorVehiculo.buscarMatricula(scan, root[0])
                    if(nodoVehiculo!=None):
                        if(nodoVehiculo[4].text!='Averiado'):#Comprobamos que el vehiculo esta disponible
                            idVehiculo =nodoVehiculo.attrib['vehiculoID']
                            matricula=nodoVehiculo[0].text
                            tarifa=nodoVehiculo[3].text
                        else:
                            print("\nLo sentimos pero ese vehiculo no esta disponible actualmente")
                    else:
                        print ('\nNo existe ese vehiculo')
            elif(opcion=="3"):
                print("\nIntroduzca una DNI de cliente") 
                scan= Utiles.escanerDni()
                if(scan!=None):
                    idCliente=scan
            elif(opcion=="4"):
                print("\nIntroduzca una fecha de inicio") 
                scan= Utiles.escanerFecha()
                if(scan!=None):
                    if(fechaFinal!=None):
                        if( Utiles.fechaDevolucionSuperior(scan,fechaFinal)!=None):#Comprobamos que introduces una feha inferior a la final
                            if( Utiles.comprobarDisponibilidad(scan, root,nodo.attrib['alquilerID'])):#Comprobamos que el vehiculo esta disponible en esa fecha
                                fechaInicio=scan
                            else:
                                print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
                        else:
                            print("\nLa fecha de inicio es mayor que la final, cambia antes la final a una mayor") 
                    else:
                        if( Utiles.fechaDevolucionSuperior(scan,nodo[3].text)!=None):#Comprobamos que introduces una feha inferior a la final
                            if( Utiles.comprobarDisponibilidad(scan, root,nodo.attrib['alquilerID'])):#Comprobamos que el vehiculo esta disponible en esa fecha
                                fechaInicio=scan
                            else:
                                print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
                        else:
                            print("\nLa fecha de inicio es mayor que la final, cambia antes la final a una mayor") 
            elif(opcion=="5"):
                print("\nIntroduzca una fecha final") 
                scan= Utiles.escanerFecha()
                if(scan!=None):
                    if(fechaInicio!=None):
                        if( Utiles.fechaDevolucionSuperior(fechaInicio,scan)!=None):#Comprobamos que introduces una feha superior a la inicial
                            if( Utiles.comprobarDisponibilidad(scan, root,nodo.attrib['alquilerID'])):#Comprobamos que el vehiculo esta disponible en esa fecha
                                fechaFinal=scan
                            else:
                                print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
                        else:
                            print("\nLa fecha de inicio es mayor que la final, cambia antes la final a una mayor") 
                    else:
                        if( Utiles.fechaDevolucionSuperior(nodo[2].text,scan)!=None):#Comprobamos que introduces una feha superior a la inicial
                            if( Utiles.comprobarDisponibilidad(scan, root,nodo.attrib['alquilerID'])):#Comprobamos que el vehiculo esta disponible en esa fecha
                                fechaFinal=scan
                            else:
                                print("\nLo sentimos pero el vehiculo esta ocupado en esa fecha")
                        else:
                            print("\nLa fecha de inicio es mayor que la final, cambia antes la final a una mayor") 
            elif(opcion=="6"):
                print("\nIntroduzca una fecha de devolucion") 
                scan= Utiles.escanerFecha()
                if(scan!=None):
                    if(fechaInicio!=None):
                        if( Utiles.fechaDevolucionSuperior(fechaInicio,scan)!=None):#Comprobamos que la fecha es superior a la inicial
                            fechaDevolucion=scan
                        else:
                            print("\nLa fecha de devolucion no puede ser inferior a la de inicio") 
                    else:
                        if( Utiles.fechaDevolucionSuperior(nodo[2].text,scan)!=None):#Comprobamos que la fecha es superior a la inicial
                            fechaDevolucion=scan
                        else:
                            print("\nLa fecha de devolucion no puede ser inferior a la de inicio")  
            elif(opcion=="7"):
                print("\nIntroduzca un kilometraje inicial") 
                scan= Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeInicial=scan
            elif(opcion=="8"):
                print("\nIntroduzca un kilometraje final") 
                scan= Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    kilometrajeFinal=scan
            elif(opcion=="9"):
                print("\nIntroduzca un precio final") 
                scan= Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    precioFinal=scan
            elif(opcion=="10"):
                print("\nIntroduzca un recargo") 
                scan= Utiles.escanerNumericoDecimal()
                if(scan!=None):
                    recargo=scan
            elif(opcion=="0"):
                continuar=False
            else:
                print("\nEscribe un numero dentro de las opciones posibles")
        else:
            continuar=False
            
    if(nodo!=None):
        print("\n¿Quieres guardar los cambios realizados?(Si o no)")
        if( Utiles.confirmacion()):#Confirmamos que quieres realizar los cambios
            print("\nLos cambios realizados tomaran efecto")#Cambiamos los campos que hayan sido cambiados
            if(idAlquiler != None):
                nodo.attrib['alquilerID']=idAlquiler
            if(idVehiculo!=None):
                nodo[0].text=idVehiculo
                nodo[0].attrib['matricula']=matricula
                nodo[0].attrib['tarifa']=tarifa
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
    '''
    Esta funcion se encarga de mostras todos los alquileres que tengan la matricula de un vehiculo que se le pedira al usuario
    :param alquileres:Un diccionario con todos los alquileres
    '''
    print("\nIntroduce la matricula de los alquileres que quieres ver")
    vehiculo= Utiles.escanerMatricula()
    if(vehiculo!=None):
        ninguno=True#Variable para que informe de que no ha encontrado nada
        for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
            if(x[0].attrib['matricula'].lower()==vehiculo.lower()):
                print("\nHe ecnontrado: ")
                Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("\nNo se ha encontrado ningun alquiler con esa matricula")
    return 0
def buscarMostrarTodosDni(alquileres):
    '''
    Esta funcion se encarga de mostras todos los alquileres que tengan el DNI de un cliente que se le pedira al usuario
    :param alquileres:Un diccionario con todos los alquileres
    '''
    print("\nIntroduce el dni de los alquileres que quieres ver")
    dni= Utiles.escanerDni()
    if(dni!=None):
        ninguno=True#Variable para que informe de que no ha encontrado nada
        for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
            if(x[1].text.lower()==dni.lower()):
                print("\nHe ecnontrado: ")
                Utiles.recorrer(x)
                ninguno=False
        if(ninguno):
                print("\nNo se ha encontrado ningun alquiler con ese Dni")
    return 0
def buscarMostrarMatriculaDni(alquileres):
    '''
    Esta funcion se encarga de mostrar todos los alquileres que contengan un DNI y matricula concretos que se le pediran al usuario
    :param alquileres:Un diccionario con todos los alquileres
    '''
    print("\nIntroduce la matricula del vehiculo que quieres ver")
    vehiculo= Utiles.escanerMatricula()
    if(vehiculo!=None):
        print("\nIntroduce el dni del cliente que quieres ver")
        dni= Utiles.escanerDni()
        if(dni!=None):
            ninguno=True#Variable para que informe de que no ha encontrado nada
            for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
                if( x[0].attrib['matricula'].lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
                    print("\nHe ecnontrado: ")
                    Utiles.recorrer(x)
                    ninguno=False
            if(ninguno):
                print("\nNo se ha encontrado ningun alquiler con esa Matricula y Dni")
    return 0
def buscarPosicionMatriculaDni(alquileres,vehiculo,dni):
    '''
    Esta funcion se encarga de buscar un alquiler que coincida con el DNI y matricula que la funcion recive y devolvera el nodo del alquiler seleccionado
    :param alquileres:Un diccionario con todos los alquileres 
    :param vehiculo:Una matricula de un vehiculo existente
    :param dni:Un DNI de un cliente 
    '''
    ninguno=True#Variable para que informe de que no ha encontrado nada
    cont=0
    opciones=[]
    for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
        if(x[0].attrib['matricula'].lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
            print(cont,"-He ecnontrado: ")
            Utiles.recorrer(x)
            opciones.append(cont)
            ninguno=False
        cont+=1
    if(ninguno):
        print("\nNo se ha encontrado ningun alquiler con esa Matricula y Dni")
    else:
        contador=0
        salir=True
        while(contador<3 and salir):
            contador+=1
            print(opciones)
            print ("\nElige el alquiler que quieres seleccionar")
            scan= Utiles.escanerNumerico()#Elegimos el alquiler con el que deseamos trabajar de los que han sido mostrados
            if(scan!=None):
                if(int(scan) in set(opciones)):
                    salir=False
                    for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
                        if(x == alquileres[int(scan)]):
                            return x
                elif(contador<3):
                    print("\nIntroduce un numero entre las opciones dadas")
                else:
                    print("\nNumero maximo de intentos alcanzado")
            else:
                salir=False
        
    return None
def buscarPosicionId(alquileres,idAlquiler):
    '''
    Esta funcion se encargara de buscar un alquiler atraves de un ID de alquiler
    :param alquileres:Un diccionario con todos los alquileres 
    :param idAlquiler:Una cadena con el ID de un alquiler
    '''
    nodo=0
    for x in alquileres:#Recorremos todos los alquileres en busca de concordancias
        if(x.attrib['alquilerID'].lower()==idAlquiler):
            return nodo
        nodo+=1
    return None
def mostrar(alquileres):
    '''
    Esta funcion se encarga de mostrar todos los alquileres 
    :param alquileres:Un diccionario con todos los alquileres 
    '''
    Utiles.recorrer(alquileres)
    return 0




