'''
Created on 3 fevr. 2014

@author: collet18u
'''

from Formes import Formes

class FormesSimples(Formes):

    def __init__(self, nom, point, couleur):
        super(FormesSimples,self).__init__(nom, point)
        self._couleur = couleur  
        
    def _get_couleur(self):
        return self._couleur

    def _set_couleur(self, couleur):
        self._couleur = couleur

    couleur = property (_get_couleur, _set_couleur)
    
    def write(self):
        super().write()
          