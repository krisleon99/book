"""Booking views."""

# Django
from django.shortcuts import render_to_response
from django.template import RequestContext

# Booking models
from book.booking.models import Booking

# Booking forms
from book.booking.forms import BookingForm


def list(request, template="list.html"):
    """Return a booking list"""
    booking = Booking.objects.all()
    return render_to_response(template, RequestContext(request, {'booking': booking}))

def upload_booking(request):
    if request.method == 'POST':
        book_form = BookingForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse("list"))
    else:
        book_form = BookingForm()
    return render_to_response('book_form.html', {'form': book_form},
                              context_instance=RequestContext(request))
