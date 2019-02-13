from django.shortcuts import render,redirect
from .models import Mentee
from .forms import PostForm
# Create your views here.

def MenteePost(request):
    Mentees = Mentee.objects.all()
    return render(request, 'Mentee.html', {'Mentees':Mentees})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(Mentee)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})
