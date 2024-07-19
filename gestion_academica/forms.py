from django import forms
from .models import Curso, Alumno, Asignatura, Profesor, Nota

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'curso']

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'curso', 'profesor']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['alumno', 'asignatura', 'nota1', 'nota2', 'nota3', 'examen_semestral']
        widgets = {
            'nota1': forms.NumberInput(attrs={'step': '0.01', 'min': '1.00', 'max': '7.00'}),
            'nota2': forms.NumberInput(attrs={'step': '0.01', 'min': '1.00', 'max': '7.00'}),
            'nota3': forms.NumberInput(attrs={'step': '0.01', 'min': '1.00', 'max': '7.00'}),
            'examen_semestral': forms.NumberInput(attrs={'step': '0.01', 'min': '1.00', 'max': '7.00'}),
        }

    def __init__(self, *args, **kwargs):
        self.alumno = kwargs.pop('alumno', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        nota = super().save(commit=False)
        if self.alumno:
            nota.alumno = self.alumno
        if commit:
            nota.save()
        return nota

