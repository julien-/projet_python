from FormesSimples import FormesSimples

class Ellipses(FormesSimples):
    #numero d'Ellipses pour cr�er le nom de chaque forme afin de differencier
    numero = 0
    def __init__(self, nom, point1, point2, couleur):
        super(Ellipses,self).__init__(nom, point1, point2, couleur) 
        
    def maj(self, p1, p2):       
        super().maj(p1, p2)
                    
    def write(self):
        super().write()        
    