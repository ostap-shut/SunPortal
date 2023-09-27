# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
PI = 3.1415926
class Sphere:
    q: float
    radius: float
    axelerate: float
    def __init__(self, q:float, radius:float, axelerate:float):
        self.q = q
        self.radius = radius
        self.axelerate = axelerate
    def getPressureInCentre(self):
        return self.radius * self.q * self.axelerate


class Planet(Sphere):
    pressureAtmosphere:float

    def __init__(self, q:float, radius:float, axelerate:float, pressureAtmosphere:float):
        self.q = q
        self.radius = radius
        self.axelerate = axelerate
        self.pressureAtmosphere = pressureAtmosphere

class Star(Sphere):
    temperature: float
    qCore: float
    def __init__(self, q: float, radius: float, axelerate: float, temperature: float, qCore: float):
        self.q = q
        self.radius = radius
        self.axelerate = axelerate
        self.temperature = temperature
        self.qCore = qCore


class Hol:
    radius: float
    def __int__(self, radius: float):
        self.radius = radius
    def getArea(self):
        return PI * (self.radius ** 2)

def furyPressure(pressure: float, area: float):
    return pressure * area


class SunBlast:
    furyPressure: float
    nullMass: float = 3*(1.660539066605 * (10 ** -27))
    startTime: float = 0
    iterTimeStamp: float = 1
    star: Star
    planet: Planet
    hol: Hol
    def __init__(self, star:Star, planet:Planet, hol:Hol):
        self.star = star
        self.planet = planet
        self.hol = hol
    def getFuryHol(self):
        return ((self.planet.pressureAtmosphere - self.star.getPressureInCentre()) * (self.hol.radius ** 2) * PI)
    def getMass(self, time: float):
        return (
            (self.getFuryHol() ** 2) * (time ** 4) * 2 * PI * self.star.qCore ** (1/3)
        )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    qS = float(1410)
    radius = float(696340000)
    gS = float(274)
    gE = float(9.8)
    pa = float(101325)
    qCoreSun = float(150000)
    nullMass: float = 3 * (1.660539066605 * (10 ** -27))
    radiusHol = 0.001
    sun = Star(q=qS, radius=radius,axelerate=gS, temperature=0, qCore=qCoreSun)
    earth = Planet(q=qS, radius=radius, axelerate=gE, pressureAtmosphere=pa)
    print("get radius of portal:")
    hol = Hol()
    hol.radius = radiusHol
    sunBlast = SunBlast(star=sun, planet=earth, hol=hol)

    # vector from Hol Sun X ------>  Earth
    for i in range(0, 100, 1):
        print( sunBlast.getMass(time=(i/1000000)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
