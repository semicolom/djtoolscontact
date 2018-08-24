from django.test import TestCase
from django.urls import reverse


class CompensationTestCase(TestCase):
    url = reverse('contact')

    def test_context_data(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
