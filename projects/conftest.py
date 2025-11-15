"""
Pytest fixtures for the 'projects' app.

This file defines reusable test data and components that are
injected into test functions.
"""
import pytest
from .models import Project, Category, Technology

@pytest.mark.django_db
@pytest.fixture
def test_technology():
    """Provides a single Technology object created in the test database."""
    technology = Technology.objects.create(name="JavaScript")
    return technology

@pytest.mark.django_db
@pytest.fixture
def test_project(test_technology):
    """
    Provides a single Project object, linked to 'test_technology',
    created in the test database.
    """
    project = Project.objects.create(
        title="Test Project 1",
        description="This is a description for our test project.",
        link="http://example.com",
    )
    project.technologies.add(test_technology)
    return project

@pytest.mark.django_db
@pytest.fixture
def project_form_data():
    """
    Provides a dictionary of valid data for submitting a ProjectForm.
    Ensures that the required Category/Technology objects exist.
    """
    # Ensure related objects exist in the test DB
    category = Category.objects.create(name="Test Category")
    tech = Technology.objects.create(name="Test Tech")

    return {
        'title': 'New Test Project',
        'description': 'A description of the new test project.',
        'category': category.pk,
        'technologies': [tech.pk],
        'link': 'http://new-project.com'
    }