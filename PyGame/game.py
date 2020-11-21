import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))  # Creating a game win
pygame.display.set_caption("Cube Game")  # Call the name of the game

# Sprites for the player's movement
walkRight = [pygame.image.load('Sprite/right_1.png'), pygame.image.load('Sprite/right_2.png'),
             pygame.image.load('Sprite/right_3.png'), pygame.image.load('Sprite/right_4.png'),
             pygame.image.load('Sprite/right_5.png'), pygame.image.load('Sprite/right_6.png')]

walkLeft = [pygame.image.load('Sprite/left_1.png'), pygame.image.load('Sprite/left_2.png'),
            pygame.image.load('Sprite/left_3.png'), pygame.image.load('Sprite/left_4.png'),
            pygame.image.load('Sprite/left_5.png'), pygame.image.load('Sprite/left_6.png')]

# Background Image
bg = pygame.image.load('Sprite/bg.jpg')
# Sprite when player is standing
playerStand = pygame.image.load('Sprite/idle.png')

clock = pygame.time.Clock()

x = 5
y = 424
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

right = False
left = False
animCount = 0


def drawWindow():
    global animCount

    win.blit(bg, (0, 0))  # Adding an image to the screen

    if animCount + 1 >= 30:  # The game will need 30 FPS for animation
        animCount = 0

    if left:  # Playing sprites when moving sideways
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:  # Displaying a standing player
        win.blit(playerStand, (x, y))
    pygame.display.update()  # To change the image on screen we need to update it


run = True
while run:
    clock.tick(30)  # Setting the game a fixed 30 FPS

    # See what events are happening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    '''Movement of the cube on surface
       In order to ger a pressed button we create an array of pressed buttons
       Then check it for buttons and move the cube accordingly
       Conditions AND we need for the borders of the screen so that player doesn't go beyond screen '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0

    if not isJump:  # During the jump the player
        if keys[pygame.K_SPACE]:  # Just like with over buttons we also check the SPACE
            isJump = True
    else:
        # Smooth movement of the jump up and down
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()  # We turn off program you can only get here if that eternal cycle ends
