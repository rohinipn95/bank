from  django import forms

from bank.models import Member,City
Gender_choice=[
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
]
Material_choice=[
    ('debit_card','Debit Card'),
    ('credit_card','Credit Card'),
    ('cheque_book','Cheque Book',)
]




class MemberCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender_choice, widget=forms.RadioSelect)
    material = forms.MultipleChoiceField(choices=Material_choice, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Member

        fields = ['name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'country', 'city', 'account',
                  'material']
        labels = {'dob': 'Date of Birth', 'phone': 'Phone Number','country':'District', 'city':'Branch','account': 'Account Type',
                  'material': 'Material Provide'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'dob': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
                   'age': forms.NumberInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'country': forms.Select(attrs={'class': 'form-select'}),
                   'city': forms.Select(attrs={'class': 'form-select'}),
                   'account': forms.Select(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

class MyForm(forms.Form):
    message = forms.CharField(max_length=200)
