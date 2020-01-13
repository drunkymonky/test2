class Car:
    def __init__(self, number="", model=""):
        self.number = number
        self.model = model

    def __str__(self):
        return self.model+' '+self.number

    def __eq__(self, other):
        return self.number == other.number


class Parking:
    def __init__(self, places_count=10):
        self.places = [Car()] * places_count
        self.EMPTY_CAR = Car()

    def park(self, car):
        for i in self.places:
            if i == :
                self.places[i] = EMPTY_CAR
                break


    def leave(self, car):
        for i in self.places:
            if self.places[i] == car:
                self.places[i] = None
                break

    def __str__(self):
        return ', '.join([str(car) for car in self.places])

    def free(self):
        return self.places.count(Car())


bmw = Car("a123aa", "BMW")
audi = Car("c523ta", "Audi")
garage = Parking()
garage.park(bmw)
garage.park(audi)
print(garage.free())
print(garage)
garage.leave(bmw)