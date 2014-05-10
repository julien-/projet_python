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
    
    def maj(self, p1, p2):
        super().maj()
        
        self._set_couleur(self.couleur);
        self._set_point1(Point(p1._get_x(), p1._get_y()));
        self._set_point2(Point(p2._get_x(), p2._get_y()));
        
    def write(self):
        super().write()
        print("nom = " + self._get_nom() + " Point1 = (" + self._get_point1().x.__str__() + "," + self._get_point1().y.__str__() + ") Point2 = (" + self._get_point2().x.__str__() + "," + self._get_point2().y.__str__() +")")
    
    def translation(self, x, y):
        super().translation()
        #Modif des points
        self._point1 = Point(self._point1._get_x() + x, self._point1._get_y() + y)
        self._point2 = Point(self._point2._get_x() + x, self._point2._get_y() + y)
    
    def zoom(self, action, coef):
        super().zoom()
        if(action):
            #Modif des points
            AModifX = round( ((self._get_largeur() * coef) - self._get_largeur()) / 2 , 0)
            AModifY = round( ((self._get_hauteur() * coef) - self._get_hauteur()) / 2 , 0 )
            
            self._point1 = Point(self._point1._get_x() - AModifX, self._point1._get_y() - AModifY)
            self._point2 = Point(self._point2._get_x() + AModifX, self._point2._get_y() + AModifY)
        else:
            #Modif des points
            AModifX = round( ((self._get_largeur() / coef) - self._get_largeur()) / 2 , 0)
            AModifY = round( ((self._get_hauteur() / coef) - self._get_hauteur()) / 2 , 0 )
            
            self._point1 = Point(self._point1._get_x() - AModifX, self._point1._get_y() - AModifY)
            self._point2 = Point(self._point2._get_x() + AModifX, self._point2._get_y() + AModifY)
        
        
    def _get_hauteur(self):
        return round(abs(self._point1._get_y() - self._get_point2()._get_y()), 0)
    
    def _get_largeur(self):
        return round(abs(self._point1._get_x() - self._get_point2()._get_x()), 0)
    
    def _get_milieu(self):
        #X
        if self._point1._get_x() < self._point2._get_x() :
            x = self._point1._get_x() + self._get_largeur() / 2
        else:
            x = self._point2._get_x() + self._get_largeur() / 2
        #Y
        if self._point1._get_y() < self._point2._get_y() :
            y = self._point1._get_y() + self._get_hauteur() / 2
        else:
            y = self._point2._get_y() + self._get_hauteur() / 2
        
        return Point(x, y)
