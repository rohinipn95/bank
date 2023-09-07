
from django.db import models

# Create your models here.

from django.db import models
from django.forms.widgets import RadioSelect
from django import forms

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    country = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    ACCOUNT_CHOICES = (
        ('sa', 'Saving Account'),
        ('ca', 'Current Account'),

    )

    name = models.CharField(max_length=124)
    dob=models.DateField()
    age=models.IntegerField()
    TYPE_SELECT = (('0', 'Female'), ('1', 'Male'),('2','Other'))
    gender = models.CharField(max_length=11, choices=TYPE_SELECT)
    phone=models.CharField(max_length=254)
    mail=models.EmailField(blank=True)
    address=models.CharField(max_length=254)
    district= models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(max_length=6, choices=ACCOUNT_CHOICES)
    debit_card=models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    cheque_book= models.BooleanField(default=False)


    def __str__(self):
        return self.name