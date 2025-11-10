import pytest
from django.urls import reverse
from urllib.parse import urlparse, parse_qs
from django.core import mail
from projects import views
from .models import Project, Technology, Category
# from django.test import TestCase

# Create your tests here.

@pytest.mark.django_db # Gives the test access to the database
def test_about_page_loads_correctly(client):

    # Arrange: Get the URL for the 'about' page
    url = reverse('about_me')

    # Act: Use the test 'client' to make a GET request to the URL
    response = client.get(url)

    # Assert: Check that the response status code is 200
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_loads_correctly(client):

    # Arrange
    url = reverse(views.project_index) # You can also use: url = reverse('project_index')

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_displays_project_title(client, test_project):

    # Arrange
    url = reverse('project_index')
    
    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    assert "Test Project 1" in str(response.content)

@pytest.mark.django_db
def test_project_detail_page_loads_correctly(client, test_project):

    # Arrange
    url = reverse('project_detail', args=[test_project.pk])

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    assert "Test Project 1" in str(response.content)
    assert "This is a description" in str(response.content)

@pytest.mark.django_db
def test_technology_detail_page_displays_project(client, test_project, test_technology):
    
    # Arrange
    url = reverse('technology_detail', args=[test_technology.name])
    
    # Act
    response = client.get(url)
    
    # Assert
    assert "Test Project 1" in str(response.content)

@pytest.mark.django_db
def test_contact_form_submission(client):

    # Arrange
    url = reverse('contact')
    form_data = {
        'name': "Test User",
        'email': "test@example.com",
        'message': "This is a test message."
     }
    
    # Act: Simulate a POST request
    response = client.post(url, form_data)

    # Assert: Check for a successful redirect
    assert response.status_code == 302 # 302 is the code for a redirect

    # Assert: Check that it redirected to the correct page
    assert response.url == reverse('project_index')

@pytest.mark.django_db
def test_contact_form_sends_email(client):

    # Arrange
    url = reverse('contact')
    form_data = {
        'name': "Test User",
        'email': "test@example.com",
        'message': "This is a test message."
     }
    
    # Act
    response = client.post(url, form_data)

    # Assert
    assert response.status_code == 302
    assert response.url == reverse('project_index')

    # Check that exactly one email was sent
    assert len(mail.outbox) == 1

    # Get the email and check its details
    sent_email = mail.outbox[0]
    assert sent_email.subject == "New Contact Form Submission from Test User"
    assert "This is a test message." in sent_email.body
    assert "test@example.com" in sent_email.body
    assert sent_email.to == ['e.zahajkiewicz@gmail.com']

@pytest.mark.django_db
def test_project_add_page_is_secure(client, project_form_data):
    """Test that the 'project_add' page redirects unauthenticated users."""
    
    # Arrange
    protected_url = reverse('project_add')
    login_url = reverse('admin:login')

    
    # Act: Visit the protected page as a logged-out user
    response = client.get(protected_url)

    # Assert
    assert response.status_code == 302 # Assert it's a redirect (302)
    # Assert the redirect location.
    # The response.url will be '/admin/login?next=/project/add/'
    # This assertion checks if that string *starts with* '/admin/login'
    assert response.url.startswith(login_url.rstrip('/'))
    
    parsed = urlparse(response.url)
    assert parsed.path.rstrip('/') == login_url.rstrip('/')
    assert parse_qs(parsed.query)['next'][0] == reverse('project_add')

# @pytest.mark.django_db <-- no need for this fixture
# Using the admin_client fixture will cause the test to automatically be marked
# for database use (no need to specify the django_db() mark)
def test_project_create_view_valid_form(admin_client, project_form_data):
    """Test that a logged-in user can create a project"""
    # Arrange
    url = reverse('project_add')

    # Act & Assert
    # 1. Check that the page loads
    response = admin_client.get(url)
    assert response.status_code == 200

    # 2. Check that the POST submission works
    # Check project count before
    assert Project.objects.count() == 0
    # Post the form data
    response = admin_client.post(url, project_form_data)
    # Assert it redirects after success
    assert response.status_code == 302
    # Assert it created a project
    Project.objects.count() == 1
    # Assert the title is correct
    Project.objects.first().title == 'New Test Project'

def test_project_update_view(admin_client, test_project):
    """Test that a logged-in user can update a project."""

    # Arrange
    url = reverse('project_edit', args=[test_project.pk])
    technologies = test_project.technologies.all()
    print("Technologies QuerySet:", technologies)  

    # New data to post, include all required fields
    updated_data = {
        'title': 'Updated Title',
        'description': 'Updated description.',
        'technologies': [t.pk for t in test_project.technologies.all()],
        'link': test_project.link,
    }
    assert test_project.title == 'Test Project 1'
    
    # Act: Post the new data
    response = admin_client.post(url, updated_data)

    # Assert
    assert response.status_code == 302 # Redirects
    # Fetch the project from the DB again to check its values
    test_project.refresh_from_db()
    assert test_project.title == 'Updated Title'

def test_project_delete_view(admin_client, test_project):
    """Test that a logged-in user can delete a project."""

    # Arrange
    url = reverse('project_delete', args=[test_project.pk])
    
    # Act & Assert
    # 1. Check that the confirmation page loads
    response = admin_client.get(url)
    assert response.status_code == 200
    
    # 2. Check that the POST submission deletes the object
    assert Project.objects.count() == 1
    response = admin_client.post(url)

    assert response.status_code == 302 # Redirects
    assert response.url.startswith(reverse('project_index'))
    assert Project.objects.count() == 0 # Project is gone

def test_project_create_view_invalid_form(admin_client):
    """
    Test that submitting an invalid form doesn't create a project
    and re-renders the form with an error.
    """
    url = reverse('project_add')
    tech = Technology.objects.create(name="Django")
    invalid_form_data = {
        'title': 'A Title',
        'description': "This is a test description.",
        #'technologies': [tech.pk],
    }

    # Act
    assert Project.objects.count() == 0
    response = admin_client.post(url, invalid_form_data)
    
    # Assert
    assert response.status_code == 200 # It should re-render the page, not redirect
    assert Project.objects.count() == 0 # No project was created
    assert "This field is required" in str(response.content) # It shows an error message
