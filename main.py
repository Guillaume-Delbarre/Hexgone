import pygame
pygame.init()

from game import Game

# Generer la fenetre du jeu
pygame.display.set_caption("Hexgone")
screen = pygame.display.set_mode((1080, 720))

# Coloration du fond en bleu
screen.fill("Light Green")

# Créer le jeu
game = Game(screen)

running=True
while running :

    # Mise à jour de l'écran
    pygame.display.flip()

    game.draw()

    # Boucle de test de la fermeture de la fenetre
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
