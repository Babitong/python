# # Defining a class
# class Car:
#     color = "red"  # Attribute

#     # Method
#     def drive(self):
#         print("The car is driving 🚗")

# # Creating an object
# my_car = Car()
# print(my_car.color)
# my_car.drive()


# class Car:
#     def __init__(rex, color, model):
#         rex.color = color    # Instance variable
#         rex.model = model    # Instance variable

# # Creating objects with unique attributes
# car1 = Car("blue", "Sedan")
# car2 = Car("red", "SUV")

# print(car1.color)  # Output: blue
# print(car2.model)  # Output: SUV



# activity one

class smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

# Creating objects with unique attributes
phone1 = smartphone("Apple", "iPhone 14")
book1 = book("1984", "George Orwell")
superhero1 = superhero("Spider-Man", "Web-slinging")

print(phone1.brand)  # Output: Apple
print(book1.title)  # Output: 1984
print(superhero1.name)  # Output: Spider-Man


# activity two
class vehicles:
    def __init__(self, type, wheels):
        self.type = type
        self.wheels = wheels
    def move(self):
        print(f"The {self.type} moves on {self.wheels} wheels.")

class car(vehicles):
    pass

class plane(vehicles):
    pass


for vehicle in [car('Red Sedan', 4), plane('Blue Boeing 747', 2)]:
    vehicle.move()
    print(f"{vehicle.type} {vehicle.wheels}")