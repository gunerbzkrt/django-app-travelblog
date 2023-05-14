from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Region, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q
import random


def post_list(request):
    posts = Post.objects.all()
    regions = Region.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts, "regions": regions})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    regions = Region.objects.all()
    comments = Comment.objects.filter(post=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "regions": regions, "form": form, "comments": comments},
    )


def post_by_region(request, slug):
    content = {
        "posts": Post.objects.filter(region__slug=slug),
        "regions": Region.objects.all(),
        "selected_region": slug,
    }
    return render(request, "blog/post_list.html", content)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})


def search(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
    else:
        posts = []
    return render(request, "blog/post_list.html", {"posts": posts})


def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect("post_detail", pk=comment.post.id)
