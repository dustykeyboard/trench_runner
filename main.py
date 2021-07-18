import sys, pygame, math

pygame.init()
clock = pygame.time.Clock()
FPS = 60
VEL = 5
SPEED = 0.5

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
speed = [0,0]
black = 0, 0, 0
orange = 255, 165, 0

player = pygame.image.load('xwing.png')
player_rect = player.get_rect()
player_rect.top = height / 2 + player_rect.height/2
player_rect.left = width / 2 - player_rect.width/2

vanishing_point = (width * .5, height*.4)

distance = 0
frames = [100, 150, 200, 250, 330, 350, 400, 450, 500]

# distance = 0-10
def frame_at(distance):
    if distance > 60:
        return

    render_distance = math.sqrt(distance/60)
    # pygame.draw.rect(screen, black, (width*0.35,height*.3,width*.3,height*.3))
    # pygame.draw.rect(screen, orange, (width*0.35,height*.3,width*.3,height*.3), 1)
    # pygame.draw.rect(screen, orange, (width*0.25,height*.235,width*.5,height*.5), 1)

    rect_left = (render_distance * 0.5)
    rect_top = (render_distance * 0.34) + 0.06
    rect_width = 1 - (rect_left * 2)
    rect_height = rect_width*1.01
    
    # pygame.draw.rect(screen, black, (width * rect_left, height * rect_top, width * rect_width, height * rect_height))
    pygame.draw.rect(screen, orange, (width * rect_left, height * rect_top, width * rect_width, height * rect_height), 1)


def draw_grid():
    pygame.draw.line(screen, orange, (width*0.05, height), vanishing_point)
    pygame.draw.line(screen, orange, (width*0.95, height), vanishing_point)
    pygame.draw.line(screen, orange, (width*1, height*.06), vanishing_point)
    pygame.draw.line(screen, orange, (width*0, height*.06), vanishing_point)
 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed[0] += VEL
            if event.key == pygame.K_LEFT:
                speed[0] -= VEL
            if event.key == pygame.K_UP:
                speed[1] -= VEL
            if event.key == pygame.K_DOWN:
                speed[1] += VEL
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_LEFT:
                speed[0] = 0
            if event.key == pygame.K_UP:
                speed[1] = 0
            if event.key == pygame.K_DOWN:
                speed[1] = 0

    clock.tick(FPS)
    distance += SPEED
    if distance > 500:
        distance = 0

    player_rect = player_rect.move(speed)
    if player_rect.left < 0 or player_rect.right > width:
        speed[0] = 0
    if player_rect.top < 0 or player_rect.bottom > height:
        speed[1] = 0

    screen.fill(black)
    draw_grid()

    for frame in frames:
        if frame > distance:
            frame_at(frame - distance)

    screen.blit(player, player_rect)
    pygame.display.flip()