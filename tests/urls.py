"""
URLConf for test suite.
"""
from django.urls import path
from djtools.contact import views


urlpatterns = [
    path('contacto', views.ContactRequestView.as_view(), name='contact'),
]
