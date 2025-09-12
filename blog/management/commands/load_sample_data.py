# blog/management/commands/load_sample_data.py
from django.core.management.base import BaseCommand
from blog.models import Category, Post, Comment
from django.utils import timezone


class Command(BaseCommand):
    help = 'Loads sample data into the database'

    def handle(self, *args, **options):
        # Clear existing data
        Post.objects.all().delete()
        Category.objects.all().delete()
        Comment.objects.all().delete()

        # Create categories with spiritual themes
        categories_data = [
            {'name': 'Daily Devotion', 'color': '#4B0082'},  # Indigo
            {'name': 'Prayer Life', 'color': '#228B22'},  # ForestGreen
            {'name': 'Women of Faith', 'color': '#8B4513'},  # SaddleBrown
            {'name': 'Bible Study', 'color': '#4169E1'},  # RoyalBlue
            {'name': 'Testimonies', 'color': '#DAA520'},  # GoldenRod
        ]

        categories = []
        for cat_data in categories_data:
            category = Category.objects.create(
                name=cat_data['name'],
                color=cat_data['color']
            )
            categories.append(category)
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Create posts with spiritual content
        posts_data = [
            {
                'title': 'The Power of Morning Prayer',
                'content': 'Starting your day with prayer sets the tone for everything that follows. When we begin our mornings in conversation with God, we invite His presence into our day. This simple practice can transform your perspective, give you strength for challenges, and help you recognize God\'s hand throughout your day.',
                'categories': [categories[0], categories[1]]
            },
            {
                'title': 'Women of Faith in Scripture',
                'content': 'Throughout the Bible, we find incredible examples of women who walked in faith and changed their world. From Esther\'s courage to Ruth\'s loyalty, from Mary\'s surrender to Lydia\'s hospitality, these women show us what it means to trust God completely in every circumstance of life.',
                'categories': [categories[2], categories[3]]
            },
            {
                'title': 'Creating a Sacred Space for Prayer',
                'content': 'Having a dedicated space for prayer can significantly enhance your spiritual practice. This doesn\'t require a large area - just a quiet corner with your Bible, a journal, and perhaps a candle. This physical space becomes a reminder to meet with God regularly and helps create a habit of prayer.',
                'categories': [categories[1], categories[0]]
            },
            {
                'title': 'How God Answered My Prayer for Healing',
                'content': 'Last year, I faced a health challenge that seemed insurmountable. Doctors were uncertain, and fear tried to take root. But through persistent prayer and the support of my faith community, I experienced God\'s healing power in ways I never imagined. This journey taught me about trust, patience, and the power of believing prayer.',
                'categories': [categories[4], categories[1]]
            },
        ]

        for i, post_data in enumerate(posts_data):
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
                author='Sarah M.',
                content='This blessed me so much! Thank you for sharing these insights.',
                created_at=timezone.now()
            )
            Comment.objects.create(
                post=post,
                author='Rebecca T.',
                content='I needed to read this today. God truly speaks through your writing!',
                created_at=timezone.now()
            )

            self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data for PrayerWord Women!'))