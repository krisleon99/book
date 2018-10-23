from django.forms import ModelForm
from django import forms
from book.booking.models import BookingStatus, Booking, BookingItem

class BookingItemForm(ModelForm):
    class Meta:
        model = BookingItem
        fields = "__all__"

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingStatusForm(ModelForm):
    class Meta:
        model = BookingStatus
        fields = "__all__"
