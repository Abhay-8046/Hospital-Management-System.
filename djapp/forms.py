from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput()
        }

        labels = {
            'p_name': "Patient Name: ",
            'p_phone': "Patient Contact: ",
            'p_email': "Patient E-mail: ",
            'doc_name': "Doctor Name: ",
            'booking_date': "Booking Date: ",

        }