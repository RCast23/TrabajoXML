'''
Created on 10 nov 2023

@author: Roberto
'''
def crear(top):
    emp1 = ET.SubElement(top,'empresa')
    
    nombre = ET.SubElement(emp1, 'nombre')
    nombre.text =input("dame un nombre")
    
    n_empleados = ET.SubElement(emp1, 'N_empleados')
    n_empleados.text =input("dame un numero de empleados")
    
    facturacion = ET.SubElement(emp1, 'Facturacion')
    facturacion.text = input("dame un numero de facturacion")
    
    #top.append(emp1)
    guardar(top)
    return 0

def modificar(top):
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


def prettify(elem):
    #prettify esta en base de datos
    from xml.etree import ElementTree
    from xml.dom import minidom
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


