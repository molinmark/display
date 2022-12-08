import pygame
import sys, os
import game_rogue
import pygame_menu
pygame.init()
pygame.mixer.init()
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
def set_rases():
    # тут в зависимости от выбора значения меняется раса, которую мы передаём в game_rogue.privetstvie()

    5

class Display():
    def __init__(self):
        BLUE = (0, 0, 255)
        game_rogue.privetstvie()
        self.person1 = game_rogue.making_character()
        self.N = 8  # количество комнат
        self.rooms = [0] * self.N
        self.monster = [0] * self.N
        self.item = [0] * self.N
        self.name = 0 # проверка на имя монстра
        self.f1 = pygame.font.Font(None, 36)
        self.text1 = self.f1.render('', True,
                                    (180, 0, 0))
        screen.blit(self.text1, (600, 50))


    def paint_score(self):
        self.pole = pygame.font.Font(None, 24)
        self.pole_text  = self.pole.render('Здоровье '+ str(self.person1.health) +
                                           ' скорость ' + str(self.person1.speed) , True, (180, 0, 0))

        self.pole2 = pygame.font.Font(None, 24)
        self.pole_text2 = self.pole2.render('Урон ' + str(self.person1.attack_damage) +
                                          ' радиус атаки ' + str(self.person1.attack_range) , True, (180, 0, 0))
        screen.blit(self.pole_text, (0,0))
        screen.blit(self.pole_text2, (0,30))


    def paint(self,room):
        screen.fill(pygame.Color(0, 0, 0))
        for i in range(0, len(room.matrix)):
            for j in range(0, len(room.matrix[i])):
                if room.matrix[i][j] == '╬':
                    walls = pygame.image.load(os.path.join( 'wall.jpg')).convert()
                    pictures = pygame.transform.scale(walls, (50, 50))
                    screen.blit(pictures, (j * 50, i * 50, 50, 50))
                    #pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(j * 50, i * 50, 50, 50))

                elif room.matrix[i][j] == '๏':
                    image = pygame.image.load(os.path.join( 'img_van.png')).convert()
                    picture = pygame.transform.scale(image, (50, 50))
                    screen.blit(picture, (j * 50, i * 50, 50, 50))

                elif room.matrix[i][j] == '☿':
                    if self.name == 1:
                        vrag_goblin = pygame.image.load(os.path.join('goblin.jpg')).convert()
                        picture_goblin = pygame.transform.scale(vrag_goblin, (50, 50))
                        screen.blit(picture_goblin, (j * 50, i * 50, 50, 50))

                    elif self.name == 2:
                        vrag_orc = pygame.image.load(os.path.join('orc.jpg')).convert()
                        picture_orc = pygame.transform.scale(vrag_orc, (50, 50))
                        screen.blit(picture_orc, (j * 50, i * 50, 50, 50))

                    elif self.name == 3:
                        vrag_razb = pygame.image.load(os.path.join('razboinik.jpg')).convert()
                        vrag_razb.set_colorkey((255, 255, 255))
                        picture_razb = pygame.transform.scale(vrag_razb, (50, 50))
                        screen.blit(picture_razb, (j * 50, i * 50, 50, 50))

                elif room.matrix[i][j] == '†':
                    chest = pygame.image.load(os.path.join( 'chest.jpg')).convert()
                    chest.set_colorkey((255, 255, 255))
                    picture_chest = pygame.transform.scale(chest, (50, 50))
                    screen.blit(picture_chest, (j * 50, i * 50, 50, 50))

        pygame.display.flip()


    def music_fon(self):
        pygame.mixer.music.load('fon.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)

    def alg(self,D1):
        sound1 = pygame.mixer.Sound('welcome-to-the-club.mp3')
        sound1.play()

        while self.person1.health>0:
            self.music_fon()
            for i in range(self.N):
                self.rooms[i] = game_rogue.room()
                self.rooms[i].generation()
                self.monster[i] = game_rogue.making_monster()
                if self.monster[i].name == 'Гоблин':
                    self.name = 1
                elif  self.monster[i].name == 'Орк':
                    self.name = 2
                elif self.monster[i].name == 'Разбойник':
                    self.name = 3
                D1.paint(self.rooms[i])
                list_items = ['Кинжал', 'Короткий лук', 'Великий меч', 'Длинный лук', 'Зелье лечения']
                name_items = game_rogue.random.choice(list_items)
                self.item[i] = game_rogue.Items(name_items)
                self.item[i].parametres()

                n = i
                #self.monster[i] = game_rogue.making_monster()

                while self.person1.health>0:
                    self.paint_score()
                    attack_action = False
                    if (abs(self.rooms[n].X0_monster0 - self.rooms[n].X0) <= self.monster[n].attack_range) and (
                            abs(self.rooms[n].Y0_monster0 - self.rooms[n].Y0) <= self.monster[n].attack_range) and self.monster[
                        n].health > 0:
                        self.monster[n].attack_result(self.person1)
                        attack_action = True

                        if self.person1.health <= 0:
                            self.pole3 = pygame.font.Font(None, 30)
                            self.pole_text3 = self.pole3.render('Вы погибли', True, (200, 100, 0))

                            screen.blit(self.pole_text3, (width/2, height/2))

                    if (abs(self.rooms[n].X0_monster0 - self.rooms[n].X0) <= self.person1.attack_range) and (
                            abs(self.rooms[n].Y0_monster0 - self.rooms[n].Y0) <= self.person1.attack_range) and self.monster[n].health > 0:
                        #текст
                        self.f1 = pygame.font.Font(None, 36)
                        self.text1 = self.f1.render('БЕЙ!(f)', True,
                                                    (180, 0, 0))
                        screen.blit(self.text1, (600, 50))
                        pygame.display.flip()
                        action = D1.button()
                        if action == ('f' or 'F'):
                            self.person1.attack_result(self.monster[n])
                            sound2 = pygame.mixer.Sound('568023243432.mp3')
                            sound2.play()

                        elif action == ('g' or 'G') and attack_action == True:
                            self.person1.start_defence(monster[n])

                        elif action == ('g' or 'G') and attack_action == False:
                            print('Враг не наносил Вам урон')
                            if self.person1.health <= 0:
                                print('Вы погибли, игра закончена')


                    for j in range(self.person1.speed):
                        self.paint_score()
                        # текст
                        self.f1 = pygame.font.Font(None, 36)
                        self.text1 = self.f1.render('ИДИ!(wasd)', True,
                                                    (180, 0, 0))
                        screen.blit(self.text1, (600, 100))
                        pygame.display.flip()

                        new_cord = self.person1.move(D1.button(), self.rooms[n].cord0, self.rooms[n].cord,self.rooms[n].exit, self.rooms[n].input, self.rooms[n].cord_monster0)


                        self.rooms[n].update_character(new_cord)
                        if self.rooms[n].input[0] == self.rooms[n].cord0[0] and self.rooms[n].input[1] == self.rooms[n].cord0[1] and n != 0:
                            n = n - 1

                        elif self.rooms[n].exit[0] - 1 == self.rooms[n].cord0[0] and self.rooms[n].exit[1] == self.rooms[n].cord0[1]:
                            n = n + 1

                        if self.rooms[i].exit[0] - 1 == self.rooms[i].cord0[0] and self.rooms[i].exit[1] == self.rooms[i].cord0[1]:
                            break
                        D1.paint(self.rooms[n])

                    if self.rooms[i].exit[0] - 1 == self.rooms[i].cord0[0] and self.rooms[i].exit[1] == self.rooms[i].cord0[1]:
                        break

                    if self.monster[n].health > 0:
                        for m in range(self.monster[i].speed):
                            new_cord_monster = self.monster[n].move(self.rooms[n].cord_monster0, self.rooms[n].cord, new_cord)
                            self.rooms[n].update_monster(new_cord_monster, self.monster[i].alive_or_ded())
                            D1.paint(self.rooms[n])
                    else:
                        self.rooms[n].update_monster(new_cord_monster, self.monster[n].alive_or_ded())
                        D1.paint(self.rooms[n])


                    if self.item[n].state == 'лежит':

                        if (abs(new_cord_monster[0] - new_cord[0]) <= 1 and abs(
                                new_cord_monster[1] - new_cord[1]) <= 1) and self.monster[n].alive_or_ded() == 'мёртв':
                            # текст
                            self.f1 = pygame.font.Font(None, 36)
                            self.text1 = self.f1.render(f'БЕРИ {self.item[n].name_items}(e)!', True,
                                                        (180, 0, 0))
                            screen.blit(self.text1, (300, 100))
                            pygame.display.flip()

                            action_predmet = D1.button()
                            if action_predmet == 'e':
                                self.item[n].state = 'взят'
                                characteristics = [self.item[n].range_attack, self.item[n].damage, self.item[n].health]
                                self.person1.attack_range += characteristics[0]
                                self.person1.attack_damage += characteristics[1]
                                self.person1.health += characteristics[2]

            print(D1.button())


    def button(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 1
                    elif event.key == pygame.K_w:
                        return 'w'
                    elif event.key == pygame.K_a:
                        return 'a'
                    elif event.key == pygame.K_s:
                        return 's'
                    elif event.key == pygame.K_d:
                        return 'd'
                    elif event.key == pygame.K_f:
                        return 'f'
                    elif event.key == pygame.K_g:
                        return 'g'
                    elif event.key == pygame.K_e:
                        return 'e'

def main():

    D1=Display()
    D1.alg(D1)

def r1():
    game_rogue.type_of_person = 'эльф'

def r2():
    game_rogue.type_of_person = 'человек'

def r3():
    game_rogue.type_of_person = 'гном'

def menu():
    pygame.mixer.music.load('music_menu.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    menu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input( 'Добро пожаловать в подземелье')

    menu.add.text_input('Выберите рассу:')
    menu.add.button('Эльф',r1)
    menu.add.button('Человек',r2)
    menu.add.button('Гном',r3)
    menu.add.button('Play', main)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

menu()