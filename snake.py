import pygame
import random
 
pygame.init()

white = (255, 255, 255) #Цвета по RGB
black = (0, 0, 0)
red = (255, 0, 0)
grey = (100,100,100)
green = (0,100,0)

dis_x = 1280 #Размер игрового поля по оси x
dis_y = 720 #Размер игрового поля по оси y
dis=pygame.display.set_mode((dis_x, dis_y))  #Задаём размер игрового поля
pygame.display.set_caption('Snake') #Название игры
snake_block=10 #Размер блока змея окоянного
snake_speed=15 #Скорость змея окоянного
font_style = pygame.font.SysFont("bahnschrift", 50, False, True) #Задаём стиль текста(Шрифт, размер, Жирный?, Курсив?)
clock = pygame.time.Clock() #Переменная отвечающая за подсчёт времени

def score(score): #Функция подсчёта и вывода счёта(длина змея - начальная длина змея)
   value = font_style.render("Ваш счёт: " + str(score-2), True, black, grey)
   dis.blit(value, [dis_x/2, 0])

def message(msg,x,y): #Функция для вывода сообщений на игровой экран
   mesg = font_style.render(msg, True, black, grey)
   dis.blit(mesg, [x, y])

def our_snake(snake_block, snake_list): #Функция для отрисовки змея окоянного
   for x in snake_list:
        if x==snake_list[len(snake_list)-1]: #Окрашиваю голову змея в белый
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block+2, snake_block+2])
        else: #Окрашиваю хвост змея в серый
            pygame.draw.rect(dis, grey, [x[0], x[1], snake_block, snake_block])

def game(): #Функция игры
    game_end=False #Флаг для закрытия игры
    defeat=False #Флаг означающий поражение игрока
    x1 = dis_x/2 #Указываем начальную координату положения змея по оси х
    y1 = dis_y/2 #Указываем начальную координату положения змея по оси y
    x1_change = 0 #Переменная, которой в цикле while будут присваиваться значения изменения положения змея по оси х
    y1_change = 0 #Переменная, которой в цикле while будут присваиваться значения изменения положения змея по оси y
    foodx = round(random.randrange(0 + snake_block*2, dis_x - snake_block*2) / 10.0) * 10.0 #Переменная, которая будет указывать расположение еды по оси х
    foody = round(random.randrange(0 + snake_block*8, dis_y - snake_block*2) / 10.0) * 10.0 #Переменная, которая будет указывать расположение еды по оси y
    snake_list = [] #Хвост змея окоянного
    snake_len = 2 #Длина змея окоянного
    stop=True #Флаг, означающий что змей стоит
    previous_key = '' #Переменная содержащая последнюю нажатую клавишу действия


    while not game_end: #Основной цикл
        for event in pygame.event.get(): #Цикл взаимодействия игрока с игрой
            print(event) #Вывод действия игрока на консоль
            if (event.type==pygame.QUIT): #Выход через закрытие окна
                game_end=True
            if (event.type == pygame.KEYDOWN): #Выбираем из взаимодействий игрока только нажатия клавиш.
                if event.key==pygame.K_ESCAPE: #Завершение игры через Escape.
                    game_end=True
                if event.key==pygame.K_SPACE: #Перезапуск игры через Space
                    print("restart") #Вывод в консоль сообщения о рестарте
                    defeat=False #Сброс ключевых переменных
                    x1 = dis_x/2 
                    y1 = dis_y/2
                    x1_change = 0
                    y1_change = 0
                    snake_len = 2
                    snake_list = []
                    stop=True
                    previous_key = ''
                if (defeat==False): #Проверка на то, что игра не проиграна
                    if (snake_head[0]%10 != 0): #Если голова змея находится не в системе координат игры из-за движения наискосок, мы её возвращаем
                            x1+=snake_block/2
                            y1+=snake_block/2
                            stop=True
                    if event.key == pygame.K_a and previous_key != 'd': #влево
                        previous_key = 'a'
                        stop=False
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_d and previous_key != 'a': #вправо
                        previous_key = 'd'
                        stop=False
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_w and previous_key != 's': #вверх
                        previous_key = 'w'
                        stop=False
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_s and previous_key != 'w': #вниз
                        previous_key = 's'
                        stop=False
                        y1_change = snake_block
                        x1_change = 0
                    elif event.key == pygame.K_e and previous_key != 'z': #вверх-направо
                        previous_key = 'e'
                        stop=False
                        y1_change = -snake_block/2
                        x1_change = snake_block/2
                    elif event.key == pygame.K_q and previous_key != 'c': #вверх-налево
                        previous_key = 'q'
                        stop=False
                        y1_change = -snake_block/2
                        x1_change = -snake_block/2
                    elif event.key == pygame.K_c and previous_key != 'q': #вниз-направо
                        previous_key = 'c'
                        stop=False
                        y1_change = snake_block/2
                        x1_change = snake_block/2
                    elif event.key == pygame.K_z and previous_key != 'e': #вниз-налево
                        previous_key = 'z'
                        stop=False
                        y1_change = snake_block/2
                        x1_change = -snake_block/2
                    elif event.key == pygame.K_x: #стоп
                        previous_key = ''
                        stop=True
                        y1_change = 0
                        x1_change = 0
        if (x1 >= dis_x-snake_block) or (x1 < 0+snake_block) or (y1 >= dis_y-snake_block) or (y1 < 0+snake_block + 50):
            defeat=True  #Поражение, если координаты головы змея окоянного выходят за границы поля
        if (defeat==False): 
            x1 += x1_change #Записываем новое значение положения змейки по оси х.
            y1 += y1_change #Записываем новое значение положения змейки по оси y.
        dis.fill(black) #Красим игровое поле в black
        pygame.draw.rect(dis, grey, [0, 0, dis_x, 50])
        if (defeat==True):
            message("Вы проиграли.",0,0)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1,y1] #голова змея окоянного
        snake_list.append(snake_head) #здесь можно добавить if, чтоб змей не уходил в себя при поражении
        if len(snake_list) > snake_len:
            del snake_list[0] #ограничиваем длину змея кол-вом длины
        if stop == False:
            for x in snake_list[:-1]:
                if x == snake_head:
                    defeat = True #поражение при столкновении
        our_snake(snake_block, snake_list) #Отрисовываем змея окоянного
        score(snake_len) #Выводим счёт
        pygame.display.update() #обновляем экран игрока
        if x1 == foodx and y1 == foody: #Собираем еду, если голова змея на клетке еды
            foodx = round(random.randrange(0 + snake_block*2, dis_x - snake_block*2) / 10.0) * 10.0 #Создаём переменную, которая будет указывать расположение еды по оси х
            foody = round(random.randrange(0 + snake_block*2 + 50, dis_y - snake_block*2) / 10.0) * 10.0 #Создаём переменную, которая будет указывать расположение еды по оси y
            snake_len += 1 #Добавляем длину змею
        clock.tick(snake_speed) #Перемещаем время игры через snake_speed (кадров?)


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
        msg = "qezc-движение наискосок "
        message(msg,0,100)
        msg = "x-остановиться"
        message(msg,0,150)
        msg = "Space-начать заново"
        message(msg,0,200)
        msg = "Esc-выйти"
        message(msg,0,250)
        msg = "Чтобы начать нажмите Space"
        message(msg,0,350)
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
