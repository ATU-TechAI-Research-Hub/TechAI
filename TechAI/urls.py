from django.urls import path

from .views import HomeView, ProjectsView, ProjectDetailView

app_name = "TechAI"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail")
]
