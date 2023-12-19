import datetime

def confirmacion():
    '''
    Metodo para confirmar si se quiere confirmar una operacion
    :return Devuelve un un boolean. El valor sera True si escribe 'si' y False si escribe 'no'
    '''
    cont = 0
    while(True):
        inputConfirmacion = input()
        if(inputConfirmacion.lower() == 'si'):
            return True
        elif(inputConfirmacion.lower() == 'no' or cont == 2):
            if(cont==2):
                print("\nSe ha superado el numero de intentos")
            return False
        else:
            print("\nValor incorrecto, pruebe otra vez")
        cont+=1
        
def recorrer(nodo):
    '''
    Metodo que recorre de forma recursiva el nodo del introducido arbol XML 
    :param nodo: Nodo introducido del arbol XML
    '''
    #Nodo es bascamente un vehiculo o todos los vehiculos o root ya que es recursivo
    #printea todos los datos del elemento y si hay subelemento tambien
    attrName=''
    attrValue=''
    if(nodo.tag=='Alquiler' or nodo.tag=='Vehiculo'):
        print('====='*10)
    print("\nNodo:",nodo.tag)
    #Para recorrer los atributos. Los atributos estan en un diccionario
    
    for attr in nodo.attrib:
        attrName = attr
        attrValue = nodo.attrib[attr]
        if(attrName!='matricula' and attrName!='tarifa'):
            print(attrName,"/ ",attrValue)
        
    if(attrName!='vehiculoID' and attrName!='alquilerID'):
        if(attrName!='matricula' and attrName!='tarifa'):
            print(nodo.text)
        else:
            print(nodo.attrib['matricula'])
    
    for n in nodo:
        print()
        recorrer(n)
    return 0

def recolectarIDVehiculo(root):
    '''
    Metodo para obtener todas las ID de vehiculos tanto del nodo Vehiculos como del nodo Alquileres
    :param root: Elemento raiz del documento XML
    :return Diccionario con todas las ID de vehiculos tanto del nodo Vehiculos como del nodo Alquileres
    '''
    #Diccionario en el que se van a guardar todas las ID
    idList={}
    #Bucle for each que guarda todas las ID de vehiculo en Vehiculos
    for x in root[0]:
        idList[x.get('vehiculoID')]='a'
    #Bucle for each que guarda todas las ID de vehiculo en Alquileres    
    for x in root[1]:
        idList[x.get('ID_Vehiculo')]='a'
        
    return idList

def comprobarIDVehiculo(idVehiculo,root):
    '''
    Se comprueba que la ID de vehiculo introducida no este tanto en el nodo Vehiculos como en el nodo Alquileres
    :param idVehiculo: ID del vehiculo a comprobar
    :param root: Elemento raiz del documento XML
    :return Devuelve la ID del vehiculo si lo encuentra y None si no
    '''
    return recolectarIDVehiculo(root).get(idVehiculo,root)

def autoasignarIDVehiculo(root):
    '''
    Metodo para asignar automaticamente la ID de un vehiculo
    :param root: Elemento raiz del documento XML
    :return Nueva ID para el vehiculo
    '''
    #Se hace un contador que se ira modificando en funcion a las ID existentes que se encuentren
    cont = 1
    #Se obtiene una lista con todas las ID de vehiculos y se hace un bucle para comprobar si exite la ID a introducir
    idList=recolectarIDVehiculo(root)
    
    while(True):
        if(idList.get(str(cont))==None):
            return str(cont)
        else:
            #Si la ID existe se suma 1
            cont+=1
            
def autoasignarIDAlquier(root):
    '''
    Metodo para asignar automaticamente la ID de un Alquiler
    :param root: Elemento raiz del documento XML
    :return Nueva ID para el Alquiler
    '''
    #Se hace un contador que se ira modificando en funcion a las ID existentes que se encuentren
    cont = 1
    #Se obtiene una lista con todas las ID alquileres y se hace un bucle para comprobar si ya exite
    idList={}
    for x in root[1]:
        idList[x.get('alquilerID')]='a'
    
    while(True):
        if(idList.get(str(cont))==None):
            return str(cont)
        else:
            #Si la ID existe se suma 1
            cont+=1

def modificarIDVehiculoCascada(root,idVieja,idNueva):
    '''
    Metodo para modificar la ID de un vehiculo en los alquileres
    :param root: Elemento raiz del documento XML
    :param idVieja: Antigua ID del vehiculo
    :param idNueva: Nueva ID del vehiculo
    '''
    #Bucle que compueba la ID de vehiculo en cada alquiler y si lo encuentra lo sutituye
    for i in root[1]:
        if(i[0]==idVieja):
            i[0]=idNueva

def modificarMatriculaVehiculoCascada(root,matriculaVieja,matriculaNueva):
    '''
    Metodo para modificar la matricula de un vehiculo en los alquileres
    :param root: Elemento raiz del documento XML
    :param matriculaVieja: Antigua ID del vehiculo
    :param matriculaNueva: Nueva ID del vehiculo
    '''
    #Bucle que compueba la matricula del vehiculo en cada alquiler y si lo encuentra lo sutituye
    for i in root[1]:
        if(i[0].get('matricula')==matriculaVieja):
            i[0].set('matricula',matriculaNueva)

def escanerID(root):
    '''
    Metodo para escanear una nueva ID de vehiculo
    :param root: Elemento raiz del documento XML
    :return Si la ID es valida devuelve una ID si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se suma el contador de intentos al iniciar la iteracion
        intentos+=1
        #Se comprueba si el texto introducido consiste solo en numeros
        scan=input()
        if(scan.isspace()==False and scan.isnumeric()):
            #Se comprueba que la ID introducida no exista ya y si no lo hace se devuelve
            if(comprobarIDVehiculo(scan,root)):
                return scan
            else:
                print("\nEl ID introducido ya esta asigando a otro vehiculo o se encuentra en el registro de alquileres")
        else:
            print('\nPorfavor introduce numeros no decimales')
    print("\nHas superado el numero de intentos")
    return None

def escanerTexto():
    '''
    Metodo para escanear un texto
    :return Si el texto es valido devuelve el texto si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce el texto y si hay algo escrito se devuelve
        scan=input()
        if(scan.isspace()==False):
            return scan
        intentos+=1
        print('\nPorfavor introduce algun caracter')
    print("\nHas superado el numero de intentos")
    return None

def escanerAlfanumerico():
    '''
    Metodo para escanear una cadena sin espacios
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce la cadena y si no hay espacios se devuelve
        scan=input()
        if(scan.isspace()==False and scan.isalnum() ):
            return scan
        intentos+=1
        print('\nPorfavor introduce alfanumericos')
    print("\nHas superado el numero de intentos")
    return None

def escanerAlfabetico():
    '''
    Metodo para escanear una cadena con solo letras
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce la cadena y si solo hay letras se devuelve
        scan=input()
        if(scan.isspace()==False and scan.isalpha() ):
            return scan
        intentos+=1
        print('\nPorfavor introduce alfabeticos')
    print("\nHas superado el numero de intentos")
    return None

def escanerNumerico():
    '''
    Metodo para escanear una cadena con solo numeros
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        scan=input()
        #Se introduce la cadena y si solo hay letras se devuelve
        if(scan.isspace()==False and scan.isnumeric() ):
            return scan
        intentos+=1
        print('\nPorfavor introduce numeros no decimales')
    print("\nHas superado el numero de intentos")
    return None

def escanerNumericoDecimal():
    '''
    Metodo para escanear una cadena de numeros con decimales
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        intentos+=1
        #Se introduce la cadena y se le hace un split por el punto
        scan=input()
        scanSplitPunto=scan.split('.')
        
        #Se comprueba que la cadena no esta vacia y si el split ha creado uno o dos valores
        if(scan.isspace()==False and len(scanSplitPunto)==1 or len(scanSplitPunto)==2):
            
            #Si el split solo crea un valor se comprueba si es un numero y se le agrega '.00' y se devuelve
            if(len(scanSplitPunto)==1 and scan.isnumeric()):
                return scan+'.00'
            
            #Si el split crea dos valores se comprueba que ambos sean numeros se comprueba la longitud del segundo campo
            elif(len(scanSplitPunto)==2 and scanSplitPunto[0].isnumeric() and scanSplitPunto[1].isnumeric()):
                
                #Si el segundo campo tiene longitud 1 se devuelve con un 0 delante
                if(len(scanSplitPunto[1])==1):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]+'0'
                
                #Si el segundo campo tiene longitud 2 se devuelve tal cual
                elif(len(scanSplitPunto[1])==2):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]
                
                #Si el segundo campo tiene mas de 2 valores se pide que se vuelva a introducir
                else:
                    print('\nPorfavor introduce solo 2 decimales')
            else:
                print('\nFormato de decimales incorrecto')
        else:
            print('\nPorfavor introduce numeros y los decimales con punto')
    print("\nHas superado el numero de intentos")
    return None

def escanerMatricula():
    '''
    Metodo para escanear una matricula
    :return Si la cadena es valida devuelve la matricula, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce la matricula y se comprueba el formato, si cumple se devuelve
        scan=input()
        if(scan.isspace()==False and len(scan)==7):
            if(scan[0:3].isnumeric() and scan[4:6].isalpha()):
                return scan.upper()
            
        intentos+=1
        print('\nPorfavor introduce una matricula (Cuatro numeros y tres letras)')
    print("\nHas superado el numero de intentos")
    return None

def escanerDni():
    '''
    Metodo para escanear un DNI
    :return Si la cadena es valida devuelve el DNI, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce el DNI y se comprueba el formato, si cumple se devuelve
        scan=input()
        if(scan.isspace()==False and len(scan)==9):
            if(scan[0:7].isnumeric() and scan[8].isalpha()):
                return scan.upper()
            
        intentos+=1
        print('\nPorfavor introduce un DNI (Ocho numeros y una letra)')
    print("\nHas superado el numero de intentos")
    return None

def escanerFecha():
    '''
    Metodo para escanear el dia, mes y anno de un alquiler
    :return Si la cadena es valida devuelve una fecha, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se crea un boolean para comprobar si se debe continuar introduciendo datos
        continuar=True
        #Se introduce un dia y se comprueba que sea un numero entre 1 y 31, si no continuar se cambia a false
        print("\nIntroduzca un dia")
        dia=input()
        if(dia.isspace() or dia.isnumeric()==False or int(dia)>31 or int(dia)<=0):
            continuar=False
        #Se introduce un mes y se comprueba que continuar sea true y que sea un numero entre 1 y 12, si no continuar se cambia a false
        if(continuar):
            print("\nIntroduzca un mes")
            mes=input()
            if(mes.isspace() or mes.isnumeric()==False or int(mes)>12 or int(mes)<=0 or continuar==False):
                continuar=False   
        #Se introduce un anno y se comprueba que continuar sea true y que sea un numero entre 2000 y 3000, si no continuar se cambia a false
        if(continuar):
            print("\nIntroduzca un anno") 
            anno=input()
            if(anno.isspace() or anno.isnumeric()==False or int(anno)>3000 or int(anno)<2000 or continuar==False):
                continuar=False 
        #Si continuar sigue siendo true se castea a datetime y se devuelve la string de la fecha
        if(continuar):
            try:
                x = datetime.datetime(int(anno), int(mes), int(dia))
                return x.strftime("%d-%m-%Y")
            except:
                print("\nLa fecha introducida no es una fecha real")
        intentos+=1
        print('\nPorfavor introduce una fecha correcta (Dia 1-31 mes 1-12 anno 2000-3000)')
    print("\nHas superado el numero de intentos")
    return None

def escanerYear():
    '''
    Metodo para escanear el anno de fabricacion de un vehiculo
    :return Si la cadena es valida devuelve un anno, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se introduce el anno y se comprueba el formato y si el anno esta entre el anno actual y 1886, si cumple se devuelve
        anno=input()
        hoy = datetime.date.today()
        if(anno.isnumeric() and len(anno)==4 and int(anno) <=hoy.year and int(anno)>1886):
            return anno+''
        intentos+=1
        print("\nPorfavor introduce un anno correcto (4 digitos entre 1886 y el anno actual)")
    print("\nHas superado el numero de intentos")
    return None

def escanerEstadoVehiculo():
    '''
    Metodo para escanear el anno de fabricacion de un vehiculo
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 3 intentos
    intentos=0
    while(intentos<3):
        #Se crea un bucle con todas las opciones para el estado
        print("\nIntroduzca el nuevo estado del vehiculo:\n1.Disponible\n2.Ocupado\n3.Averiado\n4.Otro")
        numOpcion = escanerNumerico();
        
        if(numOpcion=='1'):
            return 'Disponible'
        
        elif(numOpcion=='2'):
            return 'Ocupado'
        
        elif(numOpcion=='3'):
            return 'Averiado'
        
        elif(numOpcion=='4'):
            print('\nIntroduzca el nuevo estado del vehiculo')
            return escanerAlfabetico()
        
        else:
            print('\nOpcion no valida')
            
    print('\nHas superado el numero de intentos')
    return None
        

#necesito en utiles fechaDevolucionSuperior(fecha1, fecha2) un metodo en el cual mandes(fecha1, fecha2) y si la fecha 2 es superior a la 1 devuelve la diferencia si no, devuelve None
def fechaDevolucionSuperior(fecha1, fecha2):
    '''
    Metodo en el cual se mandan 2 fechas y se comprueba que la fecha 2 es superior a la 1
    :param fecha1: Primera fecha a comprobar
    :param fecha2: Segunda fecha a comprobar
    :return Si la fecha 2 es superior a la 1 se devuelve la cantidad de dias de diferencia, si no se devuelve none
    '''
    #Se convierten las cadenas de fechas en fechas datetime y se comparan
    fechaConvertida1 = datetime.datetime(int(fecha1.split('-')[2]),int(fecha1.split('-')[1]),int(fecha1.split('-')[0]))
    fechaConvertida2 = datetime.datetime(int(fecha2.split('-')[2]),int(fecha2.split('-')[1]),int(fecha2.split('-')[0]))
    if(fechaConvertida2>fechaConvertida1):
        return str(fechaConvertida2-fechaConvertida1).split(' ')[0]
    else:
        return None
    
def confirmarFecha(fecha1):
    '''
    Metodo para comprobar si la fecha introducida es inferior o igual a la fecha actual
    :param fecha1: Fecha a comprobar
    :return Boolean True si la fecha introducida es inferior o igual a la fecha acutal y False si no
    '''
    fechaConvertida1 = datetime.datetime(int(fecha1.split('-')[2]),int(fecha1.split('-')[1]),int(fecha1.split('-')[0]))
    hoy=datetime.datetime.today()
    if(fechaConvertida1>=hoy):
        return True
    else:
        return False
    
def comprobarDisponibilidad(fecha, root,idAlquiler):
    '''
    Metodo para comprobar si un vehiculo esta disponible en una fecha determinada
    :param fecha: Fecha a comprobar
    :param root: Elemento raiz del documento XML
    :param fecha: la id del vehiculo a comprobar para que no se compare consigo mismo
    :return Devuelve un boolean que sera True si el vehiculo no esta alquilado en esa fecha y False si si lo esta
    '''
    #Bucle que recorre todo el nodo Alquileres y comprueba que la fecha introducida no este entre las fechas de inicio y fin de alquiler
    for i in root[1]:
        if(fechaDevolucionSuperior(fecha, i[2].text)==None and fechaDevolucionSuperior(fecha, i[3].text)!=None):
            print(idAlquiler)
            if(i.attrib['alquilerID'].lower!=idAlquiler.lower):
                return False
    return True
        
def comprobarKilometraje(kilometraje, root):
    '''
    Metodo para comprobar si el kilometraje introducido es inferior a otro anterior de ese mismo vehiculo
    :param kilometraje: Kilometraje de un vehiculo
    :param root: Elemento raiz del documento XML
    :return Boolean que devuelve True si ese es el maximo kilometraje registrado de un vehiculo y False si no
    '''
    #Bucle que recorre todo el nodo Alquileres y comprueba que el kilometraje introducida no sea inferior a otro registrado
    for i in root[1]:
        if((i[6].text!='-' and float(kilometraje)<float(i[6].text)) or float(kilometraje)<float(i[5].text)):
            return False
    return True