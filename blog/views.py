from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def post_list(request):
    query = request.GET.get("q","").strip()

    posts_qs = Post.objects.filter(is_published=True)

    if query:
        posts_qs = posts_qs.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
    # пагинация
    paginator = Paginator(posts_qs, 5) # 5 постов на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": page_obj, # теперь posts = текущая страница
        "page_obj": page_obj, 
        "query": query, 
        }
    return render(request, "blog/post_list.html", context)

    #posts = Post.objects.filter(is_published=True).order_by("-created_at")
    #context = {"posts": posts}
    #return render(request, "blog/post_list.html", context)
    
def home(request):
    context = {}
    return render(request, "blog/home.html", context)
    
def about(request):
    context = {}
    return render(request, "blog/about.html")

def contacts(request):
    context = {}
    return render(request, "blog/contacts.html")
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    comments = post.comments.all().order_by("-created_at")
    similar_posts = Post.objects.filter( created_at__date = post.created_at.date()).exclude(pk=post.pk)[:3]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # привязывает комментарий к текущему посту
            comment.post = post #
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
        context = {
            "post": post, 
            "comments": comments, 
            "form": form,
            "similar_posts": similar_posts
            }
        return render(request, "blog/post_detail.html", context)

    #similar_posts = Post.objects.filter( created_at__date = post.created_at.date()).exclude(pk=post.pk)[:3]
    #context = {"post": post, "similar_posts": similar_posts}
    #return render(request, "blog/post_detail.html", context)

@login_required
def post_create(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid(): #True of false
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)   
    else:
        form = PostForm()
        context = {"form": form}
        return render(request, "blog/post_form.html", context)

@login_required
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid(): #True of false
            post = form.save()
            return redirect("post_detail", pk=post.pk)  
    else:
        form = PostForm(instance=post)
        context = {"form": form, "post":post}
        return render(request, "blog/post_form_edit.html", context)

@login_required
def post_delete(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method =="POST":
        post.delete()
        return redirect("post_list")  
    else:
        context = {"post":post}
        return render(request, "blog/post_form_delete.html", context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

