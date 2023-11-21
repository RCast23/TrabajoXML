import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.etree.ElementTree import ElementTree

def comprobarArchivo(arbol,root):
    try:
        arbol = ET.parse('agenda.xml')
        root = arbol.getroot()
        print("Agenda cargada")
        return arbol, root
    except:
        root = ET.Element('Agenda')
        vehiculos = ET.SubElement(root,'Vehiculos')
        alquileres = ET.SubElement(root,'Alquileres')
        print("Agenda creada")
        return arbol, root

def guardarArchivo(root):
    tab = prettify(root)
    file=open("agenda.xml","w")
    ElementTree(root).write(tab)
    #file.write(str(ET.(root,'utf-8')))
    file.close()
    file=open("agenda.xml","r")

def prettify(elem):
    rough_string = str(ET.tostring(elem,'utf-8'))+"a"
    print("Si soy"+rough_string.split("'")[1])
    reparsed = minidom.parseString(rough_string.split("'")[1])
    return reparsed.toprettyxml()

