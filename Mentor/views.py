from django.shortcuts import render
from .models import Mentor
from .forms import PostForm


# Create your views here.
def Mentor(request):
    return render(request, 'Mentor.html', {})

#def db_Mentor(request):
#    Mentor_all = Mentor.objects.all()
#    return render(request, 'Mentor.html', {'Mentors': Mentor})
