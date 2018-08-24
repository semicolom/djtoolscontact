from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import gettext as _


class ContactInformation(models.Model):
    """
    This model will store the comapny places to be shown in a contact page
    """

    name = models.CharField(_('nombre'), max_length=255)
    address = models.TextField(_('dirección'))
    phone_number = models.CharField(_('teléfono'), max_length=255)
    email = models.EmailField(_('email'))
    longitude = models.DecimalField(_('longitud'), max_digits=11, decimal_places=8)
    latitude = models.DecimalField(_('latitud'), max_digits=11, decimal_places=8)

    class Meta:
        verbose_name = _("Información de contacto")
        verbose_name_plural = _("Informaciones de contacto")

    def __str__(self):
        return self.name


class ContactRequest(models.Model):
    """
    This model will manage the requests from the contact form
    """

    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    name = models.CharField(_('nombre'), max_length=255)
    email = models.EmailField(_('email'))
    phone_number = models.CharField(_('teléfono'), max_length=255)
    message = models.TextField(_('mensaje'))
    contacted = models.BooleanField(_('contactado'), default=False)

    class Meta:
        verbose_name = _("Petición de contacto")
        verbose_name_plural = _("Peticiones de contacto")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        created = self.pk is None

        super().save(*args, **kwargs)

        if created:
            self._send_mail()

    def get_contact_information(self):
        if self.email and self.phone_number:
            return _("{email} o {phone_number}").format(
                email=self.email,
                phone_number=self.phone_number
            )
        if self.email:
            return self.email
        return self.phone_number

    def _send_mail(self):
        context = {'object': self}
        plain_message = render_to_string('djtools.contact/contactrequest_email.txt', context)
        html_message = render_to_string('djtools.contact/contactrequest_email.html', context)

        send_mail(
            _("Petición de contacto desde {domain}").format(domain=settings.SITE_DOMAIN),
            plain_message,
            settings.CONTACT_REQUEST_MAIL_FROM,
            settings.CONTACT_REQUEST_MAIL_TO,
            fail_silently=False,
            html_message=html_message,
        )
