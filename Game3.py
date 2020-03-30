import pygame
import os
import random
pygame.init()

screen_width=1920
screen_height=1080
window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Star Trek Discovery")

                                                            # Loading Images
bg = pygame.image.load('moon.png')
bg = pygame.transform.scale(bg, (1920, 1080))
falcon1 = pygame.image.load('falcon.png')
#falcon2 =
weapon1 = pygame.image.load('fire.png')
weapon1 = pygame.transform.scale(weapon1,(50,100))
weapon2 = pygame.image.load('bullet2.jpg')
weapon2 = pygame.transform.scale(weapon2,(100,50))



def drop_enemies(enemy_list, delay, enemy_size):
    if len(enemy_list) < 10 and delay == 10:
        enemy_position = [random.randint(0, screen_width - enemy_size[0]), 0]
        enemy_list.append(enemy_position)


def draw_enemies(enemy_list, enemy_color, enemy_size):
    for enemy_position in enemy_list:
        window.blit(weapon1(enemy_position[0], enemy_position[1]))
        pygame.display.update()
        #pygame.draw.rect(window, enemy_color, (enemy_position[0], enemy_position[1], enemy_size[0], enemy_size[1]))


def speed_update(count, speed):
    if (count % 25) == 10:
        speed = speed + 0.05
    return speed


def update_enemy_position(enemy_list, count, speed):

    for index, enemy_position in enumerate(enemy_list):
        if enemy_position[1] >= 0 and enemy_position[1] < screen_height:
            speed = speed_update(count, speed)
            enemy_position[1] = enemy_position[1] + speed
        else:
            enemy_list.pop(index)
            count = count + 1

    return count, speed





                                                            #Player Functions
class player:
    def __init__(self, width, height):
        self.width=width
        self.height=height

        self.x=screen_width/2-width/2
        self.y=screen_height/2-height/2

        self.vel=20

    def draw(self, window):
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
        window.blit(weapon1,(self.x,self.y))
        #pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)


                                                    # Redraw Function
def redraw():

    window.blit(bg,(0,0))

    ship1.draw(window)

    for bullet in bullet1:
        bullet.draw(window)

    pygame.display.update()

                                                            #mainloop

ship1 = player(50, 60)
#ship2 =
enemy_size = [30, 30]
bullet1=[]
enemy_position = [random.randint(0, screen_width - enemy_size[0]), 0]
enemy_list = [enemy_position]
delay = 9
count = 0
speed = 10
myfont = pygame.font.SysFont("monospace", 35)
myResult = pygame.font.SysFont("monospace", 50)




run = True
while run:
    pygame.time.delay(100)



                                                            # KEY CONTROLS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullet1:
        if bullet.y < screen_height and bullet.y > 0:
            bullet.y += bullet.vel
        else:
            bullet1.pop(bullet1.index(bullet))


    delay = (delay % 10) + 1
    drop_enemies(enemy_list, delay, enemy_size)

    count, speed = update_enemy_position(enemy_list, count, speed)

    text = "score: " + str(count)

    label = myfont.render(text, 1, (255, 255, 0))
    window.blit(label, (screen_width - 200, screen_height - 40))

    keys = pygame.key.get_pressed()
                        
    if keys[pygame.K_SPACE]:
        if len(bullet1)<10:
            bullet1.append(weapons(round(ship1.x + ship1.width//2), round(ship1.y + ship1.height//2), 20, (225,0,0)))

    if keys[pygame.K_LEFT] and ship1.x > ship1.vel:
        ship1.x -= ship1.vel

    if keys[pygame.K_RIGHT] and ship1.x < screen_width - (ship1.width + ship1.vel):
        ship1.x += ship1.vel

    if keys[pygame.K_UP] and ship1.y > ship1.vel:
        ship1.y -= ship1.vel

    if keys[pygame.K_DOWN] and ship1.y < screen_height -(ship1.height + ship1.vel) :
        ship1.y += ship1.vel


                                                            # calls The redraw function
    redraw()



redraw()

pygame.quit
