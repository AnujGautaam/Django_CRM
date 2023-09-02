from django.contrib import admin
from .models import Record, Record1

# Register your models here.
admin.site.register(Record) 
# one thing to note is that the record schema will always be treated as records in the admin panel and that is how it works 
# the reason this is not working is because there needs to be migration for this to work 
admin.site.register(Record1) 
