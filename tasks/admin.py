from django.contrib import admin
from tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "due_date",
        "project",
        "assignee",
        "id",
    ]
