from django.forms import ModelForm
from .models import Professor, Estudiant

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nom', 'cognom1', 'cognom2', 'email', 'cursosImpartits', 'modulsImpartits', 'rolProfessor']

class EstudiantForm(ModelForm):
    class Meta:
        model = Estudiant
        fields = ['nom', 'cognom1', 'cognom2', 'email', 'cursosMatriculats', 'modulsMatriculats', 'rolEstudiant']
