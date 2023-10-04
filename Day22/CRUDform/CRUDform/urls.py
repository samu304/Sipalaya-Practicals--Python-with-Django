
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_data, name= "show_data"),
    path('delete/<int:id>', views.delete_data, name="delete_data"),
    path('update/<int:id>', views.update_data, name="update_data"),
]
