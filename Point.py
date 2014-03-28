'''
Created on 3 fevr. 2014

@author: collet18u
'''

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
       
    def _get_x(self):
        return self._x

    def _set_x(self, x):
        self._x = x
        
    x = property (_get_x, _set_x)  
        
    def _get_y(self):
        return self._y

    def _set_y(self, y):
        self._y = y
        
    y = property (_get_y, _set_y)
    
    def write(self):
        return self._x.__str__() + ',' + self._y.__str__();
        