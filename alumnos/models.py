from django.db import models

from django.contrib import admin

# Create your models here.


class Materia(models.Model):
	nombre  =   models.CharField(max_length=30)

	def __str__(self):
		return self.nombre



class Grado(models.Model):
	nombre  =   models.CharField(max_length=30)
	descripcion = models.TextField()
	materias = models.ManyToManyField(Materia,through='Pensum')

	def __str__(self):
		return self.nombre

class Seccion(models.Model):
	nombre  =   models.CharField(max_length=30)
	grado = models.ForeignKey(Grado,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre	


class Pensum(models.Model):
	materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
	grado = models.ForeignKey(Grado,on_delete=models.CASCADE)


class PensumInLine(admin.TabularInline):
	model = Pensum
	extra = 1

class MateriaAdmin(admin.ModelAdmin):
	inlines= (PensumInLine,)

class GradoAdmin(admin.ModelAdmin):
	inlines = (PensumInLine,)
