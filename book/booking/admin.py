# Django
from django.contrib import admin
# book
from book.booking.models import TypeRoom, Room, Booking, BookingItem

admin.site.register(TypeRoom)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(BookingItem)
