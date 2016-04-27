__author__ = 'zhengxiaoyu'
from Turtle import Turtle
from Vector import *
from Color import *

class Mouse(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever.
    >>> mouse = mouse(Vector(450,350),1)
    >>> mouse.getnextstate()[0].x
    >>> 345.0
    >>> round(mouse.getshape()[0].y,3)
    >>> 351.750
    """


    def __init__(self, position, heading, angle, fill=blue, **style):
        '''
        init the mouse
        '''
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.angle =  float(angle)/60
        self.dead = False
        self.degree = 0

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        return [self.position + Vector(0,5),
                self.position - Vector(5,0),
                self.position - Vector(0,5),
                self.position + Vector(5,0)]


    def getnextstate(self):
        '''
        :return the shape of the mouse
        '''
        if self.dead:
            return self.position, 0
        return self.position.counterclockwise(Vector(450,350),self.angle), 0
