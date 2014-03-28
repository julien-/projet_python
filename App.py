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
        #id de la forme selectionnee
        self.iid = -1;
        
        # Coordonnee de la forme selectionnee
        self.x = 0
        self.y = 0
        
        # Fenetre
        self.root = root
        self.root.title("Formes")
        self.map = {}
        
        # Barre d'outils
        toolbar = Frame(root)
        toolbar.pack(expand =YES, fill =X, side =TOP)
        self.nbCercle = 0
        self.nbRectangle = 0
        propriete = Frame(root)
        propriete.pack(expand =YES, fill =X, side =RIGHT)
        self.color_name = 'white'
        rows = []
        cols = []
        
        # Labels a droite
        ln = Label(propriete, relief=RIDGE, text ='Nom')
        self.en = Entry(propriete, relief=RIDGE)
        ln.grid(row=0, column=0, sticky=NSEW)
        self.en.grid(row=0, column=1, sticky=NSEW)
        self.en.insert(END, '')
        
        lc = Label(propriete, relief=RIDGE, text ='Couleur')
        self.ec = Entry(propriete, relief=RIDGE)
        lc.grid(row=1, column=0, sticky=NSEW)
        self.ec.grid(row=1, column=1, sticky=NSEW)
        self.ec.insert(END, '')
        self.bc = Button(propriete, text='...', command=self.changerCouleur)
        self.bc.grid(row=1, column=2, sticky=NSEW)
        
        lpx = Label(propriete, relief=RIDGE, text ='Point (X)')
        self.epx = Entry(propriete, relief=RIDGE)
        lpx.grid(row=2, column=0, sticky=NSEW)
        self.epx.grid(row=2, column=1, sticky=NSEW)
        self.epx.insert(END, '')
        
        lpy = Label(propriete, relief=RIDGE, text ='Point (Y)')
        self.epy = Entry(propriete, relief=RIDGE)
        lpy.grid(row=3, column=0, sticky=NSEW)
        self.epy.grid(row=3, column=1, sticky=NSEW)
        self.epy.insert(END, '')
        
        cols.append(self.en)
        cols.append(self.ec)
        cols.append(self.epx)
        cols.append(self.epy)
        rows.append(cols)
            
        # Boutons du haut
        self.bouton = [None]*3
        self.photos = [None]*3
        
        self.photos[0] = PhotoImage(file = 'images/cercle.png');
        self.bouton[0] = Button(toolbar, image = self.photos[0], relief =GROOVE, command = self.dessiner_ellipse)
        self.bouton[0].pack(side =LEFT)
        
        self.photos[1] = PhotoImage(file = 'images/rectangle.png');
        self.bouton[1] = Button(toolbar, image = self.photos[1], relief =GROOVE, command = self.dessiner_rectangle)
        self.bouton[1].pack(side =LEFT)
        
        self.photos[2] = PhotoImage(file = 'images/polygone.png');
        self.bouton[2] = Button(toolbar, image = self.photos[2], relief =GROOVE, command = lambda x = Polygones("Polygone 1", Point(1,1), "rouge", 2, [Point(5, 4), Point(8, 6)]):self.dessiner_polygone(x))
        self.bouton[2].pack(side =LEFT)
        
        # Canvas
        w = 640
        h = 480
        self.cv = Canvas(width=w, height=h, bg='black')
        self.colorList = ["blue", "red", "green", "white", "yellow", "magenta", "orange"]
        self.cv.bind('<Button-1>', self.on_click)
        self.cv.bind("<Button1-Motion>", self.mouseMove)
        self.en.bind('<Return>', self.valider)
        self.epx.bind('<Return>', self.valider)
        self.epy.bind('<Return>', self.valider)
        self.cv.pack()
               
    def changerCouleur(self):
        color = colorchooser.askcolor()
        self.color_name = color[1]
        self.bc.configure(background=self.color_name)
        print(self.color_name)
        
    def valider(self, event):
        if (self.iid != -1):
            
            self.cv.delete(root,self.iid) 
            del self.map[self.iid]
            self.root.update()
            
            forme = Rectangles(self.en.get(), Point(self.epx.get(), self.epy.get()),55, 55, "bleu");
            r = random.randint(50, 100)
            idForme = self.cv.create_rectangle(self.epy.get(),  self.epx.get(), self.x+r, self.y+r, fill=self.color_name)
            self.root.update()
            self.x1, self.y1 =self.epx.get(), self.epy.get()
            self.map[idForme] = forme
            self.iid = idForme
        
    def mouseMove(self, event):
        
        items = self.cv.find_withtag('current')
        x2, y2 = event.x, event.y
        dx, dy = x2 -self.x1, y2 -self.y1
        #Si on selectionne une forme
        if len(items) and (y2 > 90) and (y2 < 400):
            self.iid = items[0] 
            self.cv.move(self.iid, dx, dy)
            self.x1, self.y1 = x2, y2
            self.map[items[0]]._set_point(Point(self.x1, self.y1))
            self.epx.delete(0,END)
            self.epx.insert(END, self.map[self.iid]._get_point()._get_x().__str__())
            self.epy.delete(0,END)
            self.epy.insert(END, self.map[self.iid]._get_point()._get_y().__str__())
            
    def on_click(self, event):
        self.x1, self.y1 = event.x, event.y
        self.iid = -1;
        items = self.cv.find_withtag('current')
        #Selection d'une forme
        if len(items):
            self.iid = items[0] 
            self.en.delete(0,END)
            self.en.insert(END, self.map[self.iid]._get_nom())
            self.ec.delete(0,END)
            self.ec.insert(END, self.map[self.iid]._get_couleur())
            self.epx.delete(0,END)
            self.epx.insert(END, self.map[self.iid]._get_point()._get_x().__str__())
            self.epy.delete(0,END)
            self.epy.insert(END, self.map[self.iid]._get_point()._get_y().__str__())
            print ("MAP: ", self.map)
            print ("ID: ", self.iid.__str__())
            self.map[self.iid].write()
 
    def dessiner_ellipse(self):
        print("ellipse")
        
    def dessiner_rectangle(self):
        forme = Rectangles("", Point(1,1), 18, 27, "bleu");
        self.nbRectangle = self.nbRectangle + 1
        r = random.randint(50, 100)
        color = random.choice(self.colorList)
        idForme = self.cv.create_rectangle(320, 240, self.x+r, self.y+r, fill=color)
        self.root.update()
        self.x1, self.y1 =320, 240
        forme._set_nom("Rectangle "+self.nbRectangle.__str__())
        forme._set_couleur(color)
        forme._set_point(Point(320, 240));
        self.map[idForme] = forme
        self.map[idForme].write()      
        
root = Tk()
app = App(root)
root.mainloop()

