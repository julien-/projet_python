from FormesSimples import FormesSimples

class Segments(FormesSimples):
    #numero du segment pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Segments,self).__init__(nom, point1, point2, couleur)