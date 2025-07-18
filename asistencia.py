key = True
class CollegeStudent:
    def __init__(self, name, ide, course, attendance):
        self.name = name
        self.ide = ide
        self.course = course
        self.attendance = attendance

students_compendium = []
attendace = []

def agregar_estudiante():
    student_name = input("Coloque el nombre del estudiante: ")
    student_id = input("Coloque el carné del estudiante: ")
    sudent_course = input("Coloque el curso que lleva")
    student_att = None
    temp_student = CollegeStudent(student_name,student_id,sudent_course, student_att)
    students_compendium.append(temp_student)
    print()


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