from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm

# Handles contact form submissions with success/error messaging
class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        # Save valid form to DB and show success message
        form.save()
        messages.success(self.request, "Thank you! Your message has been sent successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Show error message if form validation fails
        messages.error(self.request, "Oops! Please correct the errors below and try again.")
        return super().form_invalid(form)

