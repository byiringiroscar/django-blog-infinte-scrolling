# generate_fake_data.py

# Set up Django environment
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')  # Change 'your_project' to your Django project name
django.setup()

# Import Django models
from home.models import Article

# Import Faker
from faker import Faker
fake = Faker()

# Generate and populate fake data
for i in range(100):
    sentences = ' '.join(fake.sentences(5))
    Article.objects.create(
        title=fake.sentence(),
        content=sentences,
        photo_url=f"https://picsum.photos/seed/{i+1}/600"
    )

print("Fake data generation completed successfully.")
