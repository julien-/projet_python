from FormesSimples import FormesSimples
from Point import Point
import random

class Ellipses(FormesSimples):
    #numero d'Ellipses pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Ellipses,self).__init__(nom, point1, point2, couleur)
        
        
                    
    def write(self, p1, p2):
        super().write(p1, p2)
        #return canvas.create_oval(self._get_point1().x , self._get_point1().y , self._get_point2().x, self._get_point2().y, fill=self.couleur)