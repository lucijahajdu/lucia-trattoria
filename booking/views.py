from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')


class PostDetail(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user=request.user.id)
        booking_form = BookingForm()

        return render(
            request,
            'bookings/booking_list.html',
            {
                'bookings': bookings,
                'booked': False,
                'booking_form': booking_form,
            },
        )

    def post(self, request, *args, **kwargs):
        bookings = Booking.objects.all()
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking_form.instance.user = request.user
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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'bookings/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(
                user=self.request.user
                )
        else:
            context['bookings'] = None
        return context


class EditBooking(generic.UpdateView):
    model = Booking
    template_name = 'bookings/edit-booking.html'
    form_class = BookingForm

    def form_valid(self, form):
        self.object = form.save()
        messages.success(
            self.request, 'Your change of table reservation was successful.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')


class DeleteBooking(generic.DeleteView):
    model = Booking
    template_name = 'bookings/delete-booking.html'
    success_url = reverse_lazy('profile')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your reservation is deleted.')
        return super().delete(request, *args, **kwargs)
