import pygame
import random

pygame.init()

class color:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.grey = (100,100,100)
        self.green = (0,100,0)
        self.purple = (155,0,155)

clr = color()

class const:
    def __init__(self):
        self.dis_x = 1280 #Размер игрового поля по оси x
        self.dis_y = 720 #Размер игрового поля по оси y
        self.dis = pygame.display.set_mode((self.dis_x, self.dis_y))  #Задаём размер игрового поля
        self.snake_block = 10 #Размер блока змея окоянного
        self.snake_speed = 15 #Скорость змея окоянного

cst = const()

pygame.display.set_caption('Snake') #Название игры
font_style = pygame.font.SysFont("bahnschrift", 50, False, True) #Задаём стиль текста(Шрифт, размер, Жирный?, Курсив?)
clock = pygame.time.Clock() #Переменная отвечающая за подсчёт времени

def score(score): #Функция подсчёта и вывода счёта(длина змея - начальная длина змея)
   value = font_style.render("Ваш счёт: " + str(score-2), True, clr.black, clr.grey)
   cst.dis.blit(value, [cst.dis_x/2, 0])

def message(msg,x,y): #Функция для вывода сообщений на игровой экран
   mesg = font_style.render(msg, True, clr.black, clr.grey)
   cst.dis.blit(mesg, [x, y])

def our_snake(snake_block, snake_list): #Функция для отрисовки змея окоянного
   for x in snake_list:
        if x==snake_list[len(snake_list)-1]: #Окрашиваю голову змея в белый
            pygame.draw.rect(cst.dis, clr.white, [x[0]-1, x[1]-1, snake_block+2, snake_block+2])
        else: #Окрашиваю хвост змея в серый
            pygame.draw.rect(cst.dis, clr.grey, [x[0], x[1], snake_block, snake_block])

def game(): #Функция игры
    class game_logic:
        def __init__(self):
            self.game_end=False #Флаг для закрытия игры
            self.defeat=False #Флаг означающий поражение игрока
            self.x1 = cst.dis_x/2 #Указываем начальную координату положения змея по оси х
            self.y1 = cst.dis_y/2 #Указываем начальную координату положения змея по оси y
            self.x1_change = 0 #Переменная, которой в цикле while будут присваиваться значения изменения положения змея по оси х
            self.y1_change = 0 #Переменная, которой в цикле while будут присваиваться значения изменения положения змея по оси y
            self.foodx = round(random.randrange(0 + cst.snake_block*2, cst.dis_x - cst.snake_block*2) / 10.0) * 10.0 #Переменная, которая будет указывать расположение еды по оси х
            self.foody = round(random.randrange(0 + cst.snake_block*8, cst.dis_y - cst.snake_block*2) / 10.0) * 10.0 #Переменная, которая будет указывать расположение еды по оси y
            self.snake_list = [] #Хвост змея окоянного
            self.snake_len = 2 #Длина змея окоянного
            self.stop=True #Флаг, означающий что змей стоит
            self.previous_key = '' #Переменная содержащая последнюю нажатую клавишу действия
            self.move_accept = False
            self.portal_xy = [cst.dis_x/2, cst.dis_y/2]
            self.dot_portal = False
            self.xt = cst.dis_x/2
            self.yt = cst.dis_y/2
            self.xmouse = 0
            self.ymouse = 0

    gml = game_logic()

    class snakes:
        def __init__(self):
            self.

    snk1 = snakes
    snk2 = snakes

    while not game_end: #Основной цикл
        for event in pygame.event.get(): #Цикл взаимодействия игрока с игрой
            #print(event) #Вывод действия игрока на консоль
            if (event.type==pygame.QUIT): #Выход через закрытие окна
                game_end=True

            if (event.type == pygame.MOUSEMOTION):
                xmouse, ymouse = event.pos
                #print(xmouse,ymouse) #Вывод координат мыши в консоль

            if (event.type == pygame.KEYDOWN): #Выбираем из взаимодействий игрока только нажатия клавиш.
                if event.key==pygame.K_ESCAPE: #Завершение игры через Escape.
                    game_end=True
                if event.key==pygame.K_SPACE: #Перезапуск игры через Space
                    print("restart") #Вывод в консоль сообщения о рестарте
                    defeat=False #Сброс ключевых переменных
                    x1 = cst.dis_x/2 
                    y1 = cst.dis_y/2
                    x1_change = 0
                    y1_change = 0
                    snake_len = 2
                    snake_list = []
                    stop=True
                    previous_key = ''
                    move_accept = False
                    dot_portal=False
                    portal_xy = [cst.dis_x/2,cst.dis_y/2]
                if (defeat==False): #Проверка на то, что игра не проиграна
                    if event.key == pygame.K_a and previous_key != 'd' and move_accept == False: #влево
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'a'
                        stop = False
                        x1_change = -cst.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_d and previous_key != 'a' and move_accept == False: #вправо
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'd'
                        stop = False
                        x1_change = cst.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_w and previous_key != 's' and move_accept == False: #вверх
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'w'
                        stop=False
                        y1_change = -cst.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_s and previous_key != 'w' and move_accept == False: #вниз
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 's'
                        stop=False
                        y1_change = cst.snake_block
                        x1_change = 0

                    elif event.key == pygame.K_e and previous_key != 'z' and move_accept == False: #вверх-направо
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'e'
                        stop=False
                        y1_change = -cst.snake_block/2
                        x1_change = cst.snake_block/2
                    elif event.key == pygame.K_q and previous_key != 'c' and move_accept == False: #вверх-налево
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'q'
                        stop=False
                        y1_change = -cst.snake_block/2
                        x1_change = -cst.snake_block/2
                    elif event.key == pygame.K_c and previous_key != 'q' and move_accept == False: #вниз-направо
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'c'
                        stop=False
                        y1_change = cst.snake_block/2
                        x1_change = cst.snake_block/2
                    elif event.key == pygame.K_z and previous_key != 'e' and move_accept == False: #вниз-налево
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        move_accept = True
                        previous_key = 'z'
                        stop=False
                        y1_change = cst.snake_block/2
                        x1_change = -cst.snake_block/2

                    elif event.key == pygame.K_x: #стоп
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        previous_key = ''
                        stop=True
                        y1_change = 0
                        x1_change = 0
                    elif event.key == pygame.K_f and dot_portal == False: #Телепорт в начало
                        if (snake_head[0]%10 != 0):
                            x1+=x1_change
                            y1+=y1_change
                            snake_head = [x1,y1] #голова змея окоянного
                            snake_list.append(snake_head)
                        portal_time = 0
                        portal_xy = [x1,y1]
                        stop=False
                        xt=(xmouse//10)*10
                        yt=(ymouse//10)*10
                        x1=xt
                        y1=yt
                        dot_portal = True
        if (x1 >= cst.dis_x-cst.snake_block) or (x1 < 0+cst.snake_block) or (y1 >= cst.dis_y-cst.snake_block) or (y1 < 0+cst.snake_block + 50):
            defeat=True  #Поражение, если координаты головы змея окоянного выходят за границы поля
        if (defeat==False): 
            x1 += x1_change #Записываем новое значение положения змейки по оси х.
            y1 += y1_change #Записываем новое значение положения змейки по оси y.
        cst.dis.fill(clr.black) #Красим игровое поле в black
        pygame.draw.rect(cst.dis, clr.grey, [0, 0, cst.dis_x, 50])
        if (defeat==True):
            message("Вы проиграли.",0,0)
        pygame.draw.rect(cst.dis, clr.red, [foodx, foody, cst.snake_block, cst.snake_block])
        snake_head = [x1,y1] #голова змея окоянного
        snake_list.append(snake_head) #здесь можно добавить if, чтоб змей не уходил в себя при поражении
        if len(snake_list) > snake_len:
            del snake_list[0] #ограничиваем длину змея кол-вом длины
        if stop == False:
            for x in snake_list[:-1]:
                if x == snake_head:
                    defeat = True #поражение при столкновении
        if dot_portal == True:
            pygame.draw.rect(cst.dis, clr.purple, [portal_xy[0]-3, portal_xy[1]-3, cst.snake_block+6, cst.snake_block+6])
            pygame.draw.rect(cst.dis, clr.purple, [xt-3, yt-3, cst.snake_block+6, cst.snake_block+6])
            portal_time += 1
            if  portal_time == snake_len:
                dot_portal = False
        our_snake(cst.snake_block, snake_list) #Отрисовываем змея окоянного
        score(int((snake_len+4)/3)) #Выводим счёт
        pygame.display.update() #обновляем экран игрока
        move_accept = False
        if x1 == foodx and y1 == foody: #Собираем еду, если голова змея на клетке еды
            foodx = round(random.randrange(0 + cst.snake_block*2, cst.dis_x - cst.snake_block*2) / 10.0) * 10.0 #Создаём переменную, которая будет указывать расположение еды по оси х
            foody = round(random.randrange(0 + cst.snake_block*2 + 50, cst.dis_y - cst.snake_block*2) / 10.0) * 10.0 #Создаём переменную, которая будет указывать расположение еды по оси y
            snake_len += 3 #Добавляем длину змею
        clock.tick(cst.snake_speed) #Перемещаем время игры через snake_speed (кадров?)


    pygame.quit() #Закрываем PyGame

def start_game(): #Функия для вывода обучения, и последующего запуска игры
    learning_end = False
    start=True
    while not learning_end:
        msg="                                                        " #Выводим обучение
        for i in range(8):
            message(msg,0,((i)*50))
        msg = "Клавиши:"
        message(msg,0,0)
        msg = "wasd-движение"
        message(msg,0,50)
        msg = "qezc-движение по диагонали"
        message(msg,0,100)
        msg = "f-телепортироваться на место курсора"
        message(msg,0,150)
        msg = "x-остановиться"
        message(msg,0,200)
        msg = "Space-начать заново"
        message(msg,0,250)
        msg = "Esc-выйти"
        message(msg,0,300)
        msg = "Чтобы начать нажмите Space"
        message(msg,0,400)
        pygame.display.update()
        for event in pygame.event.get(): #выход через закрытие окна или нажатие Escape
            if event.type == pygame.QUIT:
                learning_end = True
                start=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start=False
                    learning_end = True
                if event.key == pygame.K_SPACE: #Закрытие обучения и запуск игры
                    learning_end = True

    if start==True: #Проверка на запускать ли игру
        game()
    else:
        pygame.quit()


start_game()
