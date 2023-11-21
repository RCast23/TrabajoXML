import xml.etree.ElementTree as ET
import MainXML
import BaseDeDatos 
import Utiles

def crear(alquileres):
    
    atributo=input("Dame un ID de alquiler")
    if(Utiles.validacionIDAlquiler(atributo)):
        if(buscarPosicion(alquileres,atributo)==None):
            alquiler = ET.Element('Alquiler',{'alquilerID':atributo})
            scan=input("Dame un ID de vehiculo")
            if(Utiles.validacionIDVehiculo(scan)): 
                if(GestorVehiculo.buscarPosicion(MainXML.root[0],scan)!=None):
                    idVehiculo = ET.SubElement(alquiler, 'ID Vehiculo')
                    idVehiculo.text =scan
                    
                    scan=input("Dame un ID de cliente")#que llame a utiles con un escaner  que verifique
                    if(Utiles.validacionIDCliente(scan)):
                        idCliente = ET.SubElement(alquiler, 'ID Cliente')
                        idCliente.text =scan
                        
                        scan=input("Dame una fecha de inicio")
                        if(Utiles.ValidacionFechaDeInicio(scan)):
                            fechaInicio = ET.SubElement(alquiler, 'Fecha Inicio')
                            fechaInicio.text =scan
                            
                            fechaDevolucion = ET.SubElement(alquiler, 'Fecha Devolucion')
                            fechaInicio.text ='-'
                            
                            scan=input("Dame un kilometraje inicial")
                            if(Utiles.ValidacionKilometrajeInicial(scan)):
                                kilometrajeInicial = ET.SubElement(alquiler, 'Kilometraje Inicial')
                                kilometrajeInicial.text =scan
                                
                                kilometrajeFinal = ET.SubElement(alquiler, 'Kilometraje Final')
                                kilometrajeFinal.text ='-'
                                
                                precioFinal = ET.SubElement(alquiler, 'Precio Final')
                                precioFinal.text ='-'
                                
                                recargo = ET.SubElement(alquiler, 'Recargo')
                                recargo.text ='De momento 0'
                                
                                alquileres.append(alquiler) 
                                print('Has añadido un nuevo alquiler(',atributo,') a la lista de alquileres')
                            else:
                                print ('Has introducido mal 3 veces el kilometraje inicial, saldras de este menu')
                        else:
                            print ('Has introducido mal 3 veces la fecha de inicio, saldras de este menu')
                    else:
                        print ('Has introducido mal 3 veces el ID de Cliente, saldras de este menu')
                else:
                    print ('No existe ese vehiculo')
            else:
                print ('Has introducido mal 3 veces el ID de Vehiculo, saldras de este menu')
        else:
            print ('Ya existe ese alquiler')
    else:
        print ('Has introducido mal 3 veces el ID de Alquiler, saldras de este menu')
    return 0

def modificar(root):
    idAlquiler=input("introduce el nombre de la empresa que quieres modificar")
    #nose hace falta una cosa en utiles (los escaneres)
    if(Utiles.validacionIDAlquiler()):
        nodo=buscar(top,idAlquiler)
        if(nodo!=None):
            print("Introcuce el campo que quieres modificar\n1 ID Alquiler\n2 ID Vehiculo\n3 ID Cliente\n4 Fecha Inicio\n5 Fecha Devolucion\n6 Kilometraje Inicial\n7 Kilometraje Final\n8 precio Final\n9 Recargo")
            opcion=input()
            if(opcion=="1"):
                scan=Utiles.validacionIDAlquiler()
                if(scan!=None):
                    toot[nodo].attrib['alquilerID']=scan
                else:
                    print ('Has introducido mal 3 veces el ID de Alquiler, saldras de este menu')
            elif(opcion=="2"):
                scan=Utiles.validacionIDVehiculo()
                if(scan!=None):
                    root[nodo][0].text=scan
                else:
                    print ('Has introducido mal 3 veces el ID de Alquiler, saldras de este menu')
            elif(opcion=="3"):
                scan=Utiles.validacionIDCliente()
                if(scan!=None):
                    root[nodo][1].text=scan
                else:
                    print ('Has introducido mal 3 veces el ID de Cliente, saldras de este menu')
            elif(opcion=="4"):
                scan=Utiles.validacionFechaDeInicio()
                if(scan!=None):
                    root[nodo][2].text=scan
                else:
                    print ('Has introducido mal 3 veces el fecha de inicio, saldras de este menu')
            elif(opcion=="5"):
                scan=Utiles.validacionFechaDevolucion()
                if(scan!=None):
                    root[nodo][3].text=scan
                else:
                    print ('Has introducido mal 3 veces el fecha de devolucion, saldras de este menu')
            elif(opcion=="6"):
                scan=Utiles.validacionKilometrajeInicial()
                if(scan!=None):
                    root[nodo][4].text=scan
                else:
                    print ('Has introducido mal 3 veces el kilometraje inicial, saldras de este menu')
            elif(opcion=="7"):
                scan=Utiles.validacionKilometrajeFinal()
                if(scan!=None):
                    root[nodo][5].text=scan
                else:
                    print ('Has introducido mal 3 veces el kilometraje final, saldras de este menu')
            elif(opcion=="8"):
                scan=Utiles.validacionPrecioFinal()
                if(scan!=None):
                    root[nodo][6].text=scan
                else:
                    print ('Has introducido mal 3 veces el precio final, saldras de este menu')
            elif(opcion=="9"):
                scan=Utiles.validacionRecargo()
                if(scan!=None):
                    root[nodo][7].text=scan
                else:
                    print ('Has introducido mal 3 veces el recargo, saldras de este menu')
            else:
                print("escribe bien anda")
            BaseDeDatos.guardar(top)
        else:
            print("error")
    return 0
def buscarMostrarTodosVehiculo(alquileres):
    texto=input("Introduce el id del coche que quieres ver los alquileres")
    for x in alquileres:
        if(x[0].text.lower()==texto.lower()):
            print("He ecnontrado: ",i.text)
            Utiles.recorrer(x)
    return 0
def buscarMostrarTodosDni(alquileres):
    texto=input("Introduce el id del cliente que quieres ver los alquileres")
    for x in alquileres:
        if(x[1].text.lower()==texto.lower()):
            print("He ecnontrado: ",i.text)
            Utiles.recorrer(x)
    return 0
def buscarMostrar(alquileres):
    texto=input("Introduce el id del alquiler que quieres ver")
    for x in alquileres:
        if( nodo.attrib['alquilerID'].lower()==texto.lower()):
            print("He ecnontrado: ",i.text)
            Utiles.recorrer(x)
    return 0
def buscarPosicion(alquileres,texto):
    nodo=0
    for x in alquileres:
        if( nodo.attrib['alquilerID'].lower()==texto.lower()):
            print("He ecnontrado: ",i.text)
            Utiles.recorrer(x)
            return nodo
        nodo+=1
    return None
def mostrar(root):
    Utiles.recorrer(root)
    return 0

def escanerAlfannumerico():
    intentos=0
    while(intentos<3):
        scan=imput()
        if(scan.isspace()!=False and scan.isalnum() ):
            return scan
        print('Porfavor introduce alfanumericos')
    return None


