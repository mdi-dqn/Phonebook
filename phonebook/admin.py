from django.contrib import admin
from .models import Contact, Phone

admin.site.register(Contact)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('contact', 'typePhone', 'number')
