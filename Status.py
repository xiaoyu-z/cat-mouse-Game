__author__ = 'zhengxiaoyu'
from Vector import *
from Color import *
from Turtle import *
class Status(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever.
    >>> status = Status(Vector(450,350),1)
    >>> status.getnextstate()[0].x
    >>> 450.0
    >>> round(status.getshape()[0].y,3)
    >>> 430.115
    """

    def __init__(self, position, heading, fill=black, **style):
        '''
        init the status
        '''
        Turtle.__init__(self, position, heading, fill=fill,**style)


    def getnextstate(self):
        '''
        :return the stable status
        '''
        return self.position, self.heading

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        result_list = [self.position + Vector(100*cos(i),100*sin(i)) for i in range(-180,180)]
        return result_list