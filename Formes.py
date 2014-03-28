'''
Created on 3 fevr. 2014

@author: collet18u
'''

class Formes:
    
    def __init__(self, nom, point):
        self._nom = nom
        self._point = point
        
    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        self._nom = nom
        
    def _get_point(self):
        return self._point

    def _set_point(self, point):
        self._point._set_x(point._get_x());
        self._point._set_y(point._get_y());
        
    nom = property (_get_nom, _set_nom)
        
    def write(self):
        print("Nom : " + self._nom)    
        print("Point : " + self._point._get_x().__str__())