'''
Created on 17 mars 2014

@author: collet18u
'''

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
    
    def write(self):
        super().write()
        print (" * Formes dans ce groupe: ")
        i = 0
        for i in range (self._nbFormes):
            self._listeforme[i].write()