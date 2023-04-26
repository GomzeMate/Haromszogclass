import math

class Haromszog:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def kerulet(self):
        return self.a + self.b + self.c
    
    def terulet(self):
        s = self.kerulet() / 2

    def MagassagA(self):
        return 2* self.terulet() / self.a
    
    def MagassagB(self):
        return 2* self.terulet() / self.b
    
    def MagassagC(self):
        return 2* self.terulet() / self.c
    
    def Alfa(self):
        return math.degress(math.acos((2*self.b*self.c**2 - self.a**2)/(2*self.b*self.c)))
    
    def Betta(self):
        return math.degress(math.acos((2*self.b*self.c**2 - self.b**2)/(2*self.b*self.c)))
    
    def Gamma(self):
        return math.degress(math.acos((2*self.b*self.c**2 - self.c**2)/(2*self.b*self.c)))
    
#0
print("háromszögek feldolgozása 'class' segítségével")

#1
a = input("a = ").replace(',' , '.')
b = input("b = ").replace(',' , '.')
c = input("c = ").replace(',' , '.')

har1 = Haromszog(a, b, c)
har2 = Haromszog(10,10,10)


Adatsor = "10,5;12,6;13,4"
har3 = Haromszog(*(Adatsor.replace(',' , '.').split(';')))
#Először az adatsorba kijavítjuk a hibákat és részekre osztjuk
#De ezek a részek tuplekbe kerülnek vissza
#A tuplet tovább bontsuk a oldalra, b oldalra, c oldalra, erra szolgál a *



#3
print(f"K = {har1.kerulet():.2f}")
print(f"K = {har2.kerulet():.2f}")
print(f"K = {har3.kerulet():.2f}")
print()
print(f"ma = {har1.MagassagA():.2f}")
print(f"mb = {har2.MagassagB():.2f}")
print(f"mc = {har2.MagassagC():.2f}")
print(f"alfa = {har2.Alfa():.2f}")
print(f"betta = {har2.Betta():.2f}")
print(f"gamma = {har2.Gamma():.2f}")