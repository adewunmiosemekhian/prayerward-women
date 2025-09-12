# blog/create_sample_data.py
from blog.models import Category, Post, Comment
from django.utils import timezone


def create_sample_data():
    # Create categories
    categories = [
        {'name': 'Technology', 'color': '#4e73df'},
        {'name': 'Travel', 'color': '#1cc88a'},
        {'name': 'Food', 'color': '#36b9cc'},
        {'name': 'Lifestyle', 'color': '#f6c23e'},
        {'name': 'Sports', 'color': '#e74a3b'},
    ]

    created_categories = []
    for cat_data in categories:
        cat, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'color': cat_data['color']}
        )
        created_categories.append(cat)

    # Create posts
    posts_data = [
        {
            'title': 'Getting Started with Django',
            'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design...',
            'categories': [created_categories[0]]
        },
        {
            'title': 'My Trip to Japan',
            'content': 'Japan is an amazing country with a perfect blend of traditional culture and modern technology...',
            'categories': [created_categories[1]]
        },
        {
            'title': 'The Best Pizza Recipes',
            'content': 'Making pizza at home is easier than you think. Here are my favorite recipes that will impress your friends and family...',
            'categories': [created_categories[2], created_categories[3]]
        },
        {
            'title': 'Running Tips for Beginners',
            'content': 'Starting a running routine can be challenging but rewarding. Here are some tips to help you get started...',
            'categories': [created_categories[4], created_categories[3]]
        },
    ]

    for post_data in posts_data:
        post = Post.objects.create(
            title=post_data['title'],
            content=post_data['content'],
            created_at=timezone.now()
        )
        for category in post_data['categories']:
            post.categories.add(category)

        # Add some comments
        Comment.objects.create(
            post=post,
            author='John Doe',
            content='Great post! Thanks for sharing.',
            created_at=timezone.now()
        )
        Comment.objects.create(
            post=post,
            author='Jane Smith',
            content='I found this very helpful. Looking forward to more content like this!',
            created_at=timezone.now()
        )

    print("Sample data created successfully!")