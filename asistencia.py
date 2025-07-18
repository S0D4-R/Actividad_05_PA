key = True
class CollegeStudent:
    def __init__(self, name, age, course, avg_score):
        self.name = name
        self.age = age
        self.course = course
        self.avg_score = avg_score

students_compendium = {}


def agregar_estudiante():
    pass


def registrar_asistencia():
    pass


def mostrar_lista():
    pass


def mostrar_total_presentes():
    pass


while key:
    menu_inpt = input("----------Bienvenido----------\n"
                      "\n1. Agregar estudiante a la lista"
                      "\n2. Registrar Asistencia"
                      "\n3. Mostrar lista completa"
                      "\n4. Mostrar total de estudiantes presentes"
                      "\n5. Salir\n\nSeleccione una opción: ")
    match menu_inpt:
        case "1":
            agregar_estudiante()
        case "2":
            registrar_asistencia()
        case "3":
            mostrar_lista()
        case "4":
            mostrar_total_presentes()
        case "5":
            print("Gracias por usar el programa")
            key = False