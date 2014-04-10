from Polygones import Polygones
class dessinerPolygone:
    def __init__(self, canvas, _forme):
        pass
    
    def dessiner(self, canvas, _forme):
        print (type(_forme))
        if (type(_forme) is Polygones):
            print ("ellipseeeeeee")
            return True, canvas.create_polygon(_forme._get_point1().x , _forme._get_point1().y , _forme._get_point2().x, _forme._get_point2().y, _forme._get_tabpoints(), fill=_forme.couleur)        
        else:
            return False, None
