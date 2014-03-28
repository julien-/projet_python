'''
Created on 17 mars 2014

@author: collet18u
'''

from FormesSimples import FormesSimples

class Segments(FormesSimples):

    def __init__(self, nom, point, couleur, point1, point2):

            super(Segments,self).__init__(nom, point, couleur)
            self._point1 = point1
            self._point2 = point2
  
    def _get_point1(self):
        return self._point1

    def _set_point1(self, point1):
        self._point1 = point1

    point1 = property (_get_point1, _set_point1) 
    
    def _get_point2(self):
        return self._point2

    def _set_point2(self, point2):
        self._point2 = point2

    point2 = property (_get_point2, _set_point2)
    

        
    def write(self):
        super().write()
        print("Coordonnee point1 : (" + str(self._point1._x) + "," + str(self._point1._y) + ")")
        print("Coordonnee point2 : (" + str(self._point2._x) + "," + str(self._point2._y) + ")")
        