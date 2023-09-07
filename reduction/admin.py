from django.contrib import admin
from.models import Person
# Register your models here.
from reduction.models import Branch, District, Person

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Person)
