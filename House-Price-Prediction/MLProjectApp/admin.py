from django.contrib import admin
from MLProjectApp.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'type_choice', 'desc', 'date']
    list_filter = ['type_choice']
admin.site.register(Contact, ContactAdmin)