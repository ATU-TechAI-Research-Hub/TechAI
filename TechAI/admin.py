from django.contrib import admin

from .models import Peer, Mentor, Project, Publication


@admin.register(Peer)
class PeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'major', 'degree_level',)
    list_filter = ('major', 'degree_level',)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'professor_type',)
    list_filter = ('professor_type', 'department',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'mentor', 'start_date', 'end_date',)
    list_filter = ('start_date', 'end_date',)
    search_fields = ('title', 'description', 'mentor__name', 'mentor__email',)
    ordering = ('-start_date', 'title',)
    filter_horizontal = ('peers',)
    raw_id_fields = ('mentor', 'publication',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    search_fields = ('title', 'url',)
    ordering = ('title',)
