from django.urls import path
from . import views

app_name = 'phonebook'

urlpatterns = [
    path('contact/add/', views.addContact, name='addContact'),
    path('contact/edit/<int:id>', views.editContact, name='editContact'),
    path('contact/delete/<int:id>', views.deleteContact, name='deleteContact'),
    path('contact/details/<int:id>', views.detailsContact, name='detailsContact'),
    path('phone/index/<int:id_c>', views.indexPhone, name = 'indexPhone'),
    path('phone/add/<int:id_c>', views.addPhone, name = 'addPhone'),
    path('phone/delete/<int:id_p>', views.deletePhone, name = 'deletePhone'),
    path('phone/edit/<int:id_p>', views.editPhone, name = 'editPhone'),
]