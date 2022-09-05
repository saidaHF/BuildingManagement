class Resident:

    def __init__(self):
        self.name = ""
        self.lastName = ""
        self.lastName2 = ""
        self.age = 0
        self.day = 0
        self.month = 0
        self.year = 0
        self.bornDate = ""

    def insertResident(self):
        print("Insert resident's personal information:")
        self.introInformationInResident("name")
        self.introInformationInResident("lastName")
        self.introInformationInResident("lastName2")
        self.introInformationInResident("age")
        self.introInformationInResident("day")
        self.introInformationInResident("month")
        self.introInformationInResident("year")
        self.bornDate = "{} / {} / {}".format(self.day, self.month, self.year)

    def introInformationInResident(self, word):
        print(word)
        setattr(self, word, input())

    def showInfoResident(self):
        print(f" Resident: {self.name} , {self.lastName} , {self.lastName2} , {self.age} , {self.bornDate}")
