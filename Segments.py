from FormesSimples import FormesSimples

class Segments(FormesSimples):

   #numero du segment pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Segments,self).__init__(nom, point1, point2, couleur)
  
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
    

        
    def write(self, canvas, p1, p2):
        super().write(canvas, p1, p2)
        return canvas.create_line(self._get_point1().x , self._get_point1().y , self._get_point2().x, self._get_point2().y, fill=self.couleur)
        