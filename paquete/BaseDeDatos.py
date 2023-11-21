import xml.etree.ElementTree as ET

def comprobarArchivo(arbol,root):
    try:
        arbol = ET.parse('root.xml')
        root = arbol.getroot()
        print("Agenda cargada")
        return arbol, root
    except:
        root = ET.Element('Agenda')
        print("Agenda creada")
        return arbol, root

def guardarArchivo(agenda):
    tab = prettify(agenda)
    file=open("agenda.xml","w")
    file.write(tab)
    file.close()
    file=open("agenda.xml","r")
    fileAux=open('auxXml.xml','w')
    fileAux.close()

def prettify(elem):
    from xml.etree import ElementTree
    from xml.dom import minidom
    rough_string = ElementTree.tostring(elem,'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

