

class Cat():

    def __init__(self, weight, name, color, age):
        self.weight = weight
        self.name = name
        self.color = color
        self.age = age

    def Meow(self):
        return self.name

    def is_healthy(self):
        if self.age < self.weight:
            return True
        else:
            return False

barsik = Cat(name='Bars',weight=5,color='black',age=6)

print(barsik.is_healthy())








