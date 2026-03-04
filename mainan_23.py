class Character:  #parent class
    alive = True

    def kind(self):
        print("This character is kindly warmly")

    def bad(self):
        print("This character has bad personality")

class Gender:
    def __init__(self, gender):
        self.gender = gender

        match self.gender:
            case "cowo" :
                self.looks = "handsome"
            case "cewe" :
                self.looks = "pretty"

class Sora(Gender, Character):
    smart = 100
    happiness = 20                           #children class
class Kaito(Gender, Character):
    smart = 101
    happiness = 50

sora = Sora("cewe")
kaito = Kaito("cowo")

print(kaito.looks)