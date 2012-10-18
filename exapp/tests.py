from django.test import TestCase, Client
from django.contrib.auth.models import User


class SimpleViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="demo", password="demo")
        self.c.login()

    def test_index(self):
        "Index reponds correctly to both logged in and logged out users"
        response = self.c.get("/",)
        self.assertEqual(response.status_code, 200)
        self.c.login(username="demo", password="demo")
        response = self.c.get("/",)
        self.assertEqual(response.status_code, 200)        

    def test_profile(self):
        "Profile should redirect for not logged in users and let in for logged in."
        response = self.c.get("/profile/",)
        self.assertEqual(response.status_code, 302)        
        self.c.login(username="demo", password="demo")
        response = self.c.get("/profile/",)
        self.assertEqual(response.status_code, 200)        
