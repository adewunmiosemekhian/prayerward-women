# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm


def post_list(request):
    category_id = request.GET.get('category')
    selected_category = None

    if category_id:
        try:
            selected_category = int(category_id)
            posts = Post.objects.filter(categories__id=selected_category).order_by('-created_at')
        except ValueError:
            posts = Post.objects.all().order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'selected_category': selected_category
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {
        'categories': categories
    })


def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/all_posts.html', {
        'posts': posts
    })


def contact(request):
    return render(request, 'blog/contact.html')