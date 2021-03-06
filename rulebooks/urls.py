from django.urls import path
from . import views

urlpatterns = [
    path('', views.rulebooks, name="rulebooks"),
    path('rules/<str:html_filename>', views.rules, name="rules")
]
