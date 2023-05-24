from django.contrib import admin

from Home.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Sale)