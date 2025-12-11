from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ("title", "user", "created", "important")


# Register your models here.

admin.site.register(Task, TaskAdmin)
