import pygame
pygame.init()

# Generer la fenetre du jey
pygame.display.set_caption("Hexgone")
pygame.display.set_mode((1080, 720))

running=True
while running :

    # Boucle de test de la fermeture de la fenetre
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()