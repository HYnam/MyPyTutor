class Rectangle(object):
    def __init__(self, coords, sizex, sizey):
        self._startx, self._starty = coords
        self._sizex = sizex
        self._sizey = sizey
        
    def get_bottom_right(self):
        print('(%s, %s)' % (self._startx + self._sizex, self._starty + self._sizey))

    def move(self, pos):
        self._startx, self._starty = pos
        
    def resize(self, width, height):
        self._sizex = width
        self._sizey = height
        
    def __str__(self):
        return '((%s, %s), (%s, %s))' % (self._startx, self._starty, self._startx + self._sizex,   self._starty + self._sizey)
