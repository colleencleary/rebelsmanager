# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from forum.models import ForumPost, ForumComment
from forum.forms import PostForm, CommentForm
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView


# from django.conf import settings

@login_required
def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    forumposts = ForumPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    print(forumposts)
    return render(request, 'main_page/mainpage.html', {'posts': posts, 'forumposts': forumposts})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

class BlogSearchListView(ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    model = Post
    paginate_by = 10

    def get_queryset(self):
        qs = Post.objects.published()

        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            vector = SearchVector('title', 'content')
            qs = qs.annotate(search=vector).filter(search=query)
            qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        return qs
@login_required
def forum_list(request):
    forumposts = ForumPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'forum/forum_list.html', {'forumposts': forumposts})

@login_required
def forum_detail(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    return render(request, 'forum/forum_detail.html', {'forumpost': forumpost})

@login_required
def forum_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            forumpost = form.save(commit=False)
            forumpost.author = request.user
            forumpost.published_date = timezone.now()
            forumpost.save()
            return redirect('forum_detail', pk=forumpost.pk)
    else:
        form = PostForm()
    return render(request, 'forum/forum_edit.html', {'form': form})

@login_required
def forum_edit(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=forumpost)
        if form.is_valid():
            forumpost = form.save(commit=False)
            forumpost.author = request.user
            forumpost.published_date = timezone.now()
            forumpost.save()
            return redirect('forum_detail', pk=forumpost.pk)
    else:
        form = PostForm(instance=forumpost)
    return render(request, 'forum/forum_edit.html', {'form': form})

@login_required
def forum_remove(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    forumpost.delete()
    return redirect('forum_list')

@login_required
def add_comment_to_forumpost(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forumpost = forumpost
            comment.save()
            return redirect('forum_detail', pk=forumpost.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_forumpost.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(ForumComment, pk=pk)
    comment.delete()
    return redirect('forum_detail', pk=comment.forumpost.pk)
