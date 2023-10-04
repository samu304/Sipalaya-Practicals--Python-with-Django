
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_data, name="show_data"),
    path('edit/<int:id>', views.edit_data, name="edit_data"),
    path('delete/<int:id>', views.delete_data, name="delete_data"),
]
