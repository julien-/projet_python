from FormesSimples import FormesSimples

class Rectangles(FormesSimples):
    #numero de Rectangle pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, id, point1, point2, couleur):
        super(Rectangles,self).__init__(nom, id, point1, point2, couleur)