import xml.etree.ElementTree as ET

def comprobarArchivo(arbol,agenda):
    try:
        arbol = ET.parse('agenda.xml')
        agenda = arbol.getroot()
        print("Agenda cargada")
        return agenda
    except:
        agenda = ET.Element('Agenda')
        print("Agenda creada")
        return agenda

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

