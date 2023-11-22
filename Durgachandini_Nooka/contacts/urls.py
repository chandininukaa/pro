from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),
    path('contact/<int:contact_id>/', views.detail_contact, name='detail_contact'),
    path('contact/new/', views.create_contact, name='create_contact'),
    path('contact/edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('contact/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
