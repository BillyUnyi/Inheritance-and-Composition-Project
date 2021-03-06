from graphics import *
import random
import winsound

class Window(object):
    """Draws water and the fleet"""

    def __init__(self, win):
        self.water1 = Water("Blue", win)
        self.fleet1 = Fleet(win)


class Water(object):
    """draws the water"""

    def __init__(self, color, win):
        self.water = None
        self.sun = None
        self.moon = None
        self.island = None
        self.rect = None
        self.rect1 = None
        self.rect2 = None
        self.line = None
        self.drawSun(win)
        self.drawWater(color, win)
        self.drawFlag(win)
        self.drawIsland(win)
        self.drawClouds(win)
        tank1 = SuperTank(0, 0, 1350, 480, Color.lightGray, Color.darkGray, win)
        tank2 = SuperTank(0, 0, 1475, 470, Color.lightGray, Color.darkGray, win)
        tank3 = SuperTank(0, 0, 1560, 480, Color.lightGray, Color.darkGray, win)

    def drawWater(self, color, win):
        self.water = Rectangle(Point(-25, 500), Point(1925, 1050))
        self.water.setFill(color)
        self.water.setOutline(color)
        self.water.draw(win)

    def drawIsland(self, win):
        self.island = Polygon(Point(1700, 500), Point(1500, 475), Point(1300, 500))
        self.island.setFill(Color.tan)
        self.island.setOutline("Black")
        self.island.draw(win)

    def drawFlag(self, win):
        self.rect = Rectangle(Point(1330, 300), Point(1530, 333))
        self.rect.setFill("White")
        self.rect.setOutline("White")
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(1330, 334), Point(1530, 366))
        self.rect1.setFill("Blue")
        self.rect1.setOutline("Blue")
        self.rect1.draw(win)
        self.rect2 = Rectangle(Point(1330, 367), Point(1530, 400))
        self.rect2.setFill("Red")
        self.rect2.setOutline("Red")
        self.rect2.draw(win)
        self.line = Line(Point(1530, 300), Point(1530, 500))
        self.line.setOutline("Black")
        self.line.setWidth(3)
        self.line.draw(win)

    def drawSun(self, win):
        self.sun = Circle(Point(1700, 150), 50)
        self.sun.setFill("Yellow")
        self.sun.setOutline("Black")
        self.sun.draw(win)

    def drawMoon(self, win):
        self.moon = Circle(Point(1700, 150), 50)
        self.moon.setFill(Color.darkGray)
        self.moon.setOutline(Color.lightGray)
        self.moon.draw(win)

    def drawClouds(self, win):
        self.oval = Oval(Point(300, 400), Point(400, 425))
        self.oval.setFill("White")
        self.oval.setOutline("Black")
        self.oval.draw(win)
        self.oval1 = Oval(Point(550, 140), Point(650, 165))
        self.oval1.setFill("White")
        self.oval1.setOutline("Black")
        self.oval1.draw(win)
        self.oval2 = Oval(Point(800, 120), Point(900, 145))
        self.oval2.setFill("White")
        self.oval2.setOutline("Black")
        self.oval2.draw(win)
        self.oval3 = Oval(Point(1000, 300), Point(1100, 325))
        self.oval3.setFill("White")
        self.oval3.setOutline("Black")
        self.oval3.draw(win)
        self.oval4 = Oval(Point(1750, 320), Point(1850, 345))
        self.oval4.setFill("White")
        self.oval4.setOutline("Black")
        self.oval4.draw(win)
        self.oval5 = Oval(Point(1300, 220), Point(1400, 245))
        self.oval5.setFill("White")
        self.oval5.setOutline("Black")
        self.oval5.draw(win)
        self.oval6 = Oval(Point(100, 100), Point(200, 125))
        self.oval6.setFill("White")
        self.oval6.setOutline("Black")
        self.oval6.draw(win)
        self.oval7 = Oval(Point(750, 440), Point(850, 465))
        self.oval7.setFill("White")
        self.oval7.setOutline("Black")
        self.oval7.draw(win)
        self.oval8 = Oval(Point(1500, 75), Point(1600, 100))
        self.oval8.setFill("White")
        self.oval8.setOutline("Black")
        self.oval8.draw(win)

    def undrawClouds(self):
        self.oval.undraw()
        self.oval1.undraw()
        self.oval2.undraw()
        self.oval3.undraw()
        self.oval4.undraw()
        self.oval5.undraw()
        self.oval6.undraw()
        self.oval7.undraw()
        self.oval8.undraw()

    def drawStars(self, win):
        x = 300
        y = 400
        self.star = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star.setFill("Yellow")
        self.star.setOutline("Black")
        self.star.draw(win)
        x = 550
        y = 140
        self.star1 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star1.setFill("Yellow")
        self.star1.setOutline("Black")
        self.star1.draw(win)
        x = 800
        y = 120
        self.star2 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star2.setFill("Yellow")
        self.star2.setOutline("Black")
        self.star2.draw(win)
        x = 1000
        y = 300
        self.star3 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star3.setFill("Yellow")
        self.star3.setOutline("Black")
        self.star3.draw(win)
        x = 1750
        y = 320
        self.star4 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star4.setFill("Yellow")
        self.star4.setOutline("Black")
        self.star4.draw(win)
        x = 1300
        y = 220
        self.star5 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star5.setFill("Yellow")
        self.star5.setOutline("Black")
        self.star5.draw(win)
        x = 100
        y = 100
        self.star6 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star6.setFill("Yellow")
        self.star6.setOutline("Black")
        self.star6.draw(win)
        x = 750
        y = 380
        self.star7 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star7.setFill("Yellow")
        self.star7.setOutline("Black")
        self.star7.draw(win)
        x = 1500
        y = 75
        self.star8 = Polygon(Point(x, y), Point(x + 10, y + 30), Point(x + 40, y + 40), Point(x + 10, y + 50), Point(x, y + 80),
                            Point(x - 10, y + 50), Point(x - 40, y + 40), Point(x - 10, y + 30))
        self.star8.setFill("Yellow")
        self.star8.setOutline("Black")
        self.star8.draw(win)

    def undrawStars(self):
        self.star.undraw()
        self.star1.undraw()
        self.star2.undraw()
        self.star3.undraw()
        self.star4.undraw()
        self.star5.undraw()
        self.star6.undraw()
        self.star7.undraw()
        self.star8.undraw()

class Fleet(object):
    """draws everything from the fleet"""

    def __init__(self, win):
        aircraftCarrier1 = AircraftCarrier(400, 550, "Gray", "Gray3", win)
        aircraftCarrier2 = AircraftCarrier(600, 700, "Gray", "Gray3", win)
        aircraftCarrier3 = SuperAircraftCarrier(1300, 600, "Gray", "Gray3", win)


class AircraftCarrier(object):
    """Draws an aircraft carrier and it's squadron"""

    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = SuperAirplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = SuperAirplane(x, y, -200, -400, Color.darkGray, "Black", win)
        personnel1 = Personnel(x, y, 300, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(x, y, 320, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(x, y, 280, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel4 = Personnel(x, y, 275, -35, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel5 = Personnel(x, y, 240, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel6 = Personnel(x, y, 220, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel7 = Personnel(x, y, 230, -30, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(x, y, 260, -30, Color.lightTan, Color.darkGray1, "Blue4", "Red", "Black", win)
        boat1 = Boat(x, y, -200, 100, "Gray", "Gray3", win)
        boat2 = SuperBoat(x, y, -300, 200, "Gray", "Gray3", win)

    def drawAircraftCarrier(self, x, y, color, outline, win):
        ship = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10),
                       Point(x + 340, y + 80), Point(x + 100, y + 100))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10),
                           Point(x + 100, y + 20))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(x + 100, y + 100), Point(x + 100, y + 20))
        line.setOutline(outline)
        line.draw(win)


class SuperAircraftCarrier(AircraftCarrier):
    """Includes a tank"""

    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = SuperAirplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = SuperAirplane(x, y, -200, -400, Color.darkGray, "Black", win)
        personnel1 = Personnel(x, y, 300, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(x, y, 320, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(x, y, 280, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel4 = Personnel(x, y, 275, -35, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel5 = Personnel(x, y, 240, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel6 = Personnel(x, y, 220, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel7 = Personnel(x, y, 230, -30, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(x, y, 260, -30, Color.lightTan, Color.darkGray1, "Blue4", "Red", "Black", win)
        boat1 = Boat(x, y, -200, 100, "Gray", "Gray3", win)
        boat2 = SuperBoat(x, y, -300, 200, "Gray", "Gray3", win)
        tank1 = Tank(x, y, 350, -30, Color.lightGray, Color.darkGray, win)
        tank2 = Tank(x, y, 375, -5, Color.lightGray, Color.darkGray, win)

    def drawAircraftCarrier(self, x, y, color, outline, win):
        ship = Polygon(Point(x, y), Point(x + 112, y - 37), Point(x + 450, y - 30), Point(x + 525, y + 15),
                       Point(x + 510, y + 120), Point(x + 150, y + 150))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(x, y), Point(x + 112, y - 37), Point(x + 450, y - 30), Point(x + 525, y + 15),
                           Point(x + 150, y + 30))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(x + 150, y + 150), Point(x + 150, y + 30))
        line.setOutline(outline)
        line.draw(win)


class Airplane(object):
    """Draws a fighter jet"""

    def __init__(self, X, Y, x, y, mainColor, outline, win):
        self.drawAirplane(X, Y, x, y, mainColor, outline, win)

    def drawAirplane(self, X, Y, x, y, mainColor, outline, win):
        rightWing = Polygon(Point(X + x + 60, Y + y), Point(X + x + 135, Y + y - 5), Point(X + x + 100, Y + y - 30))
        rightWing.setFill(mainColor)
        rightWing.setOutline(outline)
        rightWing.draw(win)
        plane = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10), Point(X + x + 100, Y + y - 15),
                        Point(X + x + 150, Y + y - 15),
                        Point(X + x + 155, Y + y - 10), Point(X + x + 158, Y + y), Point(X + x + 150, Y + y + 9),
                        Point(X + x + 100, Y + y + 10),
                        Point(X + x + 50, Y + y + 7))
        plane.setFill(mainColor)
        plane.setOutline(outline)
        plane.draw(win)
        window = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10), Point(X + x + 45, Y + y))
        window.setFill("Black")
        window.setOutline("Black")
        window.draw(win)
        leftWing = Polygon(Point(X + x + 75, Y + y - 2), Point(X + x + 140, Y + y - 5), Point(X + x + 180, Y + y + 15))
        leftWing.setFill(mainColor)
        leftWing.setOutline(outline)
        leftWing.draw(win)


class SuperAirplane(Airplane):
    """draws an airplane with extra detail"""

    def __init__(self, X, Y, x, y, mainColor, outline, win):
        self.drawFlames(X, Y, x, y, win)
        super().__init__(X, Y, x, y, mainColor, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 60, Y + y - 9), Point(X + x + 62, Y + y - 4), Point(X + x + 68, Y + y + - 4),
                       Point(X + x + 64, Y + y),
                       Point(X + x + 65, Y + y + 5), Point(X + x + 60, Y + y + 2), Point(X + x + 55, Y + y + 5),
                       Point(X + x + 56, Y + y),
                       Point(X + x + 52, Y + y - 4), Point(X + x + 58, Y + y - 4))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)

    def drawFlames(self, X, Y, x, y, win):
        flames = Polygon(Point(X + x + 150, Y + y - 15), Point(X + x + 165, Y + y - 20), Point(X + x + 160, Y + y - 12),
                         Point(X + x + 175, Y + y - 15),
                         Point(X + x + 165, Y + y - 5), Point(X + x + 180, Y + y), Point(X + x + 158, Y + y))
        flames.setFill("Red")
        flames.setOutline("Orange")
        flames.draw(win)


class Personnel(object):
    """draws personnel"""

    def __init__(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        self.drawPersonnel(X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win)

    def drawPersonnel(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        head = Circle(Point(X + x, Y + y), 5)
        head.setFill(skinColor)
        head.setOutline(outline)
        head.draw(win)
        hands = Polygon(Point(X + x - 10, Y + y + 6), Point(X + x + 10, Y + y + 6), Point(X + x, Y + y + 40))
        hands.setFill(uniformColor)
        hands.setOutline(outline)
        hands.draw(win)
        body = Polygon(Point(X + x - 6, Y + y + 6), Point(X + x + 6, Y + y + 6), Point(X + x + 5, Y + y + 20),
                       Point(X + x - 5, Y + y + 20), )
        body.setFill(uniformColor)
        body.setOutline(outline)
        body.draw(win)
        legs = Polygon(Point(X + x - 5, Y + y + 20), Point(X + x + 5, Y + y + 20), Point(X + x + 4, Y + y + 40),
                       Point(X + x - 4, Y + y + 40))
        legs.setFill(pantsColor)
        legs.setOutline(outline)
        legs.draw(win)
        line = Line(Point(X + x, Y + y + 25), Point(X + x, Y + y + 40))
        line.setOutline(outline)
        line.draw(win)


class Captain(Personnel):
    """draws the captain"""

    def __init__(self, X, Y, x, y, skinColor, uniformColor, pantsColor, hatColor, outline, win):
        super().__init__(X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win)
        self.drawHat(X, Y, x, y, hatColor, outline, win)

    def drawHat(self, X, Y, x, y, hatColor, outline, win):
        hat = Polygon(Point(X + x - 5, Y + y - 7), Point(X + x + 5, Y + y - 7), Point(X + x + 4, Y + y - 3),
                      Point(X + x - 4, Y + y - 3))
        hat.setFill(hatColor)
        hat.setOutline(outline)
        hat.draw(win)


class Boat(object):
    """draws a boat"""

    def __init__(self, X, Y, x, y, color, outline, win):
        self.drawBoat(X, Y, x, y, color, outline, win)
        personnel1 = Personnel(X + x, Y + y, 65, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(X + x, Y + y, 80, -35, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(X + x, Y + y, 110, -43, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(X + x, Y + y, 140, -40, Color.lightTan, Color.darkGray1, "Blue4", "Red", "Black", win)

    def drawBoat(self, X, Y, x, y, color, outline, win):
        ship = Polygon(Point(X + x, Y + y), Point(X + x + 37, Y + y - 12), Point(X + x + 150, Y + y - 10),
                       Point(X + x + 175, Y + y + 5),
                       Point(X + x + 170, Y + y + 40), Point(X + x + 50, Y + y + 50))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(X + x, Y + y), Point(X + x + 37, Y + y - 12), Point(X + x + 150, Y + y - 10),
                           Point(X + x + 175, Y + y + 5),
                           Point(X + x + 50, Y + y + 10))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(X + x + 50, Y + y + 50), Point(X + x + 50, Y + y + 10))
        line.setOutline(outline)
        line.draw(win)


class SuperBoat(Boat):
    """draws a boat with extra detail"""

    def __init__(self, X, Y, x, y, color, outline, win):
        super().__init__(X, Y, x, y, color, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 70, Y + y + 12), Point(X + x + 74, Y + y + 22), Point(X + x + 86, Y + y + 22),
                       Point(X + x + 78, Y + y + 30),
                       Point(X + x + 80, Y + y + 40), Point(X + x + 70, Y + y + 34), Point(X + x + 60, Y + y + 40),
                       Point(X + x + 62, Y + y + 30),
                       Point(X + x + 54, Y + y + 22), Point(X + x + 66, Y + y + 22))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)


class Tank(object):
    """draws a tank"""
    TANKS = []

    def __init__(self, X, Y, x, y, color, outline, win):
        personnel1 = Personnel(X + x, Y + y, 65, -55, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        self.rect = None
        self.rect1 = None
        self.circ = None
        self.circ1 = None
        self.line = None
        self.cannon = None
        self.turret = None
        self.body = None
        self.fire = None
        self.drawTreds(X, Y, x, y, color, outline, win)
        self.drawCannon(X, Y, x, y, color, outline, win)
        self.drawBody(X, Y, x, y, color, outline, win)
        self.drawFire(X, Y, x, y, win)
        Tank.TANKS.append(self)

    def drawTreds(self, X, Y, x, y, color, outline, win):
        self.rect = Rectangle(Point(X + x, Y + y - 5), Point(X + x + 96, Y + y))
        self.rect.setFill(color)
        self.rect.setOutline(outline)
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(X + x, Y + y), Point(X + x + 96, Y + y + 15))
        self.rect1.setFill("Black")
        self.rect1.setOutline("Black")
        self.rect1.draw(win)
        self.circ = Circle(Point(X + x, Y + y + 8), 7)
        self.circ.setFill("Black")
        self.circ.setOutline("Black")
        self.circ.draw(win)
        self.circ1 = Circle(Point(X + x + 96, Y + y + 8), 7)
        self.circ1.setFill("Black")
        self.circ1.setOutline("Black")
        self.circ1.draw(win)
        for i in range(9):
            self.circ = Circle(Point(X + x + i * 12, Y + y + 8), 6)
            self.circ.setFill(outline)
            self.circ.setOutline("Black")
            self.circ.draw(win)
        self.line = Line(Point(X + x, Y + y + 8), Point(X + x + 96, Y + y + 8))
        self.line.setOutline(color)
        self.line.setWidth(2)
        self.line.draw(win)

    def drawCannon(self, X, Y, x, y, color, outline, win):
        self.cannon = Polygon(Point(X + x + 50, Y + y - 25), Point(X + x + 50, Y + y - 35),
                              Point(X + x - 10, Y + y - 33), Point(X + x - 10, Y + y - 27))
        self.cannon.setFill(Color.darkGray)
        self.cannon.setOutline(outline)
        self.cannon.draw(win)
        self.turret = Polygon(Point(X + x + 30, Y + y - 15), Point(X + x + 50, Y + y - 40),
                              Point(X + x + 80, Y + y - 40), Point(X + x + 90, Y + y - 15))
        self.turret.setFill(color)
        self.turret.setOutline(outline)
        self.turret.draw(win)

    def drawBody(self, X, Y, x, y, color, outline, win):
        self.body = Polygon(Point(X + x - 10, Y + y - 5), Point(X + x + 106, Y + y - 5), Point(X + x + 96, Y + y - 15),
                            Point(X + x, Y + y - 15), )
        self.body.setFill(color)
        self.body.setOutline(outline)
        self.body.draw(win)

    def drawFire(self, X, Y, x, y, win):
        self.fire = Polygon(Point(X + x - 10, Y + y - 33), Point(X + x - 10, Y + y - 27), Point(X + x - 20, Y + y - 10),
                            Point(X + x - 17, Y + y - 25), Point(X + x - 30, Y + y - 30), Point(X + x - 17, Y + y - 35),
                            Point(X + x - 20, Y + y - 50))
        self.fire.setFill("Red")
        self.fire.setOutline("Orange")


class SuperTank(Tank):
    """draws the ultimate tank"""

    def __init__(self, X, Y, x, y, color, outline, win):
        super().__init__(X, Y, x, y, color, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 63, Y + y - 36), Point(X + x + 67, Y + y - 26), Point(X + x + 79, Y + y - 26),
                       Point(X + x + 71, Y + y - 18), Point(X + x + 73, Y + y - 8), Point(X + x + 63, Y + y - 14),
                       Point(X + x + 53, Y + y - 8), Point(X + x + 55, Y + y - 18), Point(X + x + 47, Y + y - 26),
                       Point(X + x + 59, Y + y - 26))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)


class Nuke(object):
    """drops a nuke"""
    xValue = 0

    def __init__(self, win):
        self.nuke1 = None
        self.rocket = None
        self.rect = None
        self.rect1 = None
        self.rect2 = None
        self.rightWing = None
        self.leftWing = None
        self.x = Nuke.xValue
        self.y = -25
        self.drawNuke(win)

    def drawSight(self, win):
        y = 900
        self.sight = Circle(Point(self.x, y), 75)
        self.sight.setFill(None)
        self.sight.setOutline("Green")
        self.sight.setWidth(3)
        self.sight.draw(win)
        self.line = Line(Point(self.x, y + 15), Point(self.x, y - 90))
        self.line.setOutline("Green")
        self.line.setWidth(3)
        self.line.draw(win)
        self.line1 = Line(Point(self.x - 15, y), Point(self.x + 15, y))
        self.line1.setOutline("Green")
        self.line1.setWidth(3)
        self.line1.draw(win)
        self.line2 = Line(Point(self.x, y + 60), Point(self.x, y + 90))
        self.line2.setOutline("Green")
        self.line2.setWidth(3)
        self.line2.draw(win)
        self.line3 = Line(Point(self.x - 90, y), Point(self.x - 60, y))
        self.line3.setOutline("Green")
        self.line3.setWidth(3)
        self.line3.draw(win)
        self.line4 = Line(Point(self.x + 60, y), Point(self.x + 90, y))
        self.line4.setOutline("Green")
        self.line4.setWidth(3)
        self.line4.draw(win)
        self.line5 = Line(Point(self.x - 10, y - 15), Point(self.x + 10, y - 15))
        self.line5.setOutline("Green")
        self.line5.draw(win)
        self.line6 = Line(Point(self.x - 10, y - 25), Point(self.x + 10, y - 25))
        self.line6.setOutline("Green")
        self.line6.draw(win)
        self.line7 = Line(Point(self.x - 10, y - 35), Point(self.x + 10, y - 35))
        self.line7.setOutline("Green")
        self.line7.draw(win)
        self.line8 = Line(Point(self.x - 10, y - 45), Point(self.x + 10, y - 45))
        self.line8.setOutline("Green")
        self.line8.draw(win)
        self.line9 = Line(Point(self.x - 10, y - 55), Point(self.x + 10, y - 55))
        self.line9.setOutline("Green")
        self.line9.draw(win)
        self.line10 = Line(Point(self.x - 10, y - 65), Point(self.x + 10, y - 65))
        self.line10.setOutline("Green")
        self.line10.draw(win)

    def undrawSight(self):
        self.sight.undraw()
        self.line.undraw()
        self.line1.undraw()
        self.line2.undraw()
        self.line3.undraw()
        self.line4.undraw()
        self.line5.undraw()
        self.line6.undraw()
        self.line7.undraw()
        self.line8.undraw()
        self.line9.undraw()
        self.line10.undraw()

    def drawNuke(self, win):
        self.nuke1 = Polygon(Point(self.x, self.y), Point(self.x - 15, self.y - 50), Point(self.x - 20, self.y - 100),
                             Point(self.x + 20, self.y - 100), Point(self.x + 15, self.y - 50))
        self.nuke1.setFill("Red4")
        self.nuke1.setOutline("Black")
        self.nuke1.draw(win)
        self.rocket = Rectangle(Point(self.x - 20, self.y - 300), Point(self.x + 20, self.y - 100))
        self.rocket.setFill(Color.darkGray)
        self.rocket.setOutline("Black")
        self.rocket.draw(win)
        self.rect = Rectangle(Point(self.x - 15, self.y - 290), Point(self.x - 6, self.y - 110))
        self.rect.setFill("Red")
        self.rect.setOutline("Red")
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(self.x - 5, self.y - 290), Point(self.x + 4, self.y - 110))
        self.rect1.setFill("Blue")
        self.rect1.setOutline("Blue")
        self.rect1.draw(win)
        self.rect2 = Rectangle(Point(self.x + 5, self.y - 290), Point(self.x + 15, self.y - 110))
        self.rect2.setFill("White")
        self.rect2.setOutline("White")
        self.rect2.draw(win)
        self.rightWing = Polygon(Point(self.x - 21, self.y - 300), Point(self.x - 21, self.y - 250),
                                 Point(self.x - 35, self.y - 300), Point(self.x - 40, self.y - 350))
        self.rightWing.setFill("Red")
        self.rightWing.setOutline("Black")
        self.rightWing.draw(win)
        self.leftWing = Polygon(Point(self.x + 21, self.y - 300), Point(self.x + 21, self.y - 250),
                                Point(self.x + 35, self.y - 300), Point(self.x + 40, self.y - 350))
        self.leftWing.setFill("Red")
        self.leftWing.setOutline("Black")
        self.leftWing.draw(win)

    def dropNuke(self):
        self.nuke1.move(0, 110)
        self.rocket.move(0, 110)
        self.rect.move(0, 110)
        self.rect1.move(0, 110)
        self.rect2.move(0, 110)
        self.rightWing.move(0, 110)
        self.leftWing.move(0, 110)
        time.sleep(.05)

    def undrawNuke(self):
        self.nuke1.undraw()
        self.rocket.undraw()
        self.rect.undraw()
        self.rect1.undraw()
        self.rect2.undraw()
        self.rightWing.undraw()
        self.leftWing.undraw()

    def drawExplosion(self, win):
        y = self.y + 1025
        x = self.x + random.randrange(10) - 5
        self.explosion = Polygon(Point(x - 75, y), Point(x - 80, y - 350), Point(x - 55, y - 125),
                                 Point(x - 45, y - 375), Point(x - 20, y - 150),
                                 Point(x, y - 400), Point(x + 20, y - 150), Point(x + 45, y - 375),
                                 Point(x + 55, y - 125), Point(x + 80, y - 350),
                                 Point(x + 75, y))
        self.explosion.setFill("Red")
        self.explosion.setOutline("Orange")
        self.explosion.draw(win)
        time.sleep(.05)

    def undrawExplosion(self):
        self.explosion.undraw()


class Color(object):
    """Holds colors"""
    lightGray = color_rgb(121, 121, 121)
    darkGray = color_rgb(80, 80, 80)
    darkGray1 = color_rgb(40, 40, 40)
    lightTan = color_rgb(246, 235, 204)
    tan = color_rgb(218, 193, 125)
    darkTan = color_rgb(97, 48, 0)
    darkBlue = color_rgb(0, 0, 80)


class TimeOfDay(object):
    """has day, night, and war"""

    @staticmethod
    def war(win, click):
        if click:
            click = True
            Time = 0
            winsound.PlaySound('Machine+Gun+3.wav', winsound.SND_ASYNC)
            while Time < 8 and click:
                win.setBackground(color_rgb(random.randrange(255), random.randrange(255), random.randrange(255)))
                #if random.randrange(25) == 0:
                    #winsound.PlaySound('Machine+Gun+3.wav', winsound.SND_ASYNC)
                    #time.sleep(.1)
                #elif random.randrange(25) == 0:
                    #winsound.PlaySound('Machine+Gun+4.wav', winsound.SND_ASYNC)
                    #time.sleep(.1)
                if random.randrange(10) == 0:
                    index = random.randrange(len(Tank.TANKS))
                    Tank.TANKS[index].fire.draw(win)
                    winsound.PlaySound('Explosion+3.wav', winsound.SND_ASYNC)
                    time.sleep(.1)
                    Tank.TANKS[index].fire.undraw()
                coordinate = win.checkMouse()
                Key = win.checkKey()
                if Key == "q":
                    click = False
                    win.setBackground("Red4")
                    winsound.PlaySound('Bomb+1.wav', winsound.SND_ALIAS)
                elif coordinate is None:
                    time.sleep(.05)
                    Time += .05
                else:
                    Nuke.xValue = coordinate.x
                    nuke = Nuke(win)
                    nuke.drawSight(win)
                    winsound.PlaySound('Missile+1.wav', winsound.SND_ASYNC)
                    for i in range(10):
                        nuke.dropNuke()
                    nuke.undrawNuke()
                    nuke.undrawSight()
                    winsound.PlaySound('Bomb+1.wav', winsound.SND_ASYNC)
                    for j in range(20):
                        nuke.drawExplosion(win)
                        nuke.undrawExplosion()
                    Time += 1.5
        return click

    @staticmethod
    def day(win, window, click):
        if click:
            win.setBackground("Cyan")
            window.water1.moon.undraw()
            window.water1.undrawStars()
            window.water1.drawSun(win)
            window.water1.drawClouds(win)
            window.water1.water.setFill("Blue")
            window.water1.water.setOutline("Blue")
            winsound.PlaySound('ocean-wave-1.wav', winsound.SND_ASYNC)
            click = TimeOfDay.clicked(win)
        return click

    @staticmethod
    def night(win, window, click):
        if click:
            win.setBackground(Color.darkBlue)
            window.water1.sun.undraw()
            window.water1.undrawClouds()
            window.water1.drawMoon(win)
            window.water1.drawStars(win)
            window.water1.water.setFill("Blue4")
            window.water1.water.setOutline("Blue4")
            winsound.PlaySound('ocean-wave-1.wav', winsound.SND_ASYNC)
            click = TimeOfDay.clicked(win)
        return click

    @staticmethod
    def clicked(win):
        click = True
        Time = 0
        while Time < 15 and click:
            coordinate = win.checkMouse()
            Key = win.checkKey()
            if Key == "q":
                click = False
                win.setBackground("Red4")
                winsound.PlaySound('Bomb+1.wav', winsound.SND_ALIAS)
            elif coordinate is None:
                time.sleep(.05)
                Time += .05
            else:
                Nuke.xValue = coordinate.x
                nuke = Nuke(win)
                nuke.drawSight(win)
                winsound.PlaySound('Missile+1.wav', winsound.SND_ASYNC)
                for i in range(10):
                    nuke.dropNuke()
                nuke.undrawNuke()
                nuke.undrawSight()
                winsound.PlaySound('Bomb+1.wav', winsound.SND_ASYNC)
                for j in range(20):
                    nuke.drawExplosion(win)
                    nuke.undrawExplosion()
                winsound.PlaySound('National Anthem of USSR.wav', winsound.SND_ASYNC)
                Time += 1.5
        return click


def main():
    win = GraphWin("Fleet", 1900, 1040)  # fits my window at home, change if nessasary
    win.setBackground("Cyan")
    window = Window(win)
    winsound.PlaySound('ocean-wave-1.wav', winsound.SND_ASYNC)
    click = TimeOfDay.clicked(win)
    while click:
        click = TimeOfDay.war(win, click)
        click = TimeOfDay.night(win, window, click)
        click = TimeOfDay.war(win, click)
        click = TimeOfDay.day(win, window, click)
    win.close()


main()
