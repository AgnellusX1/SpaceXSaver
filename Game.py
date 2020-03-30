import pygame
import random
import os
pygame.init()

screen_width=900
screen_height=500
window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Star Trek Discovery")

                                                            # Loading Images
bg = pygame.image.load('sky.png')
bg = pygame.transform.scale(bg, (screen_width,screen_height))
falcon1 = pygame.image.load('falcon.png')
falcon1 = pygame.transform.scale(falcon1,(150,100))
weapon1 = pygame.image.load('mis1.png')
weapon1 = pygame.transform.scale(weapon1,(10,20))
targetx = pygame.image.load('fire.png')
targetx = pygame.transform.scale(targetx,(25,50))




                                                            #Player Functions
class player:
    def __init__(self, width, height):
        self.width=width
        self.height=height

        self.x=screen_width/2-width/2
        self.y=screen_height/2-height/2
        
        self.vel=20

        self.hitbox =(self.x+50,self.y+20,self.width,self.height+20)

        
    def draw(self, window):
        self.hitbox =(self.x+50,self.y+20,self.width,self.height+20)
        pygame.draw.rect(window,(225,0,0),self.hitbox,2)
        window.blit(falcon1,(self.x,self.y))

                                                        #Weapons Function
class weapons:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.vel=50

    def draw(self, window):
       
        window.blit(weapon1,(self.x+45,self.y))     


                                                        #Target Function
class targets:
    def __init__(self,x,y,radius,col):
        self.x=x
        self.y=y
        self.color=col
        self.radius=radius
        self.vel=10
        self.hitbox =(self.x, self.y,28,50)


    def draw(self,window):
        self.hitbox =(self.x, self.y,28,50)
        pygame.draw.rect(window,(225,0,0),self.hitbox,2)
        window.blit(targetx,(self.x,self.y))

    def hit(self):
        print("HIT")

                                                    # Redraw Function
def redraw():

    window.blit(bg,(0,0))
    
    ship1.draw(window)


    for i in bullet1:
        i.draw(window)

    for target in target1:
        target.draw(window)

    pygame.display.update()

                                                            #mainloop

ship1 = player(50,50)
poslist=[]
bullet1=[]
enemy=[]
target1=[]

    

run = True
while run:

    x1=[random.randint(0,screen_width),0]
    print(x1)
    target1.append(targets(x1[0],x1[1],50,(255,0,0)))


    pygame.time.delay(100)

                                                            # KEY CONTROLS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for target in target1:
        if target.x < screen_width:
            target.y += target.vel

    for bullet in bullet1:
        if bullet.y >0:
            bullet.y -=bullet.vel
        else:
            bullet1.pop(bullet1.index(bullet))


    
    keys = pygame.key.get_pressed()
                        
    if keys[pygame.K_SPACE]:
        if len(bullet1)<10:
            bullet1.append(weapons(round(ship1.x + ship1.width//2), round(ship1.y + ship1.height//2), 20, (225,0,0)))

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


#redraw()

pygame.quit

'''
To do
3. Collosion Check
4. Score Counter

Alternative Future
1. Another Ship
2. Another set of Contol keys
3. Collison Check
4. 2 Game Score
'''
