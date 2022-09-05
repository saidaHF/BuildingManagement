from src.Apartment import Apartment

apartment = Apartment()


def program():
    try:
        while True:
            user_selection = int(input("What do you choose?\n1 Insert Apartment, 2 Show Information "
                                       "Resident or 0 for Exit\n"))

            if user_selection == 1:
                apartment.insertApartment()
                pass
            if user_selection == 2:
                apartment.showInfoApartment()
                pass
            if user_selection == 0:
                break

    except ValueError:
        print("Please enter only numbers!")


if __name__ == '__main__':
    program()
