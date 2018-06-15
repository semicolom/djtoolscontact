from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from .forms import ContactRequestForm
from .models import ContactRequest, ContactInformation


class ContactRequestView(CreateView):
    model = ContactRequest
    form_class = ContactRequestForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        """
        Displays a success message when the form is submitted correctly
        """

        messages.success(self.request, _("Su petición ha sido enviada correctamente"))
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Displays an error message when the form is submitted with errors
        """

        messages.error(self.request, _("Revise los errores del formulario"))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        """
        Adds extra information to the context data to be used in the template
        """

        context = super().get_context_data(**kwargs)

        context.update({
            'contact_information': ContactInformation.objects.get()
        })

        return context
