from django import forms
from django.utils.translation import gettext as _

from captcha.fields import ReCaptchaField

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    captcha = ReCaptchaField(label='')

    class Meta:
        model = ContactRequest
        fields = [
            'name',
            'email',
            'phone_number',
            'message'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['phone_number'].required = False

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            error = _("El email o el teléfono son obligatorios.")
            self.add_error('email', error)
            self.add_error('phone_number', error)
