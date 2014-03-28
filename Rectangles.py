'''
Created on 3 fevr. 2014

@author: collet18u
'''

from FormesSimples import FormesSimples

class Rectangles(FormesSimples):

    def __init__(self, nom, point, couleur, longueur, largeur, ):
        super(Rectangles,self).__init__(nom, point, couleur)
        self._longueur = longueur
        self._largeur = largeur
        
    def _get_longueur(self):
        return self._longueur

    def _set_longueur(self, longueur):
        self._longueur = longueur

    longueur = property (_get_longueur, _set_longueur)
    
    def _get_largeur(self):
        return self._largeur

    def _set_largeur(self, largeur):
        self._largeur = largeur

    largeur = property (_get_largeur, _set_largeur)
    
        
    def write(self):
        super().write()
        