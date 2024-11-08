# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    phone_number = forms.CharField(max_length=15, required=True, label="Número de Teléfono")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Crea el perfil con el número de teléfono al registrarse
            Profile.objects.update_or_create(user=user, defaults={'phone_number': self.cleaned_data['phone_number']})
        return user

    
class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    phone_number = forms.CharField(required=False, max_length=15, label="Número de Teléfono")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance, 'profile'):
            self.fields['phone_number'].initial = self.instance.profile.phone_number

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        if commit:
            user.save()
            phone_number = self.cleaned_data.get('phone_number')
            Profile.objects.update_or_create(user=user, defaults={'phone_number': phone_number})
        return user