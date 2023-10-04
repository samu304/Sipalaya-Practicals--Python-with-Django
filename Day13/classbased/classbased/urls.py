
from django.contrib import admin
from django.urls import path
from cbview import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.my_fview, name="funcview"), # for function based view

    path('class/', views.my_cview.as_view(), name="classview" ), # for class based views

    path('home/', views.Home.as_view(), name="template"), # for template class view

    path('extrahome/', views.Home.as_view(extra_context = {'subject': 'Python Django Developer'}), name="template"), # for template class view with extra context

    path('redirect/', views.RedirectView.as_view(), name = "redirect_View"), # for redirect view

    path('google/', views.RedirectView.as_view(url = "https://google.com"), name="google"), 

    path('pattern/', views.RedirectView.as_view(pattern_name = "funcview"), name="pattern"),
]
