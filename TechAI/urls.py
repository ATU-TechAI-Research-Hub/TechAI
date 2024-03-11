from django.urls import path

from . import views

app_name = "TechAI"
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home")
]
