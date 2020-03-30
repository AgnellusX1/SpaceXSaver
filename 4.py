import pygame
import random
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# --- Classes
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load('fire.png')
        self.image = pygame.transform.scale(targetx,(25,50))
 
        self.rect = self.image.get_rect()
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__() 
        self.image = pygame.image.load('falcon.png')
        self.image = pygame.transform.scale(falcon1,(150,100))
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load('mis1.png')
        self.image = pygame.transform.scale(weapon1,(10,20))
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

bg = pygame.image.load('sky.png')
bg = pygame.transform.scale(bg, (screen_width,screen_height))
falcon1 = pygame.image.load('falcon.png')
falcon1 = pygame.transform.scale(falcon1,(150,100))
weapon1 = pygame.image.load('mis1.png')
weapon1 = pygame.transform.scale(weapon1,(10,20))
targetx = pygame.image.load('fire.png')
targetx = pygame.transform.scale(targetx,(25,50))
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for x in range(50):
    for i in range(50):
        # This represents a block
        block = Block(BLUE)

        # Set a random location for the block
        block.rect.x = random.randrange(65,screen_width)
        block.rect.y = 0
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
        time.sleep(10)
        
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 65
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    for block in block_list:
        block.rect.y += 1

    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
    # --- Draw a frame
 
    # Clear the screen
    screen.blit(bg,(0,0))
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
