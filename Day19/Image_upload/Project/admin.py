from django.contrib import admin

# sueruser
# username = "samundra123"
# password = "sam123"

# Register your models here.
from .models import Student
@ admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','level','image','slug']
