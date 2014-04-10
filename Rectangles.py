from FormesSimples import FormesSimples

class Rectangles(FormesSimples):
    #numero de Rectangle pour créer le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Rectangles,self).__init__(nom, point1, point2, couleur)  
        
    def maj(self, p1, p2):       
        super().maj(p1, p2)
        
    def write(self):
        super().write()        