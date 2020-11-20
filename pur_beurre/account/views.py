from django.db import transaction, IntegrityError
from django.shortcuts import render

from .forms import SignUpForm, SignInForm
from .models import User

# Create your views here.
def signin(request):
    context = {

    }
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                with transaction.atomic():
                    user = User.objects.filter(username=username)
                    if user.exists():
                        # User.connect = True ??
                        context['logged'] = True
                    else:
                        raise ValidationError(
                            _('Cet utilisateur: %(username)s n\'est pas enregistré.'),
                            code='invalid',
                            params={'username': username},
                            )
                    return render(request, 'account/registered.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur est survenue. Merci de\
                recommencer votre requête."

    else:
        form = SignInForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'account/signup.html', context)

def signup (request):
    context = {

    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            try:
                with transaction.atomic():
                    user = User.objects.filter(email=email)
                    if not user.exists():
                        user = User.objects.create(
                            email = email,
                            first_name = first_name,
                            last_name = last_name,
                            password = password
                        )
                    else:
                        raise ValidationError(
                            _('Cet email: %(email)s est déjà enregistré'),
                            code='invalid',
                            params={'email': email},
                            )
                    return render(request, 'account/registered.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur est survenue. Merci de\
                recommencer votre requête."

    else:
        form = SignUpForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'account/signup.html', context)

def connexion(request):
    context={
        'connected': False
    }

    return render(request, 'account/connexion.html', context)