class Fraction():
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def plus(self, o):
        a = self.d1
        b = self.d2
        c = o.d1
        d = o.d2
        return Fraction(a * d + b * c, b * d)

    def minus(self, o):
        return Fraction(self.d1 * o.d1 - self.d2 * o.d2)

    def mul(self, o):
        return Fraction(self.d1 * o.d1, self.d2 * o.d2)

    def div(self, o):
        return Fraction(self.d1 * o.d1, self.d2 * o.d2)

    def to_float(self, o):
        pass

one_half = Fraction(1,2)

one_quater = Fraction(1,4)

print(one_half)

