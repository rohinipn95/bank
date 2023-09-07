from django.db import models

account_choice=(
    ('saving','Saving'),
    ('current','Current')
)
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=125)
    address = models.TextField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(max_length=50, choices=account_choice)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.name