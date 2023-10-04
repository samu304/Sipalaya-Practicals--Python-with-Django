
from django.contrib import admin
from django.urls import path
from authapp.views import register,log_in,dashboard,log_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register, name="register"),
    path('login/',log_in,name="log_in"),
    path('logout/',log_out,name="log_out"),
    path('dashboard/',dashboard,name="dashboard"),
]
