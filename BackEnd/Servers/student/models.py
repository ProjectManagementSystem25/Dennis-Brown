from django.db import models

# Create your models here.


from django.db import models


class Supervisor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





class StudentLead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    registered_date = models.DateTimeField(auto_now_add=True)
    supervisor = models.ForeignKey( Supervisor, on_delete=models.CASCADE, related_name="supervisors")
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    studentlead = models.OneToOneField(StudentLead, on_delete=models.CASCADE, related_name="student" )
    

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"