from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name: ")
    address = models.CharField(max_length=100, verbose_name="Address: ")
    level = models.CharField(max_length=2, verbose_name="Level: ")
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name