import xml.etree.ElementTree as ET

def crear(top):
    alquiler = ET.SubElement(top,'Alquiler',{'atr1':"ID"})
    
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
    
    #top.append(emp1) al mandar el root no hace falta 
    guardar(top)
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
        guardar(top)
    else:
        print("error")
    return 0

def buscar(nodo):
    texto=input()
    nodo1=0
    nodo2=0
    encontrado=False
    for x in top:
        for i in x:
            if(i.text==texto):
                print("He ecnontrado: ",i.text)
                print(prettify(x))
                encontrado=True
                return nodo1,nodo2
            nodo2+=1
        nodo1+=1
    return encontrado,encontrado

def mostrar(top):
    recorrer(top)
    #print(prettify(top))
    return 0



