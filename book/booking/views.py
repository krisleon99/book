"""Booking views."""

# Django
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Booking models
from book.booking.models import Booking, Room, BookingItem

# Booking forms
from book.booking.forms import BookingForm, BookingItemForm, BookingHabForm, BookingItemRoomForm


def list(request, template="list.html"):
    """Return a rooms list"""
    rooms = Room.objects.all()
    return render_to_response(template, RequestContext(request, {'items': rooms}))

def upload_booking(request, room_id):
    """saving a Book object from room"""
    if request.method == 'POST':
        date_from = request.POST.get('date_from', False)
        date_until = request.POST.get('date_until', False)
        quantity = request.POST.get('quantity', 1)
        persons = request.POST.get('persons', 1)
        notes = request.POST.get('notes', False)
        creation_date = request.POST.get('timestamp', False)
        book_form = BookingForm({'date_from': date_from, 'date_until':date_until, 'room':room_id, 'quantity':quantity,'persons':persons,'time_period':2, 'notes':notes, 'status':1,'creation_date':creation_date})
        if book_form.is_valid():
            book = book_form.save()
            return HttpResponseRedirect('../upload_booking_item/'+str(book.id))
    else:
        room = Room.objects.get(id=room_id)
        book_form = BookingHabForm()
    return render_to_response('book_form.html', {'form': book_form, 'room':room},
                              context_instance=RequestContext(request))

def upload_booking_item(request, book_id):
    """saving a BookingItem object from book"""
    book = Booking.objects.get(id=book_id)
    room = Room.objects.get(id=book.room.id)
    if request.method == 'POST':
        room.avaible = False
        room.save()
        name = request.POST.get('name', False)
        last_name = request.POST.get('last_name', False)
        email = request.POST.get('email', False)
        phone = request.POST.get('phone', False)
        total = room.type.price * book.quantity
        creation_date = request.POST.get('timestamp', False)
        book_item_form = BookingItemForm({'booking': book_id, 'name':name, 'last_name':last_name, 'email':email,'phone':phone,'total':total, 'status':1,'creation_date':creation_date})
        if book_item_form.is_valid():
            booking_item = book_item_form.save()
            return HttpResponseRedirect('../detail/'+str(booking_item.id))
    else:
        # get the price of room and we multiplication per quantity's book
        total = room.type.price * book.quantity
        book_item_form = BookingItemRoomForm()
    return render_to_response('booking_item_form.html', {'form': book_item_form, 'book':book, 'total':total},
                              context_instance=RequestContext(request))

def detail(request, booking_id, template="book_detail.html"):
    """show the detail of BookintItem object"""
    booking = BookingItem.objects.get(id=booking_id)
    return render_to_response(template, RequestContext(request, {'booking': booking}))
