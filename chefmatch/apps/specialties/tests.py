from django.test import TestCase
from .models import Specialty

class SpecialtiesTestCase(TestCase):
    def setUp(self):
        # Create two specialties for testing
        Specialty.objects.create(description='Specialty 1')
        Specialty.objects.create(description='Specialty 2')

    def test_specialties_list(self):
        # Send a GET request to the specialties list view
        response = self.client.get('/api/specialties/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected specialties
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['description'], 'Specialty 1')
        self.assertEqual(response.data[1]['description'], 'Specialty 2')

    def test_specialty_detail(self):
        # Get the first specialty
        specialty = Specialty.objects.get(description='Specialty 1')

        # Send a GET request to the specialty detail view with the specialty's ID
        response = self.client.get(f'/api/specialties/{specialty.id}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the specialty's description and ID
        self.assertContains(response, specialty.description)
        self.assertContains(response, str(specialty.id))

    def test_create_specialty(self):
        # Data for creating a new specialty
        new_specialty_data = {
            'description': 'Specialty 3'
        }

        # Send a POST request to create a new specialty
        response = self.client.post('/api/specialties/', data=new_specialty_data, content_type='application/json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the specialty was created successfully
        self.assertEqual(Specialty.objects.count(), 3)
        self.assertEqual(Specialty.objects.last().description, 'Specialty 3')

    def test_update_specialty(self):
        # Get the first specialty
        specialty = Specialty.objects.get(description='Specialty 1')

        # Data for updating the specialty
        updated_specialty_data = {
            'description': 'Updated Specialty 1'
        }

        # Send a PUT request to update the specialty
        response = self.client.put(f'/api/specialties/{specialty.id}/', data=updated_specialty_data, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the specialty was updated successfully
        specialty.refresh_from_db()
        self.assertEqual(specialty.description, 'Updated Specialty 1')

    def test_delete_specialty(self):
        # Get the first specialty
        specialty = Specialty.objects.get(description='Specialty 1')

        # Send a DELETE request to delete the specialty
        response = self.client.delete(f'/api/specialties/{specialty.id}/')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the specialty was deleted successfully
        self.assertEqual(Specialty.objects.count(), 1)
        self.assertFalse(Specialty.objects.filter(id=specialty.id).exists())