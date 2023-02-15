from django.db import models

# Create your models here.
class Ropa(models.Model):
    nombrePrenda=models.CharField(max_length=100)
    verano=models.CharField(max_length=100)
    invierno=models.CharField(max_length=100)
    talle=models.IntegerField(max_length=100)
    def __str__(self):
        return self.nombrePrenda+""+ self.talle
    

class calzado(models.Model):
    nombrePrenda=models.CharField(max_length=100)
    masculino=models.CharField(max_length=100)
    femenino=models.CharField(max_length=100)
    talle=models.IntegerField(max_length=100)
    def __str__(self):
        return self.nombrePrenda+ ""+ self.talle

class gorros(models.Model):
    nombrePrenda=models.CharField(max_length=100)
    nena=models.CharField(max_length=100)
    varon=models.CharField(max_length=100)
    talle=models.IntegerField(max_length=100)
    def __str__(self):
       return self.nombrePrenda + "" + self.talle


