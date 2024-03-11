from django.views.generic import TemplateView, ListView, DetailView

from .models import Project


class HomeView(TemplateView):
    template_name = "TechAI/index.html"


class ProjectsView(ListView):
    model = Project
    template_name = "TechAI/projects.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'TechAI/project-detail.html'
    slug_field = "slug"
    context_object_name = "project"
