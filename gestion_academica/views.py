from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Alumno, Asignatura, Profesor, Nota
from .forms import CursoForm, AlumnoForm, AsignaturaForm, ProfesorForm, NotaForm
from django.http import HttpResponse
from django import forms
import pandas as pd

class ExportForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
    asignatura = forms.ModelChoiceField(queryset=Asignatura.objects.all(), required=True)

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_academica/index.html', {'cursos': cursos})

def curso_detail(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    alumnos = Alumno.objects.filter(curso=curso)
    asignaturas = Asignatura.objects.filter(curso=curso)
    return render(request, 'gestion_academica/curso_detail.html', {'curso': curso, 'alumnos': alumnos, 'asignaturas': asignaturas})

def alumno_detail(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    notas = Nota.objects.filter(alumno=alumno)
    return render(request, 'gestion_academica/alumno_detail.html', {'alumno': alumno, 'notas': notas})

def add_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'gestion_academica/add_curso.html', {'form': form})

def add_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'gestion_academica/add_alumno.html', {'form': form})

def add_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AsignaturaForm()
    return render(request, 'gestion_academica/add_asignatura.html', {'form': form})

def add_nota(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.alumno = alumno
            nota.save()
            return redirect('alumno_detail', alumno_id=alumno.id)
    else:
        form = NotaForm()
    
    return render(request, 'gestion_academica/add_nota.html', {'form': form, 'alumno_id': alumno_id})

def edit_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('alumno_detail', alumno_id=nota.alumno.id)
    else:
        form = NotaForm(instance=nota)
    
    return render(request, 'gestion_academica/edit_nota.html', {'form': form, 'nota': nota})

def delete_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    alumno_id = nota.alumno.id
    
    if request.method == "POST":
        nota.delete()
        return redirect('alumno_detail', alumno_id=alumno_id)
    
    return render(request, 'gestion_academica/delete_nota.html', {'nota': nota})

def edit_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno_detail', alumno_id=alumno.id)
    else:
        form = AlumnoForm(instance=alumno)
    
    return render(request, 'gestion_academica/edit_alumno.html', {'form': form, 'alumno': alumno})

def delete_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == "POST":
        alumno.delete()
        return redirect('index')
    
    return render(request, 'gestion_academica/delete_alumno.html', {'alumno': alumno})

def edit_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    
    if request.method == "POST":
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('curso_detail', curso_id=asignatura.curso.id)
    else:
        form = AsignaturaForm(instance=asignatura)
    
    return render(request, 'gestion_academica/edit_asignatura.html', {'form': form, 'asignatura': asignatura})

def delete_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    curso_id = asignatura.curso.id
    
    if request.method == "POST":
        asignatura.delete()
        return redirect('curso_detail', curso_id=curso_id)
    
    return render(request, 'gestion_academica/delete_asignatura.html', {'asignatura': asignatura})

def edit_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    
    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfesorForm(instance=profesor)
    
    return render(request, 'gestion_academica/edit_profesor.html', {'form': form, 'profesor': profesor})

def delete_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    
    if request.method == "POST":
        profesor.delete()
        return redirect('index')
    
    return render(request, 'gestion_academica/delete_profesor.html', {'profesor': profesor})

def export_data(request):
    if request.method == "POST":
        form = ExportForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            asignatura = form.cleaned_data['asignatura']
            alumnos = Alumno.objects.filter(curso=curso)
            notas = Nota.objects.filter(alumno__in=alumnos, asignatura=asignatura)
            
            data = {
                'Alumnos': alumnos.values('nombre', 'apellido'),
                'Notas': notas.values('nota1', 'nota2', 'nota3', 'examen_semestral', 'promedio_semestral', 'promedio_final')
            }

            with pd.ExcelWriter('data_export.xlsx') as writer:
                for key, value in data.items():
                    df = pd.DataFrame(list(value))
                    df.to_excel(writer, sheet_name=key, index=False)

            with open('data_export.xlsx', 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename=data_export.xlsx'
                return response
    else:
        form = ExportForm()

    cursos = Curso.objects.all()
    asignaturas = Asignatura.objects.all()
    return render(request, 'gestion_academica/export_data.html', {'form': form, 'cursos': cursos, 'asignaturas': asignaturas})
