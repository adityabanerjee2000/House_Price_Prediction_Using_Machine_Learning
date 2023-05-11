from django.db import models
from django import forms

# Model defines your database
TYPE_CHOICES= (
    ('Feedback', 'Feedback'),
    ('Query', 'Query')
)

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    type_choice = models.CharField(max_length=10, choices=TYPE_CHOICES)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name