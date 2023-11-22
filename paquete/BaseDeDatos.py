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
        vehiculos.text=''
        alquileres = ET.SubElement(root,'Alquileres')
        alquileres.text=''
        print("Agenda creada")
        return arbol, root

def guardarArchivo(root):
    tab = prettify(root)
    file=open("agenda.xml","w")
    file.write(tab)
    file.close()
    file=open("agenda.xml","r")

def prettify(elem):
    rough_string = ET.tostring(elem,encoding='utf-8', method='xml')
    reparsed = minidom.parseString(rough_string)
    return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

