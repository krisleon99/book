"""Forms for the booking module."""
# Django
from django.forms import ModelForm
from django import forms
# book
from book.booking.models import Booking, BookingItem

class BookingItemForm(ModelForm):
    class Meta:
        model = BookingItem
        fields = "__all__"

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        widgets = {
            'date_from': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = "__all__"

class BookingHabForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['room','time_period','status']

class BookingItemRoomForm(ModelForm):
    class Meta:
        model = BookingItem
        exclude = ['booking','total', 'status']
