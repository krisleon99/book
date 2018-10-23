# book

Intalling dependences:

Django==1.6


This API solves the problem that hotels have regularly to reserve a room.

The project is called book, inside it has a module called booking, where are the models that allow the functioning of the API;

# Catalogs
TypeRoom: contains the catalog of the types of rooms and the corresponding price.
Rooms: contiene una relacion uno a uno con TypeRoom, un identificador único (slug) y un estatus., In this model contains the room's stock (is the product of the hotel).

# Book
Booking: is the main table, where we will save the user and their metadata and the date form and date until.
BookingItem: It is the second step of the business flow, once saved the data generated from the user, we can save the many rooms, the people and all this as it will cost the user.
BookingStatus: This model has the relationship with BookingItem and Room, since from there we will calculate the price of the room according to how many rooms it requested and according to the type of room that the user requested and it will be saved in the table Rooms a history where is marked as occupied the room, so that another user can not ask for the same room. The last status of the room,  If the set aside is False it's menas that the room is unavailable
