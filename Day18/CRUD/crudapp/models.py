from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    phone = models.CharField(max_length=10, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.first_name