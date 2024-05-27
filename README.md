# M07_UF4
# Pràctica 2: BASES DE DADES

## Índice

1. [Base de Datos](#base-de-datos)
    - [Descripción de la Base de Datos](#descripción-de-la-base-de-datos)
    - [Estructura de las Tablas](#estructura-de-las-tablas)
2. [CRUD de Estudiante](#crud-de-estudiante)
    - [READ](#read)
    - [CREATE](#create)
    - [UPDATE](#update)
    - [DELETE](#delete)
3. [CRUD de Profesor](#crud-de-profesor)
    - [READ](#read-1)
    - [CREATE](#create-1)
    - [UPDATE](#update-1)
    - [DELETE](#delete-1)

## Base de Datos

### Descripción de la Base de Datos
En esta práctica se utilizará una base de datos con el nombre `iticBCN` hecha con postgresql

### Modelos de Django

```python
class RolProfessor(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class RolEstudiant(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Modul(models.Model):
    Codi = models.CharField(max_length=100)
    def __str__(self):
        return self.Codi

class Curso(models.Model):
    Codi = models.CharField(max_length=100)
    def __str__(self):
        return self.Codi

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cursosImpartits = models.ManyToManyField(Curso)
    modulsImpartits = models.ManyToManyField(Modul)
    rolProfessor = models.ForeignKey(RolProfessor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom} {self.cognom1} {self.cognom2} {self.email} {self.cursosImpartits} {self.modulsImpartits} {self.rolProfessor}'

class Estudiant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cursosMatriculats = models.ManyToManyField(Curso)
    modulsMatriculats = models.ManyToManyField(Modul)
    rolEstudiant = models.ForeignKey(RolEstudiant, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom} {self.cognom1} {self.cognom2} {self.email} {self.cursosMatriculats} {self.modulsMatriculats} {self.rolEstudiante}'
```


### Estructura de las Tablas

![iticBCN - public](https://github.com/lcastienc/M07_UF4/assets/102548167/432c3de6-f50a-4e40-86ac-5a4caf5f4b7e)


## CRUD de Estudiante

### READ
Implementación del método para leer los datos de los estudiantes, de manera globar y individual, desde la base de datos.

![django](https://github.com/lcastienc/M07_UF4/assets/102548167/a572aa83-c3f4-4117-8f11-8b134b35c3d0)

Codigo para ver toda la informacion de los alumnos:
```python
def students(request):
    estudiants = Estudiant.objects.all()
    context = {'estudiants': estudiants}
    return render(request, 'students.html', context)
```

Codigo para ver la informacion de un alumno en concreto:
```python
def student(request, pk):
    student = Estudiant.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'student.html', context)
```

### CREATE
Implementación del método para crear nuevos registros de estudiantes en la base de datos.

![django](https://github.com/lcastienc/M07_UF4/assets/102548167/8ac32b0e-624f-4a10-b75e-ab9d6a90d812)

Codigo para añadir un alumno:
```python
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
```

### UPDATE
Implementación del método para actualizar los datos de los estudiantes en la base de datos.

![django](https://github.com/lcastienc/M07_UF4/assets/102548167/ef3a3c84-e574-4c82-abd4-bd5cde2046d4)

Codigo para actulizar los datos de un alumno:
```python
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
```

### DELETE
Implementación del método para eliminar registros de estudiantes de la base de datos.

![django](https://github.com/lcastienc/M07_UF4/assets/102548167/dc6a6a4b-5f84-46ec-af78-d6ab51e7cdf3)

Codigo para borrar un estudiante:
```python
def delete_student(request, pk):
    estudiant = Estudiant.objects.get(id=pk)
    if request.method == 'POST':
        estudiant.delete()
        return redirect('students')
    return render(request, 'delete_student.html')
```

## CRUD de Profesor

### READ
Implementación del método para leer los datos de los profesores desde la base de datos.

![django1](https://github.com/lcastienc/M07_UF4/assets/102548167/d931fc71-8d9d-4e13-8ef8-899bfd29d17a)

Codigo para ver toda la informacion de los profesores:
```python
def teachers(request):
    professors = Professor.objects.all()
    context = {'professors': professors}
    return render(request, 'teachers.html', context)
```

Codigo para ver la informacion de un profesor en concreto:
```python
def teacher(request,pk):
    teacher = Professor.objects.get(id=pk)
    context = {'teacher': teacher}
    return render(request, 'teacher.html', context)
```

### CREATE
Implementación del método para crear nuevos registros de profesores en la base de datos.

![django1](https://github.com/lcastienc/M07_UF4/assets/102548167/54fa3b02-94ee-483f-b980-cf0aaa955a44)

Codigo para añadir un profesor:
```python
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
```

### UPDATE
Implementación del método para actualizar los datos de los profesores en la base de datos.

![django1](https://github.com/lcastienc/M07_UF4/assets/102548167/c2b03cd7-4e0d-4111-95e3-d50b4fc72860)

Codigo para actulizar los datos de un profesor:
```python
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
    
```

### DELETE
Implementación del método para eliminar registros de profesores de la base de datos.

![django1](https://github.com/lcastienc/M07_UF4/assets/102548167/f55cac9c-f749-462c-b718-7fb6b6148ed3)

Codigo para borrar un profesor:
```python
def delete_teacher(request, pk):
    professor = Professor.objects.get(id=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('teachers')
    return render(request, 'delete_teacher.html', {'professor': professor})
```
