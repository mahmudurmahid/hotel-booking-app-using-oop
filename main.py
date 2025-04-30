import pandas

df = pandas.read_csv('hotels.csv', dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


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
        content = f"""
        Thank you for your reservation.
        Here is your reservation information:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.hotel_name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiry_date, holder, cvc):
        card_data = {"number": self.number, "expiration": expiry_date, "holder": holder, "cvc": cvc}

        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"]. squeeze()

        if password == given_password:
            return True
        else:
            return False


class Spa(Hotel):
    def book_spa_package(self):
        pass


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate_confirmation(self):
        content = f""" 
        Thank you for booking a spa package.
        Here is your reservation information:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.hotel_name}
        """
        return content


print(df)
hotel_ID = input("Enter the hotel ID: ")
hotel = Spa(hotel_ID)

if hotel.available_room():
    # Validate the credit card details  
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiry_date="12/26", holder="JOHN SMITH", cvc="123"):
        # Authenticate the credit card using the password
        if credit_card.authenticate(given_password="mypass"):
            hotel.book_room()
            name = input("Enter your name: ")
            reservation_ticket = ReservationConfirmation(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate_confirmation())
            # Ask if the user wants to book a spa package
            spa_reservation = input("Do you want to book a spa package? ")
            if spa_reservation == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate_confirmation())
            else:
                print("No spa package booked.")
        else:
            print("Authentication failed. Invalid password.")
    else:
        print("Invalid credit card details.")
else:
    print("No rooms available in this hotel.")
