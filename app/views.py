
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

def index(request):
    trans = translate(language = 'es')
    return render(request, 'index.html', trans)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        context = {
            'lenguaje': _('Idiomas'),
            'crear': _('Crear'),
            'guardar': _('Guardar'),
            'ejecutar': _('Ejecutar'),
            'abrir': _('Abrir'),
            'variables': _('Variables'),
            'condicionales': _('Condicionales'),
            'ciclos': _('Ciclos'),
            'funciones': _('Funciones'),
            'sintaxis': _('Sintaxis'), 
        }
    finally:
        activate(cur_language)
    return context