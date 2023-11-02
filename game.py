import pygame

class Game() :

    def __init__(self, screen, taille=4):
        self.taille = taille
        self.tableau = [[0 for i in range(taille)] for j in range(taille)]
        self.screen = screen
        self.hexagone_size = 10
        self.tableau_rect = [[0 for i in range(taille)] for j in range(taille)]

        # Récupération de la taille de l'écran
        screen_size = self.screen.get_size()

        # Calcul des coordonnées du nouvel origine pour les hexagones
        self.draw_origine = (int(screen_size[0] * 0.2), int(screen_size[1] * 0.2))

        # Calcul de la taille des hexagones
        largeur = self.taille + (self.taille - 1) * 0.5
        hauteur = 0.75 * self.taille + 0.5
        self.hexagone_size = (int((screen_size[0] * 0.6) / largeur), int((screen_size[1] * 0.7) / hauteur))

    def draw(self) :
        # Dessin des hexagones
        for index_ligne, ligne in enumerate(self.tableau) :
            for index_colonne, val in enumerate(ligne) :
                
                origine_x = (self.taille - 1 - index_colonne) * self.hexagone_size[0] * 0.5 + self.hexagone_size[0] * index_ligne
                origine_y = index_colonne * self.hexagone_size[1] * 0.75

                # Dessin des hexagones et enregistrement des rect
                self.tableau_rect[index_ligne][index_colonne] = self.dessine_hexagone(origine=(self.draw_origine[0] + origine_x, self.draw_origine[1] + origine_y), val=val)

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
        return pygame.draw.polygon(self.screen, "Black", [(origine[0] + int(0.5*self.hexagone_size[0]), origine[1]),
                                                          (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.25*self.hexagone_size[1])),
                                                          (origine[0] + int(self.hexagone_size[0]), origine[1] + int(0.75*self.hexagone_size[1])),
                                                          (origine[0] + int(0.5*self.hexagone_size[0]), origine[1] + int(self.hexagone_size[1])),
                                                          (origine[0], origine[1] + int(0.75*self.hexagone_size[1])),
                                                          (origine[0], origine[1] + int(0.25*self.hexagone_size[1]))], 3)
    
    def check_hexagone(self, pos) :
        for index_ligne, ligne in enumerate(self.tableau_rect) :
            for index_colonne, rect in enumerate(ligne) :
                if rect.collidepoint(pos) :
                    # Vérification que le click est bien sur l'hexagone
                    origine_x = self.draw_origine[0] + (self.taille - 1 - index_colonne) * self.hexagone_size[0] * 0.5 + self.hexagone_size[0] * index_ligne
                    origine_y = self.draw_origine[1] + index_colonne * self.hexagone_size[1] * 0.75

                    pos = [pos[0] - origine_x, pos[1] - origine_y]

                    if (pos[0] < (self.hexagone_size[0] / 2)) and (-0.5*pos[0]+0.75-pos[1] < 0) or (pos[0] >= (self.hexagone_size[0] / 2)) and (-0.5*pos[0]+0.75-pos[1] < 0) :
                        if self.tableau[index_ligne][index_colonne] == 1 :
                            self.tableau[index_ligne][index_colonne] = 2
                        else :
                            self.tableau[index_ligne][index_colonne] = 1