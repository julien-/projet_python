from FormesSimples import FormesSimples

class Polygones(FormesSimples):
 
    def __init__(self, nom, point1, point2, couleur, nbpoints, tuplepoints):
        if len(tuplepoints) == nbpoints:
            super().__init__(nom, point1, point2, couleur)
            self._nbpoints = nbpoints
            self._tuplecoord = tuplepoints
        else:
            print("Erreur initialisation")

    def _get_nbpoints(self):
        return self._nbpoints

    def _set_nbpoints(self, nbpoints):
        self._nbpoints = nbpoints

    nbpoints = property (_get_nbpoints, _set_nbpoints)
    
    def _get_tuplecoord(self):
        return self._tuplecoord

    def _set_tuplecoord(self, tuplecoord):
        self._tuplecoord = tuplecoord

    tuplecoord = property (_get_tuplecoord, _set_tuplecoord)
    
    def write(self):
        super().write()
        print("Nombre de points : " + str(len(self._tuplecoord))) 
        
        i = 0
        for i in range(len(self._tuplecoord)):
            print("Coordonnee point" + str(i+1) + " : (" + str(self._tuplecoord[i]._x) + "," + str(self._tuplecoord[i]._y) + ")")