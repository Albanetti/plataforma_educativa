from django.db import models
from decimal import Decimal

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    anotaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2)
    examen_semestral = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def promedio_semestral(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / Decimal('3')
        return round(promedio, 4)

    @property
    def promedio_final(self):
        promedio_semestral = self.promedio_semestral
        promedio_final = (promedio_semestral * Decimal('0.6')) + (self.examen_semestral * Decimal('0.4'))
        return round(promedio_final, 4)

    def __str__(self):
        return f"{self.alumno} - {self.asignatura} - {self.promedio_final:.4f}"
