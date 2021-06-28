from Animal import Animal


class Mammal(Animal):
    def __init__(self):
        self.weight = 7
        super().__init__()

    def walk(self):
        print("walk")


mammal = Mammal()
print(mammal.eat())

print(mammal.weight)
print(isinstance(mammal, Mammal))
