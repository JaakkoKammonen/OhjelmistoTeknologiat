import math
import matplotlib.pyplot as plt

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
    
def create_circle(tuotuympyrä):
    circle= plt.Circle((tuotuympyrä.x,tuotuympyrä.y),radius=tuotuympyrä.r)
    return circle

def show_shape(a,c,b):
    ax= plt.gca()
    ax.add_patch(a.plottable())
    ax.add_patch(b.plottable())
    ax.add_patch(c.plottable())
    plt.axis('scaled')
    plt.show()

def render(ympyra):
    a=create_circle(ympyra[0])
    b=create_circle(ympyra[1]) 
    c=create_circle(ympyra[2])
    show_shape(a,b,c)

## Koitettu myös show_shape(a,b,c)
    ##ax= plt.subplots()
	##ax.add_patch(a,b,c)
	##plt.axis('scaled')
	##plt.show() 
## Yhden saa aina, mutta ei montaa...

a = Circle(5, 5, 2)
b = Circle(-2, 2, 1)
c = Circle(0, 0, 10)
render([a, b, c]) # piirtää koordinaatistolle listan kuvioita
print('Siirretään b:tä 10 ylöspäin')
b.move(0, 10)
print('Siirretään c:tä vasemmalle')
c.move(-5, 0)
render([a, b, c])