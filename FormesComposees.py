from Formes import Formes

class FormesComposees(Formes):

    def __init__(self, nom, nbFormes, listeforme):
        super(FormesComposees,self).__init__(nom)
        self._listeforme = listeforme
        self._nbFormes = nbFormes 
        
    def _get_listeforme(self):
        return self._listeforme

    def _set_listeforme(self, listeforme):
        self._listeforme = listeforme

    listeforme = property (_get_listeforme, _set_listeforme)
    
    def _ajouter_forme(self, idforme):
        self._listeforme[idforme] = 1
        
    def _supprimer_forme(self, idforme):    
        del self._listeforme[idforme]
    
    def translation(self, x, y):
        super().translation()
        print ("--- TRANSLATION GROUPE ---")
        for i in self._listeforme:
            self._listeforme[i].translation(x, y)
        
    def write(self):
        super().write()
        print (" * Formes dans ce groupe: ")
        for i in self._listeforme:
            self._listeforme[i].write()