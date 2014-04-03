from FormesSimples import FormesSimples
from Point import Point
import random

class Ellipses(FormesSimples):
    #numero d'Ellipses pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, point1, point2, couleur):
        Ellipses.numero += 1
        super(Ellipses,self).__init__("Ellipse " + Ellipses.numero.__str__(), point1, point2, couleur)
        
                    
    def write(self, canvas, p1, p2):
        super().write(canvas, p1, p2)
        
        self._set_nom("Ellipse "+Ellipses.numero.__str__())
        return canvas.create_oval(self._get_point1().x , self._get_point1().y , self._get_point2().x, self._get_point2().y, fill=self.couleur)