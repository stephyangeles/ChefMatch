from django.test import TestCase
from django.utils import timezone
from apps.ledger.models import Ledger
from apps.reservations.models import Reservation
from apps.chefs.models import Chef
from apps.users.models import User
from apps.specialties.models import Specialty

class LedgerTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(
            name="testuser",
            email="testuser@example.com",
            telephone=123
        )

        # Create a specialty for testing
        self.specialty = Specialty.objects.create(
            description="specialty_test"
        )

        # Create a chef for testing
        self.chef = Chef.objects.create(
            name="Test Chef",
            bio="A test chef.",
            specialty_id=self.specialty.id
        )

        # Create a reservation for testing
        self.reservation = Reservation.objects.create(
            user=self.user,
            chef=self.chef,
            date=timezone.now(),
            location="Test Location"
        )

        # Create a ledger entry for testing
        self.ledger = Ledger.objects.create(
            reservation=self.reservation,
            amount=100.00,
            payment_method='Credit Card',
            state="True"
        )

    def test_ledger_list(self):
        # Send a GET request to the ledger list view
        response = self.client.get('/api/ledger/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected ledger entries
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['reservation'], self.reservation.id)
        self.assertEqual(response.data[0]['amount'], '100.00')
        self.assertEqual(response.data[0]['payment_method'], 'Credit Card')
        self.assertEqual(response.data[0]['state'], "True")

    def test_ledger_detail(self):
        # Send a GET request to the ledger detail view with the ledger's ID
        response = self.client.get(f'/api/ledger/{self.ledger.id}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the ledger's details
        self.assertContains(response, self.reservation.id)
        self.assertContains(response, str(self.ledger.amount))
        self.assertContains(response, self.ledger.payment_method)
        self.assertContains(response, str(self.ledger.state))

    def test_create_ledger(self):
        # Data for creating a new ledger entry
        new_ledger_data = {
            'reservation': self.reservation.id,
            'amount': '200.00',
            'payment_method': 'Cash',
            'state': "False"
        }

        # Send a POST request to create a new ledger entry
        response = self.client.post('/api/ledger/', data=new_ledger_data, content_type='application/json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the ledger entry was created successfully
        self.assertEqual(Ledger.objects.count(), 2)
        self.assertEqual(Ledger.objects.last().reservation_id, self.reservation.id)
        self.assertEqual(Ledger.objects.last().amount, 200.00)
        self.assertEqual(Ledger.objects.last().payment_method, 'Cash')
        self.assertEqual(Ledger.objects.last().state, "False")

    def test_update_ledger(self):
        # Data for updating the ledger entry
        updated_ledger_data = {
            'reservation': self.reservation.id,
            'amount': '150.00',
            'payment_method': 'Debit Card',
            'state': "False"
        }

        # Send a PUT request to update the ledger entry
        response = self.client.put(f'/api/ledger/{self.ledger.id}/', data=updated_ledger_data, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the ledger entry was updated successfully
        self.ledger.refresh_from_db()
        self.assertEqual(self.ledger.reservation_id, self.reservation.id)
        self.assertEqual(self.ledger.amount, 150.00)
        self.assertEqual(self.ledger.payment_method, 'Debit Card')
        self.assertEqual(self.ledger.state, "False")

    def test_delete_ledger(self):
        # Send a DELETE request to delete the ledger entry
        response = self.client.delete(f'/api/ledger/{self.ledger.id}/')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the ledger entry was deleted successfully
        self.assertEqual(Ledger.objects.count(), 0)