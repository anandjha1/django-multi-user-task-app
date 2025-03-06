from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "completed", "created_at"]


admin.site.register(Task, TaskAdmin)


