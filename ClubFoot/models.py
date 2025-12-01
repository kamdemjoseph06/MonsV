from django.db import models
import os
from django.conf import settings
from datetime import date
from django.utils import timezone

# Create your models here.

class inscription(models.Model):
    noms=models.CharField(max_length=200, null=False)
    prenoms=models.CharField(max_length=200, null=False)
    dateBirth=models.DateField(default=date.today)
    codeClub=models.CharField(max_length=200, null=False)
    pwdClub=models.CharField(max_length=200, null=False)
    datePub=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.noms

def get_static_videos():
    path = os.path.join(settings.BASE_DIR, 'static', 'staticVid')
    if not os.path.exists(path):
        return [] # Retourne une liste de tuples (valeur, affichage)
    return [(f, f) for f in os.listdir(path) if f.endswith(('.mp4', '.webm', '.ogg'))]

def get_static_images():
    path = os.path.join(settings.BASE_DIR, 'static', 'staticImg')
    if not os.path.exists(path):
        return [] # Retourne une liste de tuples (valeur, affichage)
    return [(f, f) for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))]

def get_static_doc():
    path = os.path.join(settings.BASE_DIR, 'static', 'staticDoc')
    if not os.path.exists(path):
        return [] # Retourne une liste de tuples (valeur, affichage)
    return [(f, f) for f in os.listdir(path) if f.endswith(('.pdf', '.word'))]


class imgVidUser(models.Model):
    img=models.ImageField(upload_to='mediaImage/',null=True)
    vid=models.FileField(upload_to='mediaVideo/',null=True)
    titre = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    datePub=models.DateTimeField(default=timezone.now)
    fk=models.ForeignKey(inscription,on_delete=models.CASCADE)

class img(models.Model):
    titre = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    image_choisie = models.CharField(
        max_length=200,
        choices=get_static_images(),default=''  # choix dynamiques
    )
    datePub=models.DateTimeField(default=timezone.now)

    #img=models.ImageField(upload_to='staticImg/')
    def __str__(self):
        return self.titre #or "Vidéo"
    


class Vid(models.Model):
    titre = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    video_choisie = models.CharField(
        max_length=200,
        choices=get_static_videos(),default=''  # choix dynamiques
    )
    datePub=models.DateTimeField(default=timezone.now)

    #vid=models.FileField(upload_to='static_Vid/')
    def __str__(self):
        return self.titre #or "Vidéo"

class Infomedia(models.Model):
    titre = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    datePub=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre  

class Doc(models.Model):
    titre = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    doc_choisie = models.CharField(
        max_length=200,
        choices=get_static_doc(),default=''  # choix dynamiques
    )
    datePub=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre