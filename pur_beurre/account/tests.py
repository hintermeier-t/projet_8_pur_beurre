"""
Testing 'Account' app module
"""
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse

from .models import Favorite
from catalog.models import Product


#- Signin page
class SigninPageTestCase(TestCase):
    def setUp(self):
        self.username = 'NinaS'
        self.password = 'Sinnerman'
        self.user = User.objects.create_user(
            username = self.username,
            password = self.password
        )

    def test_signin_invalid_credentials(self):
        request = self.client.post(reverse(
            'account:signin'),
            {
                'username': self.username,
                'password': "LittleGirlBlues"
            })
        self.assertEqual(request.context['Error'], 'Invalid')
        

    #- Test a signin with valid credentials
    def test_signin_valid_credentials(self):
        self.client.login(
            username = self.username,
            password = self.password
            )
        request = self.client.post(reverse('account:signin'))
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/')

#- Signup page
class SignupPageTestCase(TestCase):
    #- Test the account creation
    def test_signup_form(self):
        request = self.client.get(reverse('account:signup'))
        self.assertEqual(request.status_code, 200)
        request = self.client.post(
            reverse("account:signup"),
            {
                'username': 'AlexandreA', 
                'password1': 'OnEnAGros',
                'password2':'OnEnAGros'
            })
        user = User.objects.get(username = 'AlexandreA')
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
        
    def test_account_logged_in(self):
        self.client.login(
            username = self.username,
            password = self.password
        )
        request =  self.client.get(reverse('account:my_account'))
        self.assertEqual(request.status_code, 200)

#- Signout
class SignoutPageTestcase(TestCase):
    def setUp(self):
        self.username = 'ChesterB'
        self.password = 'InTheEnd'
        self.user = User.objects.create_user(
            username = self.username,
            password = self.password
        )
        self.client.login(
            username=self.username,
            password=self.password
            )

    #- Test the logout function
    def test_signout(self):
        request = self.client.get(
            reverse('account:signout')
        )
        self.assertEqual(request.status_code, 302)

#- Save mail
class SaveMailTestCase(TestCase):
    def setUp(self):
        self.mail = "moonlight@vermont.com"
        self.username = 'LouisA'
        self.password = 'YouRascalYou'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    #- test without logged user
    def test_no_logged_in(self):
        self.client.logout()
        response = self.client.get(
            reverse('account:mail_save'), {'email': self.mail})
        self.assertEqual(response.content, b'500')

    #- Test the mail changing.
    def test_mail_change(self):
        self.client.login(
            username=self.username,
            password=self.password
            )
        self.assertEqual(self.user.email, "")
        self.client.login(
            username=self.username,
            password=self.password
            )
        response = self.client.get(
            reverse('account:mail_save'), {'email': self.mail})
        self.assertEqual(response.content, b'209')
    
#- Save product
class SaveFavoriteTestCase(TestCase):
    def setUp(self):
        self.username = "SarahV"
        self.password = "LullabyOfBirdland"
        self.product = Product.objects.create(
            name = 'Produit à manger',
            brand = 'Chuipariche',
            code = '1234567890123',
            nutriscore = 'B',
            description = 'C\'est bon à cuisiner',
            picture = 'truc.com/image.jpg',
            url = 'truc.com/fiche.html',
        )

        self.user = User.objects.create_user(
            username = self.username,
            password = self.password
        )

    #- Test if the user is not logged in
    def test_favorite_not_logged_in(self):
        favorites_old_count = Favorite.objects.count()
        request = self.client.get(
            reverse('account:save'),
            {'product': self.product.id}
        )
        self.assertEqual(request.content, b'500')

    #- test a Favorite is saved
    def test_new_favorite_logged_in(self):
        self.client.login(
            username=self.username,
            password=self.password
            )
        favorites_old_count = Favorite.objects.count()
        request = self.client.get(
            reverse('account:save'),
            {'product': self.product.id}
        )
        self.assertEqual(request.content, b'209')
        favorites_new_count = Favorite.objects.count()
        self.assertEqual(favorites_new_count, favorites_old_count+1)