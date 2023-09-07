from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm

#def home(request):
#    return render(request, 'index.html')

class HomeView(View):

    def get(self,request):
        return render(request, 'index.html')

class PostDetail(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.all()

        return render(
            request,
            'booking/booking_list.html',
            {
                'bookings': bookings,
                'booking_form': BookingForm()
            },
        )