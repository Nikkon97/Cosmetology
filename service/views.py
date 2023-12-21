from django.views.generic import ListView, DetailView

from service.models import Service


class ServiceListView(ListView):
    model = Service


class ServiceDescriptionView(DetailView):
    model = Service
    template_name = 'service/service_description.html'
