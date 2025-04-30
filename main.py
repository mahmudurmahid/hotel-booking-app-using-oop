import pandas

df = pandas.read_csv('hotels.csv', dtype={"id":str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_confirmation(self):
        content = f"""Thank you for your reservation.
        Here is your reservation information:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.hotel_name}
        """
        return content


print(df)
hotel_ID = input("Enter the hotel ID: ")
hotel = Hotel(hotel_ID)

if hotel.available_room:
    hotel.book_room()
    name = input("Enter your name: ")
    reservation_ticket = ReservationConfirmation(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate_confirmation())
else:
    print("No rooms available in this hotel.")
