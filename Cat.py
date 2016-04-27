__author__ = 'zhengxiaoyu'
from Vector import *
from Color import *
from Turtle import *
class Cat(Turtle):       #### Inherit behavior from Turtle
    """This turtle walks in a straight line forever.
    >>> from Mouse import *
    >>> from Status import *
    >>> little_mouse = Mouse(Vector(345,350), 1, 1)
    >>> status = Status(Vector(450,350), 1)
    >>> cat = Cat(Vector(800,350), 1 ,little_mouse)
    >>> round(cat.getnextstate()[0].x,3)
    >>> 799.924
    >>> round(cat.getshape()[0].y,3)
    >>> 358.012
    >>> cat.distance_to_r()
    >>> 350.0
    >>> cat.get_cat_degree()
    >>> 0.0
    >>> cat.get_mouse_degree()
    >>> 180.0
    >>> cat.eat_mouse()
    >>> False
    >>> cat.see_the_mouse(cat.get_cat_degree(), cat.get_mouse_degree(), cat.distance_to_r())
    >>> False
    >>> cat.see_the_mouse(35, 396, 100)
    >>> False
    >>> cat.see_the_mouse(0, 45, 810)
    >>> True
    >>> cat.see_the_mouse(150, 240, 810)
    >>> False
    >>> cat.see_the_mouse(0, -57, 400)
    >>> True
    >>> round(cat.rotate()[0].x,3)
    >>> 799.924
    >>> round(cat.towards_circle()[0].x,3)
    >>> 798.333
    """
    Mouse = None
    def __init__(self, position, heading, mouse, fill=yellow, **style):
        '''
        init the cat object and assign the mouse class atttribute
        '''
        Turtle.__init__(self, position, heading, fill=fill,outline=yellow, **style)
        Cat.Mouse = mouse

        self.degree = 0

    def rotate(self):
        '''
        :return rotate 1.25/60 radians per second
        '''
        return self.position.counterclockwise(Vector(450,350), 1.25/60.0), 0

    def towards_circle(self):
        '''
        :return: forward to the status 1/60 meter per second
        '''
        if self.distance_to_r()<=100:
            return self.rotate()
        return self.position + (Vector(450, 350) - self.position).unit()*(100.0/60.0), 0

    def get_cat_degree(self):
        '''
        :return the cat's degree considering the status's coordinate
        '''
        cat_degree = self.position.degree(Vector(450,350))
        self.degree = cat_degree
        return cat_degree

    def get_mouse_degree(self):
        '''
        :return: the mouse's degree considering the status's coordinate
        '''
        mouse_degree = Cat.Mouse.position.degree(Vector(450,350))
        Cat.Mouse.degree = mouse_degree
        return mouse_degree

    def see_the_mouse(self,cat_degree,mouse_degree,r):
        '''
        :return: whether the cat can see the mouse
        '''
        return r * cos(((cat_degree % 360) - (mouse_degree % 360))*pi/180) > 100

    count = 60
    def getnextstate(self):
        '''
        :return next state
        '''
        if self.eat_mouse():
            Cat.Mouse.dead = True
            return self.position, 0

        if self.see_the_mouse(self.get_cat_degree(), self.get_mouse_degree(), self.distance_to_r()):
            if Cat.count == 60:
                Cat.count = 0
        if Cat.count < 60:
            Cat.count += 1
            return self.towards_circle()
        Cat.old_angle = self.get_cat_degree()
        return self.rotate()

    def distance_to_r(self):
        '''
        :return: return the cat radius
        '''
        self.r = Vector(450, 350).distance(self.position)
        if self.r < 90:
            self.position = Vector(600,350)
            self.r = Vector(450, 350).distance(self.position)
        return self.r

    old_angle = 0
    def eat_mouse(self):
        '''
        :return: whether the cat eat the mouse
        '''

        if self.position.distance(Cat.Mouse.position)<=15:
            if  cos(self.get_mouse_degree() - Cat.old_angle) > cos(self.get_cat_degree() - Cat.old_angle)\
                    and  cos(self.get_cat_degree() - self.get_mouse_degree()) > cos(self.get_cat_degree() - Cat.old_angle):
                return True
            else: return False
        return False

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        result_list = [self.position + Vector(10*cos(i),10*sin(i)) for i in range(-180,180)]
        return result_list