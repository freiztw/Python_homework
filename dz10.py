# class Auto:
#     def __init__(self, brand, age, mark, color=None, weight=None):
#             self.brand = brand
#             self.age = age
#             self.mark = mark
#             self.color = color
#             self.weight = weight
#     def move(self):
#         print('move')
#     def stop(self):
#         print('stop')
#     def birthday(self):
#         self.age += 1
#
# auto = Auto('Honda', 20, 'Legend', 'black', 1850)
# print(auto.age)
# auto.birthday()
# print(auto.age)
# auto.move()
# auto.stop()
# print(auto.brand)


import time




class Auto:
    def __init__(self, brand, age):
            self.brand = brand
            self.age = age


    def move(self):
        print('move')



class Truck(Auto):
    def __init__(self, brand, age, max_load):
        super().__init__(brand, age)
        self.max_load = max_load
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)
    def move(self):
        print('attention')
        super().move()
        # super().__init__(brand, age, mark, color=None, weight=None)


class Car(Auto):
    def __init__(self, brand, age, max_speed):
        super().__init__(brand, age)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("Move!")
        print(f"Max speed is {self.max_speed}")


car1 = Car("Toyota", 3, 120)
car2 = Car("Honda", 2, 130)
print(car1.brand)
print(car1.age)
print(car1.max_speed)
car1.move()
print(car2.brand)
print(car2.age)
print(car2.max_speed)
car2.move()

# truck1 = Truck("Ford", 5, 5000)
# truck2 = Truck("Kia", 3, 7000)
# print(truck1.brand)
# print(truck1.age)
# print(truck1.max_load)
#
# truck1.move()
# truck1.load()
# print(truck2.brand)
# print(truck2.age)
# print(car2.max_speed)
# truck2.move()
# truck2.load()


# class Car(Auto):
#     pass