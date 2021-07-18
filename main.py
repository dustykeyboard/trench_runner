import sys, pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60
VEL = 5

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
speed = [0,0]
black = 0, 0, 0

player = pygame.image.load('xwing.png')
player_rect = player.get_rect()
player_rect.top = height / 2
player_rect.left = width / 2 - player_rect.width/2

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move right
                speed[0] += VEL
            if event.key == pygame.K_LEFT:
                # Move left
                speed[0] -= VEL
            if event.key == pygame.K_UP:
                # Move up
                speed[1] -= VEL
            if event.key == pygame.K_DOWN:
                # Move down
                speed[1] += VEL
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Move right
                speed[0] -= VEL
            if event.key == pygame.K_LEFT:
                # Move left
                speed[0] += VEL
            if event.key == pygame.K_UP:
                # Move up
                speed[1] += VEL
            if event.key == pygame.K_DOWN:
                # Move down
                speed[1] -= VEL

    clock.tick(FPS)

    player_rect = player_rect.move(speed)
    if player_rect.left < 0 or player_rect.right > width:
        speed[0] = 0
    if player_rect.top < 0 or player_rect.bottom > height:
        speed[1] = 0

    screen.fill(black)
    screen.blit(player, player_rect)
    pygame.display.flip()