from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth import password_validation
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

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        min_length=2,
        required=True,
        help_text='Required.',
        error_messages={
            'min_legth': 'Plese, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        max_length=30,
        min_length=2,
        required=True,
        help_text='Required.',
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Use the same password as before.',
        required=False,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email','username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        passwd = cleaned_data.get('password1')

        if passwd:
            user.set_password(passwd)
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas são diferentes.')
                )

        return super().clean()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Email já utilizado!!', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as err:
                self.add_error(
                    'password1',
                    ValidationError(err),
                )

        return password1
