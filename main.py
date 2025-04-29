import pandas

df = pandas.read_csv('hotels.csv')

class Hotel:
    def __init__(self, id):
        pass

    def book_room(self):
        pass

    def available_room(self):
        pass


class ReservationConfirmation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate_confirmation(self):
        pass


print(df)
id = input("Enter the hotel ID: ")
hotel = Hotel(id)

if hotel.available_room:
    hotel.book_room()
    customer_name = input("Enter your name: ")
    reservation_ticket = ReservationConfirmation(customer_name, hotel_object)
    reservation_ticket.generate_confirmation()
else:
    print("No rooms available in this hotel.")
