from .models import Booking
from django import  forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guests', 'date', 'time', 'first_name', 'last_name', 'email', 'requirements')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    time_choices = [
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '09:00 PM'),
        ('20:00', '08:00 PM'),
        ('21:00', '09:00 PM'),
    ]

    time = forms.ChoiceField(
        choices=time_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )






