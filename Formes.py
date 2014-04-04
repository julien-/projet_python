

class Formes:
    
    def __init__(self, nom):
        self._nom = nom
        
    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        self._nom = nom
        
    nom = property (_get_nom, _set_nom)
    
    def write(self, canvas, p1, p2): pass
        #print("DESSIN")
        #print("Nom : " + self._nom)
    
    def translation(self): pass #pass c'est quand une fonction ne fait rien (virtuelle pure en gros)