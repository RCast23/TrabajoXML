import xml.etree.ElementTree as ET
from xml.dom import minidom

def comprobarArchivo(root):
    '''
    Metodo que se usa para cargar los datos del archivo XML o crearlo si no existe
    :param arbol: Arbol del XML del archivo a cargar
    :param root: Elemento raiz del arbol XML
    '''
    #Se intenta cargar el archivo XML y si lo consigue se guarda y se devuelve el arbol y la raiz
    try:
        arbol = ET.parse('Alquiler.xml')
        root = arbol.getroot()
        print("\nArbol XML cargado")
        return root
    
    #Si al cargar salta la excepcion por que no existe se crea un nuevo archivo y un nuevo arbol
    except:
        root = ET.Element('EmpresaAlquiler')
        vehiculos = ET.SubElement(root,'Vehiculos')
        vehiculos.text=''
        alquileres = ET.SubElement(root,'Alquileres')
        alquileres.text=''
        print("\nArbol XML creado")
        return root


def guardarArchivo(root):
    '''
    Metodo para guardar el arbol XML
    :param root: Elemento raiz del arbol XML
    '''
    #Se crea una variable para guardar la raiz con el formato deseado y se escribe en el archivo
    tab = prettify(root)
    file=open("Alquiler.xml","w")
    file.write(tab)
    file.close()


def prettify(root):
    '''
    Metodo para dar formato al elemento raiz del XML
    :param root: Elemento raiz del arbol XML
    '''
    #Se transforma la raiz a una string y se le da formato con el toprettyxml
    rough_string = ET.tostring(root,encoding='utf-8', method='xml')
    reparsed = minidom.parseString(rough_string)
    return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

