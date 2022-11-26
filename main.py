import pygame
import game_rogue



def display(room):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for i in range(0, len(room.matrix)):
            for j in range(0, len(room.matrix[i])):
                if room.matrix[i][j] == '╬':
                    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(j * 50, i * 50, 50, 50))
                elif room.matrix[i][j] == '๏':
                    pygame.draw.rect(screen, (0, 225, 55), pygame.Rect(j * 50, i * 50, 50, 50))
                elif room.matrix[i][j] == '☿':
                    pygame.draw.rect(screen, (0, 225, 15), pygame.Rect(j * 50, i * 50, 50, 50))

        pygame.display.flip()


"""menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
#menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', display(room))
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)"""


def main():
    global N, rooms, monster, item, person1
    game_rogue.privetstvie()
    person1 = game_rogue.making_character()
    """
    может быть принты перенести в сам pygame
    """
    print(f'''Имя: {person1.name}, уровень жизни : {person1.health}, уровень защиты: {person1.armor}, 
дальность атаки: {person1.attack_range}, урон: {person1.attack_damage} и скорость: {person1.speed}''')

    N = 3  # количество комнат
    rooms = [0] * N
    monster = [0] * N
    item = [0] * N
    rooms[1] = game_rogue.room()
    rooms[1].generation()
    display(rooms[1])


"""""""""


    for i in range(N):
        rooms[i] = game_rogue.room()
        rooms[i].generation()
        display()
        list_items = ['Кинжал', 'Короткий лук', 'Великий меч','Длинный лук']
        name_items = game_rogue.random.choice(list_items)
        item[i] = game_rogue.Items(name_items)
        item[i].parametres()

        n = i

        monster[i] = game_rogue.making_monster()

        while True:
            print(f'В начале хода у Вас: {person1.health} здоровья')
            attack_action = False

            if (abs(rooms[n].X0_monster0 - rooms[n].X0) <= monster[n].attack_range) and (abs(rooms[n].Y0_monster0 - rooms[n].Y0) <= monster[n].attack_range) and monster[n].health > 0:
                monster[n].attack_result(person1)
                attack_action = True
                print(f'Здоровье персонажа после атаки: {person1.health}')
                if person1.health <= 0:
                    print('Вы погибли, игра закончена')
                    raise SystemExit

            if (abs(rooms[n].X0_monster0 - rooms[n].X0) <= person1.attack_range) and (
                    abs(rooms[n].Y0_monster0 - rooms[n].Y0) <= person1.attack_range) and monster[n].health > 0:
                action = input('Желаете напасть на врага? Если да - нажмите f, если хотите защититься - нажмите g')
                if action == ('f' or 'F'):
                    person1.attack_result(monster[n])
                    print(f'Здоровье монстра после атаки: {monster[n].health}')

                elif action == ('g' or 'G') and attack_action == True:
                    person1.start_defence(monster[n])

                elif action == ('g' or 'G') and attack_action == False:
                    print('Враг не наносил Вам урон')
                    if person1.health <= 0:
                        print('Вы погибли, игра закончена')

            if monster[n].health > 0:
                print(f'Вы видите в комнате {monster[n].name}')

            for j in range(person1.speed):
                new_cord = person1.move(input('Введите напраление "w", "a", "s", "d"'), rooms[n].cord0, rooms[n].cord,
                                        rooms[n].exit, rooms[n].input, rooms[n].cord_monster0)

                rooms[n].update_character(new_cord)
                if rooms[n].input[0] == rooms[n].cord0[0] and rooms[n].input[1] == rooms[n].cord0[1] and n != 0:
                    n = n - 1

                elif rooms[n].exit[0] - 1 == rooms[n].cord0[0] and rooms[n].exit[1] == rooms[n].cord0[1]:
                    n = n + 1

                if rooms[i].exit[0] - 1 == rooms[i].cord0[0] and rooms[i].exit[1] == rooms[i].cord0[1]:
                    break
                rooms[n].display()

            if rooms[i].exit[0] - 1 == rooms[i].cord0[0] and rooms[i].exit[1] == rooms[i].cord0[1]:
                break

            if monster[n].health > 0:
                for m in range(monster[i].speed):
                    new_cord_monster = monster[n].move(rooms[n].cord_monster0, rooms[n].cord, new_cord)
                    rooms[n].update_monster(new_cord_monster, monster[i].alive_or_ded())
                    rooms[n].display()
            else:
                rooms[n].update_monster(new_cord_monster, monster[n].alive_or_ded())
                rooms[n].display()

            print(monster[n].name, monster[n].alive_or_ded())

            if item[n].state =='лежит':
                item[n].loot(new_cord_monster, new_cord, monster[n].alive_or_ded())
                if item[n].state == 'взят':
                    characteristics = [item[n].range_attack, item[n].damage]
                    person1.attack_range = characteristics[0]
                    person1.attack_damage = characteristics[1]


    print('ВЫ ПОБЕДИЛИ !!!')
"""""""""
main()