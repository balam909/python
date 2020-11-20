from django.db import models

# Create your models here.

class Actor(models.Model):
	nombre = models.CharField(max_length=30)
	date = models.DateField(max_length=30)
	def __str__(self):
		return '{}'.format(self.nombre)

class Pelicula(models.Model):
	nombre = models.CharField(max_length=30)
	anio_estreno = models.IntegerField(null=True)
	actors = models.ManyToManyField(Actor)
	def __str__(self):
		return '{}'.format(self.nombre)
