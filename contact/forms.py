from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
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

