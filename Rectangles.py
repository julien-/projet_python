from FormesSimples import FormesSimples
from Point import Point

class Rectangles(FormesSimples):
     #numero de Rectangle pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Rectangles,self).__init__(nom, point1, point2, couleur)
        
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
    
        
    def write(self, canvas, p1, p2):
        super().write(canvas, p1, p2)
        
        #return canvas.create_rectangle(self._get_point1().x , self._get_point1().y , self._get_point2().x, self._get_point2().y, fill=self.couleur)