from FormesSimples import FormesSimples

class Polygones(FormesSimples):
 
    numero = 0
    def __init__(self, nom, point1, point2, couleur, nbpoints, tabpoints):
        super(Polygones,self).__init__(nom, point1, point2, couleur)
        self._nbpoints = nbpoints
        self._tabpoints = tabpoints

    def _get_nbpoints(self):
        return self._nbpoints

    def _set_nbpoints(self, nbpoints):
        self._nbpoints = nbpoints

    nbpoints = property (_get_nbpoints, _set_nbpoints)
    
    def _get_tabpoints(self):
        return self._tabpoints

    def _set_tabpoints(self, tabpoints):
        self._tabpoints = tabpoints

    tabpoints = property (_get_tabpoints, _set_tabpoints)
    
    def maj(self, p1, p2, nbpoints, tabpoints):       
        super().maj(p1, p2)
        self._set_nbpoints(nbpoints)
        self._set_tabpoints(tabpoints)
    
    def write(self):
        super().write()
        
        i = 0
        j = 3
        while (i < len(self._tabpoints)-1):
            print("Point" + str(j) + " : " + str(self._tabpoints[i]) + "," + str(self._tabpoints[i+1]))
            i = i+2
            j = j+1
            
    def translation(self, x, y):
        super().translation(x, y)
        
        #i = 0
        #while (i < len(self._tabpoints)-1):
            #self._tabpoints[i] = self.tabpoints[i] + x
            #self._tabpoints[i+1] = self.tabpoints[i] + y
            #i = i+2
        