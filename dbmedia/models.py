from django.db import models

class Obrazek(models.Model):
    nazev = models.CharField(max_length=120)
    #obrazek = models.FileField(upload_to='obrazek', null=True, blank=True)
    #obrazek2 = models.FileField(upload_to='obrazek', null=True, blank=True)
    obrazek = models.FileField(upload_to='dbmedia.File_Obrazek_obrazek/bytes/filename/mimetype', null=True, blank=True)
    obrazek2 = models.ImageField(upload_to='dbmedia.File_Obrazek_obrazek2/bytes/filename/mimetype', null=True, blank=True)

class File_Obrazek_obrazek(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

class File_Obrazek_obrazek2(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
