
from django.contrib import admin
from django.urls import path
from noteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name="show_note"),
    path('delete/<int:id>', views.delete_note, name="delete_note"),
    path('update/<int:id>', views.update_note, name="update_note"),
]
