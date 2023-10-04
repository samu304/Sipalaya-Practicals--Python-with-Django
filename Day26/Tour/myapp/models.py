from django.db import models

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    when = models.DateField()
    count = models.IntegerField()
    contact = models.CharField(max_length=10)
    time = models.CharField(max_length=50)