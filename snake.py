import pygame
import random

pygame.init()
 
screen_width = 600
screen_height = 500


game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.time.Clock()
pygame.display.update()

def text(text, color, font, x,y):
    font = pygame.font.SysFont(None, font)
    screen = font.render(text, True, color)
    game_window.blit(screen, [x,y])

def play_sound(sound):
    pygame.mixer.music.load(sound)
    while True:
        # time.sleep(0.5)
        pygame.mixer.music.play()
        break

def display_snake(game_window, color, snk_list, side):
    # print(snk_list)
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, side, side])
        # print(x,y)

white = (255, 255, 255)
red = (255,0,0)
black = (0,0,0)

def game_loop():
    g_exit = False
    g_over = False 
    position_x = 80
    position_y = 100
    side = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0
    snk_list = []
    snk_length = 1
    fps  = 60
    clock = pygame.time.Clock()
    
    while not g_exit:
        if g_over == True:
            play_sound("game_over.mp3")
            game_window.fill(black)
            text("Game Over: press Enter to Continue", white, 30,100, 200)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    g_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    g_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x  = 2.8
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 2.8
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - 2.8
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 2.8
                        velocity_x = 0

            position_x = position_x + velocity_x
            position_y = position_y + velocity_y

            if abs(position_x - food_x)<8 and abs(position_y - food_y)<8:
                print("score: ", score)
                play_sound("eat_app.mp3")
                food_x = random.randint(30, screen_width/2)
                food_y = random.randint(30, screen_height/2)
                score = score+10
                snk_length +=5

            game_window.fill(white)
            text("score: " + str(score), red,50, 5,5)
            pygame.draw.rect(game_window, red, [food_x, food_y, side, side])

            snk_head =[]
            snk_head.append(position_x)
            snk_head.append(position_y)
            snk_list.append(snk_head)
            # print(snk_list)
                
            if len(snk_list)>snk_length:
                del snk_list[0]
            # pygame.draw.rect(game_window, black, [position_x, position_y, side, side]) #(jaha dikhana hai, kis color me dikhana hai, [x me position , y me position, length, breath])
            if ((position_x<0) or (position_x>screen_width) or (position_y<0) or (position_y>screen_height) or (snk_head in snk_list[:-1])):
                g_over = True
                
                print("Game Over")
            display_snake(game_window, black, snk_list, side)
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    exit()


game_loop()
#8406975656
