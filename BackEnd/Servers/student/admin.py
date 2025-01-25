from django.contrib import admin
from .models import StudentLead, Supervisor, Project
# Register your models here.


admin.site.register(StudentLead)
admin.site.register(Supervisor)
admin.site.register(Project)