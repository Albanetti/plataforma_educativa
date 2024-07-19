from django.contrib import admin
from .models import Curso, Alumno, Asignatura, Profesor, Nota

admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Profesor)
admin.site.register(Nota)