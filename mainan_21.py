#OOP Python (class)

class Enemy:
    def __init__(self, type, damage):
        self.type = type
        self.damage = damage

    def hitting(self):
        print(f"u get hit by {self.type}!")

    def get_hit(self):
        print("HP decrease... Enemy is dead!")

dracula = Enemy("Dracula", 500)

print(dracula.damage)
dracula.hitting()