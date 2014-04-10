from FormesSimples import FormesSimples

class Ellipses(FormesSimples):
    #numero d'Ellipses pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Ellipses,self).__init__(nom, point1, point2, couleur) 
      
    