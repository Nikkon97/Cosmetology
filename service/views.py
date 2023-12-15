from django.shortcuts import render
from django.views.generic import ListView

from service.models import Service


def index(request):
    context = {
        'object_list': Service.objects.all(),
        'title': 'Мои услуги'
    }
    return render(request, 'service/index.html', context)


class ServiceListView(ListView):
    model = Service
