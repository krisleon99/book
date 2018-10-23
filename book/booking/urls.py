"""Booking URLs module."""
from django.conf.urls import url, patterns

from book.booking import views

urlpatterns = patterns('book.booking.views',
                       # main view's method show the Rooms and Typeroom relation, for rooms avaibles or unavaible
                       url(r'^list/$', 'list', name='list'),
                       # method for adding a Book object of model.
                       url(r'^upload_booking/(?P<room_id>\d+)$', 'upload_booking', name='upload_booking'),
                       # method for adding a BookingItem object of model.
                       url(r'^upload_booking_item/(?P<book_id>\d+)$', 'upload_booking_item', name='upload_booking_item'),
                       # method for detail a Booking saved by user.
                       url(r'^detail/(?P<booking_id>\d+)$', 'detail', name='detail'),
                       )
