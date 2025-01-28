from rest_framework import serializers
from .models import Supervisor, StudentLead, Project, StudentTeam


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'


class StudentLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLead
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class StudentTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTeam
        fields = '__all__'
