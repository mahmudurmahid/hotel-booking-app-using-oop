import pandas

df = pandas.read_csv('hotels.csv', dtype={"id":str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book_room(self):
        """ Books a room in the hotel by changing the availability status to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv('hotels.csv', index=False)

    def available_room(self):
        """ Check if the hotel has available rooms """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationConfirmation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate_confirmation(self):
        pass


print(df)
hotel_ID = input("Enter the hotel ID: ")
hotel = Hotel(hotel_ID)

if hotel.available_room:
    hotel.book_room()
    customer_name = input("Enter your name: ")
    reservation_ticket = ReservationConfirmation(customer_name, hotel_object)
    reservation_ticket.generate_confirmation()
else:
    print("No rooms available in this hotel.")
