from Formes import Formes

class FormesComposees(Formes):

    def __init__(self, nom, listeforme):
        super(FormesComposees,self).__init__(nom)
        self._listeforme = listeforme
        
    def _get_listeforme(self):
        return self._listeforme

    def _set_listeforme(self, listeforme):
        self._listeforme = listeforme

    listeforme = property (_get_listeforme, _set_listeforme)
    
    def _ajouter_forme(self, id, forme):
        self._listeforme[id] = forme;
         
    def _supprimer_forme(self, id):
        del self._listeforme[id];
    
    def zoom(self, coeff):
        print ("--- ZOOM GROUPE ---")
        for id in self._listeforme:
            self._listeforme[id].zoom(coeff)
            
    def dezoom(self, coeff):
        print ("--- DEZOOM GROUPE ---")
        for id in self._listeforme:
            self._listeforme[id].dezoom(coeff)
            
    def translation(self, x, y):
        #super().translation()
        print ("--- TRANSLATION GROUPE ---")
        for id in self._listeforme:
            self._listeforme[id].translation(x, y)
        
    def write(self):
        super().write()
        print (" * Formes dans ce groupe: ")
        for i in self._listeforme:
            self._listeforme[i].write()
    
    def getForme(self, id):
        return self._listeforme[id]