import xml.etree.ElementTree as ET
import MainXML
import BaseDeDatos 
import Utiles

def crear(alquileres):
    continuar=True
    #---------------------------------------
    
    alquiler = ET.Element('Alquiler',{'alquilerID':atributo})
        
    #-----------------------------------------
    print("Dame un ID de vehiculo") 
    scan=Utiles.escanerMatricula()
    if(scan!=None and continuar): 
        if(GestorVehiculo.buscarMatricula(scan, MainXML.root[0])!=None):
            idVehiculo = ET.SubElement(alquiler, 'ID_Vehiculo')
            idVehiculo.text =scan
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
        
        precioFinal = ET.SubElement(alquiler, 'Precio:Final')
        precioFinal.text ='-'
        
        recargo = ET.SubElement(alquiler, 'Recargo')
        recargo.text ='De momento 0'
        
        alquileres.append(alquiler) 
        print('Has añadido un nuevo alquilerç a la lista de alquileres')
    else:
        continuar=False
        
    return 0

def modificar(root):
    if(Utiles.validacionIDAlquiler()):
        nodo=buscarPosicion(top,vehiculo,dni)
        continuar=True
        while(continuar):
            if(nodo!=None):
                # por si aaso crear una copia de los datos originales y cambiar el nombre a todos los campos
                
                print("Introcuce el campo que quieres modificar\n1 ID Alquiler\n2 ID Vehiculo\n3 ID Cliente\n4 Fecha Inicio\n5 Fecha Devolucion\n6 Kilometraje Inicial\n7 Kilometraje Final\n8 precio Final\n9 Recargo\n0 Salir")
                opcion=Utiles.escanerNumerico()
                if(opcion=="1"):
                    scan=Utiles.escanerNumerico()
                    if(scan!=None):
                        root[nodo].attrib['alquilerID']=scan
                elif(opcion=="2"):
                    scan=Utiles.escanerMatricula()
                    if(scan!=None):
                        root[nodo][0].text=scan
                elif(opcion=="3"):
                    scan=Utiles.escanerDni()
                    if(scan!=None):
                        root[nodo][1].text=scan
                elif(opcion=="4"):
                    scan=Utiles.escanerFecha()
                    if(scan!=None):
                        root[nodo][2].text=scan
                elif(opcion=="5"):
                    scan=Utiles.escanerFecha()
                    if(scan!=None):
                        root[nodo][3].text=scan
                elif(opcion=="6"):
                    scan=Utiles.escanerNumericoDecimal()
                    if(scan!=None):
                        root[nodo][4].text=scan
                elif(opcion=="7"):
                    scan=Utiles.escanerNumericoDecimal()
                    if(scan!=None):
                        root[nodo][5].text=scan
                elif(opcion=="8"):
                    scan=Utiles.escanerNumericoDecimal()
                    if(scan!=None):
                        root[nodo][6].text=scan
                elif(opcion=="9"):
                    scan=Utiles.escanerNumericoDecimal()
                    if(scan!=None):
                        root[nodo][7].text=scan
                elif(opcion=="0"):
                    continuar=False
                else:
                    print("Escribe un numero dentro de las opciones posibles")
                
            else:
                print("No encontrado ningun alquiler con la matricula de ese coche y ese dni de cliente")
            print("Quieres guardar los cambios realizados?")
            if(Utiles.confirmacion()):
                #Preguntar a roberto como carajos guardo algo
                BaseDeDatos.guardar(top)
    return 0
def buscarMostrarTodosVehiculo(alquileres):
    texto=input("Introduce el id del coche que quieres ver los alquileres")
    for x in alquileres:
        if(x[0].text.lower()==texto.lower()):
            print("He ecnontrado: ",x.text)
            Utiles.recorrer(x)
    return 0
def buscarMostrarTodosDni(alquileres):
    texto=input("Introduce el id del cliente que quieres ver los alquileres")
    for x in alquileres:
        if(x[1].text.lower()==texto.lower()):
            print("He ecnontrado: ",x.text)
            Utiles.recorrer(x)
    return 0
def buscarMostrar(alquileres):
    
    vehiculo=input("Introduce la matricula del vehiculo que quieres ver")
    dni=input("Introduce el dni del cliente que quieres ver")
    
    for x in alquileres:
        if( x[0].text.lower()==vehiculo.lower() and x[1].text.lower()==dni.lower()):
            print("He ecnontrado: ",x.text)
            Utiles.recorrer(x)
    return 0
def buscarPosicion(alquileres,vehiculo,dni):
    #reacer buscando por matricula y dni
    #con una tupla , tiene que permitir elegir un
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
def mostrar(root):
    Utiles.recorrer(root)
    return 0




