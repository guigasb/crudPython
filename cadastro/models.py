from django.db import models

# Create your models here.

ESTILO_CHOICES =[
    ('CC', 'CC'),
    ('SPI', 'SPI'),
    ('ADS', 'ADS'),

]

class Meususer(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True, verbose_name="Sua idade")
    curso = models.CharField(max_length=20, verbose_name="Curso", choices=ESTILO_CHOICES, default="CC")
    periodo = models.IntegerField(blank=True, null=True, verbose_name="Seu período")

    def __str__(self):
        return self.nome