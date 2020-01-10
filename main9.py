
class Car:
    model = 'BMW'
    velocity = 0
    color = ""
    horses = ""

    def __init__(self, model, color, horses =0):
        pass

    # то что будет возвращать по print(bmw)
    def __str__(self):
        return self.model + ' ' + self.color

    def speedUp(self, vel):
        self.velocity += vel


bmw = Car("BMW","black",100)
bmw.speedUp(10)
print(bmw.velocity)




print(bmw.__dict__)
print(bmw._)






