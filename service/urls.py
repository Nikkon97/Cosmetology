from django.urls import path

from service.apps import ServiceConfig
from service.views import ServiceListView

app_name = ServiceConfig.name

urlpatterns = [
    path('', ServiceListView.as_view(), name='services_list')
]
