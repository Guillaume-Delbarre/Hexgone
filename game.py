import pygame

class Game() :

    def __init__(self, screen, taille=5):
        self.taille = taille
        self.tableau = [[0] * taille] * taille
        self.screen = screen
        self.hexagone_size = 10

        # Récupération de la taille de l'écran
        screen_size = self.screen.get_size()

        # Calcul des coordonnées du nouvel origine pour les hexagones
        self.draw_origine = (int(screen_size[0] * 0.2), int(screen_size[1] * 0.2))

        # Calcul de la taille des hexagones
        largeur = (1 + (self.taille - 1) * 0.75)
        hauteur = (self.taille + 0.5)
        self.hexagone_size = (int((screen_size[0] * 0.6) / largeur), int((screen_size[1] * 0.7) / hauteur))

    def draw(self) :
        for index_ligne, ligne in enumerate(self.tableau) :
            for index_colonne, val in enumerate(ligne) :

                # Calcul de l'origine de l'hexagone en fonction des index ligne et colonne
                if index_colonne%2 == 0 :
                    origine_y = (0.5 + index_ligne) * self.hexagone_size[1]
                else :
                    origine_y = index_ligne * self.hexagone_size[1]
                
                origine_x = 0.75 * index_colonne * self.hexagone_size[0]


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
        pygame.draw.polygon(self.screen, couleur, [(origine[0] + int(0.25*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(0.75*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.5*self.hexagone_size[1])),
                                                   (origine[0] + int(0.75*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0] + int(0.25*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.5*self.hexagone_size[1]))])
        # Dessin des contours
        pygame.draw.polygon(self.screen, "Black", [(origine[0] + int(0.25*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(0.75*self.hexagone_size[0]), origine[1]),
                                                   (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.5*self.hexagone_size[1])),
                                                   (origine[0] + int(0.75*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0] + int(0.25*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                   (origine[0], origine[1] + int(0.5*self.hexagone_size[1]))], 3)