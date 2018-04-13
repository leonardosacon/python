# Create your models here.
from django.db import models

class Zona(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    descricao = models.CharField(max_length=150, verbose_name='Zona')

class Localidade(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    descricao = models.CharField(max_length=100)
    id_zona = models.ForeignKey(Zona, models.DO_NOTHING, blank=True, null=True)

class Bairro(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    descricao = models.CharField(max_length=150, verbose_name='Bairro')

class Municipio(models.Model):
    UF = (
        ('PR', 'PR'),
        ('SC', 'SC'),
        ('RS', 'RS')
    )
    id = models.IntegerField(primary_key=True, auto_created=True)
    descricao = models.CharField(max_length=100, verbose_name='Município')
    uf = models.CharField(max_length=2, choices=UF, verbose_name='UF')

class ModalidadeTransporte(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Modalidade Transporte')
