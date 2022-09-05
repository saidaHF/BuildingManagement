from src.Resident import Resident

resident = Resident()


class Apartment:

    def __init__(self):
        self.residents = []
        self.floor = 0
        self.door = 0
        self.type = ""

    def insertApartment(self):
        # si no hay ninguno pide introducir al menos un residente:
        # si ya hay alguno, pregunta si quiere meter más:
        if len(self.residents) == 0:
            resident.insertResident()
            self.residents.append(resident)
        self.askMoreResidents()
        self.introInformationInApartment("floor")
        self.introInformationInApartment("door")
        self.introInformationInApartment("type")

    def introInformationInApartment(self, word):
        print(word)
        setattr(self, word, input())

    def askMoreResidents(self):

        try:
            while True:
                user_selection = int(
                    input("If do you want introduce an other resident press 1 for continue or 0 for continue:"))
                if user_selection == 1:
                    resident.insertResident()
                    self.residents.append(resident)
                if user_selection == 0:
                    break
        except ValueError:
            print("Please enter only numbers!")


    def showInfoApartment(self):
        for resident in self.residents:
            resident.showInfoResident()
        print(f"floor: {self.floor} , door: {self.door} , type: {self.type}")