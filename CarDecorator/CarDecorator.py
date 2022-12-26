class Car: # Car class
    def __init__(self, description):
        self._description = description
    def description(self):
        return self._description
    def safety_rating(self):
        return 0

class SuperMini(Car): # SuperMini class
    def description(self): # Override
        return super().description() + "(SuperMini)"
    def safety_rating(self): # Override
        return 1

class SUV(Car): # SUV class
    def description(self): # Override
        return super().description() + "(SUV)"
    def safety_rating(self): # Override
        return 2

class CarDecorator(Car): # Car decorator class
    def __init__(self, decoratedCar):
        self._decoratedCar = decoratedCar
    def decoratedCar(self):
        return self._decoratedCar
    def description(self): # Override
        return self._decoratedCar.description()
    def safety_rating(self): # Override
        return self._decoratedCar.safety_rating()

class ABS(CarDecorator): # ABS class
    def __init__(self, decoratedCar):
        CarDecorator.__init__(self, decoratedCar)
    def description(self): # Override
        return self.decoratedCar().description() + " with ABS"
    def safety_rating(self): # Override
        return self.decoratedCar().safety_rating() + 2

class AEB(CarDecorator): # AEB class
    def __init__(self, decoratedCar):
        CarDecorator.__init__(self, decoratedCar)
    def description(self): # Override
        return self.decoratedCar().description() + " with AEB"
    def safety_rating(self): # Override
        return self.decoratedCar().safety_rating() + 4

class KeyLess(CarDecorator): # Key less class
    def __init__(self, decoratedCar):
        CarDecorator.__init__(self, decoratedCar)
    def description(self): # Override
        return self.decoratedCar().description() + " is keyless"

# Checks for decorator
car1 = SuperMini("Scoda Fabia")
car1 = KeyLess(car1)
car1 = AEB(car1)
assert(car1.description() == "Scoda Fabia(SuperMini) is keyless with AEB")
assert(car1.safety_rating() == 5)
car1 = ABS(car1)
assert(car1.description() == "Scoda Fabia(SuperMini) is keyless with AEB with ABS")
assert(car1.safety_rating() == 7)