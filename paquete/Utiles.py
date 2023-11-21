#def validacion(): 3 intentos
    
def confirmacion():
    while(True):
        inputConfirmacion = input()
        if(inputConfirmacion.lower() == 'si'):
            return True
        elif(inputConfirmacion.lower() == 'no'):
            return False
        else:
            print("Valor incorrecto, pruebe otra vez")
        

def recorrer(nodo):
    #Nodo es bascamente un vehiculo o todos los vehiculos o root ya que es recursivo
    #printea todos los datos del elemento y si hay subelemento tambien
    print("Tipo nodo: ",nodo.tag,end="")
    #Para recorrer los atributos. Los atributos estan en un diccionario
    for attr in nodo.attrib:
        attrName = attr
        attrValue = nodo.attrib[attr]
        print("\t","Nombre atributo: ",attrName,"/ Valor atributo: ",attrValue," ",end="")
    print("\nNodo:","\t",nodo.text)
    for n in nodo:
        recorrer(n)
    return 0