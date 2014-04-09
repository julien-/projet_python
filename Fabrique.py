class Fabrique:
    def __init__(self):
        self.formes = []
        
    def ajouter_forme(self, forme):
        self.formes.append(forme)
 
    def fabriquer_forme(self, _foorme, cv):
        for forme in self.formes:
            constructeur = forme(cv, _foorme)
            resultat = constructeur.dessiner(cv, _foorme)
            if (resultat[0] == True):
                return resultat[1]