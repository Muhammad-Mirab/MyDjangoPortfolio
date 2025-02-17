from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm

def blogView(request):
    posts = Blog.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)

def blogCategorizedView(request, category):
    posts = Blog.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "categorizedBlog.html", context)

def blogDetail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:blogDetail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blogDetail.html", context)