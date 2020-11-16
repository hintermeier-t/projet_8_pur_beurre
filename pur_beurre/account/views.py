from django.db import transaction, IntegrityError
from django.shortcuts import render

from .forms import SignUpForm
from .models import User

# Create your views here.
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