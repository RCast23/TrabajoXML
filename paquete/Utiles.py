#def validacion(): 3 intentos

#def reintentar(): (Para crear, borrar y modificar)

#def modificar(): (Confirmacion)


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