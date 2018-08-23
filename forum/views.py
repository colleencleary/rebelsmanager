# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import ForumPost, ForumComment
from .forms import PostForm, CommentForm


# from django.conf import settings

@login_required
def forum_list(request):
    forumposts = ForumPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'forum/forum_list.html', {'forumposts': forumposts})

@login_required
def forum_detail(request, pk):
    forumpost = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            forumcomment = form.save(commit=False)
            forumcomment.author = request.user
            forumcomment.forumpost = forumpost
            forumcomment.save()
            return redirect('forum_detail', pk=forumpost.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/forum_detail.html', {'forumpost': forumpost, 'form': form})

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
            forumcomment = form.save(commit=False)
            forumcomment.author = request.user
            forumcomment.forumpost = forumpost
            forumcomment.save()
            return redirect('forum_detail', pk=forumpost.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_forumpost.html', {'form': form})

@login_required
def forumcomment_remove(request, pk):
    forumcomment = get_object_or_404(ForumComment, pk=pk)
    forumcomment.delete()
    return redirect('forum_detail', pk=forumcomment.forumpost.pk)
