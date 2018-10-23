"""Models for the booking module."""
# Django
from django.conf import settings
from django.db import models

class TypeRoom(models.Model):
    """
     Display an individual :model:`book.booking.TypeRoom`.

    **Context**

    ``TypeRoom``
        An instance of :model:`book.booking.TypeRoom`.
    
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
    :slug: A unique slug identifier of room.
    :type: A ForeignKey of TypeRoom.
    :avaible: spend of the room, if spend is True, the room is avaibleself.
    """
    slug = models.SlugField(verbose_name = "Slug")
    type = models.ForeignKey(TypeRoom, verbose_name = "Type room", related_name='type_room_fk',blank=True, null=True)
    avaible = models.BooleanField(default= True, verbose_name = "Avaible", blank=True)

    def __unicode__(self):
        return self.slug+"-"+self.type.type


class Booking(models.Model):
    """
    Model to contain information about a booking.
    :date_from (optional): From when the booking is active.
    :date_until (optional): Until when the booking is active.
    :quantity: Quantity of rooms items.
    :persons (optional): Quantity of persons, who are involved in this booking.
    :time_period (autogenerate): How long the period from date_from will be.
      e.g.: 10 (days).
    :notes (optional): Staff notes.
    :creation_date: Date of the booking.
    :status: Current status of the booking.
    """
    date_from = models.DateField(verbose_name='From', blank=True, null=True)
    date_until = models.DateField(verbose_name='Until', blank=True, null=True)
    room = models.ForeignKey(Room, related_name='room_fk', verbose_name = "Room", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    persons = models.PositiveIntegerField(default=1,verbose_name='Persons',blank=True, null=True)
    time_period = models.IntegerField(verbose_name = "Time period", null=True, blank=True)
    notes = models.TextField(verbose_name='Notes',max_length=1024,blank=True, null=True)
    status = models.BooleanField(verbose_name = "Activa", default=1)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.room.slug) or u''

class BookingItem(models.Model):
    """
    Model to connect a booking with a related object.
    :booking: Connection to related booking.
    :name (optional): name of user.
    :last_name (optional): last name of user.
    :email: Email of the user.
    :phone (optional): Phone number of the user.
    :total (autogenerate): quantity * price of TypeRoom.
    :status: Current status of the booking.
    :creation_date: Date of the booking.
    """
    booking = models.ForeignKey(Booking, related_name='book_fk', verbose_name = "Book", null=True, blank=True)
    name = models.CharField(verbose_name = "Name", max_length=250, blank=True, null=True)
    last_name = models.CharField(verbose_name = "Last name",max_length=250, blank=True, null=True)
    email = models.EmailField(verbose_name = "Email", max_length=70,blank=True)
    phone = models.CharField(verbose_name = "Phone", max_length=256, blank=True)
    total = models.DecimalField(max_digits=36, decimal_places=2,verbose_name = "Total", null=True, blank=True)
    status = models.BooleanField(verbose_name = "Activa", default=1)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
		return unicode(self.name+""+self.last_name) or u''
