



from django.urls import path
from . import views

urlpatterns = [
    # StudentLead endpoints
    path('student_leads/', views.student_leads, name='student_leads'),
    path('student_leads/<int:id>/', views.student_lead, name='student_lead'), 

    # Supervisor endpoints
    path('supervisors/', views.supervisors, name='supervisors'), 
    path('supervisors/<int:id>/', views.supervisor, name='supervisor'),

    # Project endpoints
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.project, name='project'), 

    # StudentTeam endpoints
    path('student_teams/', views.student_teams, name='student_teams'),
    path('student_teams/<int:id>/', views.student_team, name='student_team'), 
]
