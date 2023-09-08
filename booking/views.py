from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#def home(request):
#    return render(request, 'index.html')

class HomeView(View):

    def get(self,request):
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
            context['bookings'] = Booking.objects.filter(user=self.request.user)
        else:
            context['bookings'] = None  # Handle the case where the user is not authenticated
        return context

#lass ProfileView(TemplateView):
  #  template_name = 'bookings/profile.html'

   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   context['bookings'] = Booking.objects.filter(user=self.request.user)
      #  return context

#class ProfileView(View):
 #   template_name = 'bookings/profile.html'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['bookings'] = Booking.objects.filter(user=self.request.user)
        #return context
    #def get(self, request, *args, **kwargs):
     #   if request.user.is_authenticated:
            # Retrieve bookings for the logged-in user
      #      bookings = Booking.objects.filter(user=request.user)
       #     return render(
        #        request,
         #       self.template_name,
          #      {
           #         'bookings': bookings,
            #    },
            #)
        #else:
         #   return render(
          #      request,
           #     self.template_name,
            #    {
             #       'bookings': None,
              #  },
            #)
            
            # Handle the case where the user is not authenticated (e.g., redirect to login)
            # You can customize this part based on your requirements
       # bookings = Booking.objects.filter(user=request.user)
       #return render(
        #    request,
         #   self.template_name,
          #  {
           #     'bookings': bookings,
            #},
        #)
        #return render(request, self.template_name, context)
    #def post(self, request, *args, **kwargs):
        # Your POST request handling logic here
        # For example, handle form submissions to update the profile
     #   return render(request, self.template_name, context)


class EditBooking(generic.UpdateView):
    model = Booking
    template_name = 'bookings/edit-booking.html'
    success_url = '../{id}'
    form_class = BookingForm

    def get_success_url(self):
        return reverse_lazy('home', args=[str(self.object.id)])

class DeleteBooking(generic.DeleteView):
    model = Booking
    template_name = 'bookings/delete-booking.html'
    success_url = reverse_lazy('profile')  # Redirect to the list view after deletion