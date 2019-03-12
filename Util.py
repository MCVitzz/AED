import math

class Util:
    @staticmethod
    def lcm(x, y):
        lcm = (x*y)//math.gcd(x,y)
        return lcm


print(Util.lcm(4, 2))