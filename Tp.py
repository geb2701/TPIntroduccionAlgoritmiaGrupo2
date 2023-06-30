legajosLista=[]
nombresLista=[]


def AltaEstudiante():  #Se ingresa legajo y nombre
    print ("Alta Estudiante")
    legajo=int(input("Ingrese legajo => "))
    i=0
    maximoi=len(legajosLista)
    encontrado=False
    while i < legajosLista and encontrado==False:
        if legajo==legajosLista [i]:
            encontrado=True
        else:
            i=+1
        


    
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