from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .import forms
from .models import Hotel
from .forms import HotelForm
# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = HotelForm()
    return render(request, 'picture/hotel_image_form.html', {'form' : form})



def success(request):
    return HttpResponse('successfuly uploaded')

def index(request):
    return HttpResponse('hey yo!')
