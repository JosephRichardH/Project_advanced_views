from django.shortcuts import render,redirect
from .models import Mentor
from .forms import PostForm


def MentorPost(request):
    Mentors = Mentor.objects.all()
    return render(request, 'Mentor.html', {'Mentors':Mentors})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(Mentor)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

#def db_Mentor(request):
#    Mentor_all = Mentor.objects.all()
#    return render(request, 'Mentor.html', {'Mentors': Mentor})
