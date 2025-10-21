import pytest
from .models import Project, Technology

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