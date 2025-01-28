from django.core.exceptions import ValidationError
from django.db import models

# Supervisor model
class Supervisor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if Supervisor.objects.filter(first_name=self.first_name, last_name=self.last_name).exclude(id=self.id).exists():
            raise ValidationError(f"A supervisor with the name {self.first_name} {self.last_name} already exists.")


# StudentLead model
class StudentLead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if StudentLead.objects.filter(first_name=self.first_name, last_name=self.last_name).exclude(id=self.id).exists():
            raise ValidationError(f"A student with the name {self.first_name} {self.last_name} already exists.")


# Project model
class Project(models.Model):
    class Category(models.TextChoices):
        AI = "AI", "Artificial Intelligence"
        WEB_DEV = "WEB_DEV", "Web Development"

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.WEB_DEV
    )
    studentOwner = models.OneToOneField(
        StudentLead, on_delete=models.CASCADE, related_name="project",null=True, blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


# StudentTeam model
class StudentTeam(models.Model):
    Leaderlead = models.OneToOneField(
        StudentLead, on_delete=models.CASCADE, related_name="team_lead"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if StudentTeam.objects.filter(first_name=self.first_name, last_name=self.last_name).exclude(id=self.id).exists():
            raise ValidationError(f"A student with the name {self.first_name} {self.last_name} already exists.")
