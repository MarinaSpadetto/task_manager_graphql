from django.contrib import admin
from task_manager.models import Task


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)
