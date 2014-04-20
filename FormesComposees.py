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
    
    def _get_nbFormes(self):
        return self._nbFormes

    def _set_nbFormes(self, nbFormes):
        self._nbFormes = nbFormes

    nbFormes = property (_get_nbFormes, _set_nbFormes)
    
    def _ajouter_forme(self, forme):
        self._nbFormes = self._nbFormes + 1
        self._listeforme.append(forme)
    
    def _presence_forme(self, forme):    
        for i in range (self._nbFormes):
            if(self._listeforme[i]._get_id() == forme._get_id()):
                return 1
        return 0
        
    def write(self):
        super().write()
        print (" * Formes dans ce groupe: ")
        i = 0
        for i in range (self._nbFormes):
            print(self._listeforme[i]._get_nom())
    