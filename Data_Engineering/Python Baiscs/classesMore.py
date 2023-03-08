

class country():

    def __init__(self, continent, climate, language):
        self.continent = continent
        self.climate = climate
        self.language = language


england = country('eu', 'cold', 'english')
cont = england.continent
print(cont)

class city(country):

    def __init__(self, city_name, continent, climate, language):
        self.city_name = city_name
        super().__init__()


class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

myanmial = Dog()