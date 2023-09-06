from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})

def home(request):
    return render(request, 'index.html')