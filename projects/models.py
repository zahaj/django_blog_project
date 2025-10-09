from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title