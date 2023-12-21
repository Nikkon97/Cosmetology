from django.urls import path

from service.apps import ServiceConfig
from service.views import ServiceListView, ServiceDescriptionView

app_name = ServiceConfig.name

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDescriptionView.as_view(), name='service_view'),
]
