"""
Integration Tests for the projects application's Django Rest Framework API.

These tests focus on security, permissions, and CRUD (Create, Read, Update, Delete) 
functionality of the ModelViewSets, ensuring the API behaves correctly for both 
anonymous and authenticated users.
"""
import pytest
from django.urls import reverse
from projects.models import Project, Technology, Category 

# --- INTEGRATION TESTS: REST API Security and CRUD ---

@pytest.mark.django_db
def test_project_api_delete_is_secure_for_anonymous_user(client, test_project):
    """
    Tests that an anonymous (logged-out) user CANNOT delete a project 
    due to IsAuthenticatedOrReadOnly permission.
    """
    url = reverse('project-detail', args=[test_project.pk])
    initial_count = Project.objects.count()
    
    response = client.delete(url)
    
    assert response.status_code == 403
    assert Project.objects.count() == initial_count

@pytest.mark.django_db
def test_project_api_delete_succeeds_for_admin_user(admin_client, test_project):
    """
    Tests that an authenticated admin user CAN delete a project.
    """
    url = reverse('project-detail', args=[test_project.pk])
    initial_count = Project.objects.count()
    
    response = admin_client.delete(url)

    assert response.status_code == 204
    assert Project.objects.count() == initial_count - 1

@pytest.mark.django_db
def test_api_project_creation_and_database_write(admin_client):
    """
    Integration test to verify the full API creation process:
    1. Authenticated user (admin_client) POSTs valid JSON data.
    2. Checks the API response status code (201 Created).
    3. Checks that the new project object exists in the database.
    """
    # Ensure related objects exist for the serializer
    Category.objects.get_or_create(name='Web Development')
    Technology.objects.get_or_create(name='Python')
    Technology.objects.get_or_create(name='Django')

    url = reverse('project-list')
    initial_count = Project.objects.count()

    new_project_data = {
        'title': 'API Test Project',
        'description': 'Created via a successful API POST request.',
        'link': 'http://apitest.com',
        'category': 'Web Development', # Serializer looks for the __str__ name
        'technologies': ['Python', 'Django'] # Serializer looks for the __str__ names
    }

    response = admin_client.post(
        url,
        new_project_data,
        format='json'
    )

    assert response.status_code == 201
    assert Project.objects.count() == initial_count + 1

    new_project = Project.objects.get(title='API Test Project')
    assert new_project.link == 'http://apitest.com'
    assert new_project.category.name == 'Web Development'
    assert new_project.technologies.count() == 2