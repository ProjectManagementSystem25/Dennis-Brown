from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentTeam, StudentLead, Supervisor, Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# ?serializers
from .serializers import StudentLeadSerializer, StudentTeamSerializer, SupervisorSerializer, ProjectSerializer


# Create your views here.

# STUDENT_LEAD AS PLURAL
@api_view(['GET', 'POST'])
def student_leads(request):

    try:
        student_leads = StudentLead.objects.all()
    except StudentLead.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = StudentLeadSerializer(student_leads, many=True)
        return Response(serializers.data, status = status.HTTP_302_FOUND)

    elif request.method == 'POST':
        serializers = StudentLeadSerializer( data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,  status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

# STUDENT_LEAD AS INDIVIDUAL
@api_view(['GET', 'PUT', 'DELETE'])
def student_lead(request, id):
    try:
        student_lead_one = StudentLead.objects.get(pk = id)
    except StudentLead.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = StudentLeadSerializer(student_lead_one)
        return Response( student_lead_one.data, status = status.HTTP_302_FOUND)

    elif request.method == 'PUT':
        serializers = StudentLeadSerializer( student_lead_one, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,  status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student_lead_one.delete()
        return Response( student_lead_one.data, status = status.HTTP_202_ACCEPTED)


# SUPERVISORS AS PLURAL
@api_view(['GET', 'POST'])
def supervisors(request):

    try:
        supervisors = Supervisor.objects.all()
    except Supervisor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SupervisorSerializer(supervisors, many=True)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'POST':
        serializers = SupervisorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# SUPERVISOR AS INDIVIDUAL
@api_view(['GET', 'PUT', 'DELETE'])
def supervisor(request, id):
    try:
        supervisor_one = Supervisor.objects.get(pk=id)
    except Supervisor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SupervisorSerializer(supervisor_one)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'PUT':
        serializers = SupervisorSerializer(supervisor_one, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        supervisor_one.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


# PROJECTS AS PLURAL
@api_view(['GET', 'POST'])
def projects(request):

    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'POST':
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# PROJECT AS INDIVIDUAL
@api_view(['GET', 'PUT', 'DELETE'])
def project(request, id):
    try:
        project_one = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = ProjectSerializer(project_one)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'PUT':
        serializers = ProjectSerializer(project_one, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project_one.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


# STUDENT_TEAMS AS PLURAL
@api_view(['GET', 'POST'])
def student_teams(request):

    try:
        student_teams = StudentTeam.objects.all()
    except StudentTeam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = StudentTeamSerializer(student_teams, many=True)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'POST':
        serializers = StudentTeamSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# STUDENT_TEAM AS INDIVIDUAL
@api_view(['GET', 'PUT', 'DELETE'])
def student_team(request, id):
    try:
        student_team_one = StudentTeam.objects.get(pk=id)
    except StudentTeam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = StudentTeamSerializer(student_team_one)
        return Response(serializers.data, status=status.HTTP_302_FOUND)

    elif request.method == 'PUT':
        serializers = StudentTeamSerializer(student_team_one, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_team_one.delete()
        return Response(status=status.HTTP_202_ACCEPTED)









# admindb, zxcvbnm,./ 