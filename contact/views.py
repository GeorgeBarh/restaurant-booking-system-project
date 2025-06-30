from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()  # Save the message to the database
        messages.success(self.request, "Thank you! Your message has been sent successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Oops! Please correct the errors below and try again.")
        return super().form_invalid(form)
