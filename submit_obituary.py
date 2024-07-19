# Import necessary modules
import os
import django
from datetime import datetime
from django.utils.text import slugify
from obituaries.models import Obituary  

def submit_obituary(name, date_of_birth, date_of_death, content, author):
    try:
        # Connect to Django ORM
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obituary_platform.settings')
        django.setup()

        # Create slug from name 
        slug = slugify(name)

        # Create and save the obituary object
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()

        # Return success message
        return f"Obituary for {name} submitted successfully!"
    
    except Exception as e:
        # Handle exceptions
        return f"Error submitting obituary: {str(e)}"


