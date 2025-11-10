import pytest
from .models import Project, Category, Technology

@pytest.fixture
def test_technology():
    technology = Technology.objects.create(name="JavaScript")
    return technology

@pytest.fixture
def test_project(test_technology):
    """
    Creates a single test Project instance in the temporary test database.
    """
    project = Project.objects.create(
        title="Test Project 1",
        description="This is a description for our test project.",
        link="http://example.com",
    )
    project.technologies.add(test_technology)
    return project

@pytest.fixture
def project_form_data():
    """Returns a dictionary of valid data for the ProjectForm."""
    Category.objects.create(name="Test Category")
    Technology.objects.create(name="Test Tech")

    return {
        'title': 'New Test Project',
        'description': 'A description of the new test project.',
        'category': Category.objects.first().pk,
        # this is a ManyRelatedManager (ManyToMany fields are managers, not direct attributes)
        'technologies': [Technology.objects.first().pk],
        'link': 'http://new-project.com'
    }