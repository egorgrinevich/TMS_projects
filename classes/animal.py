class Animal:

    def __init__(self, name: str, family: str):
        self.name = name
        self.family = family
        self.sound = self.calculate_sound()


    def calculate_sound(self) -> str:
        if self.family == "Caninae":
            return "Woof"
        if self.family == "Feline":
            return "Мeow"
        if self.family == "Perissodactyla":
            return "Neigh"

class Horse(Animal):

    def __init__(self, name: str, family: str, functionality: str):
        super().__init__(name, family)
        self.name = name
        self.family = family
        self.functionality = functionality

class Dog(Animal):

    def __init__(self, name: str, family: str, titul: str):
        super().__init__(name, family)
        self.name = name
        self.family = family
        self.titul = titul

class Cat(Animal):

    def __init__(self, name: str, family: str, food: str):
        super().__init__(name, family)
        self.name = name
        self.family = family
        self.food = food

