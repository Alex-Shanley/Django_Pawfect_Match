from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
import os


def pet_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('uploads', filename)


class Pet(models.Model):
    
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Rabbit', 'Rabbit'),
        ('Bird', 'Bird'),
        ('Reptile', 'Reptile'),
    ]
    
    img = models.ImageField(upload_to=pet_image_upload_path, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    breed = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.species})'

    @property
    def image_url(self):
        
        if self.img:
            return self.img.url
        return None