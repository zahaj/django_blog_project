"""
Integration Tests for the projects application's standard Django Views (HTML).

These tests verify the end-to-end functionality of user-facing features,
including standard page loads, form submissions (Contact, CRUD),
and security/redirects.
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
    url = reverse('projects:about')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_loads_correctly(client):
    """Tests that the homepage (project index) loads with a 200 OK status."""
    url = reverse('projects:project_index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_project_index_displays_project_title(client, test_project):
    """Tests that a project's title appears on the homepage."""
    url = reverse('projects:project_index')
    response = client.get(url)
    assert response.status_code == 200
    assert test_project.title in str(response.content)

@pytest.mark.django_db
def test_project_detail_page_loads_correctly(client, test_project):
    """Tests that a project's detail page loads and shows its content."""
    url = reverse('projects:project_detail', args=[test_project.pk])
    response = client.get(url)
    assert response.status_code == 200
    assert test_project.title in str(response.content)
    assert test_project.description in str(response.content)

@pytest.mark.django_db
def test_technology_detail_page_displays_project(client, test_project, test_technology):
    """Tests that a technology's page correctly lists an associated project."""
    url = reverse('projects:technology_detail', args=[test_technology.name])
    response = client.get(url)
    assert response.status_code == 200
    assert test_project.title in str(response.content)

# --- Contact Form Test ---

@pytest.mark.django_db
def test_contact_form_sends_email_and_redirects(client):
    """
    Tests that a valid contact form submission sends an email
    and correctly redirects the user to the homepage.
    """
    url = reverse('projects:contact')
    form_data = {
        'name': "Test User",
        'email': "test@example.com",
        'subject': "Test Subject",
        'message': "This is a test message."
     }
    
    assert len(mail.outbox) == 0
    
    response = client.post(url, form_data)

    assert response.status_code == 302
    assert response.url == reverse('projects:project_index')
    assert len(mail.outbox) == 1

    sent_email = mail.outbox[0]
    assert sent_email.subject == f"Portfolio Contact: {form_data['subject']}"
    assert "This is a test message." in sent_email.body
    assert sent_email.to == [settings.ADMIN_EMAIL]

# --- View "Write" Tests (CRUD & Security) ---

@pytest.mark.django_db
def test_project_add_page_is_secure(client):
    """Test that the 'project_add' page redirects unauthenticated users."""
    protected_url = reverse('projects:project_add')
    login_url = reverse('admin:login')
    response = client.get(protected_url)
    assert response.status_code == 302
    assert response.url.startswith(login_url.rstrip('/'))

@pytest.mark.django_db
def test_project_create_view_valid_form(admin_client, project_form_data):
    """Test that a logged-in user can successfully create a new project"""
    url = reverse('projects:project_add')
    
    response = admin_client.get(url)
    assert response.status_code == 200

    assert Project.objects.count() == 0
    response = admin_client.post(url, project_form_data)

    assert response.status_code == 302
    assert Project.objects.count() == 1
    assert Project.objects.first().title == project_form_data['title']

@pytest.mark.django_db
def test_project_create_view_invalid_form(admin_client):
    """
    Test that submitting an invalid form (e.g., missing title)
    re-renders the form with errors and does not create a project.
    """
    url = reverse('projects:project_add')
    invalid_form_data = {
        'description': "A description without a title.",
    }

    assert Project.objects.count() == 0
    response = admin_client.post(url, invalid_form_data)
    
    assert response.status_code == 200 # Re-renders the page
    assert Project.objects.count() == 0
    assert "This field is required" in str(response.content)

@pytest.mark.django_db
def test_project_update_view(admin_client, test_project):
    """Test that a logged-in user can update a project."""
    url = reverse('projects:project_edit', args=[test_project.pk])
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
    url = reverse('projects:project_delete', args=[test_project.pk])
    
    response = admin_client.get(url)
    assert response.status_code == 200
    
    assert Project.objects.count() == 1
    response = admin_client.post(url)

    assert response.status_code == 302
    assert response.url == reverse('projects:project_index')
    assert Project.objects.count() == 0