"""Models for the booking module."""
from django.conf import settings
from django.db import models

class TypeRoom(models.Model):
    """
    Containing the category of Rooms types.
    :price: A cost of room by type.
    :type: type of room
    :status: status of the room
    """
    price = models.DecimalField(max_digits=36,decimal_places=2,verbose_name = "Price", null=True, blank=True)
    type = models.CharField(verbose_name = "Type", max_length=256, blank=True)
    status = models.BooleanField(verbose_name = "Activa", blank=True)

    def __unicode__(self):
        return self.type

class Room(models.Model):
    """
    Containing the catalog of Rooms.
    :slug: A unique slug identifier.
    :type: A ForeignKey of TypeRoom.
    :status: status of the room
    """
    price = models.DecimalField(max_digits=36,decimal_places=2,verbose_name = "Price", null=True, blank=True)
    type = models.CharField(verbose_name = "Type", max_length=256, blank=True)
    status = models.BooleanField(verbose_name = "Activa", blank=True)

    def __unicode__(self):
        return self.type

class Booking(models.Model):
    """
    Model to contain information about a booking.
    :user (optional): Connection to Django's User model.
    :phone (optional): Phone number of the user.
    :email: Email of the user.
    :date_from (optional): From when the booking is active.
    :date_until (optional): Until when the booking is active.
    :time_period (autogenerate): How long the period from date_from will be.
      e.g.: 10 (days).
    :creation_date: Date of the booking.
    :status: Current status of the booking.
    :notes (optional): Staff notes.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = "User", related_name='user_booking',blank=True, null=True)
    email = models.BooleanField(verbose_name = "Email", blank=True)
    phone = models.CharField(verbose_name = "Phone", max_length=256, blank=True)
    date_from = models.DateTimeField(default=1, verbose_name='From', blank=True, null=True)
    date_until = models.DateTimeField(default=1, verbose_name='Until', blank=True, null=True)
    notes = models.TextField(verbose_name='Notes',max_length=1024,blank=True, null=True)
    time_period = models.DecimalField(max_digits=10,decimal_places=2, verbose_name = "Time period", null=True, blank=True)
    status = models.BooleanField(verbose_name = "Activa", default=1)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.name

class BookingItem(models.Model):
    """
    Model to connect a booking with a related object.
    :quantity: Quantity of rooms items.
    :persons (optional): Quantity of persons, who are involved in this booking.
    :total (autogenerate): quantity * price of TypeRoom.
    :booking: Connection to related booking.
    :creation_date: Date of the booking.
    :status: Current status of the booking.
    """
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    booking = models.ForeignKey(Booking, related_name='book_fk', verbose_name = "Book", null=True, blank=True)
    persons = models.PositiveIntegerField(verbose_name='Persons',blank=True, null=True)
    total = models.DecimalField(max_digits=36, decimal_places=2,verbose_name = "Subtotal", null=True, blank=True)
    status = models.BooleanField(verbose_name = "Activa", default=1)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
		return unicode(self.quantity) or u''

class BookingStatus(models.Model):
    """
    Containing all booking status.
    :room: A ForeignKey of Room.
    :booking_item: A ForeignKey of BookingItem
    :status: status of the roomself.
    :creation_date: Date of the booking.
    """
    slug = models.SlugField(verbose_name = "Slug")
    room = models.ForeignKey(Room, related_name='room_fk', verbose_name = "Room", null=True, blank=True)
    booking_item = models.ForeignKey(BookingItem, related_name='booking_item_fk', verbose_name = "BookingItem", null=True, blank=True)
    status = models.BooleanField(verbose_name = "Activa", blank=True)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.slug
