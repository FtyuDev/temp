from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Sinf(models.Model):
    title = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.title


class Sinfnom(models.Model):
    nomi = models.CharField(max_length=1,null=True,default='A')

    def __str__(self):
        return self.nomi


class Kunlar(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Fan(models.Model):
    sinf = models.ForeignKey(Sinf, on_delete=models.CASCADE)
    sinfnom = models.ForeignKey(Sinfnom, on_delete=models.CASCADE,null=True)
    kun = models.ForeignKey(Kunlar, on_delete=models.CASCADE)
    fan1 = models.CharField(max_length=200)
    fan2 = models.CharField(max_length=200)
    fan3 = models.CharField(max_length=200)
    fan4 = models.CharField(max_length=200)
    fan5 = models.CharField(max_length=200)
    fan6 = models.CharField(max_length=200,null=True,default='--',blank=True)

    def __str__(self):
        return f"{self.sinf}{self.sinfnom}-{self.kun}"
