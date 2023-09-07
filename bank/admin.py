from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from bank.models import City, Country, Member

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Member)