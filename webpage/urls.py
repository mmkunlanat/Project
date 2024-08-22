from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name="contact"),
    path("table/", views.table_Page, name="table-page"),
    path("card/", views.card_Page, name="card-page"),
    path("card_color/", views.cardColorPage, name="color"),
    path("form/", views.form_Page, name="form"),
]
