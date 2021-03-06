"""
            A Point Class Definition
A two-dimensional point may be represented by an x- and y-coordinate. In this problem, you will write a Point class which stores this information and provides useful methods to work with points.

We have provided an __init__ definition for the Point class. You will note that this accepts two arguments, being the x- and y-coordinates of the point.

We have also included a __repr__ method, which will provide a canonical string representation of the point. Make sure you don’t change this method, as we will use it for some tests. Note that the output of __repr__ could be copied into the interpreter in order to create an identical point. This is a characteristic of most good __repr__ methods.

The first thing our Point class should be able to do is determine the distance between points. Write a method dist_to_point, which accepts another instance of the Point class as an argument, and returns the Euclidean distance between the two points. It may be helpful to use math.sqrt.

Using dist_to_point, now write a method is_near which returns whether two points are close. Remember that you can call other methods in a method definition using self, eg self.other_method(arg)

A point is considered ‘close’ if it is within epsilon of another point. We defined epsilon to be a really small number using scientific notation (so, eg, 1e-3 is 1x10^-3 is 0.001

Finally, we want to be able to add two points together. Write a method add_point that adds the position of the Point object given as an argument to the position of self
"""
import math
epsilon = 1e-5


class Point(object):
    """A 2D point in the cartesian plane"""
    def __init__(self, x, y):
        """
        Construct a point object given the x and y coordinates

        Parameters:
            x (float): x coordinate in the 2D cartesian plane
            y (float): y coordinate in the 2D cartesian plane
        """

        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self._x, self._y)

    
    def dist_to_point(self,point):
        delta_x = self._x - point._x
        delta_y = self._y - point._y
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    
    def is_near(self, point):
        if (self.dist_to_point(point) < epsilon):
            return True
        return False
        
    def add_point(self, point):
        self._x += point._x
        self._y += point._y