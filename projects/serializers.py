from rest_framework import serializers
from .models import Project, Technology, Category

class TechnologySerializer(serializers.ModelSerializer):
    """Serializer to map the Technology model to JSON."""
    class Meta:
        model = Technology
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Category model to JSON."""
    class Meta:
        model = Category
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Project model to JSON.
    Includes nested serializers for readable relationships.
    """
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    technologies = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Project
        fields = (
            'url',
            'id', 
            'title', 
            'description', 
            'link', 
            'image', 
            'created_at',
            'category', 
            'technologies'
        )