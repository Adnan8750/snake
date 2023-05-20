import pygame
import random

pygame.init()
pygame.mixer.init()
 
screen_width = 600
screen_height = 500

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.time.Clock()
pygame.display.update()

def text(text, color, size, style, x,y):
    font = pygame.font.Font(style, size)
    screen = font.render(text, True, color)
    game_window.blit(screen, [x,y])

def display_snake(game_window, color, snk_list, side):
    # print(snk_list)
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, side, side])
        # print(x,y)


clock = pygame.time.Clock()
white = (255, 255, 255)
bg_color = (78, 242, 94)
red = (255,0,0)
black = (0,0,0)
over_bg = (31, 161, 43)

def start_window():
    g_exit = False
    while not g_exit:
        game_window.fill(bg_color)
        text("Welcome to Snake game", black, 50,"Reglisse_Back.otf", 55, 190)
        text("Press Space bar to play", black, 36,"Reglisse.otf", 125, 260)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit == True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)

def game_loop():
    g_exit = False
    score = 0
    g_over = False 
    position_x = 80
    position_y = 100
    side = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(10, screen_width)
    food_y = random.randint(10, screen_height)
    snk_list = []
    snk_length = 1
    fps  = 60
    img = pygame.image.load("snake_bg.jpg")
    with open("score.txt", "r") as f:
        hiscore = f.read()

    # clock = pygame.time.Clock()
    
    while not g_exit:
        # game_window.blit(img, (0,0))
        if g_over == True:
            pygame.mixer.music.load("game_over.mp3")
            pygame.mixer.music.play()
            with open("score.txt", "w") as f:
                f.write(str(hiscore))
            # play_sound("game_over.mp3")
            game_window.fill(black)
            text("Game Over", white, 50, "Reglisse_Back.otf", 100, 180)
            text("Press Enter to Continue", white, 30,"Reglisse.otf", 100, 250)
            text(f"score: {str(score)}", black,40,"Reglisse.otf", 150,280)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    g_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_window()
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

                    if event.key == pygame.K_d:
                        velocity_x  = 2.8
                        velocity_y = 0
                    if event.key == pygame.K_a:
                        velocity_x = - 2.8
                        velocity_y = 0
                    if event.key == pygame.K_w:
                        velocity_y = - 2.8
                        velocity_x = 0
                    if event.key == pygame.K_s:
                        velocity_y = 2.8
                        velocity_x = 0

            position_x = position_x + velocity_x
            position_y = position_y + velocity_y

            if abs(position_x - food_x)<7 and abs(position_y - food_y)<7:
                pygame.mixer.music.load("eat_app.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(30, screen_width/2)
                food_y = random.randint(30, screen_height/2)
                score = score+10
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
            
           
            game_window.fill(bg_color)
            text(f"score: {str(score)} Hiscore: {hiscore}", black,40,"Reglisse_Back.otf", 5,5)
            pygame.draw.rect(game_window, red, [food_x, food_y, side, side])

            snk_head =[]
            snk_head.append(position_x)
            snk_head.append(position_y)
            snk_list.append(snk_head)
            # print(snk_list)
                
            if len(snk_list)>snk_length:
                del snk_list[0]
            if ((position_x<0) or (position_x>screen_width) or (position_y<0) or (position_y>screen_height) or (snk_head in snk_list[:-1])):
                g_over = True
            display_snake(game_window, black, snk_list, side)
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    exit()


start_window()
