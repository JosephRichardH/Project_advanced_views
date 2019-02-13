from django.shortcuts import render,redirect
from .models import Blog
from .forms import PostForm

# Create your views here.
def BlogPost(request):
    Postingans = Blog.objects.all()
    return render(request, 'Blog.html', {'Postingans':Postingans})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(BlogPost)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_detail(request, post_id):
    Postingans = Blog.objects.get(pk=post_id)
    return render(request, 'Blog_detail.html', {'Postingans':Postingans})
