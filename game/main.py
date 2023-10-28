import pygame
pygame.init()

# Generer la fenetre du jeu
pygame.display.set_caption("Hexgone")
screen = pygame.display.set_mode((1080, 720))

running=True
while running :

    # Coloration du fond en bleu
    screen.fill("Light Blue")

    # Mise à jour de l'écran
    pygame.display.flip()

    # Boucle de test de la fermeture de la fenetre
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()