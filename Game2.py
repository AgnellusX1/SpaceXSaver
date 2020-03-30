import pygame
import os
import sys
import random
pygame.init()

screen_width=800
screen_height=500
window=pygame.display.set_mode((screen_width,screen_height))


bg = pygame.image.load('moon.png')
bg = pygame.transform.scale(bg, (800, 500))
falcon1 = pygame.image.load('falcon.png')




def pregame():
    pygame.display.set_caption("Star Trek")
    myResult = pygame.font.SysFont("monospace", 50)
    window.fill((0, 100, 255))

    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        text = "....Battle of the Binary...."

        label = myResult.render(text, 1, (255, 255, 255))
        window.blit(label, (0, screen_height // 3))
        pygame.display.update()



class player:
    def __init__(self, width, height):
        self.width=width
        self.height=height

        self.x=screen_width/2-width/2
        self.y=screen_height/2-height/2

        self.vel=20

    def draw(self, window):
        window.blit(falcon1,(self.x,self.y))



def drop_enemies(enemy_list, delay, enemy_size):
    if len(enemy_list) < 10 and delay == 10:
        enemy_position = [random.randint(0, screen_width - enemy_size[0]), 0]
        enemy_list.append(enemy_position)


def draw_enemies(enemy_list, enemy_color, enemy_size):
    for enemy_position in enemy_list:
        pygame.draw.rect(window, enemy_color, (enemy_position[0], enemy_position[1], enemy_size[0], enemy_size[1]))


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


def detect_collision(player_position, enemy_position, player_size, enemy_size):
    p_x = player_position[0]
    e_x = enemy_position[0]
    p_y = player_position[1]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size[0])) or (p_x >= e_x and p_x < (e_x + enemy_size[0])):
        if (e_y >= p_y and e_y < (p_y + player_size[1])) or (p_y >= e_y and p_y < (e_y + enemy_size[1])):
            return True
    return False


def collision_check(enemy_list, player_position, player_size, enemy_size):
    for enemy_position in enemy_list:
        if detect_collision(player_position, enemy_position, player_size, enemy_size):
            return True
            break
    else:
        return False


def redraw():

    window.blit(bg,(0,0))

    ship1.draw(window)

    pygame.display.update()



        


def game():
    ship1 = player(50, 60)
    clock = pygame.time.Clock()
    speed = 10
    delay = 9
    count = 0
    myfont = pygame.font.SysFont("monospace", 35)
    myResult = pygame.font.SysFont("monospace", 50)

    player_color = (255, 100, 0)
    player_size = [50, 50]
    player_position = [screen_width / 2, screen_height - 2 * player_size[1]]

    enemy_color = (255, 0, 0)
    enemy_size = [30, 30]
    enemy_position = [random.randint(0, screen_width - enemy_size[0]), 0]
    enemy_list = [enemy_position]

    run= True

    pygame.display.set_caption("Save The Galaxy")

    while run:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and ship1.x > ship1.vel:
            ship1.x -= ship1.vel

        if keys[pygame.K_RIGHT] and ship1.x < screen_width - (ship1.width + ship1.vel):
            ship1.x += ship1.vel

        if keys[pygame.K_UP] and ship1.y > ship1.vel:
            ship1.y -= ship1.vel

        if keys[pygame.K_DOWN] and ship1.y < screen_height -(ship1.height + ship1.vel) :
            ship1.y += ship1.vel


        redraw()
                        

        # final output
        clock.tick(30)
        #window.fill(_color)

        # enemy update
        delay = (delay % 10) + 1
        drop_enemies(enemy_list, delay, enemy_size)

        count, speed = update_enemy_position(enemy_list, count, speed)

        text = "score: " + str(count)

        label = myfont.render(text, 1, (255, 255, 0))
        window.blit(label, (screen_width - 200, screen_height - 40))

        if collision_check(enemy_list, player_position, player_size, enemy_size):
            game_over = True

        draw_enemies(enemy_list, enemy_color, enemy_size)

        pygame.draw.rect(window, player_color, (player_position[0], player_position[1], player_size[0], player_size[1]))


    else:
        pygame.display.set_caption("GAME OVER")
        end = False
        while not end:
            window.fill((0, 100, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game()

            text = "FINAL SCORE : " + str(count)

            label = myResult.render(text, 1, (0, 0, 0))
            window.blit(label, (width // 5, height // 2))

            text = "PRESS SPACE TO RETRY"
            label = myfont.render(text, 1, (0, 0, 0))
            window.blit(label, (screen_width // 4, screen_height - 40))

            pygame.display.update()



ship1 = player(50, 60)

pregame()
