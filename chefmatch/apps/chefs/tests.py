from django.test import TestCase
from .models import Chef, Specialty

class ChefTestCase(TestCase):
    def setUp(self):
        # Create a specialty for testing
        self.specialty = Specialty.objects.create(description='Italian Cuisine')

        # Create a chef for testing
        self.chef = Chef.objects.create(
            name="John Doe",
            bio="A passionate chef specializing in Italian cuisine.",
            specialty=self.specialty
        )

    def test_chefs_list(self):
        # Send a GET request to the chefs list view
        response = self.client.get('/api/chefs/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected chefs
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')
        self.assertEqual(response.data[0]['bio'], 'A passionate chef specializing in Italian cuisine.')
        self.assertEqual(response.data[0]['specialty'], self.specialty.id)

    def test_chef_detail(self):
        # Send a GET request to the chef detail view with the chef's ID
        response = self.client.get(f'/api/chefs/{self.chef.id}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the chef's name, bio, and specialty ID
        self.assertContains(response, self.chef.name)
        self.assertContains(response, self.chef.bio)
        self.assertContains(response, str(self.chef.specialty.id))

    def test_create_chef(self):
        # Data for creating a new chef
        new_chef_data = {
            'name': 'Jane Doe',
            'bio': 'A talented pastry chef.',
            'specialty': self.specialty.id
        }

        # Send a POST request to create a new chef
        response = self.client.post('/api/chefs/', data=new_chef_data, content_type='application/json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the chef was created successfully
        self.assertEqual(Chef.objects.count(), 2)
        self.assertEqual(Chef.objects.last().name, 'Jane Doe')
        self.assertEqual(Chef.objects.last().bio, 'A talented pastry chef.')
        self.assertEqual(Chef.objects.last().specialty, self.specialty)

    def test_update_chef(self):
        # Data for updating the chef
        updated_chef_data = {
            'name': 'John Smith',
            'bio': 'An experienced chef with a focus on Italian cuisine.',
            'specialty': self.specialty.id
        }

        # Send a PUT request to update the chef
        response = self.client.put(f'/api/chefs/{self.chef.id}/', data=updated_chef_data, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the chef was updated successfully
        self.chef.refresh_from_db()
        self.assertEqual(self.chef.name, 'John Smith')
        self.assertEqual(self.chef.bio, 'An experienced chef with a focus on Italian cuisine.')
        self.assertEqual(self.chef.specialty, self.specialty)

    def test_delete_chef(self):
        # Send a DELETE request to delete the chef
        response = self.client.delete(f'/api/chefs/{self.chef.id}/')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the chef was deleted successfully
        self.assertEqual(Chef.objects.count(), 0)