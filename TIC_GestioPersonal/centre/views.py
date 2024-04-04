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