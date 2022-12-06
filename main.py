import pygame
import sys
import game_rogue

class Display():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        BLUE = (0, 0, 255)
        game_rogue.privetstvie()
        self.person1 = game_rogue.making_character()
        self.N = 8  # количество комнат
        self.rooms = [0] * self.N
        self.monster = [0] * self.N
        self.item = [0] * self.N

        self.f1 = pygame.font.Font(None, 36)
        self.text1 = self.f1.render('', True,
                                    (180, 0, 0))
        self.screen.blit(self.text1, (600, 50))

    def paint(self,room):
        self.screen.fill(pygame.Color(0, 0, 0))
        for i in range(0, len(room.matrix)):
            for j in range(0, len(room.matrix[i])):
                if room.matrix[i][j] == '╬':
                    pygame.draw.rect(self.screen, (0, 125, 255), pygame.Rect(j * 50, i * 50, 50, 50))
                elif room.matrix[i][j] == '๏':
                    pygame.draw.rect(self.screen, (0, 225, 55), pygame.Rect(j * 50, i * 50, 50, 50))
                elif room.matrix[i][j] == '☿':
                    pygame.draw.rect(self.screen, (0, 225, 15), pygame.Rect(j * 50, i * 50, 50, 50))
                elif room.matrix[i][j] == '†':
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(j * 50, i * 50, 50, 50))

        pygame.display.flip()


    def alg(self,D1):
        while True:
            for i in range(self.N):
                self.rooms[i] = game_rogue.room()
                self.rooms[i].generation()
                D1.paint(self.rooms[i])
                list_items = ['Кинжал', 'Короткий лук', 'Великий меч', 'Длинный лук']
                name_items = game_rogue.random.choice(list_items)
                self.item[i] = game_rogue.Items(name_items)
                self.item[i].parametres()

                n = i

                self.monster[i] = game_rogue.making_monster()

                while True:

                    attack_action = False

                    if (abs(self.rooms[n].X0_monster0 - self.rooms[n].X0) <= self.monster[n].attack_range) and (
                            abs(self.rooms[n].Y0_monster0 - self.rooms[n].Y0) <= self.monster[n].attack_range) and self.monster[
                        n].health > 0:
                        self.monster[n].attack_result(self.person1)
                        attack_action = True

                        if self.person1.health <= 0:

                            raise SystemExit

                    if (abs(self.rooms[n].X0_monster0 - self.rooms[n].X0) <= self.person1.attack_range) and (
                            abs(self.rooms[n].Y0_monster0 - self.rooms[n].Y0) <= self.person1.attack_range) and self.monster[n].health > 0:
                        #текст
                        self.f1 = pygame.font.Font(None, 36)
                        self.text1 = self.f1.render('БЕЙ!(f)', True,
                                                    (180, 0, 0))
                        self.screen.blit(self.text1, (600, 50))
                        pygame.display.flip()
                        #
                        action = D1.button()
                        if action == ('f' or 'F'):
                            self.person1.attack_result(self.monster[n])


                        elif action == ('g' or 'G') and attack_action == True:
                            self.person1.start_defence(monster[n])

                        elif action == ('g' or 'G') and attack_action == False:
                            print('Враг не наносил Вам урон')
                            if self.person1.health <= 0:
                                print('Вы погибли, игра закончена')




                    for j in range(self.person1.speed):
                        # текст
                        self.f1 = pygame.font.Font(None, 36)
                        self.text1 = self.f1.render('ИДИ!(wasd)', True,
                                                    (180, 0, 0))
                        self.screen.blit(self.text1, (600, 100))
                        pygame.display.flip()

                        #
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
                            self.screen.blit(self.text1, (300, 100))
                            pygame.display.flip()

                            #
                            action_predmet = D1.button()
                            if action_predmet == 'e':
                                self.item[n].state = 'взят'
                                characteristics = [self.item[n].range_attack, self.item[n].damage]
                                self.person1.attack_range = characteristics[0]
                                self.person1.attack_damage = characteristics[1]




            print('ВЫ ПОБЕДИЛИ !!!')
            print(D1.button())




    def button(self):
        ii = 10
        while True:
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



main()