from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext as _

from .models import ContactRequest, ContactInformation


def _send_mail(contact_request):
    """
    Given a contact request instance sends an email to the web admin with the
    notification about its creation.
    Retruns the amount of sent emails.
    """

    message = render_to_string(
        'contactrequest_email.html',
        {'object': contact_request}
    )

    return send_mail(
        _("Petición de contacto desde {}").format(settings.DJTOOLS_CONTACT_SITE_DOMAIN),
        message,
        settings.DJTOOLS_CONTACT_MAIL_FROM,
        settings.DJTOOLS_CONTACT_MAIL_TO,
        fail_silently=False,
    )


def create_contact_request(name, email, phone_number, message):
    """
    Creates a new instance of ContactRequest and sends a notification email.
    """

    contact_request = ContactRequest.objects.create(
        name=name,
        email=email,
        phone_number=phone_number,
        message=message
    )
    amount_sent_emails = _send_mail(contact_request)
    return contact_request, amount_sent_emails


def get_contact_information():
    """
    Returns the only one Contact Information instance.
    """

    return ContactInformation.objects.get()
