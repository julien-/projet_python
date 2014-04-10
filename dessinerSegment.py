from Segments import Segments
class dessinerSegment:
    def __init__(self, canvas, _forme):
        pass
    
    def dessiner(self, canvas, _forme):
        print (type(_forme))
        if (type(_forme) is Segments):
            return True, canvas.create_line(_forme._get_point1().x , _forme._get_point1().y , _forme._get_point2().x, _forme._get_point2().y, fill=_forme.couleur)
        
        else:
            return False, None