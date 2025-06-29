from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/contact/?success=true"

    def form_valid(self, form):
        # In production, send email or log message
        return super().form_valid(form)
