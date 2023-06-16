finalDePrograma=False
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
    
def SalirPrograma():
    print ("a")

def Main():
    print ("a")
    while finalDePrograma==False:
        MostrarElementos(menuOpciones)
        def Opcion():
            input()
        
def MostrarElementos(lista):
    for i in range(len(lista)):
        print(str(i + 1) + ")", lista[i])
        

menuFunciones = [
    AltaEstudiante(), BajaEstudiante(), ModificacionEstudiante(), ListadoEstudiantes(), CargaNotaEstudiante(),
    ListaEstudiantesReprobados(), ListaEstudiantesAprobados(), ListadoEstudiantes(), SalirPrograma()   
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