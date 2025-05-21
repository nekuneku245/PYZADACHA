# class Airplane:
#     def __init__(self, brand, model, year, power, hours):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.__power = power
#         self.__hours = hours
#     def print(self):
#         print(f"Марка самолета = {self.brand}, Год выпуска самолета = {self.year} год, Мощность самолета = {self.__power} Лс, Самолет налетал = {self.__hours} часов.")

# airplane1 = Airplane("Boeing", "Boeing-737", 1916, 25000, 12000)
# airplane2 = Airplane("Boeing", "Boeing-777", 1922, 18000, 3002)
# airplane3 = Airplane("British Aerospace", "Aerospace-212", 1822, 15300, 8900)
# airplane4 = Airplane("Cirrus", "Cirrus-4", 202, 10340, 1200)
# airplane1.print()
# airplane2.print()
# airplane3.print()
# airplane4.print()


# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name
    
#     def display_info(self):
#         print(f"Имя {self.__name}")
              
# class Child(Person):
#      def

class Father:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes

    def print(self):
        print(f"Фамилия = {self.surname} iq = {self.iq} цвет глаз = {self.colorEyes}")

class Mother:
    def __init__(self, surname, iqmama, colorEyes):
        self.surname = surname
        self.iqmama = iqmama
        self.colorEyes = colorEyes

    def print(self):
        print(f"Фамилия = {self.surname} iq = {self.iqmama} цвет глаз = {self.colorEyes}")
    def printiqmama(self):
        print(f"{self.printiqmama}")

class Child(Father, Mother):
    def __init__(self, surname, iq, iqmama, colorEyes, colorHair):
        super().__init__(surname, iq, iqmama, colorEyes)
        self.colorHair = colorHair

mama = Mother('Фамилия Папа', 120, 'blue')
pahan = Father('Фамилия Папы', 100, 'black')
arnold = Child('Фамилия родителей', 150, 'BlueBlack', 'цвет волос папы')
arnold.print()
