from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser




class Member(models.Model):

    full_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    domain = models.CharField(max_length=255)  # Ex : Droit commercial, Droit civil
    year_experience = models.PositiveIntegerField()
    bar = models.CharField(max_length=100, blank=True, null=True) #barreau
    statut = models.CharField(
        max_length=50,
        choices=[
            ('disponible', 'Disponible'),
            ('occupe', 'Occupé'),
            ('indisponible', 'Indisponible'),
        ],
        default='disponible'
    )
    

    def __str__(self):

        return f'{self.full_name} - {self.domain}'

class Area(models.Model):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', verbose_name="Image", blank=True, null=True)
    tag = models.CharField(max_length=128,  verbose_name="tag") # slogan
    description = models.CharField(max_length=255,  verbose_name="description", blank=True, default='')

    def __str__(self):
        return f'{self.name}'
    

class Title(models.Model):
    
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.name} - ({self.area})'
    

class Service(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} - {(self.title)}'
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\d{8,15}$', message="Le numéro doit contenir uniquement des chiffres (8-15 caractères).")]
    )
    profession = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.email}"
    




class Meeting(models.Model):
    full_name = models.CharField(max_length=100)  # Nom du client
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    heure = models.TimeField()
    topic = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('confirmé', 'Confirmé'),
            ('annulé', 'Annulé'),
        ],
        default='en_attente'
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rendez-vous avec {self.full_name} - {self.date} à {self.heure}"


class Folder(models.Model):
    full_name = models.CharField(max_length=100)  # Nom du client
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    profession = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=100, default='') 
    description = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('confirmé', 'Confirmé'),
            ('annulé', 'Annulé'),
        ],
        default='en_attente'
    )
    

    def __str__(self):
        return f"Rendez-vous avec {self.full_name} - {self.profession}"
