from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curso/<int:curso_id>/', views.curso_detail, name='curso_detail'),
    path('alumno/<int:alumno_id>/', views.alumno_detail, name='alumno_detail'),
    path('add_curso/', views.add_curso, name='add_curso'),
    path('add_alumno/', views.add_alumno, name='add_alumno'),
    path('add_asignatura/', views.add_asignatura, name='add_asignatura'),
    path('add_nota/<int:alumno_id>/', views.add_nota, name='add_nota'),
    path('edit_nota/<int:pk>/', views.edit_nota, name='edit_nota'),
    path('delete_nota/<int:pk>/', views.delete_nota, name='delete_nota'),
    path('edit_alumno/<int:pk>/', views.edit_alumno, name='edit_alumno'),
    path('delete_alumno/<int:pk>/', views.delete_alumno, name='delete_alumno'),
    path('edit_asignatura/<int:pk>/', views.edit_asignatura, name='edit_asignatura'),
    path('delete_asignatura/<int:pk>/', views.delete_asignatura, name='delete_asignatura'),
    path('edit_profesor/<int:pk>/', views.edit_profesor, name='edit_profesor'),
    path('delete_profesor/<int:pk>/', views.delete_profesor, name='delete_profesor'),
    path('export_data/', views.export_data, name='export_data'),
]
