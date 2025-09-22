from django.db import models

# Create your models here.


class Submission(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100)
    terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
         return f'{self.first_name} {self.surname} - {self.created_at.strftime("%Y-%m-%d %H:%M")}'