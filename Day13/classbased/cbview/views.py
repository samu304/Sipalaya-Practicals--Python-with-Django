from typing import Any, Dict, Optional
from django.shortcuts import render

# Create your views here.

# for funcrion based view
from django.http import HttpResponse
def my_fview(request):
    return HttpResponse("<h1> This is a Function-based view</h1>")

# for class based view (Base View -> View)
from django.views import View

class my_cview(View):
    def get(self,request):
        return HttpResponse("<h1> This is a Class Based views</h1>")
    
# for (Base View -> Template View)
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

    # for context based view
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["name"] = "Samundra Khanal"
        context["age"] = 22
        context["address"] = "Bharatpur-12"
        context["level"] = "Bachelor"
        context["married"] = False
        return context
    
# for (Base View -> Redirect View)
from django.views.generic.base import RedirectView

# class Redirect(RedirectView):
    
    
#      # redirects to this name id url not given
#     permanent = False
#     query_string = False

#     def get_redirect_url(self, *args, **kwargs):
#         print(**kwargs)
#         return super().get_redirect_url(*args, **kwargs)
