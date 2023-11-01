import pygame

class Game() :

    def __init__(self, screen, taille=14):
        self.taille = taille
        self.tableau = [[0] * taille] * taille
        self.screen = screen
        self.hexagone_size = 10
        self.tableau_rect = [[0] * taille] * taille

        # Récupération de la taille de l'écran
        screen_size = self.screen.get_size()

        # Calcul des coordonnées du nouvel origine pour les hexagones
        self.draw_origine = (int(screen_size[0] * 0.2), int(screen_size[1] * 0.2))

        # Calcul de la taille des hexagones
        largeur = self.taille + (self.taille - 1) * 0.5
        hauteur = 0.75 * self.taille + 0.5
        self.hexagone_size = (int((screen_size[0] * 0.6) / largeur), int((screen_size[1] * 0.7) / hauteur))

    def draw(self) :
        for index_ligne, ligne in enumerate(self.tableau) :
            for index_colonne, val in enumerate(ligne) :
                
                origine_x = (self.taille - 1 - index_colonne) * self.hexagone_size[0] * 0.5 + self.hexagone_size[0] * index_ligne
                origine_y = index_colonne * self.hexagone_size[1] * 0.75

                self.dessine_hexagone(origine=(self.draw_origine[0] + origine_x, self.draw_origine[1] + origine_y), val=val)

    def dessine_hexagone(self, origine, val) :
        # On détermine la couleur de l'héxagone en fonction de sa valeur
        if val == 0 :
            couleur = "White"
        elif val == 1 :
            couleur = "Blue"
        elif val == 2 :
            couleur = "Red"
        else :
            couleur = "Black"
        
        # Dessin de l'hexagone
        pygame.draw.polygon(self.screen, couleur, [(origine[0] + int(0.5*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.25*self.hexagone_size[1])),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.75*self.hexagone_size[1])),
                                                   (origine[0] + int(0.5*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.75*self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.25*self.hexagone_size[1]))])
        # Dessin des contours
        pygame.draw.polygon(self.screen, "Black", [(origine[0] + int(0.5*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.25*self.hexagone_size[1])),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.75*self.hexagone_size[1])),
                                                   (origine[0] + int(0.5*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.75*self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.25*self.hexagone_size[1]))], 3)
        