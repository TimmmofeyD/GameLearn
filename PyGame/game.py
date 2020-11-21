import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))  # Creating a game win
pygame.display.set_caption("Cube Game")  # Call the name of the game

x = 50
y = 50
width = 40
height = 40
speed = 5
isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)  # We need a delay so that the loop doesn't run too fast

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
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed

    if not isJump:  # During the jump the player can't move UP and DOWN this we need to block it
        if keys[pygame.K_UP] and y > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height:
            y += speed
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

    win.fill((0, 0, 0))  # Fill the screen with black so that we do not draw but move it
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))  # Creating player
    pygame.display.update()  # To change the image on screen we need to update it

pygame.quit()  # We turn off program you can only get here if that eternal cycle ends
