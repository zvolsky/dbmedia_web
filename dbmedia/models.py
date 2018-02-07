from django.db import models

class Obrazek(models.Model):
    nazev = models.CharField(max_length=120)
    obrazek = models.FileField(upload_to="incidents")
