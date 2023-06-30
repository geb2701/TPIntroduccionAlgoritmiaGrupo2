legajosLista=[1,2,3]
nombresLista=["Juan","Pedro","Maxi"]
notas=[0,0,0]

def Confirmar():
    while True:
        ingreso = str(input("¿Desea Confirmar la Operacion? Ingrese 1/Si para Confiramar o 0/No para Cancelar =>"))
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
    i=0

    if legajo==0:
        return
    legajoNuevo = False
    while legajoNuevo == False:
        encontrado=False
        while i < len(legajosLista) and encontrado==False:
            if legajo==legajosLista [i]:
                encontrado=True
            else:
                i += 1
        if encontrado == True:
            print ("Legajo Existente")
            print("Ingrese 0 para regresar")
            legajo=int(input("Ingrese el Legajo del Alumno => "))
            if legajo == 0:
               return
        else:
            legajoNuevo = True

    nombre=input("Ingrese el Nombre del Alumno => ")
    if nombre == "":
        print ("Nombre Invalido")
        print("Ingrese 0 para regresar")
        nombre=input("Ingrese el Nombre del Alumno => ")
        if nombre == 0:
            return

    print("Datos Alta Alumno")
    print("Legajo:", legajo)
    print("Nombre:", nombre)
    confirmacion = Confirmar()
    if confirmacion == True:
        legajosLista.append(legajo)
        nombresLista.append(nombre)
        notas.append(0)
        print("Operacion Exitosa")
    else:
        print("Operacion Cancelada")

    nuevamente = str(input("Pulse 1 si quiere Realizar una Nueva Operación, de lo contario Enter para volver al menu"))
    if nuevamente == "1": #no usamos cambiante a lower o upper
        AltaEstudiante()

    
def BajaEstudiante(): #se ingresa legajo y se elimina todas las listas de estudiantes
    print ("a")
    
def ModificacionEstudiante(): #se ingresa legajo, se muestra el nombre actual, y se permite cambiar el nombre
    print ("a")
    
def ListadoEstudiantes():#ordenado por nro. de Legajo (por metodo de selección)
    print ("a")
    
def CargaNotaEstudiante():  #Se ingresa legajo y nota (entre 1 y 10,siendo las notas nro. enteros)
                            #En caso que el legajo no haya sido cargado, se debe mostrar la leyenda “Legajo inexistente”. La carga finaliza con legajo igual a -1. 
    print ("a")
    
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
        opcionSeleccionada = int(input("Por Favor Seleccione una Opcion =>"))
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