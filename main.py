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

    for event in pygame.event.get() :
        # Test de la fermeture de la fenetre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
        # Test d'un click souris
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            game.check_hexagone(pos)
