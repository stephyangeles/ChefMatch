from django.test import TestCase
from django.utils import timezone  # Import timezone utilities
from datetime import timedelta
from apps.chefs.models import Chef, Specialty
from apps.users.models import User
from apps.reservations.models import Reservation

class ReservationTestCase(TestCase):
    def setUp(self):
        # Create a Specialty instance
        self.specialty = Specialty.objects.create(description='Italian Cuisine')

        # Create a User instance
        self.user = User.objects.create(name='testuser', email='test@example.com')

        # Create a Chef instance with the required specialty
        self.chef = Chef.objects.create(
            name='Test Chef',
            bio='Test Bio',
            specialty=self.specialty  # Associate the specialty
        )

        # Create a Reservation instance with a timezone-aware datetime
        self.reservation = Reservation.objects.create(
            user=self.user,
            chef=self.chef,
            date=timezone.now() + timedelta(days=1),  # Reservation for tomorrow
            location='Test Location'
        )

    def test_reservations_list(self):
        # Send a GET request to the reservations list view
        response = self.client.get('/api/reservations/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected reservations
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[0]['chef'], self.chef.id)
        self.assertEqual(response.data[0]['location'], 'Test Location')

    def test_reservation_detail(self):
        # Send a GET request to the reservation detail view with the reservation's ID
        response = self.client.get(f'/api/reservations/{self.reservation.id}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the reservation's details
        self.assertContains(response, str(self.reservation.user.id))
        self.assertContains(response, str(self.reservation.chef.id))
        self.assertContains(response, self.reservation.location)

    def test_create_reservation(self):
        # Data for creating a new reservation with a timezone-aware datetime
        new_reservation_data = {
            'user': self.user.id,
            'chef': self.chef.id,
            'date': (timezone.now() + timedelta(days=2)).isoformat(),  # Reservation for 2 days later
            'location': 'New Location'
        }

        # Send a POST request to create a new reservation
        response = self.client.post('/api/reservations/', data=new_reservation_data, content_type='application/json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the reservation was created successfully
        self.assertEqual(Reservation.objects.count(), 2)
        self.assertEqual(Reservation.objects.last().user, self.user)
        self.assertEqual(Reservation.objects.last().chef, self.chef)
        self.assertEqual(Reservation.objects.last().location, 'New Location')

    def test_update_reservation(self):
        # Data for updating the reservation with a timezone-aware datetime
        updated_reservation_data = {
            'user': self.user.id,
            'chef': self.chef.id,
            'date': (timezone.now() + timedelta(days=3)).isoformat(),  # Update reservation date
            'location': 'Updated Location'
        }

        # Send a PUT request to update the reservation
        response = self.client.put(f'/api/reservations/{self.reservation.id}/', data=updated_reservation_data, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the reservation was updated successfully
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.location, 'Updated Location')
        self.assertEqual(self.reservation.date.date(), (timezone.now() + timedelta(days=3)).date())

    def test_delete_reservation(self):
        # Send a DELETE request to delete the reservation
        response = self.client.delete(f'/api/reservations/{self.reservation.id}/')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the reservation was deleted successfully
        self.assertEqual(Reservation.objects.count(), 0)