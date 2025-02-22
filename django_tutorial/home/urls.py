from django.urls import path
from .views import index, about, services, portfolio, contact_view, contact_success_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]