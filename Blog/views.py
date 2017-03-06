from django.shortcuts import get_object_or_404, redirect, render
from django.template import Context
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = Context({
        'title': 'Blog',
        'header': 'Blog Main Header',
        'subheader': 'This is the blog subheader.',
        'posts': posts,
        'allow_add_post': True,
        })
    for post in posts:
        post.url = post.title.replace(' ', '_')
    return render(request, 'blog_index.html', context)

def post(request, post_url):
    post = get_object_or_404(Post, title=post_url.replace('_', ' '))
    return render(request, 'blog_post.html', {'post': post})

def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True) # if the form is valid, save to DB.
            return redirect(index)
        else:
            print(form.errors)
    else:
        form = PostForm()
        context = Context({
            'form': form,
            'allow_add_post': True,
            })
        return render(request, 'new_post.html', context)