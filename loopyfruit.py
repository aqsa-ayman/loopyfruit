import pygame, random, os
import apples, worms

pygame.init()

# set width and height of game screen
width = 800
height = 600

# set size of game screen
game_display = pygame.display.set_mode((width, height))
# set up font
subtitle_font_size = pygame.font.SysFont("Consolas", 20)
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

def start_screen():

    # start with blank screen
    game_display.fill(pink)

    # put game title over it
    title = pygame.font.Font("Autumn in November.ttf", 100)
    title = title.render("Loopyfruit", 1, black)
    game_display.blit(title, (100, 160))

    # put a subtitle over it
    subtitle = subtitle_font_size.render("Catch the apples and avoid the worms! Press a to play.", 1, black)
    game_display.blit(subtitle, (110, 350))

    # update the display and the frames per second
    pygame.display.update()

    # make variable to keep a while loop running indefinitely
    # so that we are always checking if the quit or play button is being pressed
    intro = True

    while intro:
        for event in pygame.event.get():
            # if they press the x in the top right corner exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if they press a exit the loop so rest of the code can run
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False


def main_loop():

    start_screen()

    # starting position of basket
    basket_x = 300
    basket_y = 475
    basket_width = 120
    basket_height = 115
    x_change = 0
    score = 0

    # load image that we are going to move right and left
    basket = pygame.image.load('basket2.png')
    # scale image
    basket = pygame.transform.scale(basket, (basket_width, basket_height))

    # function to move basket
    def move_basket(x, y):
        game_display.blit(basket, (x, y))

    # set score in left top corner
    def score_to_screen():
        myfont = pygame.font.Font("Autumn-in-November", 30)
        score_text = myfont.render("Score: "+str(score), 1, black)
        game_display.blit(score_text, (5, 5))

    #def lives_to_screen():

    # define a function that tells the user they caught a worm
    def caught_worm():

        # record their score
        score_list = open("highscores.txt", 'a')
        score_list.write(str(score) + "\n")
        score_list.close()

        # check for the highest score in the score list
        max = 0
        with open('highscores.txt', 'r') as data:
            for line in data.readlines():
                if int(line) >= max:
                    max = int(line)

        # blank screen first
        game_display.fill(pink)

        # tell player they caught a worm
        large_text = pygame.font.Font("Autumn in November.ttf", 70)
        worm_text = large_text.render("You caught a worm!", 1, black)
        game_display.blit(worm_text, (65, 170))

        # tell player their score
        final_score = subtitle_font_size.render("Your Score: " + str(score), 1, black)
        high_score = subtitle_font_size.render("High Score: " + str(max), 1, black)
        replay = subtitle_font_size.render("Press r to replay or q to quit", 1, black)
        game_display.blit(final_score, (300, 325))
        game_display.blit(high_score, (300, 350))
        game_display.blit(replay, (220, 430))

        pygame.display.update()

        # loop runs indefinitely to check if player is quitting or wants to replay
        while True:
            for event in pygame.event.get():
                # if they press the x in the top right corner exit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                # if they press r run the main loop again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main_loop()


    # create 4 apple instances
    apple1 = apples.Apple()
    apple2 = apples.Apple()
    apple3 = apples.Apple()
    apple4 = apples.Apple()

    # create 3 worm instance
    worm1 = worms.Worm()
    worm2 = worms.Worm()
    worm3 = worms.Worm()

    # create group for class to access useful functions add and draw
    apple_group = pygame.sprite.Group()
    worm_group = pygame.sprite.Group()
    apple_group.add(apple1, apple2, apple3, apple4)
    worm_group.add(worm1, worm2, worm3)

    # set initial apple x and y (otherwise the first 3 apples fall at same time)
    apple1.rect.centerx = random.randrange(50, 750)
    apple1.rect.centery = random.randrange(-800, -5)
    apple2.rect.centerx = random.randrange(50, 750)
    apple2.rect.centery = random.randrange(-800, -5)
    apple3.rect.centerx = random.randrange(50, 750)
    apple3.rect.centery = random.randrange(-800, -5)
    apple4.rect.centerx = random.randrange(50, 750)
    apple4.rect.centery = random.randrange(-800, -5)

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

        # ADD TO SCORE WHEN BASKET MAKES CONTACT WITH APPLES
        # (x, y) is basket top left
        # (x + basket_width, y) is basket top right
        # (x, y + basket_height) is basket bottom left
        # (x + basket_width, y + basket_height) is basket bottom right
        if (basket_x) < apple1.rect.centerx < (basket_x + basket_width) and (basket_y) < apple1.rect.centery < (basket_y + basket_height):
            # send apples back up to fall again so it looks like theyre always falling
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
        if (basket_x) < apple4.rect.centerx < (basket_x + basket_width) and (basket_y) < apple4.rect.centery < (basket_y + basket_height):
            apple4.rect.centery = random.randrange(-800, -5)
            apple4.rect.centerx = random.randrange(50, 750)
            score += 1

        # if basket touches worm player loses a life!
        if score > 11 and (basket_x) < worm1.rect.centerx < (basket_x + basket_width) and (basket_y) < worm1.rect.centery < (basket_y + basket_height):
            # we call the function we made earlier since the player caught a worm
            caught_worm()
            # send the worm back up so worms keep falling
            worm1.rect.centery = random.randrange(-800, -5)
            worm1.rect.centerx = random.randrange(50, 750)
        if score > 11 and (basket_x) < worm2.rect.centerx < (basket_x + basket_width) and (basket_y) < worm2.rect.centery < (basket_y + basket_height):
            caught_worm()
            worm2.rect.centery = random.randrange(-800, -5)
            worm2.rect.centerx = random.randrange(50, 750)
        if score > 11 and (basket_x) < worm3.rect.centerx < (basket_x + basket_width) and (basket_y) < worm3.rect.centery < (basket_y + basket_height):
            caught_worm()
            worm3.rect.centery = random.randrange(-800, -5)
            worm3.rect.centerx = random.randrange(50, 750)

        # if score increases make the apples fall faster
        if score > 5:
            apple1.dy = 6
            apple2.dy = 7
        if score > 15:
            apple1.dy = 7
            apple2.dy = 8
            apple3.dy = 8
            apple4.dy = 6
            worm1.dy = 7
        if score > 30:
            apple1.dy = 10
            apple2.dy = 9
            apple4.dy = 11
            worm1.dy = 9
            worm2.dy = 10
            worm3.dy = 12
        if score > 50:
            apple1.dy += 1
            apple2.dy += 1
            apple4.dy += 1
            worm1.dy += 1
            worm2.dy += 1
            worm3.dy += 1

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
        apple_group.update()
        worm_group.update()

        # put score on screen
        score_to_screen()

        # update display before running code again
        pygame.display.update()

        # frames per second
        clock.tick(50)

main_loop()
pygame.quit
quit()
