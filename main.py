import sys, pygame, math

pygame.init()
clock = pygame.time.Clock()
FPS = 60
VEL = 5
SPEED = 5

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
speed = [0,0]
bg = 50, 50, 100
grid = 0, 0, 0

player = pygame.image.load('xwing.png')
player_rect = player.get_rect()
player_rect.top = height / 2 + player_rect.height/2
player_rect.left = width / 2 - player_rect.width/2

vanishing_point = (width * .5, height*.25)

distance = 0
obstacles = []

# distance = 0-10
def frame_at(distance):
    if distance < -1:
        return
    if distance > 1000:
        return

    render_position = math.sqrt(math.sqrt(distance/1000))

    rect_left = (render_position * 0.5)
    rect_top = (render_position * 0.25) + 0.0
    rect_width = 1 - (rect_left * 2)
    rect_height = rect_width*1.01
    
    # pygame.draw.rect(screen, bg, (width * rect_left, height * rect_top, width * rect_width, height * rect_height))
    pygame.draw.rect(screen, grid, (width * rect_left, height * rect_top, width * rect_width, height * rect_height), 1)

def draw_grid():
    frame_at((0-distance)%1000)
    frame_at((100-distance)%1000)
    frame_at((200-distance)%1000)
    frame_at((300-distance)%1000)
    frame_at((400-distance)%1000)
    frame_at((500-distance)%1000)
    frame_at((600-distance)%1000)
    frame_at((700-distance)%1000)
    frame_at((800-distance)%1000)
    frame_at((900-distance)%1000)
    frame_at((1000-distance)%1000) 

    # pygame.draw.line(screen, grid, (width*0.05, height), vanishing_point)
    # pygame.draw.line(screen, grid, (width*0.95, height), vanishing_point)
    # pygame.draw.line(screen, grid, (width*1, height*.06), vanishing_point)
    # pygame.draw.line(screen, grid, (width*0, height*.06), vanishing_point)
    pygame.draw.line(screen, grid, (width*0, height), vanishing_point)
    pygame.draw.line(screen, grid, (width*1, height), vanishing_point)
    pygame.draw.line(screen, grid, (width*1, height*0), vanishing_point)
    pygame.draw.line(screen, grid, (width*0, height*0), vanishing_point)
 

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

    player_rect = player_rect.move(speed)
    if player_rect.left < 0 or player_rect.right > width:
        speed[0] = 0
    if player_rect.top < 0 or player_rect.bottom > height:
        speed[1] = 0

    screen.fill(bg)
    draw_grid()

    for obstacle in obstacles:
        if obstacle.distance > distance:
            frame_at(frame - (distance % 50))

    screen.blit(player, player_rect)
    pygame.display.flip()