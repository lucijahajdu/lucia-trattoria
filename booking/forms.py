from .models import Booking
from django import  forms


class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = ('guests', 'date', 'time', 'first_name', 'last_name', 'email', 'requirements')