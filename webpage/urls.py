from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage),
    path("about/", views.aboutPage),
    path("contact/", views.contactPage),
]
