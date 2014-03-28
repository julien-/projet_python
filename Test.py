'''
Created on 3 fevr. 2014

@author: collet18u
'''
from FormesGeometriques import Rectangles, Polygones, Point, Triangles, Segments, Ellipses, FormesComposees

def main():
    
    '''Test Rectangle'''
    CoordHG = Point.Point(1,1)
    rectangle1 = Rectangles.Rectangles("rect1","bleu",12,4,CoordHG)
    rectangle1.write()
    print("////////////////////////////////////////////")    
    
    '''Test Triangle'''
    Point1 = Point.Point(1,2)
    Point2 = Point.Point(2,3)
    Point3 = Point.Point(3,4)
    triangle1 = Triangles.Triangles("triangle1","orange",Point1,Point2,Point3)
    triangle1.write()
    print("////////////////////////////////////////////")
    
    '''Test Segment'''
    Point1 = Point.Point(1,2)
    Point2 = Point.Point(2,3)
    segment1 = Segments.Segments("segment1","rose",Point1,Point2)
    segment1.write()
    print("////////////////////////////////////////////")
    
    '''Test Ellipse'''
    Point1 = Point.Point(1,2)
    Point2 = Point.Point(2,3)
    ellipse1 = Ellipses.Ellipses("ellipse1","rouge",Point1,Point2)
    ellipse1.write()
    print("////////////////////////////////////////////")   
     
    '''Test Polygone'''
    Point1 = Point.Point(1,2)
    Point2 = Point.Point(2,2)
    Point3 = Point.Point(3,2)
    Point4 = Point.Point(4,2)
    t = (Point1, Point2, Point3, Point4)
    polygone1 = Polygones.Polygones("polygone1","vert",4,t)
    polygone1.write()
    print("////////////////////////////////////////////")
    
    '''Test Formes Composees'''
    t1 =(segment1, ellipse1)
    groupe1 = FormesComposees.FormesComposees("Groupe1",2,t1)
    groupe1.write()
    
    
    
if __name__ == '__main__':
    main()