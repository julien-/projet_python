from Formes import Formes
from Point import Point

class FormesSimples(Formes):

    def __init__(self, nom, point1, point2, couleur):
        super(FormesSimples,self).__init__(nom)
        self._point1 = point1
        self._point2 = point2
        self._couleur = couleur  
    #_couleur    
    def _get_couleur(self):
        return self._couleur

    def _set_couleur(self, couleur):
        self._couleur = couleur
    #_point1
    def _get_point1(self):
        return self._point1
    
    def _set_point1(self, point):
        self._point1._set_x(point._get_x());
        self._point1._set_y(point._get_y());
    #_point2
    def _get_point2(self):
        return self._point2
    
    def _set_point2(self, point):
        self._point2._set_x(point._get_x());
        self._point2._set_y(point._get_y());
    
    couleur = property (_get_couleur, _set_couleur)
    point1 = property (_get_point1, _set_point1)
    point2 = property (_get_point2, _set_point2)
        
    def write(self, canvas, p1, p2):
        super().write(canvas, p1, p2)
        
        self._set_couleur(self.couleur);
        self._set_point1(Point(p1._get_x(), p1._get_y()));
        self._set_point2(Point(p2._get_x(), p2._get_y()));
        #print("Couleur : " + self._couleur.__str__())
        print("Point1 : " + self._point1._get_x().__str__() + "," + self._point1._get_y().__str__())
        print("Point2 : " + self._point2._get_x().__str__() + "," + self._point2._get_y().__str__())
    
    def translation(self, x, y):
        super().translation()
        #Point1
        self._point1 = Point(self._point1._get_x() + x, self._point1._get_y() + y)
        self._point2 = Point(self._point2._get_x() + x, self._point2._get_y() + y)