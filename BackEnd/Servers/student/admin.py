from django.contrib import admin
from .models import StudentLead, Supervisor, Project, StudentTeam
# Register your models here.


admin.site.register(Supervisor)
admin.site.register(StudentLead)
admin.site.register(StudentTeam)
admin.site.register(Project)