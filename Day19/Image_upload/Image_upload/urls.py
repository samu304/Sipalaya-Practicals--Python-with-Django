
from django.contrib import admin
from django.urls import path
from Project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_data, name="show_data"),
    path('del/<slug:slug>/', views.delete_data, name="delete_data"),
    path('update/<slug:slug>/', views.update_data, name="update_data"),

    
] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
