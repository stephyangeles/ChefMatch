from .models import User
from django.test import TestCase

class SpecialtiesTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(name="John Doe", email="john@example.com", telephone="123")

    def test_specialties_list(self):
        # Send a GET request to the specialties list view
        response = self.client.get('/api/users/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected specialties
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')

    def test_users_detail(self):
        # Send a GET request to the user detail view with the user's ID
        response = self.client.get(f'/api/users/{self.user.id}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the user's name and ID
        self.assertContains(response, self.user.name)
        self.assertContains(response, str(self.user.id))

    def test_create_user(self):
        # Data for creating a new user
        new_user_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'telephone': '456'
        }

        # Send a POST request to create a new user
        response = self.client.post('/api/users/', data=new_user_data, content_type='application/json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the user was created successfully
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().name, 'Jane Doe')

    def test_update_user(self):
        # Data for updating the user
        updated_user_data = {
            'name': 'John Smith',
            'email': 'john@example.com',
            'telephone': '123'
        }

        # Send a PUT request to update the user
        response = self.client.put(f'/api/users/{self.user.id}/', data=updated_user_data, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the user was updated successfully
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'John Smith')

    def test_delete_user(self):
        # Send a DELETE request to delete the user
        response = self.client.delete(f'/api/users/{self.user.id}/')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the user was deleted successfully
        self.assertEqual(User.objects.count(), 0)