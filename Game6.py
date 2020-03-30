import pygame
import random
import os
pygame.init()

screen_width=900
screen_height=500
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Star Trek Discovery")
clock = pygame.time.Clock()


                                                            # Loading Images
bg = pygame.image.load('moon.png')
bg = pygame.transform.scale(bg, (screen_width,screen_height))
falcon1 = pygame.image.load('falcon.png')
falcon1 = pygame.transform.scale(falcon1,(150,100))
weapon1 = pygame.image.load('mis1.png')
weapon1 = pygame.transform.scale(weapon1,(10,20))
targetx = pygame.image.load('fire.png')
targetx = pygame.transform.scale(targetx,(25,50))

                                                            #Player Functions
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width=150
        self.height=100
        self.x=screen_width/2-150/2
        self.y=screen_height/2-100/2
        self.image = pygame.Surface([150, 100])
        self.rect = self.image.get_rect()
        self.vel=20
        self.hitbox =(self.x+50,self.y+20,self.width,self.height+20)

    def draw(self, window):
        self.hitbox =(self.x+50,self.y+20,self.width,self.height+20)
        pygame.draw.rect(window,(225,0,0),self.hitbox,2)
        window.blit(falcon1,(self.x,self.y))

                                                        #Weapons Function
class weapons(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        super().__init__()
        self.x=x
        self.y=y
        self.radius=radius
        self.vel=50
        self.image=pygame.Surface([10,20])
        self.rect=self.image.get_rect()

    def draw(self, window):
        window.blit(weapon1,(self.x+45,self.y))     


                                                        #Target Function
class targets(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        super().__init__()
        self.x=x
        self.y=y
        self.radius=radius
        self.vel=10
        self.image = pygame.Surface([25,50])
        self.rect=self.image.get_rect()
        self.hitbox =(self.x, self.y,28,50)


    def die(self):
        for enemy in t1:
           if target.rect.x<100:
             t1.remove(enemy)
        
    def draw(self,window):
        self.hitbox =(self.x, self.y,28,50)
        pygame.draw.rect(window,(225,0,0),self.hitbox,2)
        window.blit(targetx,(self.x,self.y))


                                                    # Redraw Function
def redraw():
    window.blit(bg,(0,0))
    ship1.draw(window)

    hit = pygame.sprite.pygame.sprite.spritecollide(ship1, t1, False, collided = None)
    if hit:
        SystemExit()


    for i in b1:
        i.draw(window)

    for target in t1:
       target.draw(window)
       
    pygame.display.update()

                                                            #mainloop
ship1 = player()
poslist=[]
bullet1=[]
enemy=[]
target1=[]

tot=pygame.sprite.Group()
b1=pygame.sprite.Group()
t1=pygame.sprite.Group()

run = True
while run:

        
    
    t2=targets(0,0,0)
    t2.rect.x = random.randint(0,screen_width)
    x1=[random.randint(0,screen_width),0]
    target1=targets(x1[0],x1[1],50)
    t1.add(target1)
    pygame.time.delay(100)

                                                            # KEY CONTROLS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for target in t1:
        if target.x < screen_width:
            target.y += target.vel

    for bullet in b1:
        if bullet.y >0:
            target1.die()
            bullet.y -=bullet.vel
        else:
            b1.remove(bullet)

    hits = pygame.sprite.groupcollide(t1, b1, True, True)
    
    keys = pygame.key.get_pressed()
                        
    if keys[pygame.K_SPACE]:
        if len(b1)<10:
            
            bullet1=weapons(round(ship1.x + ship1.width//2), round(ship1.y + ship1.height//2), 20)
            b1.add(bullet1)

    if keys[pygame.K_LEFT] and ship1.x > (ship1.vel-50):
        ship1.x -= ship1.vel

    if keys[pygame.K_RIGHT] and ship1.x < (screen_width-50 - ship1.width - ship1.vel):
        ship1.x += ship1.vel

    if keys[pygame.K_UP] and ship1.y > (ship1.vel):
        ship1.y -= ship1.vel

    if keys[pygame.K_DOWN] and ship1.y < (screen_height-50 - ship1.height - ship1.vel):
        ship1.y += ship1.vel

                                                            # calls The redraw function
    redraw()

pygame.quit
