from django.db import models
from datetime import date

# Create your models here.
class Blog(models.Model):
    gambar = models.ImageField(blank=True,null=True,upload_to="")
    judul = models.CharField(max_length=255)
    teks = models.TextField(max_length=1000)
    tanggal_dibuat = models.DateField(default=date.today())
    def __str__(self):
        return self.judul   