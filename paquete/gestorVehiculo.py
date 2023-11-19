import xml.etree.ElementTree as ET

def alta(agenda):
    empresa = ET.SubElement(agenda,'Empresa')
    
    nombre = ET.SubElement(empresa,'Nombre')
    nombre.text = input("Intoduzca el nombre de la empresa")
    
    numEmpleados = ET.SubElement(empresa,'NumEmpleados')
    numEmpleados.text = input("Intoduzca el numero de empleados de la empresa")
    
    facturacion = ET.SubElement(empresa,'Facturacion')
    facturacion.text = input("Introduzca la facturacion de la empresa")
    
def baja(agenda): #Requiere confirmacion
    empresa = buscar(agenda)
    if(empresa!=None):
        mostrarTodos(empresa)
        confirm=input("¿Seguro que desea borrar esta empresa?")
        if(confirm=='si'):
            agenda.remove(empresa)
            print("Empresa eliminada")

def modificar(agenda): #Requiere confirmacion
    empresa = buscar(agenda)
    if(empresa!=None):
        mostrarTodos(empresa)
        empresa[0].text=input("Introduzca el nuevo nombre de la empresa")
        empresa[1].text=input("Introduzca el nuevo numero de empleados de la empresa")
        empresa[2].text=input("Introduzca la nueva facturacion de la empresa")
    
def buscar(agenda):
    nom = input("Introduzca el nombre de la empresa")
    i=0;
    try:
        while(True):
            aux=agenda[i][0].text            
            if(nom==aux):
                print("Empresa encontrada")
                return agenda[i]
            i+=1
    except:
        print("No se ha encontrado la empresa")
    

def mostrarTodos(agenda):
    print(agenda.tag,end="")
    #Para recorrer los atributos. Los atributos estan en un diccionario
    for attr in agenda.attrib:
        attrName = attr
        attrValue = agenda.attrib[attr]
        print("\t",attrName,":",attrValue," ",end="")
    print("\n\t",agenda.text)
    for n in agenda:
        mostrarTodos(n)
