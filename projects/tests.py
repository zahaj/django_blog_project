import pytest
from django.urls import reverse
from projects import views 
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

