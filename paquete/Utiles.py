import datetime


#crear metodo para encontrar numero de ID mas alto para la autoasignacion
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
    attrName=''
    attrValue=''
    for attr in nodo.attrib:
        attrName = attr
        attrValue = nodo.attrib[attr]
        if(attrName!='matricula'):
            print("\t","Nombre atributo: ",attrName,"/ Valor atributo: ",attrValue," ",end="")
        
    if(nodo.text != ''):
        if(attrName=='matricula'):
            print("\nNodo:",attrValue)
        else:
            print("\nNodo:",nodo.text)
    for n in nodo:
        recorrer(n)
    return 0

def recolectarIDVehiculo(root):
    idList={}
    for x in root[0]:
        idList[x.get('vehiculoID')]='a'
        
    for x in root[1]:
        idList[x.get('ID_Vehiculo')]='a'
        
    return idList

def comprobarIDVehiculo(idVehiculo,root):
    return recolectarIDVehiculo(root).get(idVehiculo,root)

def autoasignarIDVehiculo(root):
    cont = 1
    idList=recolectarIDVehiculo(root)
    while(True):
        if(idList.get(str(cont))==None):
            return str(cont)
        else:
            cont+=1

def modificarIDVehiculoCascada(root,idVieja,idNueva):
    for x in root[1]:
        if(x[0]==idVieja):
            x[0]=idNueva

def modificarMatriculaVehiculoCascada(root,matriculaVieja,matriculaNueva):
    for x in root[1]:
        if(x[0].get('matricula')==matriculaVieja):
            x[0].set('matricula',matriculaNueva)

def escanerID(root):
    intentos=0
    while(intentos<3):
        intentos+=1
        scan=input()
        if(scan.isspace()==False and scan.isnumeric()):
            if(comprobarIDVehiculo(scan,root)):
                return scan
            else:
                print("El ID introducido ya esta asigando a otro vehiculo o se encuentra en el registro de alquileres")
        else:
            print('Porfavor introduce numeros no decimales')
    print("Has superado el numero de intentos")
    return None

def escanerTexto():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False):
            return scan
        intentos+=1
        print('Porfavor introduce algun caracter')
    print("Has superado el numero de intentos")
    return None

def escanerAlfanumerico():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False and scan.isalnum() ):
            return scan
        intentos+=1
        print('Porfavor introduce alfanumericos')
    print("Has superado el numero de intentos")
    return None

def escanerAlfabetico():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False and scan.isalpha() ):
            return scan
        intentos+=1
        print('Porfavor introduce alfabeticos')
    print("Has superado el numero de intentos")
    return None

def escanerNumerico():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False and scan.isnumeric() ):
            return scan
        intentos+=1
        print('Porfavor introduce numeros no decimales')
    print("Has superado el numero de intentos")
    return None

def escanerNumericoDecimal():
    intentos=0
    while(intentos<3):
        intentos+=1
        scan=input()
        scanSplitPunto=scan.split('.')
        if(scan.isspace()==False and len(scanSplitPunto)==1 or len(scanSplitPunto)==2):
            if(len(scanSplitPunto)==1 and scan.isnumeric()):
                return scan+'.00'
            elif(len(scanSplitPunto)==2 and scanSplitPunto[0].isnumeric() and scanSplitPunto[1].isnumeric()):
                if(len(scanSplitPunto[1])==1):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]+'0'
                elif(len(scanSplitPunto[1])==2):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]
                else:
                    print('Porfavor introduce solo 2 decimales')
            else:
                print('Formato de decimales incorrecto')
        else:
            print('Porfavor introduce numeros y los decimales con punto')
    print("Has superado el numero de intentos")
    return None

def escanerMatricula():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False and len(scan)==7):
            if(scan[0:3].isnumeric() and scan[4:6].isalpha()):
                return scan.upper()
        intentos+=1
        print('Porfavor introduce una matricula (Cuatro numeros y tres letras)')
    print("Has superado el numero de intentos")
    return None

def escanerDni():
    intentos=0
    while(intentos<3):
        scan=input()
        if(scan.isspace()==False and len(scan)==9):
            if(scan[0:7].isnumeric() and scan[8].isalpha()):
                return scan.upper()
        intentos+=1
        print('Porfavor introduce un DNI (Ocho numeros y una letra)')
    print("Has superado el numero de intentos")
    return None

def escanerFecha():
    intentos=0
    while(intentos<3):
        continuar=True
        print("Dame un dia")
        dia=input()
        if(dia.isspace() or dia.isnumeric()==False or int(dia)>31 or int(dia)==0):
            continuar=False
        print("Dame un mes")
        mes=input()
        if(mes.isspace() or mes.isnumeric()==False or int(mes)>12 or int(mes)==0 or continuar==False):
            continuar=False   
        print("Dame un anno") 
        anno=input()
        if(anno.isspace() or anno.isnumeric()==False or int(anno)>3000 or int(anno)<2000 or continuar==False):
            continuar=False 
        if(continuar):
            x = datetime.datetime(int(anno), int(mes), int(dia))
            return x.strftime("%d-%m-%Y")
        intentos+=1
        print('Porfavor introduce una fecha correcta (Dia 1-31 mes 1-12 anno 2000-3000)')
    print("Has superado el numero de intentos")
    return None

def escanerYear():
    intentos=0
    while(intentos<3):
        anno=input()
        hoy = datetime.date.today()
        if(anno.isnumeric() and len(anno)==4 and int(anno) <=hoy.year and int(anno)>1886):
            return anno+''
        intentos+=1
        print("Porfavor introduce un anno correcto (4 digitos entre 1886 y el anno actual)")
    print("Has superado el numero de intentos")
    return None

#necesito en utiles fechaDevolucionSuperior(fecha1, fecha2) un metodo en el cual mandes(fecha1, fecha2) y si la fecha 2 es superior a la 1 devuelve la diferencia si no, devuelve None