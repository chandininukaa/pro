from django.urls import include, path
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/contacts/')),
    path('contacts/', include('contacts.urls')),
    # Other URL patterns for your project
]

