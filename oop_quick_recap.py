
# 1. Basic Class and Object

class PersonBasic:
    pass

def demo_basic_class():
    p = PersonBasic()
    print("Basic Class Example:", type(p))



# 2. Class Attributes

class PersonWithAttributes:
    name = "Memo"
    age = 22

def demo_class_attributes():
    p = PersonWithAttributes()
    print("Class Attributes:", p.name, p.age)


# 3. Constructor (__init__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def demo_constructor():
    p = Person("Memo", 22)
    print("Constructor:", p.name, p.age)


# 4. Methods

class PersonWithMethod:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello my name is", self.name)

def demo_methods():
    p = PersonWithMethod("Memo")
    p.greet()


# 5. Class vs Instance Attributes

class PersonCountry:
    country = "Egypt"

    def __init__(self, name):
        self.name = name

def demo_class_vs_instance():
    p1 = PersonCountry("Memo")
    p2 = PersonCountry("soly")
    print("Country for p1:", p1.country)
    print("Country for p2:", p2.country)



# 6. Encapsulation (Private Variable)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

def demo_encapsulation():
    acc = BankAccount(1000)
    acc.deposit(500)
    acc.show_balance()



# 7. Inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

def demo_inheritance():
    d = Dog()
    d.speak()
    d.bark()


# 8. Method Overriding

class AnimalOverride:
    def speak(self):
        print("Animal sound")

class DogOverride(AnimalOverride):
    def speak(self):
        print("Bark")

def demo_overriding():
    d = DogOverride()
    d.speak()



# 9. Polymorphism

class Cat:
    def sound(self):
        print("Meow")

class DogPoly:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

def demo_polymorphism():
    c = Cat()
    d = DogPoly()
    make_sound(c)
    make_sound(d)


# 10. Simple Project Example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print("Car:", self.brand, self.model)

def demo_car():
    car = Car("Toyota", "Corolla")
    car.info()


# Run All Demos

if __name__ == "__main__":
    print("\n--- OOP Python Tutorial Demo ---\n")

    demo_basic_class()
    demo_class_attributes()
    demo_constructor()
    demo_methods()
    demo_class_vs_instance()
    demo_encapsulation()
    demo_inheritance()
    demo_overriding()
    demo_polymorphism()
    demo_car()

    print("\n--- End of Demo ---")
