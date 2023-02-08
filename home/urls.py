from . import views
from django.urls import path
from .views import  contactView, successView

urlpatterns = [
    path('index/', views.index, name="index"), 
    path('', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('featured/', views.featured, name="featured"), 
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
]
    