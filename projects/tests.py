"""
Tests for the 'projects' app.

This file contains the pytest test suite for all models, views,
and forms in the 'projects' app.
"""
import pytest
from django.urls import reverse
from django.core import mail
from django.conf import settings
from .models import Project, Technology, Category

# --- View "Read" Tests (GET requests) ---

@pytest.mark.django_db
def test_about_page_loads_correctly(client):
    """Tests that the 'about' page loads with a 200 OK status."""

    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_loads_correctly(client):
    """Tests that the homepage (project index) loads with a 200 OK status."""

    url = reverse('project_index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_displays_project_title(client, test_project):
    """Tests that a project's title appears on the homepage."""
    url = reverse('project_index')
    response = client.get(url)

    assert response.status_code == 200
    assert test_project.title in str(response.content)

@pytest.mark.django_db
def test_project_detail_page_loads_correctly(client, test_project):
    """Tests that a project's detail page loads and shows its content."""
    url = reverse('project_detail', args=[test_project.pk])
    response = client.get(url)

    assert response.status_code == 200
    assert test_project.title in str(response.content)
    assert test_project.description in str(response.content)

@pytest.mark.django_db
def test_technology_detail_page_displays_project(client, test_project, test_technology):
    """Tests that a technology's page correctly lists an associated project."""
    url = reverse('technology_detail', args=[test_technology.name])
    response = client.get(url)

    assert response.status_code == 200
    assert test_project.title in str(response.content)

# --- Contact Form Tests ---

@pytest.mark.django_db
def test_contact_form_submission_redirects(client):
    """Tests that a valid contact form submission redirects."""
    url = reverse('contact')
    form_data = {
        'name': "Test User",
        'email': "test@example.com",
        'message': "This is a test message."
     }
    
    response = client.post(url, form_data)

    assert response.status_code == 302 # Check for redirect
    assert response.url == reverse('project_index') # Check redirect location

@pytest.mark.django_db
def test_contact_form_sends_email(client):
    """Tests that a valid contact form submission sends an email."""
    url = reverse('contact')
    form_data = {
        'name': "Test User",
        'email': "test@example.com",
        'message': "This is a test message."
     }
    
    response = client.post(url, form_data)

    assert response.status_code == 302
    assert response.url == reverse('project_index')
    assert len(mail.outbox) == 1 # Check that one email was sent

    sent_email = mail.outbox[0]
    assert sent_email.subject == "New Contact Form Submission from Test User"
    assert "This is a test message." in sent_email.body
    assert sent_email.to == [settings.ADMIN_EMAIL]

# --- View "Write" Tests (CRUD & Security) ---

@pytest.mark.django_db
def test_project_add_page_is_secure(client):
    """Test that the 'project_add' page redirects unauthenticated users."""
    protected_url = reverse('project_add')
    login_url = reverse('admin:login')

    response = client.get(protected_url)

    assert response.status_code == 302
    assert response.url.startswith(login_url.rstrip('/'))

@pytest.mark.django_db
def test_project_create_view_valid_form(admin_client, project_form_data):
    """Test that a logged-in user can successfully create a new project"""
    url = reverse('project_add')

    # Check that the page loads
    response = admin_client.get(url)
    assert response.status_code == 200

    # Check project count before submission
    assert Project.objects.count() == 0

    # Post the valid form data
    response = admin_client.post(url, project_form_data)

    assert response.status_code == 302  # Redirects on success
    assert Project.objects.count() == 1
    assert Project.objects.first().title == project_form_data['title']

def test_project_create_view_invalid_form(admin_client):
    """
    Test that submitting an invalid form (e.g., missing title)
    re-renders the form with errors and does not create a project.
    """
    url = reverse('project_add')

    invalid_form_data = {
        'description': "A description without a title.",
    }

    assert Project.objects.count() == 0
    response = admin_client.post(url, invalid_form_data)
    
    assert response.status_code == 200 # Re-renders the page
    assert Project.objects.count() == 0 # No project was created
    assert "This field is required" in str(response.content)

@pytest.mark.django_db
def test_project_update_view(admin_client, test_project):
    """Test that a logged-in user can update a project."""
    url = reverse('project_edit', args=[test_project.pk])

    updated_data = {
        'title': 'Updated Title',
        'description': 'Updated description.',
        'technologies': [t.pk for t in test_project.technologies.all()],
        'link': test_project.link,
    }
    
    response = admin_client.post(url, updated_data)

    assert response.status_code == 302
    test_project.refresh_from_db()
    assert test_project.title == updated_data['title']

@pytest.mark.django_db
def test_project_delete_view(admin_client, test_project):
    """Test that a logged-in user can delete a project."""
    url = reverse('project_delete', args=[test_project.pk])
    
    # Check that the confirmation page loads
    response = admin_client.get(url)
    assert response.status_code == 200
    
    # Check count before deletion
    assert Project.objects.count() == 1

    # Post to confirm deletion
    response = admin_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('project_index')
    assert Project.objects.count() == 0

# --- API Tests ---

@pytest.mark.django_db
def test_project_api_delete_is_secure_for_anonymous_user(client, test_project):
    """
    Tests that an anonymous (logged-out) user CANNOT delete a project.
    """
    url = reverse('project-detail', args=[test_project.pk])
    assert Project.objects.count() == 1
    
    response = client.delete(url)
    
    assert response.status_code == 403
    assert Project.objects.count() == 1

@pytest.mark.django_db
def test_project_api_delete_succeeds_for_admin_user(admin_client, test_project):
    """
    Tests that an authenticated admin user CAN delete a project.
    """
    url = reverse('project-detail', args=[test_project.pk])
    assert Project.objects.count() == 1
    
    response = admin_client.delete(url)

    assert response.status_code == 204
    assert Project.objects.count() == 0