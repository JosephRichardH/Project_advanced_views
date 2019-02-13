from django import forms

from .models import Mentor

class PostForm(forms.ModelForm):

    class Meta:
        model = Mentor
        fields = ('gambar','Nama', 'pengalaman','quote')
