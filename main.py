# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Sphere:
    q:float
    radius:float
    axelerate:float
    def __init__(self, q, radius, axelerate):
        self.q = q
        self.radius = radius
        self.axelerate = axelerate
    def getPressureInCentre(self):
        return self.r*self.q*self.axelerate


class Planet(Sphere):
    pressureAtmosphere:float

    def __init__(self, q, radius, axelerate, pressureAtmosphere):
        super(q, radius, axelerate)
        self.pressureAtmosphere = pressureAtmosphere

class Star(Sphere):
    temperature:float
    qCore:float
    def __init__(self, q, radius, axelerate, temperature, qCore):
        super(q, radius, axelerate)
        self.temperature = temperature
        self.qCore = qCore


class Hol:
    radius:float
    def __int__(self, radius):
        self.radius = radius
    def getArea(self):
        return 3.1415926 * pow(radius, 2)

def furyPressure(pressure, area):
    return  (pressure * area)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    qS = float(1410)
    radius = float(696340000)
    gS = float(274)
    gE = float(9.8)
    pa = float(101325)
    qCoreSun = float(150000)
    radiusHol = 0.001
    sun = Star(q=qS, radius=radius,axelerate=gS, temperature=0, qCore=qCoreSun)
    earth = Planet(q=qS, radius=radius, axelerate=gE, pressureAtmosphere=pa)
    print("get radius of portal:")
    hol = Hol(radius=radiusHol)

    pressureHolFromEarthFace = earth.pressureAtmosphere
    pressureHolFromSunFace = sun.getPressureInCentre()
    # vector from Hol Sun X ------>  Earth
    pressureFromHol = pressureHolFromEarthFace - pressureHolFromEarthFace
    furyPressureFromHol = furyPressure(pressureFromHol, hol.getArea())
    V
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
