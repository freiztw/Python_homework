# class Auto:
#     def __init__(self, brand, age, mark, color=None, weight=None):
#             self.brand = brand
#             self.age = age
#             self.color = color
#             self.mark = mark
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
# auto.move()
# auto.stop()
# print(auto.brand)


import time




class Auto:
    def move(self):
        print('attention')

class Truck(Auto):
    def __init__(self, max_load, load):
        self.max_load = max_load
        self.load = load
    def move(self):
        super().move()

class Car(Auto):
    def move(self, max_speed):
        self.max_speed = max_speed

# print("attention")
# print("move")
time.sleep(1)
print("load")
time.sleep(1)



class Car(Auto):
    pass