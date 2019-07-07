from django.db import models

# Create your models here.
class Persona(models.Model):
	rut = models.CharField(max_length=10)
	telefono = models.CharField(max_length=15)
	def __str__(self):
		return self.rut
		
