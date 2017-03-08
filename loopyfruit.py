import pygame, random
import apples
import worms

pygame.init()

# set width and height of game screen
width = 800
height = 600
score = 0

# set size of game screen
game_display = pygame.display.set_mode((width, height))
# set title of game
pygame.display.set_caption("loopyfruit")
# colours
red = (255,0,0)
white = (255, 255, 255)
brown = (139,69,19)
black = (0,0,0)
pink = (255, 198, 222)
blue = (160, 193, 247)

# return a clock object to later choose frames per second of moving object
clock = pygame.time.Clock()

# starting position of basket
basket_x = 300
basket_y = 475
basket_width = 120
basket_height = 115
x_change = 0

# load image that we are going to move right and left
basket = pygame.image.load('basket2.png')
# scale image
basket = pygame.transform.scale(basket, (basket_width, basket_height))

# function to move basket
def move_basket(x, y):
    game_display.blit(basket, (x, y))

# create 3 apple instances
apple1 = apples.Apple()
apple2 = apples.Apple()
apple3 = apples.Apple()

# create 1 worm instance
worm1 = worms.Worm()
worm2 = worms.Worm()

# create group for class to access useful functions add and draw
apple_group = pygame.sprite.Group()
worm_group = pygame.sprite.Group()
apple_group.add(apple1, apple2, apple3)
worm_group.add(worm1)

# set initial apple x and y (otherwise the first 3 apples fall at same time)
apple1.rect.centerx = random.randrange(50, 750)
apple1.rect.centery = random.randrange(-800, -5)
apple2.rect.centerx = random.randrange(50, 750)
apple1.rect.centery = random.randrange(-800, -5)
apple3.rect.centerx = random.randrange(50, 750)
apple1.rect.centery = random.randrange(-800, -5)

# initialises loop
game_exit = False

# keeps the following code going until we define game_exit = true and exit
while not game_exit:
    for event in pygame.event.get():
        # exit the loop and game if user presses x
        if event.type == pygame.QUIT:
            game_exit = True
        key = pygame.key.get_pressed()
        # if left/right arrow key pressed move basket left/right
        if key[pygame.K_LEFT]:
            x_change = -13
        elif key[pygame.K_RIGHT]:
            x_change = 13
        else:
            x_change = 0

    # change background colour
    game_display.fill(pink)

    # move basket
    basket_x += x_change
    move_basket(basket_x, basket_y)

    # if basket touches apple score goes up
    # (x, y) is basket top left
    # (x + basket_width, y) is basket top right
    # (x, y + basket_height) is basket bottom left
    # (x + basket_width, y + basket_height) is basket bottom right
    if (basket_x) < apple1.rect.centerx < (basket_x + basket_width) and (basket_y) < apple1.rect.centery < (basket_y + basket_height):
        apple1.rect.centery = random.randrange(-800, -5)
        apple1.rect.centerx = random.randrange(50, 750)
        score += 1
    if (basket_x) < apple2.rect.centerx < (basket_x + basket_width) and (basket_y) < apple2.rect.centery < (basket_y + basket_height):
        apple2.rect.centery = random.randrange(-800, -5)
        apple2.rect.centerx = random.randrange(50, 750)
        score += 1
    if (basket_x) < apple3.rect.centerx < (basket_x + basket_width) and (basket_y) < apple3.rect.centery < (basket_y + basket_height):
        apple3.rect.centery = random.randrange(-800, -5)
        apple3.rect.centerx = random.randrange(50, 750)
        score += 1

    # if basket touches worm player loses a life!
    if (basket_x) < worm1.rect.centerx < (basket_x + basket_width) and (basket_y) < worm1.rect.centery < (basket_y + basket_height):
        worm1.rect.centery = random.randrange(-800, -5)
        worm1.rect.centerx = random.randrange(50, 750)


    # put score on screen
    myfont = pygame.font.SysFont("monospace", 20)
    score_text = myfont.render("Score: "+str(score), 1, black)
    game_display.blit(score_text, (5, 5))

    # if score increases make the apples fall faster
    if score > 10:
        apple1.dy = 5
        apple2.dy = 6
    if score > 20:
        apple1.dy = 6
        apple2.dy = 7
        apple3.dy = 8
        worm1.dy = 6
        if not worm2.alive:
            worm_group.add(worm2)
    if score > 60:
        apple1.dy = 7
        apple2.dy = 9
        worm1.dy = 9

    # if basket goes off screen bring it back around
    if basket_x > width:
        basket_x = -basket_width
    elif basket_x < -basket_width:
        basket_x = width

    # use sprite group function to draw the apples and worm on the screen
    apple_group.draw(game_display)
    if score > 10:
        worm_group.draw(game_display)

    # use update function from the classes to make objects "fall"
    apple1.update()
    apple2.update()
    apple3.update()
    worm1.update()

    pygame.display.update()

    # frames per second
    clock.tick(50)

pygame.quit
quit()
