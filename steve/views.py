from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import ContactForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about-us.html"

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)