from django import forms
from .models import bookings

class DateInput(forms.DateInput):
    input_type = 'date'

class bookingsForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'
        
        widgets ={
            'date':DateInput()
        }
        labels ={
            'from_s':'FROM',
            'to_s':'TO',
            'bus_name':'BUS'
        }