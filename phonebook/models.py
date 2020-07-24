from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    REAL = 'Real'
    LEGAL = 'Legal'
    TYPE_CHOICES = [
        (REAL, 'Real'),
        (LEGAL, 'Legal'),
    ]
    typeContact = models.CharField(choices=TYPE_CHOICES, max_length=5, default='Real')
    fullName = models.CharField(max_length=40)
    image = models.ImageField(upload_to='contact/image', max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.fullName}'



class Phone(models.Model):
    INTERNET = 'Internet'
    FIXED = 'Fixed'
    FAX = 'Fax'
    MCI = 'Mci'
    IRANCELL = 'Irancell'
    RIGHTEL = 'Rightel'

    TYPE_CHOICES = [
        (INTERNET, 'Internet'),
        (FIXED, 'Fixed'),
        (FAX, 'Fax'),
        (MCI, 'Mci'),
        (IRANCELL, 'Irancell'),
        (RIGHTEL, 'Rightel'),
    ]
    typePhone = models.CharField(choices=TYPE_CHOICES, max_length=8, default='Mci')
    number = models.CharField(max_length=11)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)

    def __str__(self):
        return self.number
