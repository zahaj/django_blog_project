"""
Data models for the 'projects' app.

This file defines the database schema for the portfolio.
It includes models for Projects, the Technologies used, and the
Categories they belong to. These models are the single source of truth
for the application's data structure.
"""
from django.db import models

class Technology(models.Model):
    """Represents a single technology or framework (e.g., Python, Django)."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """A category to group projects (e.g., Web Development, Data Science)."""
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    """The core model representing a single portfolio project."""
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title