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

	def __str__(self):

        return self.nombre

class Seccion(models.Model):
	nombre  =   models.CharField(max_length=30)

	def __str__(self):

        return self.nombre	
