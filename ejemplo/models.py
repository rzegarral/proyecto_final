from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
 #   creado_el = models.DateTimeField()         #  nuevo campo de ctrl

    def __str__(self):
      return f"{self.id},{self.nombre}, {self.numero_pasaporte}, {self.id}"

###  ----  Agregado por mi ---
class Amigos(models.Model):
    nombre    = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    pais      = models.CharField(max_length=20)
    edad      = models.IntegerField()

    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.direccion}, {self.pais}, {self.edad}"

class Carros(models.Model):
    marca     = models.CharField(max_length=100)
    origen    = models.CharField(max_length=200)
    ano       = models.IntegerField()
    valor     = models.IntegerField()

    def __str__(self):
      return f"{self.marca}, {self.origen}, {self.ano}, {self.valor}"

class Escuelas(models.Model):
    nombre    = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    curso     = models.CharField(max_length=200)
    tiempo_mes= models.IntegerField()
    costo_mes = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.curso}, {self.tiempo_mes}, {self.costo_mes}"

    