import pygame
import time
import random

pygame.init()
dis_width = 400
dis_height = 300

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)
black = (0, 0, 0)

# x1 = dis_width/2
# y1 = dis_height/2
 
# x1_next = 0       
# y1_next = 0



clock = pygame.time.Clock()

pygame.display.set_caption('Snake game')
game_over=False

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_next = 0
    y1_next = 0
 
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - 5) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - 5) / 10.0) * 10.0

    speed = 10

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_next = -5
                    y1_next = 0
                if event.key == pygame.K_UP:
                    x1_next = 0
                    y1_next = -5
                if event.key == pygame.K_RIGHT:
                    x1_next = 5
                    y1_next = 0
                if event.key == pygame.K_DOWN:
                    x1_next = 0
                    y1_next = 5

        # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #     game_over = True
        if x1>=dis_width:
            x1=0
        if y1>=dis_height:
            y1=0
        if x1<0:
            x1=dis_width
        if y1<0:
            y1=dis_height
        x1 += x1_next
        y1+=y1_next
        dis.fill(white)
        pygame.draw.rect(dis, black, [foodx, foody, 5, 5])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                print(snake_List)
                print('snakehead')
                game_close = True

        # pygame.draw.rect(dis,blue,[x1,y1,10,10])
        our_snake(5, snake_List)
        score = Length_of_snake - 1
        Your_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - 5) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 5) / 10.0) * 10.0
            Length_of_snake += 1
            speed+=5

        clock.tick(speed)
        # print(game_close)


    message("You lost",red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

gameLoop()