from django.test import TestCase, Client

class HomePageTest(TestCase):

    def test_home_page(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)
