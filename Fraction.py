import math

class Fraction:
    def __init__(self, num, den):
        if type(num) is int and type(den) is int:
            raise ValueError()
        gcd =  math.gcd(num, den)
        self.den = int(den // gcd)
        self.num = int(num // gcd)

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    def __add__(self, other):
        gcd = math.gcd(self.den, other.den)
        num1 = (gcd // self.den) * self.num
        num2 = (gcd // other.den) * other.num
        return Fraction(num1 + num2, gcd)

    def __sub__(self, other):
        gcd = math.gcd(self.den, other.den)
        num1 = (gcd // self.den) * self.num
        num2 = (gcd // other.den) * other.num
        return Fraction(num1 - num2, gcd)

    def __mul__(self, other):
        den = self.den * other.den
        num = self.num * other.num
        return Fraction(num, den)

    def __truediv__(self, other):
        den = self.den * other.num
        num = self.num * other.den
        return Fraction(num, den)

    def get_real(self):
        return self.num / self.den

    def __gt__(self, other):
        return self.get_real() > other.get_real()

    def __ge__(self, other):
        return self.get_real() >= other.get_real()

    def __lt__(self, other):
        return self.get_real() < other.get_real()
    
    def __le__(self, other):
        return self.get_real() <= other.get_real()

    def __ne__(self, other):
        return self.get_real() != other.get_real()

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __iadd__(self, other):
        frac = self + other
        return frac

    def __radd__(self, other):
        if type(other) is int:
            frac = Fraction(other, 1)
            return frac + self
        raise NotImplementedError()
        
    def __repr__(self):
        return 'Numerator: ' + str(self.num) + '\nDenominator: ' + str(self.den)

        