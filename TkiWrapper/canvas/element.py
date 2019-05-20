from math import sqrt, sin, cos, atan2
from math import degrees, radians
from math import pi as PI
from TkiWrapper.canvas.point import Point

class Element:
    '''Class used to store data of elements that are to be drawn on canvas
    Object oriented approach is helpful in organizing parameters
    and making parameters easily updatable'''
    def __init__(self):
        pass
    def reInit(self, canvas):
        self.cnv = canvas
        self.color = canvas.FOREGROUND
        self.stroke = canvas.STROKE_WIDTH
    def remove(self):
        self.cnv.elements = [e for e in self.cnv.elements if e is not self]
    def _handleDrawMode(self, drawMode):
        if drawMode.upper() not in ['STROKE', 'FILL']:
            raise Exception('Invalid draw mode. Use "STROKE" or "FILL"')
        self.drawMode = drawMode.upper()


class Line(Element):
    '''Straight line between point A and point B'''
    def __init__(self, pointA, pointB):
        super().__init__()
        self.pointA, self.pointB = Point(*pointA), Point(*pointB)
    def draw(self):
        c = self.cnv.canvas
        pointA = self.pointA.transposedClone(self.cnv.ANCHOR, self.cnv.SCALE)
        pointB = self.pointB.transposedClone(self.cnv.ANCHOR, self.cnv.SCALE)
        c.create_line((*pointA.get(), *pointB.get()), fill=self.color,
            width=self.stroke)


class Circle(Element):
    '''Filled circle with center in specified point'''
    def __init__(self, point, drawMode='FILL'):
        super().__init__()
        self.point = Point(*point)
        self._handleDrawMode(drawMode)
    def draw(self):
        c = self.cnv.canvas
        point = self.point.transposedClone(self.cnv.ANCHOR, self.cnv.SCALE)
        bound1 = point.shiftedClone(Point(-self.stroke, -self.stroke))
        bound2 = point.shiftedClone(Point(self.stroke, self.stroke))
        if self.drawMode == 'FILL':
            c.create_arc(*bound1.get(), *bound2.get(), fill=self.color,
                width=self.stroke, extent=359, outline='')
        elif self.drawMode == 'STROKE':
            c.create_arc(*bound1.get(), *bound2.get(), outline=self.color,
                width=self.stroke, extent=359, fill='')


class Vector(Line): # TODO
    '''Drawable vector. Needs optimalization'''
    ARROW_LEN_FRAC = 0.175
    ARROW_LEN_MAX = 3.5
    ARROW_ANGLE = 15
    def draw(self, isArrow=False):
        # print('Dict {\n '+'\n '.join([f'{k}: {v}' for k, v in self.__dict__.items()])+'\n}')
        super().draw()
        if not isArrow:
            mag, angle = self.getMag(), self.getAzimuth()
            angle = angle + 180 % 360
            arrowAngle = Vector.ARROW_ANGLE
            arrowLength = mag * Vector.ARROW_LEN_FRAC
            if arrowLength > Vector.ARROW_LEN_MAX: arrowLength = Vector.ARROW_LEN_MAX
            arrow1 = Vector.polar(self.pointB, angle+arrowAngle, arrowLength)
            arrow1.reInit(self.cnv)
            arrow2 = Vector.polar(self.pointB, angle-arrowAngle, arrowLength)
            arrow2.reInit(self.cnv)
            arrow1.draw(isArrow=True)
            arrow2.draw(isArrow=True)
    @classmethod
    def polar(cls, pointA, angle, mag):
        obj = cls.__new__(cls)
        obj.pointA = pointA
        x = cos(radians(angle)) * mag + obj.pointA.x
        y = sin(radians(angle)) * mag + obj.pointA.y
        obj.pointB = Point(x, y)
        return obj
    def scale(self, scalar):
        mag, angle = self.getMag(), self.getAzimuth()
        new = Vector.polar(self.pointA, angle, mag*scalar)
        self.pointB = new.pointB
    def getAzimuth(self):
        pt1 = self.pointA.clone()
        pt2 = self.pointB.clone()
        delta = Point(pt2.x-pt1.x, pt2.y-pt1.y)
        theta = atan2(delta.x, delta.y)
        theta = - theta - 1.5 * PI
        while theta < 0: theta += 2 * PI
        return degrees(theta)
    def getMag(self):
        pt1 = self.pointA.clone()
        pt2 = self.pointB.clone()
        delta = Point(pt2.x-pt1.x, pt2.y-pt1.y)
        return sqrt(delta.x**2 + delta.y**2)
