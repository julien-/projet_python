from Rectangles import Rectangles
class dessinerRectangle:
    def __init__(self, canvas, _forme):
        pass
    
    def dessiner(self, canvas, _forme):
        if (type(_forme) is Rectangles):
            return True, canvas.create_rectangle(_forme._get_point1().x , _forme._get_point1().y , _forme._get_point2().x, _forme._get_point2().y, fill=_forme.couleur)
        else:
            return False, None