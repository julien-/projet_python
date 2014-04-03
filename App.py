from tkinter import *
import random
import time
from Rectangles import Rectangles
from Polygones import Polygones
from Ellipses import Ellipses
from Point import Point
from Formes import Formes;
from tkinter import colorchooser


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
        self.forme_active = None;
        
        # Labels a droite
        ln = Label(propriete, relief=RIDGE, text ='Nom')
        self.entry_droite_name = Entry(propriete, relief=RIDGE)
        ln.grid(row=0, column=0, sticky=NSEW)
        self.entry_droite_name.grid(row=0, column=1, sticky=NSEW)
        self.entry_droite_name.insert(END, '')
        
        lc = Label(propriete, relief=RIDGE, text ='Couleur')
        self.entry_droite_couleur = Entry(propriete, relief=RIDGE)
        lc.grid(row=1, column=0, sticky=NSEW)
        self.entry_droite_couleur.grid(row=1, column=1, sticky=NSEW)
        self.entry_droite_couleur.insert(END, '')
        self.bc = Button(propriete, text='...', command=self.changerCouleur)
        self.bc.grid(row=1, column=2, sticky=NSEW)
        
        lpx = Label(propriete, relief=RIDGE, text ='Point1 (X,Y)')
        self.entry_droite_point1 = Entry(propriete, relief=RIDGE)
        lpx.grid(row=2, column=0, sticky=NSEW)
        self.entry_droite_point1.grid(row=2, column=1, sticky=NSEW)
        self.entry_droite_point1.insert(END, '')
        
        lpy = Label(propriete, relief=RIDGE, text ='Point2 (X,Y)')
        self.entry_droite_point2 = Entry(propriete, relief=RIDGE)
        lpy.grid(row=3, column=0, sticky=NSEW)
        self.entry_droite_point2.grid(row=3, column=1, sticky=NSEW)
        self.entry_droite_point2.insert(END, '')
        
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
        self.cv.bind("<ButtonPress-1>", self.onMouseDown)
        self.cv.bind("<ButtonRelease-1>", self.onMouseUp)
        self.cv.bind("<Button1-Motion>", self.onMouseMove)
        #Entry
        self.entry_droite_name.bind('<Return>', self.valider)
        self.entry_droite_point1.bind('<Return>', self.valider)
        self.entry_droite_point2.bind('<Return>', self.valider)
        self.cv.pack()
               
    def changerCouleur(self):
        color = colorchooser.askcolor()
        self.color_name = color[1]
        self.entry_droite_couleur.configure(background=self.color_name)
        print("Changement de couleur entry_droite_name : ",self.color_name)
        
    def valider(self, event):
        #active les ENTRY si une forme est selectionne
        
        if(self.forme_active._get_nom() != ""):
            self.cv.delete(root,self.forme_active)
            del self.map[self.forme_active]
            self.root.update()  
            forme = Formes(self.entry_droite_name.get());
            r = random.randint(50, 100)
            idForme = self.cv.create_rectangle(self.entry_droite_point2.get(),  self.entry_droite_point1.get(), self.x+r, self.y+r, fill=self.color_name)
            self.root.update()
            self.x1, self.y1 =self.entry_droite_point1.get(), self.entry_droite_point2.get()
            self.map[idForme] = forme
            self.forme_active = idForme
    
    def onMouseDown(self, event):
        self.mouse_pressed = True
        
        self.clic_depart = Point(event.x, event.y)

        items = self.cv.find_withtag('current')
        
        self.root.update()
        
        if len(items):
            print("selection forme")
            self.forme_active = items[0]
            #Mise a jour des ENTRY
            self.entry_droite_name.delete(0,END)
            self.entry_droite_name.insert(END, self.map[self.forme_active]._get_nom())
            self.entry_droite_couleur.delete(0,END)
            self.entry_droite_couleur.insert(END, self.map[self.forme_active]._get_couleur())
            self.entry_droite_point1.delete(0,END)
            self.entry_droite_point1.insert(END, self.map[self.forme_active]._get_point1()._get_x().__str__() + "," + self.map[self.forme_active]._get_point1()._get_y().__str__())
            self.entry_droite_point2.delete(0,END)
            self.entry_droite_point2.insert(END, self.map[self.forme_active]._get_point2()._get_x().__str__() + "," + self.map[self.forme_active]._get_point2()._get_y().__str__())
            print ("MAP: ", self.map)
            print ("ID: ", self.forme_active.__str__())
        else:
            print("dessinDown")
            try:
                #id de la forme sur le canvas
                self.idForme = self.forme_active.write(self.cv, Point(event.x, event.y), Point(event.x,event.y) )
                self.map[self.idForme] = self.forme_active
                
                #Mise a jour des ENTRY
                self.entry_droite_name.delete(0,END)
                self.entry_droite_name.insert(END, self.forme_active._get_nom())
                self.entry_droite_couleur.delete(0,END)
                self.entry_droite_couleur.insert(END, self.forme_active._get_couleur())
                self.entry_droite_point1.delete(0,END)
                self.entry_droite_point1.insert(END, self.forme_active._get_point1()._get_x().__str__() + "," + self.forme_active._get_point1()._get_y().__str__())
                self.entry_droite_point2.delete(0,END)
                self.entry_droite_point2.insert(END, self.forme_active._get_point2()._get_x().__str__() + "," + self.forme_active._get_point2()._get_y().__str__())
                
                self.root.update()
            except: pass #ne rien faire quand aucune action est selectionnee (clic dans le vide)


    def onMouseUp(self, event):
        self.mouse_pressed = False
        print("lache")
        
        #modif de la forme
        
        
    
    def onMouseMove(self, event):
        #bouge la souris + clic gauche
        self.clic_fin = Point(event.x, event.y)
        #print("DEPART: "+ self.clic_depart._get_x().__str__() + ", " + self.clic_depart._get_y().__str__())
        #print("FIN: "+ self.clic_fin._get_x().__str__() + ", " + self.clic_fin._get_y().__str__())
        
        #Recupere la forme selectionnee
        items = self.cv.find_withtag('current')
        #Si on selectionne une forme
        if len(items):
            x_vecteur, y_vecteur = self.clic_fin.x - self.clic_depart.x , self.clic_fin.y - self.clic_depart.y   #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
        
            #x_nouveau, y_nouveau = event.x, event.y #nouvelles coprdonnees apres le deplacement
            #x_vecteur, y_vecteur = x_nouveau -self.x1, y_nouveau -self.y1   #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
        
            #MAJ Canvas
            self.forme_active = items[0]
            self.cv.move(self.forme_active, x_vecteur, y_vecteur)
            #print("VECTEUR: ("+ x_vecteur.__str__() +"," +y_vecteur.__str__()+")")
            #print("EVENT: ("+ event.x.__str__() +"," + event.y.__str__()+")")
            
            
            #MAJ OBJET
            self.clic_depart = self.clic_fin
            self.map[self.forme_active].translation(x_vecteur, y_vecteur)
            
            
           # self.x1, self.y1 = x_nouveau, y_nouveau
            #self.map[items[0]]._set_point1(Point(self.x1, self.y1))
            
            #Mise a jour des ENTRY
            self.entry_droite_point1.delete(0,END)
            self.entry_droite_point1.insert(END, self.map[self.forme_active]._get_point1()._get_x().__str__() + "," + self.map[self.forme_active]._get_point1()._get_y().__str__())
            self.entry_droite_point2.delete(0,END)
            self.entry_droite_point2.insert(END, self.map[self.forme_active]._get_point2()._get_x().__str__() + "," + self.map[self.forme_active]._get_point2()._get_y().__str__())
        else:
            print("dessinMove")
            
            #modifie le dessin
            
            try:
                #if(self.forme_active._get_nom() != ""):
                #print("NOMdown:" + self.forme_active._get_nom())
                self.cv.delete(self.idForme)
                #self.cv.delete("all")  #supprime l'ancienne forme du canvas
                self.cv.update() #MAJ de la fenetre
                    
                self.forme_active._set_point2(Point(event.x, event.y)) #MAJ forme active
                
                self.idForme = self.forme_active.write(self.cv, self.forme_active._get_point1(), self.forme_active._get_point2() )
                
                self.map[self.idForme] = self.forme_active
                
                #Mise a jour des ENTRY
                self.entry_droite_point1.delete(0,END)
                self.entry_droite_point1.insert(END, self.map[self.forme_active]._get_point1()._get_x().__str__() + "," + self.map[self.forme_active]._get_point1()._get_y().__str__())
                self.entry_droite_point2.delete(0,END)
                self.entry_droite_point2.insert(END, self.map[self.forme_active]._get_point2()._get_x().__str__() + "," + self.map[self.forme_active]._get_point2()._get_y().__str__())
            except: pass #ne rien faire quand aucune action est selectionnee (clic dans le vide)
       
    
    def clic_btn_ellipse(self):
        print("Creation Ellipse")
        self.forme_active =  Ellipses(Point(0, 0), Point(0,0), self.color_name)
        
    def clic_btn_rectangle(self):
        print("Creation Rectangle")
        self.forme_active =  Rectangles(Point(0,0), Point(0, 0), self.color_name) 
        
root = Tk()
app = App(root)
root.mainloop()

