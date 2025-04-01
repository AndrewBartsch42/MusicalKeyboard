import pygame # https://www.pygame.org/news
import winsound
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                winsound.Beep(196, 100)
            elif event.key == pygame.K_w:
                winsound.Beep(293, 100)
            elif event.key == pygame.K_e:
                winsound.Beep(440, 100)
            elif event.key == pygame.K_r:
                winsound.Beep(659, 100)

                
pygame.quit()