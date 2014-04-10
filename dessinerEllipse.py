from Ellipses import Ellipses
class dessinerEllipse:
    #Classe appelee par la fabrique
    def __init__(self, canvas, _forme):
        pass
    
    def dessiner(self, canvas, _forme):
        print (type(_forme))
        if (type(_forme) is Ellipses):
            print ("dessinerEllipse")
            return True, canvas.create_oval(_forme._get_point1().x , _forme._get_point1().y , _forme._get_point2().x, _forme._get_point2().y, fill=_forme.couleur)        
        else:
            return False, None