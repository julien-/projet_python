import random
import time
import os
from tkinter import *
from tkinter import colorchooser

from Ellipses import Ellipses
from Point import Point
from Polygones import Polygones
from Rectangles import Rectangles


from Formes import Formes;


class App:
    
    def __init__(self, root):
        #Liste des formes crees
        self.map = {}
        
        # Fenetre
        self.root = root
        self.root.title("Formes")
        
        # Barre d'outils
        toolbar = Frame(root)
        toolbar.pack(expand =YES, fill =X, side =TOP)
        propriete = Frame(root)
        propriete.pack(expand =YES, fill =X, side =RIGHT)
        self.color_name = 'white'
        rows = []
        cols = []
        self.forme_active = None
        self.idForme = None
        self.zoom = 0;
        
        # Labels a droite
        ln = Label(propriete, relief=RIDGE, text ='Nom')
        ln.grid(row=0, column=0, sticky=NSEW)
        self.Valeur_entry_nom = StringVar()
        self.entry_droite_name = Entry(propriete, relief=RIDGE, textvariable = self.Valeur_entry_nom)
        self.entry_droite_name.grid(row=0, column=1, sticky=NSEW)
        
        lc = Label(propriete, relief=RIDGE, text ='Couleur de la forme')
        lc.grid(row=1, column=0, sticky=NSEW)
        self.Valeur_entry_couleur = StringVar()
        self.entry_droite_couleur = Entry(propriete, relief=RIDGE, textvariable = self.Valeur_entry_couleur)
        self.entry_droite_couleur.grid(row=1, column=1, sticky=NSEW)
        
        self.bc = Button(propriete, text='...', command=self.changerCouleur)
        self.bc.grid(row=1, column=2, sticky=NSEW)
        
        lp1 = Label(propriete, relief=RIDGE, text ='Point1 (X,Y)')
        lp1.grid(row=2, column=0, sticky=NSEW)
        self.Valeur_entry_point1 = StringVar()
        self.entry_droite_point1 = Entry(propriete, relief=RIDGE, textvariable = self.Valeur_entry_point1)
        self.entry_droite_point1.grid(row=2, column=1, sticky=NSEW)
        
        
        lp2 = Label(propriete, relief=RIDGE, text ='Point2 (X,Y)')
        lp2.grid(row=3, column=0, sticky=NSEW)
        self.Valeur_entry_point2 = StringVar()
        self.entry_droite_point2 = Entry(propriete, relief=RIDGE, textvariable = self.Valeur_entry_point2)
        self.entry_droite_point2.grid(row=3, column=1, sticky=NSEW)
        
        lz = Label(propriete, relief=RIDGE, text ='Zoom')
        lz.grid(row=4, column=0, sticky=NSEW)
        self.Valeur_entry_zoom = StringVar()
        self.Valeur_entry_zoom.set( self.zoom.__str__())
        self.entry_droite_zoom = Entry(propriete, relief=RIDGE, textvariable = self.Valeur_entry_zoom)
        self.entry_droite_zoom.grid(row=4, column=1, sticky=NSEW)
        
        cols.append(self.entry_droite_name)
        cols.append(self.entry_droite_couleur)
        cols.append(self.entry_droite_point1)
        cols.append(self.entry_droite_point2)
        rows.append(cols)
            
        # Boutons du haut
        self.bouton = [None]*3
        self.photos = [None]*3
        
        self.photos[0] = PhotoImage(file = 'images/cercle.png');
        self.bouton[0] = Button(toolbar, image = self.photos[0], relief =GROOVE, command = self.clic_btn_ellipse)
        self.bouton[0].pack(side =LEFT)
        
        self.photos[1] = PhotoImage(file = 'images/rectangle.png');
        self.bouton[1] = Button(toolbar, image = self.photos[1], relief =GROOVE, command = self.clic_btn_rectangle)
        self.bouton[1].pack(side =LEFT)
        
        self.photos[2] = PhotoImage(file = 'images/polygone.png');
        self.bouton[2] = Button(toolbar, image = self.photos[2], relief =GROOVE, command = lambda x = Polygones("Polygone 1", Point(1,1), Point(2,2), "rouge", 2, [Point(5, 4), Point(8, 6)]):self.dessiner_polygone(x))
        self.bouton[2].pack(side =LEFT)
        
        # Canvas
        self.cv = Canvas(width=640, height=480, bg='black')
        #self.colorList = ["blue", "red", "green", "white", "yellow", "magenta", "orange"]
        #Gestion des clics
        self.mouse_pressed = False
        self.cv.bind("<ButtonPress-1>", self.onMouseClic)
        self.cv.bind("<ButtonRelease-1>", self.onMouseUp)
        self.cv.bind("<Button1-Motion>", self.onMouseMove)
        self.cv.bind("<ButtonPress-3>", self.onClicZoom)
        self.cv.bind("<Button3-Motion>", self.onZoomMove)
        #Entry
        self.entry_droite_name.bind('<Return>', self.modifByEdit)
        self.entry_droite_point1.bind('<Return>', self.modifByEdit)
        self.entry_droite_point2.bind('<Return>', self.modifByEdit)
        self.cv.pack()
               
    def changerCouleur(self):
        color = colorchooser.askcolor()
        self.color_name = color[1]
        self.entry_droite_couleur.configure(background=self.color_name)
        print("Changement de couleur entry_droite_name : ",self.color_name)
        
    def modifByEdit(self, event):
        #active les ENTRY si une forme est selectionne
         
        if(self.forme_active._get_nom() != ""):
            self.cv.delete(root,self.forme_active)
            del self.map[self.idForme]
            self.root.update()  
            forme = Formes(self.entry_droite_name.get());
            r = random.randint(50, 100)
            idForme = self.cv.create_rectangle(self.entry_droite_point2.get(),  self.entry_droite_point1.get(), self.x+r, self.y+r, fill=self.color_name)
            self.root.update()
            self.x1, self.y1 =self.entry_droite_point1.get(), self.entry_droite_point2.get()
            self.map[idForme] = forme
            self.forme_active = idForme
            
    def majEntry(self):
        if(self.idForme is not None):
            self.Valeur_entry_nom.set(self.map[self.idForme]._get_nom())
            self.Valeur_entry_couleur.set(self.map[self.idForme]._get_couleur())
            self.Valeur_entry_point1.set(self.map[self.idForme]._get_point1()._get_x().__str__() + "," + self.map[self.idForme]._get_point1()._get_y().__str__())
            self.Valeur_entry_point2.set(self.map[self.idForme]._get_point2()._get_x().__str__() + "," + self.map[self.idForme]._get_point2()._get_y().__str__())
        if(self.zoom > 0):
            self.Valeur_entry_zoom.set("+" + self.zoom.__str__())
        else:
            self.Valeur_entry_zoom.set(self.zoom.__str__())
        
    def onMouseClic(self, event):
        items = self.cv.find_withtag('current')
        self.ClicGauche_depart = Point(event.x, event.y)
        
        #on deselectionne la forme active actuelle (suppression du contour)
#A FAIRE        
        
        if len(items):
            print("selection forme")
            
            self.idForme = items[0]
            self.forme_active = self.map[self.idForme]
            
            #dessiner le contour de selection
            
            print ("MAP: " + self.map.__str__())
            print ("ID: " + self.idForme.__str__())
            
            print ("NOM: " +  self.forme_active._get_nom())
        else:
            print("dessinDown")
            try:
                #id de la forme sur le canvas
                self.idForme = self.forme_active.write(self.cv, Point(event.x, event.y), Point(event.x,event.y) )
                self.map[self.idForme] = self.forme_active
                
            except:pass  #ne rien faire quand aucune action est selectionnee (clic dans le vide)
        self.majEntry()
        self.root.update()

    def onMouseUp(self, event):
        print("lache")
        
    #bouge la souris + clic gauche
    def onMouseMove(self, event):
        self.ClicGauche_fin = Point(event.x, event.y)
        print("DEPART: "+ self.ClicGauche_depart._get_x().__str__() + ", " + self.ClicGauche_depart._get_y().__str__())
        print("FIN: "+ self.ClicGauche_fin._get_x().__str__() + ", " + self.ClicGauche_fin._get_y().__str__())
        
        #Recupere la forme selectionnee
        items = self.cv.find_withtag('current')
        #Si on selectionne une forme
        if len(items):
            x_vecteur, y_vecteur = self.ClicGauche_fin.x - self.ClicGauche_depart.x , self.ClicGauche_fin.y - self.ClicGauche_depart.y   #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
        
            #MAJ Canvas
            self.cv.move(self.idForme, x_vecteur, y_vecteur)
            print ("MAPmoove: " + self.map.__str__())
            print ("IDmoove: " + self.idForme.__str__())
            
            print ("NOMmoove: " +  self.forme_active._get_nom())
            print("VECTEURmoove: ("+ x_vecteur.__str__() +"," +y_vecteur.__str__()+")")
            print("EVENTmoove: ("+ event.x.__str__() +"," + event.y.__str__()+")")
            
            
            #MAJ OBJET
            self.ClicGauche_depart = self.ClicGauche_fin
            self.map[self.idForme].translation(x_vecteur, y_vecteur)
            
            self.majEntry()
        else:
            print("dessinMove")
            
            #modifie le dessin
            
            try:
                print("NOMdown:" + self.forme_active._get_nom())
                self.cv.delete(self.idForme) #supprime l'ancienne forme du canvas
                del self.map[self.idForme]  #supprime l'ancinne forme de la map
                
                self.forme_active._set_point2(Point(event.x, event.y)) #MAJ forme active
                
                self.idForme = self.forme_active.write(self.cv, self.forme_active._get_point1(), self.forme_active._get_point2() )
                
                self.map[self.idForme] = self.forme_active
                
                self.majEntry()
            except: pass #ne rien faire quand aucune action est selectionnee (clic dans le vide)
    def onClicZoom(self, event):
        print("Clic Droit")
        print ("MAP: " + self.map.__str__())
        self.ClicDroit_depart = Point(event.x, event.y)
    
    def onZoomMove(self, event):
        print("Bouge clic Droit")
        self.ClicDroit_fin = Point(event.x, event.y)
        #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
        y_vecteur = self.ClicDroit_fin.y - self.ClicDroit_depart.y
        print("zoom=" + self.zoom.__str__())
        self.zoom = self.zoom - y_vecteur
        for i in self.map: #parcours de TOUTES LES FORMES DESSINES
            print("i="+i.__str__())
           
            self.cv.delete(i) #supprime l'ancienne forme du canvas
            self.forme_active = self.map[i] #copie intermediaire (forme_active a associer au CANVAS )
            p1 = Point(self.forme_active._get_point1()._get_x() - y_vecteur , self.forme_active._get_point1()._get_y() - y_vecteur )
            p2 = Point(self.forme_active._get_point2()._get_x() + y_vecteur , self.forme_active._get_point2()._get_y() + y_vecteur )
            self.forme_active._set_point1(p1)
            self.forme_active._set_point2(p2)
            self.idForme = self.forme_active.write(self.cv, p1 , p2 )
            self.map[self.idForme] = self.forme_active
            del self.map[i]
            self.majEntry()
            self.ClicDroit_depart = self.ClicDroit_fin
#             copie = self.idForme
            
#             
        
        

        #MAJ forme active
#             self.forme_active = self.map[self.idForme]
#             print("ZOOM avant"+self.zoom.__str__())
#             x1 = self.forme_active._get_point1()._get_x()
#             print("ZOOM avant"+self.zoom.__str__())
#             print("x1 " + x1.__str__())
        
#             p1 = Point( ,)
#             p2 = Point( ,)
#             
            
# #             
            
            
#             
        #MAJ OBJET
        
        
       
            
        
        
        
        
    def clic_btn_ellipse(self):
        print("Creation Ellipse")
        self.forme_active =  Ellipses(Point(0, 0), Point(0,0), self.color_name)
        
    def clic_btn_rectangle(self):
        print("Creation Rectangle")
        self.forme_active =  Rectangles(Point(0,0), Point(0, 0), self.color_name) 
        
root = Tk()
app = App(root)
root.mainloop()

