from django.db import models

class Obrazek(models.Model):
    nazev = models.CharField(max_length=120)
    obrazek = models.FileField(upload_to='dbmedia.File_Obrazek_Obrazek/bytes/filename/mimetype')

class File_Obrazek_Obrazek(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
