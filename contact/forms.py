from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*,'
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'picture',
            'category'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        
        #self.add_error(
        #    'first_name',
        #    ValidationError(
        #        'Mensagem do error',
        #        code='invalid',
        #    )
        #)

        return super().clean()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email já utilizado!!', code='invalid')
            )

        return email
