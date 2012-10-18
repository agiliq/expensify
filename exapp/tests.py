from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core import mail

from exapp.models import ExpenseCategory, Expense


class SimpleViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="demo", password="demo")
        self.category = ExpenseCategory.objects.create(title = "Foo", 
            description = "Bar")

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

    def test_create(self):
        response = self.c.get("/create/",)
        self.assertEqual(response.status_code, 302)        
        self.c.login(username="demo", password="demo")
        response = self.c.get("/create/",)
        self.assertEqual(response.status_code, 200)          

    def test_reimburse(self):
        response = self.c.get("/reimburse/",)
        self.assertEqual(response.status_code, 302)        
        self.c.login(username="demo", password="demo")
        response = self.c.get("/reimburse/",)
        self.assertEqual(response.status_code, 200)    

    def test_reimburse_post(self):
        "Test that an Expense object is created and a mail is sent."
        self.c.login(username="demo", password="demo")
        response = self.c.post("/reimburse/",
            {"date": "10/04/2012", 
            "amount": 100,
            "category": self.category.pk, 
            }
            )
        self.assertEqual(response.status_code, 302)        
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="demo", password="demo")
        self.category = ExpenseCategory.objects.create(title = "Foo", 
            description = "Bar")

    def test_emails(self):
        "Creating Expense objects and changing their status should send mails"
        expense = Expense.objects.create(amount=100, date="2012-10-13", 
            category=self.category, usr=self.user)
        self.assertEqual(len(mail.outbox), 1)
        expense.status = True
        expense.save()
        self.assertEqual(len(mail.outbox), 2)


