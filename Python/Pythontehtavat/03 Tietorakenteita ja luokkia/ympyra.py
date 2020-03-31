import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        area = math.pi * self.r ** 2
        return area
    
    def circumference(self):
        circumference = 2 * math.pi * self.r
        return circumference
    
    def overlaps(self,ympyratuotu):
        x1 = self.x
        y1 = self.y
        x2 = ympyratuotu.x
        y2 = ympyratuotu.y
        ylitys = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        if ylitys > ympyratuotu.r + self.r:
            return True
        else:
            return False

    def move(self, i,j):
        self.x = self.x + i
        self.y = self.y + j
    
    
a = Circle(5, 5, 2)
b = Circle(-2, 2, 1)
c = Circle(0, 0, 10) 

print('Ympyrän a ala:', a.area()) 
print('Ympyrän b piiri:', b.circumference())
print('a ja b ovat päällekkäin:', a.overlaps(b))
print('b ja c ovat päällekkäin:', b.overlaps(c))
print('Siirretään b:tä 10 ylöspäin') 
b.move(0, 10)
print('b ja c ovat päällekkäin:', b.overlaps(c)) 
