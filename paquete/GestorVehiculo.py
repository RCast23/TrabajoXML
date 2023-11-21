import xml.etree.ElementTree as ET
from paquete.BaseDeDatos import guardarArchivo

def crear(agenda):
    scan=input("dame una matricula")#que llame a utiles con un escaner  que verifique
    vehiculo = ET.SubElement(agenda,'Vehiculo',{'atr1':scan})
    
    matricula = ET.SubElement(vehiculo, 'Matricula')
    scan=input("dame una matricula")#que llame a utiles con un escaner  que verifique
    matricula.text =scan
    
    marcaYmodelo = ET.SubElement(vehiculo, 'Marca y Modelo')
    scan=input("dame una marca y modela")#que llame a utiles con un escaner  que verifique
    marcaYmodelo.text =scan
    
    annoDeFabricacion = ET.SubElement(vehiculo, 'Anno De Fabricacion')
    scan=input("dame un Anno De Fabricacion")#que llame a utiles con un escaner  que verifique
    annoDeFabricacion.text =scan
    
    tarifa = ET.SubElement(vehiculo, 'Tarifa')
    scan=input("dame una tarifa por dia")#que llame a utiles con un escaner  que verifique
    tarifa.text =scan
    
    estadoVehiculo = ET.SubElement(vehiculo, 'Estado Vehiculo')
    scan=input("dame un estado del vehiculo")#que llame a utiles con un escaner  que verifique
    estadoVehiculo.text =scan
    
    #top.append(emp1) al mandar el root no hace falta 
    guardarArchivo(agenda)
    
def borrar(agenda): #Requiere confirmacion
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
