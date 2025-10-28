# animals.py

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def info(self) -> str:
        return f"Animal(name={self.name})"


class Dog(Animal):
    def __init__(self, name: str, breed: str = "Jindo"):
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"

    def info(self) -> str:
        return f"{super().info()}, Dog(breed={self.breed})"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"