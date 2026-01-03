import pygame
from pygame.locals import *


pygame.init()

screen_width = 864
screen_height= 750
clock= pygame.time.Clock()
fps= 60

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

bg= pygame.image.load("images/bg.png")
ground_img= pygame.image.load("images/ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index=0
        self.counter=0
        for num in range (1,4):
            img= pygame.image.load(f"images/bird{num}.png")
            self.images.append(img)
        self.image= self.images[self.index]
        self.rect= self.image.get_rect()
        self.rect.center= [x,y]
        
bird_group= pygame.sprite.Group()
flappy_bird= Bird(100, int(screen_height/2))
bird_group.add(flappy_bird)

#define game variables
ground_scroll=0
scroll_speed= 2

run = True

while run:
    
    clock.tick(60)
    #draw background
    screen.blit(bg, (0,0))
    
    screen.blit(ground_img, (ground_scroll,600))
    ground_scroll -= scroll_speed
    bird_group.draw(screen)
    
    if abs(ground_scroll) > 35:
        ground_scroll=0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
      
    pygame.display.update()       
pygame.quit()