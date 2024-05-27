from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import EstudiantForm,ProfessorForm
from .models import Professor, Estudiant

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
    #El retorn de dades de profesor en aquest apartat no es viables perque s'ha modificat
    #tot per tal de fer el crud
    professor = {"nom": "John", "cognom": "Doe", "edat": 25}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor['nom'], 'cognom':professor['cognom'], 'edat':professor['edat']})
    return HttpResponse(dades)


#Practica 1 a, teachers y students
'''
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
'''

'''
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
'''

#Practica 1b, teachers y students con links individuales

# def teacher(request, pk):
#     teacher_obj = None
#     teachers = {
#         'teacher1': {
#             'id': '1',
#             'nom': 'Roger',
#             'cognom1': 'Sobrino',
#             'cognom2': 'Gil',
#             'email': 'roger.sobrino@iticbcn.cat',
#             'curs': ['DAW1B', 'DAM2B'],
#             'tutor': 'SI',
#             'modulsImpartits': ['M01', 'M02', 'M03']
#         },
#         'teacher2': {
#             'id': '2',
#             'nom': 'Juanma',
#             'cognom1': 'Sanchez',
#             'cognom2': 'Biel',
#             'email': 'juanmanuel.sanchez@iticbcn.cat',
#             'curs': ['DAW1B', 'SMIX2B'],
#             'tutor': 'NO',
#             'modulsImpartits': ['M02', 'M05', 'M09']
#         },
#         'teacher3': {
#             'id': '3',
#             'nom': 'Oriol',
#             'cognom1': 'Roca',
#             'cognom2': 'Fabra',
#             'email': 'joseporiol.roca@iticbcn.cat',
#             'curs': ['DAM1B', 'SMIX2A'],
#             'tutor': 'SI',
#             'modulsImpartits': ['M07', 'M10', 'M12']
#         }
#     }
#
#     for key, value in teachers.items():
#         if value['id'] == pk:
#             teacher_obj = value
#             break
#
#     return render(request, 'teacher.html', {'teacher': teacher_obj})

'''
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
'''


#Practica 2 CRUD Professors i Estudiants
def teachers(request):
    professors = Professor.objects.all()
    context = {'professors': professors}
    return render(request, 'teachers.html', context)

def teacher(request,pk):
    teacher = Professor.objects.get(id=pk)
    context = {'teacher': teacher}
    return render(request, 'teacher.html', context)

def add_teacher(request):
    form = ProfessorForm
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = ProfessorForm()
        context = {'form': form}
        return render(request, 'add_teacher.html', context)

def edit_teacher(request, pk):
    professor = Professor.objects.get(id=pk)
    form = ProfessorForm(instance=professor)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        context = {'form': form}
        return render(request, 'edit_teacher.html', context)

def delete_teacher(request, pk):
    professor = Professor.objects.get(id=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('teachers')
    return render(request, 'delete_teacher.html', {'professor': professor})

def student(request, pk):
    student = Estudiant.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'student.html', context)

def students(request):
    estudiants = Estudiant.objects.all()
    context = {'estudiants': estudiants}
    return render(request, 'students.html', context)

def add_student(request):
    form = EstudiantForm
    if request.method == 'POST':
        form = EstudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = EstudiantForm()
        context = {'form': form}
        return render(request, 'add_student.html', context)

def edit_student(request, pk):
    estudiant = Estudiant.objects.get(id=pk)
    form = EstudiantForm(instance=estudiant)
    if request.method == 'POST':
        form = EstudiantForm(request.POST, instance=estudiant)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        context = {'form': form}
        return render(request, 'edit_student.html', context)

def delete_student(request, pk):
    estudiant = Estudiant.objects.get(id=pk)
    if request.method == 'POST':
        estudiant.delete()
        return redirect('students')
    return render(request, 'delete_student.html')