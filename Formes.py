class Formes:
    
    def __init__(self, nom):
        self._nom = nom
        self._groupe = -1
        
    def _get_nom(self):
        return self._nom

    def _set_nom(self, nom):
        self._nom = nom
        
    nom = property (_get_nom, _set_nom)
    
    def write(self): pass
    
    def maj(self): pass
    
    def translation(self): pass
    
    def zoom(self): pass
    
    def selectionner(self, canvas, id): pass