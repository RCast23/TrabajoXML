import xml.etree.ElementTree as ET

def crear(top):
    
    scan=input("dame un ID de alquiler")
    alquiler = ET.Element('Alquiler',{'alquilerID':scan})
    
    idVehiculo = ET.SubElement(alquiler, 'ID Vehiculo')
    scan=input("dame un ID de vehiculo")#que llame a utiles con un escaner  que verifique
    #metodo que te diga si existe el vehiculo(el buscar de vehiculo)
    idVehiculo.text =scan
    
    idCliente = ET.SubElement(alquiler, 'ID Cliente')
    scan=input("dame un ID de cliente")#que llame a utiles con un escaner  que verifique
    idCliente.text =scan
    
    fechaInicio = ET.SubElement(alquiler, 'Fecha Inicio')
    scan=input("dame una fecha de inicio")#que llame a utiles con un escaner  que verifique
    fechaInicio.text =scan
    
    fechaDevolucion = ET.SubElement(alquiler, 'Fecha Devolucion')
    fechaInicio.text ='Fecha devolucion todavia no dada'
    
    kilometrajeInicial = ET.SubElement(alquiler, 'Kilometraje Inicial')
    scan=input("dame un kilometraje inicial")#que llame a utiles con un escaner  que verifique
    kilometrajeInicial.text =scan
    
    kilometrajeFinal = ET.SubElement(alquiler, 'Kilometraje Final')
    kilometrajeFinal.text ='Kilometraje final todavia no dado'
    
    precioFinal = ET.SubElement(alquiler, 'Precio Final')
    precioFinal.text ='Precio final todavia no dado'
    
    recargo = ET.SubElement(alquiler, 'Recargo')
    recargo.text ='Recargo de momento 0'
    
    top.append(alquiler) 
    guardar(top.getparent())
    return 0

def modificar(top):
    #decidir como vamos a hacer los buscar antes de hacer nada
    print("introduce el nombre de la empresa que quieres modificar")
    nodo1,nodo2=buscar(top)
    if(nodo1!=False):
        print("introcuce el campo que quieres modificar\nNombre 1\nNumero empleados 2\nFacturacion 3")
        opcion=input()
        if(opcion=="1"):
            top[nodo1][0].text=input("introduce el nuevo nombre")
        elif(opcion=="2"):
            top[nodo1][1].text=input("introduce el nuevo numero de empleados")
        elif(opcion=="3"):
            top[nodo1][2].text=input("introduce el nuevo numero de facturacion")
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
def buscarPosicion(alquileres):
    texto=input("Introduce el id del alquiler que quieres ver")
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



