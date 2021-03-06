import random
import time
import os
from tkinter import *
from tkinter import colorchooser
from tkinter.ttk    import *    # Widgets avec 
from Ellipses import Ellipses
from Point import Point
from Polygones import Polygones
from Rectangles import Rectangles
from Segments import Segments
from Fabrique import Fabrique
from FormesComposees import FormesComposees
from copy import deepcopy

from Formes import Formes;
from dessinerRectangle import dessinerRectangle;
from dessinerEllipse import dessinerEllipse;
from dessinerSegment import dessinerSegment;
from dessinerPolygone import dessinerPolygone;

class App(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        #Liste des formes crees
        self.map = {}
        self.mapGroupe = {}
        self.nbFormes = 0
        self.PeutDessiner = FALSE
        
        self.tabpoints = [None]*2
        
        self.i = 0
        self.j = 0
        self.GroupeActif = -1
        # Fenetre
        self.root = self
        self.root.title("Formes")
        
        formes = [dessinerRectangle, dessinerEllipse, dessinerSegment, dessinerPolygone]
        self.fabrique = Fabrique()
        for forme in formes:
            self.fabrique.ajouter_forme(forme)
            
        # Barre d'outils
        toolbar = Frame(self.root)
        toolbar.pack(expand =YES, fill =X, side =TOP)
        propriete = Frame(self.root)
        propriete.pack(expand =YES, fill =X, side =RIGHT)
        self.color_name = 'white'
        rows = []
        cols = []
        self.forme_active = None
        self.idForme = None
        self.zoom = 0;
        
        # Labels a droite
        ln = Label(propriete, text ='Nom')
        ln.grid(row=0, column=0, sticky=NSEW)
        self.Valeur_entry_nom = StringVar()
        self.entry_droite_name = Entry(propriete, textvariable = self.Valeur_entry_nom)
        self.entry_droite_name.grid(row=0, column=1, sticky=NSEW)
        
        lc = Label(propriete, text ='Couleur de la forme')
        lc.grid(row=1, column=0, sticky=NSEW)
        self.label_droite_couleur = Label(propriete)
        self.label_droite_couleur.grid(row=1, column=1, sticky=NSEW)
        
        
        lp1 = Label(propriete, text ='Point1 (X,Y)')
        lp1.grid(row=2, column=0, sticky=NSEW)
        self.Valeur_entry_point1 = StringVar()
        self.entry_droite_point1 = Entry(propriete, textvariable = self.Valeur_entry_point1)
        self.entry_droite_point1.grid(row=2, column=1, sticky=NSEW)
        
        
        lp2 = Label(propriete, text ='Point2 (X,Y)')
        lp2.grid(row=3, column=0, sticky=NSEW)
        self.Valeur_entry_point2 = StringVar()
        self.entry_droite_point2 = Entry(propriete, textvariable = self.Valeur_entry_point2)
        self.entry_droite_point2.grid(row=3, column=1, sticky=NSEW)
        
        lhauteur = Label(propriete, text ='Hauteur')
        lhauteur.grid(row=4, column=0, sticky=NSEW)
        self.Valeur_entry_hauteur = StringVar()
        self.entry_droite_hauteur = Entry(propriete, textvariable = self.Valeur_entry_hauteur)
        self.entry_droite_hauteur.grid(row=4, column=1, sticky=NSEW)
        
        llargeur = Label(propriete, text ='Largeur')
        llargeur.grid(row=5, column=0, sticky=NSEW)
        self.Valeur_entry_largeur = StringVar()
        self.entry_droite_largeur = Entry(propriete, textvariable = self.Valeur_entry_largeur)
        self.entry_droite_largeur.grid(row=5, column=1, sticky=NSEW)
        
        
        lz = Label(propriete, text ='Zoom')
        lz.grid(row=6, column=0, sticky=NSEW)
        self.Valeur_entry_zoom = StringVar()
        self.Valeur_entry_zoom.set( self.zoom.__str__())
        self.entry_droite_zoom = Entry(propriete, textvariable = self.Valeur_entry_zoom)
        self.entry_droite_zoom.grid(row=6, column=1, sticky=NSEW)
        
        lg = Label(propriete, text ='Groupe')
        lg.grid(row=7, column=0, sticky=NSEW)
        self.Valeur_groupe    = StringVar()
        self.listeGroupes    = ['']
        self.comboBoxGroupe    = Combobox(propriete, textvariable = self.Valeur_groupe, values = self.listeGroupes, state = 'readonly')
        self.comboBoxGroupe.grid(row=7, column=1, sticky=NSEW)
        self.comboBoxGroupe.bind('<<ComboboxSelected>>', self.onChangeCombobox)
        self.comboBoxGroupe.current(0)
        
        lga = Label(propriete, text="Groupe actif : ")
        lga.grid(row=8, column=0, sticky=NSEW)
        self.Valeur_labelgroupeactif    = StringVar()
        lgroupeactif = Label(propriete, textvariable = self.Valeur_labelgroupeactif) #valeur definie par Valeur_groupeactif
        lgroupeactif.grid(row=8, column=1, sticky=NSEW)
        

        
        
        cols.append(self.comboBoxGroupe)
        cols.append(self.entry_droite_name)
        cols.append(self.label_droite_couleur)
        cols.append(self.entry_droite_point1)
        cols.append(self.entry_droite_point2)
        rows.append(cols)
            
        # Boutons du haut
        self.bouton = [None]*6
        self.photos = [None]*6
        
        self.photos[0] = PhotoImage(file = 'images/cercle.png');
        self.bouton[0] = Button(toolbar, image = self.photos[0], command = lambda new_forme = Ellipses("Ellipse ", Point(0, 0) , Point(0,0) , self.color_name ):self.clic_btn_creation(new_forme))
        self.bouton[0].pack(side =LEFT)
        
        self.photos[1] = PhotoImage(file = 'images/rectangle.png');
        self.bouton[1] = Button(toolbar, image = self.photos[1], command = lambda new_forme = Rectangles("Rectangle ",Point(0,0), Point(0, 0), self.color_name) :self.clic_btn_creation(new_forme))
        self.bouton[1].pack(side =LEFT)

        self.photos[2] = PhotoImage(file = 'images/segment.png');
        self.bouton[2] = Button(toolbar, image = self.photos[2], command = lambda new_forme = Segments("Segment ", Point(0, 0), Point(0,0), self.color_name):self.clic_btn_creation(new_forme))
        self.bouton[2].pack(side =LEFT)
        
        self.photos[3] = PhotoImage(file = 'images/triangle.png');
        self.bouton[3] = Button(toolbar, image = self.photos[3], command = lambda new_forme = Polygones("Triangle ", Point(0,0), Point(0,0), self.color_name, 3, self.tabpoints):self.clic_btn_creation(new_forme))
        self.bouton[3].pack(side =LEFT)
        
        self.photos[4] = PhotoImage(file = 'images/polygone.png');
        self.bouton[4] = Button(toolbar, image = self.photos[4])
        self.bouton[4].pack(side =LEFT)
        
        self.bouton[4].bind("<ButtonPress-1>", lambda event, arg = toolbar:self.DefNombrePointsPolygone(event, arg))
        
        self.photos[5] = PhotoImage(file = 'images/groupe.png');
        self.bouton[5] = Button(toolbar, image = self.photos[5], command = self.clic_btn_groupe)
        self.bouton[5].pack(side =LEFT)
        
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
        self.cv.bind("<Button-2>", self.onMouseMolette)
        self.root.bind("<Control-g>", self.selectionGroupe)
        self.root.bind("<Control-Up>", self.selectionSuperGroupe)
        #Entry
        self.entry_droite_name.bind('<Return>', self.modifByEdit)
        self.entry_droite_point1.bind('<Return>', self.modifByEdit)
        self.entry_droite_point2.bind('<Return>', self.modifByEdit)
        self.label_droite_couleur.bind('<ButtonPress-1>', self.changerCouleur)
        self.root.bind('<Delete>', self.supprimerForme)
        self.cv.pack()

        
    def DefNombrePointsPolygone(self, event, toolbar):
        self.data = IntVar()
        self.entry_nbpts_poly = Entry(toolbar, textvariable = self.data)
        self.entry_nbpts_poly.pack(side = RIGHT)
        self.labelnb = Label(toolbar, text="Nombre de points: ")
        self.labelnb.pack(side = RIGHT)
        self.entry_nbpts_poly.bind('<Return>',self.NewPoly)
        
    def NewPoly(self, event):
        self.tabpoints = [None]*(2*(self.data.get()-2))
        new_forme = Polygones("Polygone ", Point(0,0), Point(0,0), self.color_name, self.data.get(), self.tabpoints)
        self.entry_nbpts_poly.destroy()
        self.labelnb.destroy()
        self.clic_btn_creation(new_forme)
               
    def changerCouleur(self, event):

        color = colorchooser.askcolor()
        self.color_name = color[1]
        self.label_droite_couleur.configure(background=self.color_name)
        if(self.forme_active is not None):
            if (self.GroupeActif != -1):
                #===========================================================
                # #On colore tout le groupe actif
                #===========================================================
                print("==================ColorationDuGroupe="+self.GroupeActif.__str__()+"===========")
                print("MAP GROUPE = "+self.mapGroupe.__str__() )
                copie = deepcopy(self.forme_active)
                for id in self.mapGroupe[self.GroupeActif].listeforme:
                    #MAJ des objets
                    self.map[id]._set_couleur(self.color_name)
                    #Maj du Canvas
                    self.regenererForme(id)
            else:
                self.forme_active._set_couleur(self.color_name)
                self.regenererForme()
            
            print("Changement de couleur entry_droite_name : ",self.color_name)
        
    def onMouseMolette(self, event):
        self.coordPoint = Point(event.x, event.y)
        if(self.i == self.forme_active._get_nbpoints()-1):
                
            self.tabpoints[len(self.tabpoints)-2]=(self.coordPoint.x)
            self.tabpoints[len(self.tabpoints)-1]=(self.coordPoint.y)
                
            print(self.tabpoints)
            
            self.forme_active.maj(Point(self.coordpoint1.x, self.coordpoint1.y), Point(self.coordpoint2.x, self.coordpoint2.y), self.forme_active._get_nbpoints(), self.tabpoints)
            self.forme_active.write()
            self.idForme =self.fabrique.fabriquer_forme(self.forme_active, self.cv)
            self.map[self.idForme] = self.forme_active
            self.majEntry()
            self.i = 0
            self.j = 0
            self.tabpoints = [None]*2
        else:
            if(self.i == 0):
                self.coordpoint1 = self.coordPoint
            if(self.i == 1):
                self.coordpoint2 = self.coordPoint
            if(self.i >1):
                self.tabpoints[self.j]=(self.coordPoint.x)
                self.tabpoints[self.j+1]=(self.coordPoint.y)
                self.j = self.j+2
            self.i = self.i+1
    
    def supprimerForme(self, event):
        items = self.cv.find_withtag('current')
        #Si on selectionne une forme
        if len(items):
            if(self.map[self.idForme]._groupe != -1):            
                self.mapGroupe[self.map[self.idForme]._groupe]._supprimer_forme(self.idForme)        
            del self.map[self.idForme]
            self.cv.delete(self.root,self.idForme)
            self.idForme = None
            self.majEntry()
            self.root.update()
        

    def regenererForme(self, id = None):
        if (id is not None): #id en parametre 
            self.cv.delete(self.root, id)
            self.map[id].write()
            newIdForme = self.fabrique.fabriquer_forme(self.map[id], self.cv)
            self.map[newIdForme] = deepcopy(self.map[id])
            #MAJ map
            del self.map[id]
            print ("regeneration" + id.__str__())
            self.map[newIdForme]._set_nom(self.entry_droite_name.get())
            #MAJ mapGroupe
            del self.mapGroupe[self.GroupeActif].listeforme[id]
            self.mapGroupe[self.GroupeActif].listeforme[newIdForme] = 1
            
            self.root.update()
        else: #id pas defini
            self.cv.delete(self.root, self.idForme)
            self.forme_active.write()
            newIdForme = self.fabrique.fabriquer_forme(self.forme_active, self.cv)
            self.map[newIdForme] = deepcopy(self.map[self.idForme])
            #MAJ map
            del self.map[self.idForme]
            print ("regeneration" + self.idForme.__str__())
            self.idForme = newIdForme
            self.map[self.idForme]._set_nom(self.entry_droite_name.get())
            
            self.forme_active = self.map[self.idForme]
            self.root.update()
        

    def modifByEdit(self, event):
        #active les ENTRY si une forme est selectionne
         
        if(self.forme_active._get_nom() != ""):

            self.forme_active._set_couleur(self.color_name)

            pos = self.entry_droite_point1.get().find(',')
            
            difference = [self.forme_active._get_point1()._get_x() - (int(self.entry_droite_point1.get()[0:pos])), self.forme_active._get_point1()._get_y() - int(self.entry_droite_point1.get()[pos+1: len(self.entry_droite_point1.get())])]
            
            self.forme_active._set_point1(Point(int(self.entry_droite_point1.get()[0:pos]), int(self.entry_droite_point1.get()[pos+1: len(self.entry_droite_point1.get())])))
            self.forme_active._set_point2(Point(self.forme_active._get_point2()._get_x() - difference[0], self.forme_active._get_point2()._get_y() - difference[1]))

            self.x1, self.y1 =self.entry_droite_point1.get(), self.entry_droite_point2.get()
            
            self.regenererForme()
            self.majEntry()
            print ("modif")
            
    def majEntry(self):
        if(self.idForme is not None and self.GroupeActif == -1):
            #FORME SIMPLE
            print("=========majEntry=========")
            print ("IDFORME :" + self.idForme.__str__())
            print ("MAP: " + self.map.__str__())
            print ("FORMEACTIVE: " +  self.forme_active._get_nom())
            #nom
            self.Valeur_entry_nom.set(self.map[self.idForme]._get_nom())
            #couleur
            self.label_droite_couleur.configure(background=self.map[self.idForme]._get_couleur())
            #point1
            self.Valeur_entry_point1.set(self.map[self.idForme]._get_point1()._get_x().__str__() + "," + self.map[self.idForme]._get_point1()._get_y().__str__())
            #point2
            self.Valeur_entry_point2.set(self.map[self.idForme]._get_point2()._get_x().__str__() + "," + self.map[self.idForme]._get_point2()._get_y().__str__())
            #hauteur
            self.Valeur_entry_hauteur.set(self.map[self.idForme]._get_hauteur().__str__())
            #largeur
            self.Valeur_entry_largeur.set(self.map[self.idForme]._get_largeur().__str__())
            #liste deroulante
            if (self.map[self.idForme]._groupe != -1):
                self.comboBoxGroupe.current(self.map[self.idForme]._groupe)
            else:
                self.comboBoxGroupe.current(0)
        elif (self.GroupeActif != -1):
            print ("GROUPE ACTIF")
            self.Valeur_entry_nom.set(self.mapGroupe[self.GroupeActif]._get_nom())
            #couleur
            self.label_droite_couleur.configure(background=self.map[self.idForme]._get_couleur())
            #point1
            self.Valeur_entry_point1.set(self.map[self.idForme]._get_point1()._get_x().__str__() + "," + self.map[self.idForme]._get_point1()._get_y().__str__())
            #point2
            self.Valeur_entry_point2.set(self.map[self.idForme]._get_point2()._get_x().__str__() + "," + self.map[self.idForme]._get_point2()._get_y().__str__())
            #hauteur
            self.Valeur_entry_hauteur.set(self.map[self.idForme]._get_hauteur().__str__())
            #largeur
            self.Valeur_entry_largeur.set(self.map[self.idForme]._get_largeur().__str__())
            #liste deroulante
            if (self.mapGroupe[self.map[self.idForme]._groupe]._groupe != -1):
                self.comboBoxGroupe.current(self.mapGroupe[self.map[self.idForme]._groupe]._groupe)
            else:
                self.comboBoxGroupe.current(0)
        else:
            print ("AUCUNE SELECTION")
            self.Valeur_entry_nom.set('')
            self.label_droite_couleur.configure(background='')
            self.Valeur_entry_point1.set('')
            self.Valeur_entry_point2.set('')
            self.Valeur_entry_hauteur.set('')
            self.Valeur_entry_largeur.set('')
            self.comboBoxGroupe.current(0) 
        #zoom    
        if(self.zoom > 0):
            self.Valeur_entry_zoom.set("+" + self.zoom.__str__())
        else:
            self.Valeur_entry_zoom.set(self.zoom.__str__())
            
        #groupe actif ou pas
        if(self.GroupeActif  == -1):
            self.Valeur_labelgroupeactif.set("Aucun");
        else :
            self.Valeur_labelgroupeactif.set( self.mapGroupe[self.GroupeActif]._get_nom() );
        
    def onMouseClic(self, event):
        items = self.cv.find_withtag('current')
        self.ClicGauche_depart = Point(event.x, event.y)
        
        if len(items):
            print("selection forme")
            
            self.idForme = items[0]
            self.forme_active = self.map[self.idForme]
            
            #dessiner le contour de selection
            
            print ("MAP: " + self.map.__str__())
            print ("ID: " + self.idForme.__str__())
            
            print ("NOM: " +  self.forme_active._get_nom())
            self.majEntry()
        else:
            try:
                print("dessinDown")
                if self.PeutDessiner :
                    #id de la forme sur le canvas
                    self.forme_active.maj(Point(event.x, event.y), Point(event.x,event.y))
                    self.forme_active.write()
                    self.idForme =self.fabrique.fabriquer_forme(self.forme_active, self.cv)
                    self.map[self.idForme] = self.forme_active
                else :
                    #Deselection de tout
                    self.GroupeActif = -1
                self.majEntry()
            except:pass  #ne rien faire quand aucune action est selectionnee (clic dans le vide)
        #self.root.update()

    def onMouseUp(self, event):
        if self.PeutDessiner : 
            self.PeutDessiner = FALSE
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
            #Vecteur de deplacement X = 0 ou Y = 1
            x_vecteur, y_vecteur = self.ClicGauche_fin.x - self.ClicGauche_depart.x , self.ClicGauche_fin.y - self.ClicGauche_depart.y   #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
            print (self.cv.winfo_width().__str__())
            #Gestion dans le cadre du canvas
            if (((self.map[self.idForme])._get_point1()._get_x() + x_vecteur) >= 0) and (((self.map[self.idForme])._get_point2()._get_x() + x_vecteur) <= self.cv.winfo_width() and (((self.map[self.idForme])._get_point1()._get_y() + y_vecteur) >= 0) and (((self.map[self.idForme])._get_point2()._get_y() + y_vecteur) <= self.cv.winfo_height())):
                print ("entre  a " + ((self.map[self.idForme])._get_point1()._get_x() + x_vecteur).__str__())
                #----------------
                # TRANSLATION
                #----------------
                if(self.GroupeActif != -1):
                    
                    #===== GROUPE ========= On bouge tout le groupe de la forme active
                    
                    print("BOUGE le groupe de " + x_vecteur.__str__() + " , " + y_vecteur.__str__())
                    print("==================BougeTouteFormeDuGroupe="+self.GroupeActif.__str__()+"===========")
                    #On bouge tout le groupe de la forme en mouvement dans onMouseMove
                    #if(self.GroupeActif is not None):
                    print("MAP GROUPE = "+self.mapGroupe.__str__() )
                    
                    print("TRANSLATION GROUPE")
                    #TRANSLATION du groupe
                    self.mapGroupe[self.GroupeActif].translation(x_vecteur, y_vecteur)
                    for id in self.mapGroupe[self.GroupeActif].listeforme:
                        #Maj du Canvas
                        self.cv.move(id, x_vecteur, y_vecteur)
                    #TRANSLATION des autres lies
                    for g in self.mapGroupe: #pour chaque groupe de la mapGroupe
                        if (self.GroupeActif == self.mapGroupe[g]._groupe): #si le groupe est lie a l'actuel
                            self.mapGroupe[g].translation(x_vecteur, y_vecteur)
                            for id in self.mapGroupe[g].listeforme:
                                #Maj du Canvas
                                self.cv.move(id, x_vecteur, y_vecteur)

                else:
                    #On bouge que la forme elle-meme
                    #MAJ Canvas
                    self.cv.move(self.idForme, x_vecteur, y_vecteur)
                    print ("MAPmoove: " + self.map.__str__())
                    print ("IDmoove: " + self.idForme.__str__())
                    
                    print ("NOMmoove: " +  self.forme_active._get_nom())
                    print("VECTEURmoove: ("+ x_vecteur.__str__() +"," +y_vecteur.__str__()+")")
                    print("EVENTmoove: ("+ event.x.__str__() +"," + event.y.__str__()+")")
                    
        
                    #MAJ OBJET
                    self.map[self.idForme].translation(x_vecteur, y_vecteur)
                    
                    
                self.ClicGauche_depart = self.ClicGauche_fin
                self.majEntry()
            else:
                print ("entre PAS a " + ((self.map[self.idForme])._get_point1()._get_x() - x_vecteur).__str__())
            
        else:
            print("dessinMove")
            
            #modifie le dessin
            
            try:
                if self.PeutDessiner :
                    print("NOMdown:" + self.forme_active._get_nom())
                    self.cv.delete(self.idForme) #supprime l'ancienne forme du canvas
                    del self.map[self.idForme]  #supprime l'ancinne forme de la map
                    
                    self.forme_active._set_point2(Point(event.x, event.y)) #MAJ forme active
                    
                    self.forme_active.maj(self.forme_active._get_point1(), self.forme_active._get_point2())
                    self.forme_active.write()
                    self.idForme =self.fabrique.fabriquer_forme(self.forme_active, self.cv)
                    self.map[self.idForme] = self.forme_active
                    
                    self.majEntry()
            except: pass #ne rien faire quand aucune action est selectionnee (clic dans le vide)
    
    
    def onClicZoom(self, event):
        print("Clic Droit " + event.x.__str__() + " ; " + event.y.__str__() )
        print ("MAP: " + self.map.__str__())
        self.ClicDroit_depart = Point(event.x, event.y)
        

    
    def onZoomMove(self, event):
        if self.idForme is not None:
            #--------------------------------
            #ZOOM que par deplacement vertical
            #---------------------------------
            if True:
                print("===============Bouge clic2 Droit================="+ event.x.__str__() + " ; " + event.y.__str__() )
                #recupere l'endroit actuel de la souris
                self.ClicDroit_fin = Point(event.x, event.y)
                
                
                #difference entre anciennes et nouvelles coordonees (donc calcul du vecteur)
                y_vecteur = self.ClicDroit_fin.y - self.ClicDroit_depart.y
                action = None #Zoom ou dezoom
                
                if y_vecteur < 0:
                    action = False
                    
                if y_vecteur > 0:
                    action = True
                
                coef = 1.1 #10%
                
                print("VECTEUR=" + y_vecteur.__str__())
                
                print("zoom=" + self.zoom.__str__())
                self.zoom = self.zoom +y_vecteur
                
                
                if action is not None:
                    
                    print ("MAP AVANT: " + self.map.__str__())
                    i = self.idForme
                    self.cv.delete(i) #supprime l'ancienne forme du canvas
                    print("i="+i.__str__())
                    self.forme_active = self.map[i] #copie intermediaire (forme_active a associer au CANVAS )
                    
                    #----------Deplace selon l'endroit du clic pour pouvoir choisir son endroit du zoom
                    #Difference entre l'endroit du clic et le milieu de la forme
                    #DistanceX = self.ClicDroit_fin._get_x() - self.forme_active._get_milieu()._get_x()
                    #DistanceY = self.ClicDroit_fin._get_y() - self.forme_active._get_milieu()._get_y()
                    #-------------------------------------------
                    #Action de zoom/dezoom sur une forme/groupe 
                    #-------------------------------------------
                    #MAJ des objets
                    if(self.GroupeActif != -1):
                        #---------------
                        # GROUPE
                        #---------------
                            
                        print("ZOOM GROUPE")
                        #ZOOM du groupe
                        self.mapGroupe[self.GroupeActif].zoom(action, coef)
                        #ZOOM des autres lies
                        for g in self.mapGroupe: #pour chaque groupe de la mapGroupe
                            if (self.GroupeActif == self.mapGroupe[g]._groupe): #si le groupe est lie a l'actuel
                                self.mapGroupe[g].zoom(action, coef)
                                #MISE A JOUR DU GROUPE PARCOURU
                                for index in self.mapGroupe[g].listeforme:
                                    self.cv.delete(index);
                                    #VISUEL:Dessine toutes les formes du groupe
                                    x = self.fabrique.fabriquer_forme(self.mapGroupe[g].listeforme[index], self.cv)
                                    
                                    #DONNEES
                                    self.map[x] = self.map[index]
                                    # MAJ de la mapGroupe car les id de map ont change mais pas ceux de mapgroupe
                                    self.majMapGroupe(index, x)
                                    #Suppression de l'ancienne forme
                                    del self.map[index]
                                    #Conserve la Forme selectionnee
                                    if index == self.idForme:
                                        self.idForme = x
                                            
                                            
                        #MISE A JOUR DU GROUPE ACTUEL 
                        for index in self.mapGroupe[self.GroupeActif].listeforme:
                            self.cv.delete(index);
                            #VISUEL:Dessine toutes les formes du groupe
                            x = self.fabrique.fabriquer_forme(self.mapGroupe[self.GroupeActif].listeforme[index], self.cv)
                            
                            
                            #DONNEES
                            self.map[x] = self.map[index]
                            # MAJ de la mapGroupe car les id de map ont change mais pas ceux de mapgroupe
                            self.majMapGroupe(index, x)
                            #Suppression de l'ancienne forme
                            del self.map[index]
                            #Conserve la Forme selectionnee
                            if index == self.idForme:
                                self.idForme = x
                    else:
                        #---------------
                        #FORME
                        #---------------
                        self.forme_active.zoom(action, coef)
                        #self.forme_active.translation( DistanceX - DistanceX * coef, DistanceY - DistanceY * coef)#Deplace selon le coef
                       
                        #Suppression de l'ancienne forme
                        del self.map[i]
                        #VISUEL: Dessine la forme active
                        self.idForme = self.fabrique.fabriquer_forme(self.forme_active, self.cv)
                        self.map[self.idForme] = self.forme_active
                        r = self.idForme
                        # MAJ de la mapGroupe car les id de map ont change mais pas ceux de mapgroupe
                        self.majMapGroupe(i, r)
                        if i == self.idForme:#Forme selectionnee
                            self.idForme = r
                    print ("MAP APRES: " + self.map.__str__())
                    print ("MAPGRP APRES: " + self.mapGroupe.__str__())
                    #self.idForme = r
                    self.ClicDroit_depart = self.ClicDroit_fin
                    self.majEntry()
    def clic_btn_creation(self, forme):
        self.PeutDessiner = TRUE
        print(forme)
        self.nbFormes = self.nbFormes + 1
        
        type(forme).numero += 1
        self.forme_active = deepcopy(forme)
        self.forme_active._set_nom(self.forme_active._get_nom()+ type(forme).numero.__str__())
        #self.forme_active._set_nom("Forme " + self.nbFormes.__str__())
        print (Rectangles.numero.__str__())
        print(type(forme).numero.__str__()) 
        
    def clic_btn_groupe(self):

        rows = []
        cols = []
        self.fenetreGroupe=Toplevel()
        self.fenetreGroupe.resizable(False,False)
        self.fenetreGroupe.title("Nouvelle fenetre")
        
        
        labelGroupe = Label(self.fenetreGroupe, text ='Entrez le nom du groupe')
        labelGroupe.grid(row=0, column=0, sticky=NSEW)
        
        entryGroupe=Entry(self.fenetreGroupe, justify='left')
        entryGroupe.grid(row=1, column=0, sticky=NSEW)
        entryGroupe.focus_set() #donne le focus a l'ouverture

        boutonGroupe=Button(self.fenetreGroupe, text="Creer le groupe", command = lambda: self.creerGroupe(entryGroupe.get()))
        boutonGroupe.grid(row=2, column=0)

        cols.append(entryGroupe)
        cols.append(boutonGroupe)
        rows.append(cols)
        
    def creerGroupe(self, groupe):
        self.fenetreGroupe.withdraw()
        self.listeGroupes.append(groupe)
        self.comboBoxGroupe.configure(values= self.listeGroupes)
        self.mapGroupe[len(self.listeGroupes) - 1] = FormesComposees(groupe, {}) #listeforme de mapGroupe est un dictionnaire vide
        
    def onChangeCombobox(self, lol):
        if (self.GroupeActif == -1):   
            if (self.comboBoxGroupe.current() != 0): # si un groupe selectionne dans la box
                print("allocation") 
                if(self.map[self.idForme]._groupe != -1): # si la forme a deja un groupe on la change de groupe
                    self.mapGroupe[self.map[self.idForme]._groupe]._supprimer_forme(self.idForme)
                    self.map[self.idForme]._groupe = -1
                self.mapGroupe[self.comboBoxGroupe.current()]._ajouter_forme(self.idForme, self.map[self.idForme])
                self.map[self.idForme]._groupe = self.comboBoxGroupe.current()
                print ("MAPGROUPE= "+self.mapGroupe.__str__())
            else: # si aucun groupe selectionne dans la box
                print("desallocation")
                if(self.map[self.idForme]._groupe != -1): # on retire la forme du groupe
                    self.mapGroupe[self.map[self.idForme]._groupe]._supprimer_forme(self.idForme)
                    self.map[self.idForme]._groupe = -1 
        else: #Changement a tout un groupe
            if (self.comboBoxGroupe.current() != 0): # Selection d'un groupe
                print("SUPERallocation")   
                self.mapGroupe[self.GroupeActif]._groupe = self.comboBoxGroupe.current() #sous groupe du groupe selectionne
                #self.mapGroupe[self.comboBoxGroupe.current()]._ajouter_forme(self.GroupeActif, self.mapGroupe[self.GroupeActif]) #ajoute le groupe actif au groupe choisi
                
                
                
                
            else:#Desallocation d'un superGroupe
                print("SUPERdesalocation")
                self.mapGroupe[self.GroupeActif]._groupe = -1
                
                
    def selectionGroupe(self, event): #appele par CtrlG
        #print("==================SelectionneTouteFormeDuGroupe============")
        
        if(self.GroupeActif == -1) : #Selection car aucun selectionne
            print("===Selection GROUPE car aucun selectionne")
            self.GroupeActif = self.map[self.idForme]._groupe
        else:
            print("===Deselection GROUPE")
            self.GroupeActif = -1 #deselectionne
        self.majEntry()
    
    
    def selectionSuperGroupe(self, event):
        if (self.GroupeActif != -1 and self.mapGroupe[self.GroupeActif]._groupe != -1):
            print("===Selectionne superGROUPE car deja un selectionne et en plus forme appartient a un groupe")
            self.GroupeActif = self.mapGroupe[self.GroupeActif]._groupe
            self.majEntry()
        
        
        
    def majMapGroupe(self, idoriginal, nouvelid):
        #===========================================================
        # MAJ de la mapGroupe car les id de map changent lors d'un dessin mais pas ceux de mapgroupe
        #===========================================================
        
        for g in self.mapGroupe: #pour chaque groupe de la mapGroupe
            if ( any(idoriginal == val for val in self.mapGroupe[g].listeforme) ): #si la forme fait partie du groupe
                self.mapGroupe[g]._supprimer_forme(idoriginal); #supprime l'ancienne forme
                self.mapGroupe[g]._ajouter_forme(nouvelid, self.map[nouvelid]); #ajoute la nouvelle forme
            
                    
        
if(__name__ == '__main__'):
    application = App()    # Instanciation de la classe
    application.mainloop()        # Boucle pour garder le programme en vie
    application.quit()    
