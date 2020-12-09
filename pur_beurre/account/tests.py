from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Favorite
from catalog.models import Product


#- Signin page
class SigninPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'NinaS'
        self.password = 'Sinnerman'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    #- Test a signin with valid credentials
    def test_signin_valid_credentials(self):
        self.client.logout()
        self.client.login(username=self.username, password=self.password)
        request = self.client.post(reverse('account:signin'))
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/')

#- Signup page
class SignupPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_signup_form(self):
        request = self.client.get(reverse('account:signup'))
        self.assertEqual(request.status_code, 200)
        request = self.client.post(reverse("account:signup"), {'username': 'Foo', 'password1': 'Foo12345','password2':'Foo12345'})
        #self.assertEqual(request.status_code, 302)
        user = User.objects.get(username='Foo')
        self.assertIsNotNone(user)

#- Account page
class AccountPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'MilesD'
        self.password = 'KindOfBlue'
        self.user = User.objects.create_user(
            username = self.username,
            password = self.password
        )

    def test_account_not_logged_in(self):
        request =  self.client.get(reverse('account/my_account'))
        self.assertRedirects(request, '/')

