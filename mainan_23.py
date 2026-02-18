class Character:  #parent class
    alive = True

    def kind(self):
        print("This character is kindly warmly")

    def bad(self):
        print("This character has bad personality")

class Sora(Character):
    face = "beautiful"
    smart = 100
    happiness = 20
                                #children class
class Kaito(Character):
    face = "handsome"
    smart = 101
    happiness = 50

sora = Sora()
kaito = Kaito()

print(sora.face)
sora.kind()