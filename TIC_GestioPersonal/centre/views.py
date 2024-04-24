from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#First route, index_one with path ''
def index_one(request):
    return HttpResponse("Hello World, Bienvenidos a DJ DJango Oleee.")

#Second route, with path 'about/'
def about(request):
    return HttpResponse("About me, sobre mi. Soy Django, un framwrok de python para crear aplicaciones webs.")

#Third route, with path 'index/'
def index(request):
    #return HttpResponse("Hello, world")
    professor = {"nom": "John", "cognom": "Doe", "edat": 25}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor['nom'], 'cognom':professor['cognom'], 'edat':professor['edat']})
    return HttpResponse(dades)


#Practica 1 a, teachers y students
def teachers(request):
    teachers = {
        'teacher1': {
            'id': '1',
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'email': 'roger.sobrino@iticbcn.cat',
            'curs': ['DAW1B','DAM2B'],
            'tutor': 'SI',
            'modulsImpartits': ['M01','M02','M03']
        },
        'teacher2': {
            'id': '2',
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Biel',
            'email': 'juanmanuel.sanchez@iticbcn.cat',
            'curs': ['DAW1B','SMIX2B'],
            'tutor': 'NO',
            'modulsImpartits': ['M02','M05','M09']
        },
        'teacher3': {
            'id': '3',
            'nom': 'Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'email': 'joseporiol.roca@iticbcn.cat',
            'curs': ['DAM1B','SMIX2A'],
            'tutor': 'SI',
            'modulsImpartits': ['M07','M10','M12']
        }
    }
    context = {'teachs': teachers}
    return render(request, 'teachers.html', context)

def students(request):
    students = {
        'student1': {
            'id': '1',
            'nom': 'Luis',
            'cognom1': 'Castillo',
            'cognom2': 'Encinas',
            'email': 'lcastill@juamebalmes.net',
            'curs': 'DAW2B',
            'modulsMatriculats': ['M06','M07','M12']
        },
        'student2': {
            'id': '2',
            'nom': 'Leonardo',
            'cognom1': 'Chavez',
            'cognom2': 'Ricaurte',
            'email': '2023_leonardo.chavez@iticbcn.cat',
            'curs': 'DAM1A',
            'modulsMatriculats': ['M01','M03','M12']
        },
        'student3': {
            'id': '3',
            'nom': 'Herson',
            'cognom1': 'Vega',
            'cognom2': '',
            'email': '2023_herson.vega@iticbcn.cat',
            'curs': 'SMX1B',
            'modulsMatriculats': ['M04','M07','M09']
        }
    }
    context = {'studs': students}
    return render(request, 'students.html', context)



#Practica 1b, teachers y students con links individuales

def teacher(request, pk):
    teacher_obj = None
    teachers = {
        'teacher1': {
            'id': '1',
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'email': 'roger.sobrino@iticbcn.cat',
            'curs': ['DAW1B', 'DAM2B'],
            'tutor': 'SI',
            'modulsImpartits': ['M01', 'M02', 'M03']
        },
        'teacher2': {
            'id': '2',
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Biel',
            'email': 'juanmanuel.sanchez@iticbcn.cat',
            'curs': ['DAW1B', 'SMIX2B'],
            'tutor': 'NO',
            'modulsImpartits': ['M02', 'M05', 'M09']
        },
        'teacher3': {
            'id': '3',
            'nom': 'Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'email': 'joseporiol.roca@iticbcn.cat',
            'curs': ['DAM1B', 'SMIX2A'],
            'tutor': 'SI',
            'modulsImpartits': ['M07', 'M10', 'M12']
        }
    }

    for key, value in teachers.items():
        if value['id'] == pk:
            teacher_obj = value
            break

    return render(request, 'teacher.html', {'teacher': teacher_obj})

def student(request, pk):
    student_obj = None
    students = {
        'student1': {
            'id': '1',
            'nom': 'Luis',
            'cognom1': 'Castillo',
            'cognom2': 'Encinas',
            'email': 'lcastill@juamebalmes.net',
            'curs': 'DAW2B',
            'modulsMatriculats': ['M06','M07','M12']
        },
        'student2': {
            'id': '2',
            'nom': 'Leonardo',
            'cognom1': 'Chavez',
            'cognom2': 'Ricaurte',
            'email': '2023_leonardo.chavez@iticbcn.cat',
            'curs': 'DAM1A',
            'modulsMatriculats': ['M01','M03','M12']
        },
        'student3': {
            'id': '3',
            'nom': 'Herson',
            'cognom1': 'Vega',
            'cognom2': '',
            'email': '2023_herson.vega@iticbcn.cat',
            'curs': 'SMX1B',
            'modulsMatriculats': ['M04','M07','M09']
        }
    }
    for key, value in students.items():
        if value['id'] == pk:
            student_obj = value
    return render(request, 'student.html', {'student': student_obj})