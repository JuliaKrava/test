
class Flat:
    def __init__(self,  storona1=0, storona2=0 ):
        self.storona1 = storona1
        self.storona2 = storona2
        self.S = storona1*storona2
        self.P = 2*(storona1+storona2)

a=Flat(5,10)
print(a.P, a.S, sep='\n')

import math
class Karta:
    def __init__(self, X=0, Y=0, X1=0, Y1=0):
        self.X = X
        self.Y = Y
        self.RasstoyanieDo = math.sqrt(((X-X1)**2)+((Y-Y1)**2))

b=Karta(4,1)
print(round(b.RasstoyanieDo))

c=Karta(4, 4, 1, 1)
print(c.RasstoyanieDo)
