from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event_Services)
admin.site.register(Service_Category)
admin.site.register(booking)
class PersonDetailAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateTimeField: {'input_formats': ('%m/%d/%Y',)},
    }
