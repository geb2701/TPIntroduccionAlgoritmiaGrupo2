def AltaEstudiante():
    print ("a")

def BajaEstudiante():
    print ("a")
    
def ModificacionEstudiante():
    print ("a")
    
def ListadoEstudiantes():
    print ("a")
    
def CargaNotaEstudiante():
    print ("a")
    
def ListaEstudiantesReprobados():
    print ("a")
    
def ListaEstudiantesAprobados():
    print ("a")
     
def ListadoMejoresEstudiantes():
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