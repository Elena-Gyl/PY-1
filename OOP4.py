"""Множественное наследование, статические атрибуты"""
from OOP3 import Person

#Базовый класс
#Ромбовидное наследование
class MixinPlay:
    @staticmethod
    def play(chanel=1):
        match chanel:
            case 1: print('Звучит "Beatles"')
            case 2: print('Звучит "ABBA"')
            case 3: print('Звучит "Leps"')
            case 4: print('Звучит "Новостной канал"')
            case 5: print('Звучит "Концерт Игоря Крутого"')



class Car(MixinPlay):
    #статическое поле
    name = 'Автомобиль'
    def ride(self):
        print(f'Как {Car.name} едет по дороге')

    # #Статический метод
    # @staticmethod
    # def play():
    #     print('Звучит "Beatles"')


class Boat(MixinPlay):
    def swim(self):
        print('Ходит по воде')

    # @staticmethod
    # def play():
    #     print('Звучит "ABBA"')


class Amphibian(Car, Boat):
    def display(self):
        print('Амфибия: ')


car = Car()
boat = Boat()
car.ride()
boat.swim()
am = Amphibian()
am.display()
am.ride()
am.swim()
# print(isinstance(am, Car))
# print(isinstance(am, Boat))
# print(isinstance(am, Amphibian))
am.play(3)

class A:
    # def display(self):
    #      print('A')
    pass
#
#
class B(A):
#     # def display(self):
#     #     print('B')
     pass
#
#
class C(A):
#     # def display(self):
#     #     print('C')
     pass


class D(B, C, Person):
    def __init__(self, name='Marpha', age=19):
        Person.__init__(self, name, age)
    # def display(self):
    #     print('D')
    pass


print(D.mro())
obj = D()
obj.display()
print(obj)


class Name:
    def __init__(self, name):
        self.name = name


class Age:
    def __init__(self, age):
        self.age = age


class Human(Name, Age):
    def __init__(self, name, age):
        super().__init__(name)
        Age.__init__(self, age)

    #для print
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    #для сбора в коллекции
    def __repr__(self):
        return f'{self.name} - {self.age}'


h = Human('Harry', 19)
h1 = Human('John', 23)
print(h)
humans = [h, h1]
print(humans)





