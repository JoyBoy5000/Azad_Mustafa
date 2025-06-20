import pygame
import random

pygame.init()
BREITE, HÖHE = 400, 300
BLOCK = 20
FPS = 10


SCHWARZ = (0, 0, 0)
GRUEN = (0, 255, 0)
ROT = (255, 0, 0)


fenster = pygame.display.set_mode((BREITE, HÖHE))
pygame.display.set_caption("Einfache Snake")
uhr = pygame.time.Clock()

def neue_position():
    return (random.randrange(0, BREITE, BLOCK), random.randrange(0, HÖHE, BLOCK))

def spiel():
    schlange = [(100, 100)]
    richtung = (BLOCK, 0)
    futter = neue_position()
    aktiv = True

    while aktiv:
        uhr.tick(FPS)

        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                aktiv = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_w:
                    richtung = (0, -BLOCK)
                elif ereignis.key == pygame.K_s:
                    richtung = (0, BLOCK)
                elif ereignis.key == pygame.K_a:
                    richtung = (-BLOCK, 0)
                elif ereignis.key == pygame.K_d:
                    richtung = (BLOCK, 0)

        
        kopf = (schlange[0][0] + richtung[0], schlange[0][1] + richtung[1])

        
        if kopf in schlange or not (0 <= kopf[0] < BREITE) or not (0 <= kopf[1] < HÖHE):
            aktiv = False

        schlange.insert(0, kopf)

        if kopf == futter:
            futter = neue_position()
        else:
            schlange.pop()

        
        fenster.fill(SCHWARZ)
        for teil in schlange:
            pygame.draw.rect(fenster, GRUEN, (*teil, BLOCK, BLOCK))
        pygame.draw.rect(fenster, ROT, (*futter, BLOCK, BLOCK))
        pygame.display.flip()

    pygame.time.wait(2000)

spiel()
pygame.quit()