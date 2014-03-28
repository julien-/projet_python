'''
Created on 3 fevr. 2014

@author: collet18u
'''

from FormesSimples import FormesSimples

class Ellipses(FormesSimples):
    
    def __init__(self, nom, point, couleur, point2):

            super(Ellipses,self).__init__(nom, point, couleur)
            self._point2 = point2
  
    
    def _get_point2(self):
        return self._point2

    def _set_point2(self, point2):
        self._point2 = point2

    point2 = property (_get_point2, _set_point2)
    

        
    def write(self):
        super().write()
        forme = Ellipses("", Point(1,1), 'blanc', Point(1,1))
        self.nbCercle = self.nbCercle + 1
        r = random.randint(50, 100)
        color = random.choice(self.colorList)
        idForme = self.cv.create_oval(320, 240, self.x+r, self.y+r, fill=color)
        self.root.update()
        self.x1, self.y1 =320, 240
        forme._set_nom("Cercle "+self.nbCercle.__str__())
        forme._set_couleur(color);
        forme._set_point(Point(320, 240));
        self.map[idForme] = forme