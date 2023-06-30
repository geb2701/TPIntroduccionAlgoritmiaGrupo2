legajosLista=[3,2,1]
nombresLista=["Juan","Pedro","Maxi"]
listaNotas=[0,0,0]

def ObtenerNombre():
    nombre=input("Ingrese el Nombre del Alumno => ")
    if nombre == "0":
        return ""
    while nombre == "":
        print ("Nombre Invalido")
        print("Ingrese 0 para regresar")
        nombre=input("Ingrese el Nombre del Alumno => ")
        if nombre == "0":
            return ""
    return nombre
    
def EncontrarLegajo(legajo, legajoCreado): #legajoCreado es un bolean0o que determina si existe o no el legajo
                                            #True el legajo ya esta creado
                                            #False el legajo ya no esta creado
    i=0
    legajoBusqueda = False
    while legajoBusqueda == False:
        encontrado=False
        while i < len(legajosLista) and encontrado==False:
            if legajo==legajosLista [i]:
                encontrado=True
            else:
                i += 1
        if encontrado == legajoCreado:
            if legajoCreado == True:
                print ("Este Legajo Ya Existente")
            else: 
                print ("Este Legajo No Existe")
            print("Ingrese 0 para regresar")
            legajo=int(input("Ingrese el Legajo del Alumno => "))
            if legajo == 0:
               return
            i=0
        else:
            legajoBusqueda = True
    return [legajo, i] #retornamos el numero del legajo y su posicion en el array

def OrdenarListas():
    n=len(legajosLista)
    desordenado=True
    while desordenado:
        desordenado=False
        for j in range(1,n):
            if (legajosLista[j-1] > legajosLista[j]):
                
                aux=legajosLista[j-1]
                legajosLista[j-1]=legajosLista[j]
                legajosLista[j]=aux

                aux=nombresLista[j-1]
                nombresLista[j-1]=nombresLista[j]
                nombresLista[j]=aux

                aux=listaNotas[j-1]
                listaNotas[j-1]=listaNotas[j]
                listaNotas[j]=aux
                
                desordenado=True
        n-=1

    for i in range (len(legajosLista)):
        print (str(legajosLista[i]) + ")", nombresLista[i])

    input("Pulse para Continuar => ")

def Confirmar():
    while True:
        ingreso = str(input("¿Desea Confirmar la Operacion? Ingrese 1/Si para Confiramar o 0/No para Cancelar => "))
        if ingreso == "1" or ingreso == "Si" or ingreso == "SI" or ingreso == "si": #no usamos cambiante a lower o upper
            return True
        elif ingreso == "0" or ingreso == "No" or ingreso == "NO" or ingreso == "no": #no usamos cambiante a lower o upper
            return False
        else:
            print ("Error en Confirmacion")
    
def AltaEstudiante():  #Se ingresa legajo y nombre
    print ("Alta Estudiante")
    print("Ingrese 0 para regresar")
    legajo=int(input("Ingrese el Legajo del Alumno => "))
    

    if legajo==0:
        return
    
    encontrarLegajo = EncontrarLegajo(legajo, True)

    legajo = encontrarLegajo[0]

    nombre = ObtenerNombre()
    if nombre == "":
        return

    print("Datos Alta Alumno")
    print("Legajo:", legajo)
    print("Nombre:", nombre)
    confirmacion = Confirmar()
    if confirmacion == True:
        legajosLista.append(legajo)
        nombresLista.append(nombre)
        listaNotas.append(0)
        print("Operacion Exitosa")
    else:
        print("Operacion Cancelada")

    nuevamente = str(input("Pulse 1 si quiere Realizar una Nueva Operación, de lo contario Enter para volver al menu => "))
    if nuevamente == "1": #no usamos cambiante a lower o upper
        AltaEstudiante()
    
def BajaEstudiante(): #se ingresa legajo y se elimina todas las listas de estudiantes
    print ("Baja Estudiante")
    print("Ingrese 0 para regresar =>")
    legajo=int(input("Ingrese el Legajo del Alumno => "))
    
    if legajo==0:
        return
    
    encontrarLegajo = EncontrarLegajo(legajo, False)
    legajo = encontrarLegajo[0]
    indice = encontrarLegajo[1]

    print("Datos Baja Alumno")
    print("Legajo:", str(legajosLista[indice]))
    print("Nombre:", nombresLista[indice])
    confirmacion = Confirmar()
    if confirmacion == True:
        legajosLista.pop(indice)
        nombresLista.pop(indice)
        listaNotas.pop(indice)
        print("Operacion Exitosa")
    else:
        print("Operacion Cancelada")

    nuevamente = str(input("Pulse 1 si quiere Realizar una Nueva Operación, de lo contario Enter para volver al Menu =>"))
    if nuevamente == "1": #no usamos cambiante a lower o upper
        AltaEstudiante()

def ModificacionEstudiante(legajosLista, nombresLista):
    print("Modificacion Estudiante")
    print("Ingrese 0 para regresar =>")
    legajo = int(input("Ingrese el Legajo del Alumno => "))
    
    if legajo == 0:
        return

    encontrarLegajo = EncontrarLegajo(legajo, False)
    legajo = encontrarLegajo[0]
    indice = encontrarLegajo[1]
    
    print(str(legajosLista[indice] + ")", nombresLista[indice]))
    nombre = ObtenerNombre()
    if nombre == "":
        return
        
    print("Datos Modificacion Alumno")
    print("Legajo:", legajo)
    print("Nombre:", nombre)
    confirmacion = Confirmar()
    if confirmacion == True:
        nombresLista[indice] = nombre
        print("Operacion Exitosa")
    else:
        print("Operacion Cancelada")

    nuevamente = str(input("Pulse 1 si quiere Realizar una Nueva Operación, de lo contario Enter para volver al menu => "))
    if nuevamente == "1": #no usamos cambiante a lower o upper
        ModificacionEstudiante()
    
def ListadoEstudiantes():#ordenado por nro. de Legajo (por metodo de selección)
    OrdenarListas()

    for i in range (len(legajosLista)):
        print (str(legajosLista[i]) + ")", nombresLista[i])
        if listaNotas[i] > 0:
            print("Nota:", listaNotas[i])

    input("Pulse para Continuar => ")

def CargaNotaEstudiante():  #Se ingresa legajo y nota (entre 1 y 10,siendo las listaNotas nro. enteros)
                            #En caso que el legajo no haya sido cargado, se debe mostrar la leyenda “Legajo inexistente”. La carga finaliza con legajo igual a -1. 
    print ("Alta Notas")
    print("Ingrese 0 o -1 para regresar")
    legajo=int(input("Ingrese el Legajo del Alumno => "))
    if legajo == 0 or legajo == -1:
        return

    indice=0
    legajoBusqueda = False
    while legajoBusqueda == False:
        encontrado=False
        while indice < len(legajosLista) and encontrado==False:
            if legajo==legajosLista [indice]:
                encontrado=True
            else:
                indice += 1
        if encontrado == False:
            print ("Este Legajo No Existe")
            print("Ingrese 0 o -1 para regresar")
            legajo=int(input("Ingrese el Legajo del Alumno => "))
            if legajo == 0:
               return
            indice=0
        else:
            legajoBusqueda = True
    
    if (listaNotas[indice]!= 0):
        print("Este Alumno ya tiene una Nota Cargada")
    else:
        nota = int(input("Ingrese la Nota del Alumno"))
        while 1 > nota or nota > 10: #validamos que la nota este entre 1 y 10
            print("La Nota debe estar entre 1 y 10")
            print("Ingrese 0 o -1 para regresar")
            nota = int(input("Ingrese la Nota del Alumno"))

        
        confirmacion = Confirmar()
        if confirmacion == True:
            listaNotas[indice] = nota
            print("Operacion Exitosa")
        else:
            print("Operacion Cancelada")

    CargaNotaEstudiante()

        
         
def ListaEstudiantesReprobados():#(nro. de Legajo ,  nombre y nota) 
    print ("a")
    
def ListaEstudiantesAprobados():#(nro. de Legajo ,  nombre y nota) 
    print ("a")
     
def ListadoMejoresEstudiantes(): #estudiantes (nro. de Legajo ,  nombre y nota) de aquellos  que tengan nota más alta 
    print ("a")

def Main():
    finalDePrograma=False
    while finalDePrograma==False:
        MostrarElementos(menuOpciones)
        opcionSeleccionada = int(input("Por Favor Seleccione una Opcion => "))
        if (opcionSeleccionada != 0):
            if opcionSeleccionada == len(menuOpciones):
                finalDePrograma=True
            else:
                menuFunciones[int(opcionSeleccionada - 1)]()
        
        
def MostrarElementos(lista):
    for i in range(len(lista)):
        print(str(i + 1) + ")", lista[i])
    print("0) Repetir Opciones",)

menuFunciones = [
    AltaEstudiante, BajaEstudiante, ModificacionEstudiante, ListadoEstudiantes, CargaNotaEstudiante,
    ListaEstudiantesReprobados, ListaEstudiantesAprobados, ListadoEstudiantes  
]
menuOpciones = [
    "Alta Estudiante", 
    "Baja Estudiante", 
    "Modificacion Estudiante", 
    "Listado Estudiantes", 
    "Carga de Nota Estudiante", 
    "Listado de Estudiantes Reprobados", #Nro. Legajo, Nombre y Nota
    "Listado de Estudiantes Aprobados", #Nro. Legajo, Nombre y Nota
    "Listado de Mejores Estudiantes", #Nro. Legajo, Nombre y Nota
    "Salir del Programa"
] 
Main()