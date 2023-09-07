from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberCreationForm
from .models import Member, City


def create_view(request):
    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')


    return render(request, 'bankreg.html', {'form': form})




# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})