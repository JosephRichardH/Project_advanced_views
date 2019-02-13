from django.db import models

# Create your models here.
class Mentee(models.Model):
    gambar = models.FileField()
    Nama = models.TextField(max_length=225)
    quote = models.TextField(max_length=225)
    def __str__(self):
        return self.Nama
