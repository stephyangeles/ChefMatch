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

        # Check if the response contains the specialty's name and ID
        self.assertContains(response, specialty.description)
        self.assertContains(response, str(specialty.id))
