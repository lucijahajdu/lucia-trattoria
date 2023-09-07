from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy

#def home(request):
#    return render(request, 'index.html')

class HomeView(View):

    def get(self,request):
        return render(request, 'index.html')

class PostDetail(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user=request.user.id)

        return render(
            request,
            'bookings/booking_list.html',
            {
                'bookings': bookings,
                'booked': False,
                'booking_form': BookingForm()
            },
        )

    def post(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking_form.instance.user = request.user.id
            booking = booking_form.save(commit=False)
            booking.save()
        else:
            booking_form = BookingForm()

        

        return render(
            request,
            'bookings/booking_list.html',
            {
                'bookings': bookings,
                'booked': True,
                'booking_form': BookingForm()
            },
        )

class EditBooking(generic.UpdateView):
    model = Booking
    template_name = 'bookings/edit-booking.html'
    success_url = '../{id}'
    form_class = BookingForm

    def get_success_url(self):
        return reverse_lazy('home', args=[str(self.object.id)])