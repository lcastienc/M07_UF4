from django.db import models

# Create your models here.
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
